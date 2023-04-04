import os
import openai
import argparse

MAX_INPUT_LENGTH = 50

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input

    print(f"User input: {user_input}")
    if user_input and len(user_input) < MAX_INPUT_LENGTH:
        get_movie_recommendation(user_input)
    else:
        raise ValueError(
            f"Input length is too long. Must be under {MAX_INPUT_LENGTH}. Submitted input is {user_input}"
        )

def get_movie_recommendation(prompt: str) -> str:
    # Load your API key from an environment variable or secret management service
    openai.api_key = os.getenv("OPENAI_API_KEY")
    # export OPENAI_API_KEY=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
    enriched_prompt = f"Recommend 3 movies with the topics of {prompt} with links to netflix"
    print(enriched_prompt)

    response = openai.Completion.create(
        engine="text-davinci-003", prompt=enriched_prompt, max_tokens=4000
    )

    # Extract output text.
    movie_list: str = response["choices"][0]["text"]

    # Strip whitespace.
    movie_list = movie_list.strip()

    print(f"Snippet: {movie_list}")
    return movie_list


if __name__ == "__main__":
    main()