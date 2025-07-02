from datasets import load_dataset
import google.generativeai as genai
from dotenv import load_dotenv
import os
import requests

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
    data=response.json()

    commit_message = data["commit"]["message"]
    changed_files = []
    for file in data.get("files", []):
        filename = file["filename"]
        patch = file.get("patch", "[no diff available]")
        changed_files.append({
            "filename": filename,
            "patch": patch
        })

    print(commit_message)
    print(changed_files)

    return {
        "message": commit_message,
        "files": changed_files
    }

def create_prompt(problem_statement, commit_info):
    prompt = f"""You are an expert software engineer. Help fix the bug described below.
    Problem:{problem_statement}
    Commit Message and Code Changes (before the bug was fixed): {commit_info}
    Please suggest a fix by writing a patch, do not give explanation other than the patch itself.
    """
    return prompt.strip()

def ask_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text.strip()

def testing(test_patch):
    pass

ds = load_dataset("SWE-bench/SWE-bench_Lite")
test_split = ds['test']
sampled = test_split.shuffle().select(range(5))

output_dir = "results_SWE_bench"
os.makedirs(output_dir, exist_ok=True)

for instance in sampled:
    repo = instance["repo"]
    id = instance["instance_id"]
    base_commit = instance["base_commit"]
    problem_statement = instance["problem_statement"]
    test_patch = instance["test_patch"]
    golden_patch = instance["patch"]

    commit_info = get_commit_info(repo,base_commit)
    prompt = create_prompt(problem_statement,commit_info)
    response = ask_gemini(prompt)

    safe_name = id.replace(" ", "_").replace("/", "_")
    filename = f"results_{safe_name}_software.txt"
    filepath = f"{output_dir}/{filename}"

    header = (
        f"Repo: {repo}\n"
        f"Repo ID: {id}\n"
        f"Problem Statement: {problem_statement}\n\n"
        f"GenAI's Patch:\n"
    )

    PR_patch = (
        f"\n\nGolden Patch: {golden_patch}\n"
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(header + response + PR_patch)
