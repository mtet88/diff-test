import sys

from gpt4all import GPT4All

def main():

    if len(sys.argv) != 2:
        print("::error::One argument is required.")
        sys.exit(1)

    prompt = str(sys.argv[1])
    model_path = str(sys.argv[1])

    model = GPT4All(model_name="Meta-Llama-3-8B-Instruct.Q4_0.gguf", model_path=model_path, allow_download=True)

    response = model.generate(
        prompt=prompt,
        max_tokens=280,
        temp=0.2,         # Lower temperature for more deterministic output
        top_k=5,                 # Narrow down the token selection
        top_p=0.5,               # Focus on higher probability tokens
        repeat_penalty=1.5,  # Discourage repetition
        streaming=False,             # Stop at the end of the line
    )

    print(response)

    sys.exit(0)    

if __name__ == "__main__":
    main()
