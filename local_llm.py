
import os
import time
import pandas as pd
import ollama

DATASET_DIR = "dataset"
MODEL_NAME = "gemma3:1b"


def main():
    prompts_file = os.path.join(DATASET_DIR, "prompts.csv")

    prompts_df = pd.read_csv(prompts_file)
    responses = []
    history = []

    print("WEEK 8: LOCAL LLM INFERENCE")
    print("Model:", MODEL_NAME)
    print("Total prompts:", len(prompts_df))

    for _, row in prompts_df.iterrows():
        prompt = row["prompt"]

        print(f"\nPrompt {row['id']}: {prompt}")
        start_time = time.time()

        try:
            result = ollama.chat(
                model=MODEL_NAME,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                options={"temperature": 0.3}
            )

            response = result["message"]["content"]
            elapsed = round(time.time() - start_time, 2)

            print("Response:", response)

            responses.append({
                "id": row["id"],
                "domain": row["domain"],
                "model": MODEL_NAME,
                "prompt": prompt,
                "response": response,
                "word_count": len(response.split()),
                "response_time_seconds": elapsed
            })

            history.append(
                f"Prompt: {prompt}\n"
                f"Response: {response}\n"
                f"Response time: {elapsed} seconds\n"
                f"{'-' * 40}\n"
            )

        except Exception as error:
            print("Error:", error)

    if not responses:
        print("No responses generated. Check Ollama.")
        return

    df = pd.DataFrame(responses)

    df.to_csv(
        os.path.join(DATASET_DIR, "llm_responses.csv"),
        index=False,
        encoding="utf-8"
    )

    df[
        ["id", "domain", "model", "word_count",
         "response_time_seconds"]
    ].to_csv(
        os.path.join(DATASET_DIR, "response_comparison.csv"),
        index=False
    )

    with open(
        os.path.join(DATASET_DIR, "conversation_history.txt"),
        "w",
        encoding="utf-8"
    ) as file:
        file.writelines(history)

    print("\nProject completed successfully!")
    print("Check the dataset folder for generated files.")


if __name__ == "__main__":
    main()
