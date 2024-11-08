import sys
import requests

API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-3.1-405B"
headers = {"Authorization": "Bearer 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"}

def main():

    output = query({
    "inputs": "What's the capital of Colombia?",
    })

    print(output)

    sys.exit(0)

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

if __name__ == "__main__":
    main()
