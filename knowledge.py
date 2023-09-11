import json
from difflib import get_close_matches #allows match best responses

#load knowledge base from the JSON File
def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data
# save dict to knowledge base.
def save_knoledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)
        

 

