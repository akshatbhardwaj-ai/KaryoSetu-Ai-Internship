# Karyosetu Service Classification — QLoRA Fine-tuning
# Run this in Google Colab with a GPU.
#
# Base model: meta-llama/Llama-3.2-3B-Instruct
# Training method: supervised fine-tuning (SFT) + LoRA/4-bit QLoRA
#
# Before running:
# 1) In Colab: Runtime -> Change runtime type -> GPU
# 2) Accept the Llama 3.2 license / have Hugging Face access.
# 3) Upload train.jsonl and validation.jsonl to /content/karyosetu_finetuning/
#
# Install:
!pip -q install -U "transformers" "datasets" "accelerate" "bitsandbytes" "peft" "trl"

import os, json, torch
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import LoraConfig
from trl import SFTConfig, SFTTrainer

MODEL_ID = "meta-llama/Llama-3.2-3B-Instruct"
DATA_DIR = "/content/karyosetu_finetuning"
OUTPUT_DIR = "/content/karyosetu_lora"

train_ds = load_dataset("json", data_files=f"{DATA_DIR}/train.jsonl", split="train")
val_ds   = load_dataset("json", data_files=f"{DATA_DIR}/validation.jsonl", split="train")

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

def format_example(example):
    # Convert conversational messages into the model's chat template.
    return tokenizer.apply_chat_template(
        example["messages"],
        tokenize=False,
        add_generation_prompt=False
    )

compute_dtype = torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=compute_dtype,
    bnb_4bit_use_double_quant=True,
)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    quantization_config=bnb_config,
    device_map="auto",
)
model.config.use_cache = False

peft_config = LoraConfig(
    r=16,
    lora_alpha=32,
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
    target_modules=["q_proj","k_proj","v_proj","o_proj","gate_proj","up_proj","down_proj"],
)

args = SFTConfig(
    output_dir=OUTPUT_DIR,
    num_train_epochs=3,
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,
    learning_rate=2e-4,
    logging_steps=10,
    eval_strategy="steps",
    eval_steps=50,
    save_steps=50,
    save_total_limit=2,
    bf16=torch.cuda.is_bf16_supported(),
    fp16=not torch.cuda.is_bf16_supported(),
    max_length=512,
    report_to="none",
    packing=False,
)

trainer = SFTTrainer(
    model=model,
    args=args,
    train_dataset=train_ds,
    eval_dataset=val_ds,
    processing_class=tokenizer,
    peft_config=peft_config,
    formatting_func=format_example,
)

trainer.train()
trainer.save_model(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)

print("Fine-tuning complete. Adapter saved to:", OUTPUT_DIR)
