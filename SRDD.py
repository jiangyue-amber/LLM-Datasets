import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")


genai.configure(api_key=api_key)
model = genai.GenerativeModel("models/gemini-2.0-flash")


input_path = "/Users/amberjiang/Desktop/cs research/SRDD data/data_attribute_format.csv"
df = pd.read_csv(input_path)


def build_prompt(name, description, category):
    return f"""
        You are a software evaluation expert.

        Below is a software description. Please evaluate whether it satisfies each of the five design rules listed.

        Software Name: {name}
        Software Category: {category}
        Software Description: {description}

        The 5 Evaluation Rules:
        1. Describe the primary function of this software, emphasizing its simplicity, commonality, and feasibility in implementation.
        2. Craft a clear and comprehensive description that encapsulates all the essential information required to define the software's fundamental functionality.
        3. Specify that the software does not require internet access, highlighting its self-contained nature.
        4. This software can be realized without relying on real-world data sources.
        5. Highlight the software's user-friendliness, emphasizing that it can be operated by a single individual and does not necessitate multiple users for testing, in contrast to online chat software.

        Your Task:
        For each rule, respond with either ✅ or ❌ followed by a short explanation.
        Finally, give the total number of rules it satisfies as: CountObey: X
        """

sampled_df = df.sample(n=10, random_state=42)

for _, row in sampled_df.iterrows():
    name = row['Name']
    description = row['Description']
    category = row['Category']

    print(f"Software Name: {name}")
    print(f"Category: {category}")
    print(f"Description:\n{description}\n")

    prompt = build_prompt(name, description, category)
    response = model.generate_content(prompt)

    print("Gemini's Evaluation:")
    print(response.text.strip())
    print("\n" + "=" * 100 + "\n")
