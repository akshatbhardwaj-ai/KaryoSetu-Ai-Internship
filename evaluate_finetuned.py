import json, re, torch, pandas as pd
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

BASE_MODEL = "meta-llama/Llama-3.2-3B-Instruct"
ADAPTER = "/content/karyosetu_lora"
TEST_FILE = "/content/karyosetu_finetuning/test.csv"

tokenizer = AutoTokenizer.from_pretrained(ADAPTER)
base = AutoModelForCausalLM.from_pretrained(BASE_MODEL, device_map="auto", torch_dtype="auto")
model = PeftModel.from_pretrained(base, ADAPTER)
model.eval()

df = pd.read_csv(TEST_FILE)

def predict(query):
    messages = [
        {"role":"system","content":"You are a service classification assistant. Classify the user's service request. Return only JSON with category and subcategory."},
        {"role":"user","content":f"Service query: {query}"}
    ]
    prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=80, do_sample=False)
    text = tokenizer.decode(out[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True).strip()
    m = re.search(r"\{.*\}", text, re.S)
    if not m:
        return None, None, text
    try:
        obj=json.loads(m.group(0))
        return obj.get("category"), obj.get("subcategory"), text
    except:
        return None, None, text

rows=[]
for _,r in df.iterrows():
    cat, sub, raw = predict(r["query"])
    rows.append({
        "query":r["query"],
        "expected_category":r["category"],
        "expected_subcategory":r["subcategory"],
        "predicted_category":cat,
        "predicted_subcategory":sub,
        "category_correct":cat==r["category"],
        "subcategory_correct":sub==r["subcategory"],
        "raw_output":raw
    })

out=pd.DataFrame(rows)
out.to_csv("/content/finetuned_evaluation_results.csv",index=False)

print("Category accuracy:", out["category_correct"].mean()*100)
print("Subcategory accuracy:", out["subcategory_correct"].mean()*100)
print("Both correct:", ((out["category_correct"]) & (out["subcategory_correct"])).mean()*100)
print("Saved: /content/finetuned_evaluation_results.csv")
