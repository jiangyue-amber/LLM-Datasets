import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_KEY")


genai.configure(api_key=api_key)
model = genai.GenerativeModel("models/gemini-2.0-flash")


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

output_dir = "results_SRDD_software"
os.makedirs(output_dir, exist_ok=True)

for _, row in sampled_df.iterrows():
    name = row['Name']
    description = row['Description']
    category = row['Category']

    prompt = build_prompt(name, description, category)
    response = model.generate_content(prompt)
    gemini_response = response.text.strip()
    if gemini_response.startswith("```python") and gemini_response.endswith("```"):
        parsed_response = gemini_response[9:-3].strip()
    else:
        parsed_response = gemini_response

    safe_name = name.replace(" ", "_").replace("/", "_")
    filename = f"results_{safe_name}_software.py"
    filepath = f"{output_dir}/{filename}"

    header = (
        f"# Software Name: {name}\n"
        f"# Category: {category}\n"
        f"# Description: {description}\n\n"
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(header + parsed_response)