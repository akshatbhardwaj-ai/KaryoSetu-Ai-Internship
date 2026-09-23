# Karyosetu Fine-tuning Package

This package prepares the uploaded 3,500-query labelled dataset for supervised fine-tuning.

## Split
- train.csv / train.jsonl
- validation.csv / validation.jsonl
- test.csv / test.jsonl

The split is stratified on category + subcategory with random seed 42.

## Fine-tuning
The included `finetune_colab.py` uses:
- Meta Llama 3.2 3B Instruct
- Supervised Fine-Tuning (SFT)
- LoRA / 4-bit QLoRA
- Hugging Face Transformers + TRL + PEFT

Run it in a GPU-enabled Kaggle environment.

## Evaluation
The held-out `test.csv` is not used for training. After fine-tuning, run `evaluate_finetuned.py` to calculate category, subcategory, and joint accuracy.

Do not claim an accuracy number until the fine-tuning and held-out test evaluation has actually been executed.

## Important
This is a fine-tuning experiment using a smaller open model rather than training the 70B Groq endpoint itself. The current Groq/Llama 3.3 70B setup can remain as the baseline/inference system for comparison.
