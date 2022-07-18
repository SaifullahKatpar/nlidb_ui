import requests


API_URL = "https://api-inference.huggingface.co/models/google/tapas-base-finetuned-wikisql-supervised"

headers = {"Authorization": f"Bearer {'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'}"}


def query(question, table_data):
    payload = {
        "inputs": {
            "query": question,
            "table":table_data},
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

