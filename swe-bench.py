from datasets import load_dataset
import google.generativeai as genai

genai.configure(api_key="AIzaSyBKVgbAcfyJeP1SHttkM4LpksIWDLlhnSQ")
model = genai.GenerativeModel("models/gemini-2.0-flash")

def run_inference(example):
    problem_statement = example['problem_statement']
    base_commit = example['base_commit']

    print("Problem statement:\n", problem_statement)
    print("Base commit:\n", base_commit)

    prompt = f"""GitHub issue:
    {problem_statement}
    Base commit:
    {base_commit}
    Write a code patch that fixes this issue:"""

    print("Running Gemini inference...")
    response = model.generate_content(prompt)
    generated_patch = response.text

    print("Generated patch:\n", generated_patch)

def main():
    ds = load_dataset("SWE-bench/SWE-bench_Lite")

    for i in range(13):
        example = ds['dev'][i] # Or ds['test'][0]
        run_inference(example)
        print("\n" + "=" * 100 + "\n")

if __name__ == "__main__":
    main()
