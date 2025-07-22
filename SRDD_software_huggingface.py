import pandas as pd
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from huggingface_hub import login
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("HUGGING_FACE_KEY")

login(token=api_key)

model_id = "Qwen/Qwen-7B"  # or do llama "codellama/CodeLlama-7b-Instruct-hf"
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto", trust_remote_code=True)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

input_path = "SRDD data/data_attribute_format.csv"
df = pd.read_csv(input_path)


def build_prompt(name, description, category):
    return f"""
        You are a software development expert.

        Below is a software description. Please write python script for this software. 
        **Important:** Return only the Python code as plain text, **do NOT include markdown formatting such as triple backticks (```) or any extra text.**

        Software Name: {name}
        Software Category: {category}
        Software Description: {description}
        """

sampled_df = df.sample(n=10)

output_dir = "results_SRDD_software_HF"
os.makedirs(output_dir, exist_ok=True)

for _, row in sampled_df.iterrows():
    name = row['Name']
    description = row['Description']
    category = row['Category']

    prompt = build_prompt(name, description, category)

    response = generator(prompt, max_new_tokens = 512, temperature = 0.7)[0]["generated_text"]
    llama_response = response.text.strip()
    if llama_response.startswith("```python") and llama_response.endswith("```"):
        parsed_response = llama_response[9:-3].strip()
    else:
        parsed_response = llama_response

    safe_name = name.replace(" ", "_").replace("/", "_")
    filename = f"results_{safe_name}_software_HF.py"
    filepath = f"{output_dir}/{filename}"

    header = (
        f"# Software Name: {name}\n"
        f"# Category: {category}\n"
        f"# Description: {description}\n\n"
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(header + parsed_response)