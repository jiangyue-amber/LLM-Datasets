from datasets import load_dataset
import google.generativeai as genai
from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()
api_key = os.getenv("GEMINI_KEY")


genai.configure(api_key=api_key)
model = genai.GenerativeModel("models/gemini-2.0-flash")

def get_commit_info(repo,base_commit):
    key = os.getenv("GITHUB_KEY")
    headers = {
        "Authorization": f"token {key}",
    }
    url = f"https://api.github.com/repos/{repo}/commits/{base_commit}"
    response = requests.get(url, headers = headers)
    return response.json()

def create_prompt(problem_statement):
    pass

def ask_gemini():
    pass

def testing(test_patch):
    pass

ds = load_dataset("SWE-bench/SWE-bench_Lite")
test_split = ds['test']
sampled = test_split.shuffle().select(range(3))

output_dir = "results_SWE_bench"
os.makedirs(output_dir, exist_ok=True)

for instance in sampled:
    repo = instance["repo"]
    base_commit = instance["base_commit"]
    problem_statement = instance["problem_statement"]
    test_patch = instance["test_patch"]

    get_commit_info(repo,base_commit)