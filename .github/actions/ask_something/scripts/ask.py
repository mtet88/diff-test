import argparse
import sys
import os

from gpt4all import GPT4All

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ask like a tweet")
    parser.add_argument('prompt', type=str, help='Prompt')
    args = parser.parse_args()

    model = GPT4All(model_name="Meta-Llama-3-8B-Instruct.Q4_0.gguf", model_path="../LLM/", allow_download=False)

    response = model.generate(
        prompt=args.prompt,
        max_tokens=280,
        temp=0.2,         # Lower temperature for more deterministic output
        top_k=5,                 # Narrow down the token selection
        top_p=0.5,               # Focus on higher probability tokens
        repeat_penalty=1.5,  # Discourage repetition
        streaming=False,             # Stop at the end of the line
    )

    print(response)

    sys.exit(0)    
