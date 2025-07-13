import pdb

from openai import OpenAI
import openai
import torch
import numpy as np
from tqdm import tqdm
import json
import random

import argparse
import os

## Import OpenAI Key
openai.organization = "your openai organization"
chatgpt_client = OpenAI(api_key='your openai key')

def setup_seed(seed):
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

setup_seed(2024)

parser = argparse.ArgumentParser(description="Run Counting Stars with specific task type and number of documents")
parser.add_argument("--dataset", type=str, required=True, help="The specific Ref-Long dataset")
parser.add_argument("--prompt_type", type=str, required=True, help="The prompt type (e.g., 'ori/before')")
parser.add_argument("--task_type", type=str, required=True, help="The task type (e.g., 'single_stars_easy')")
parser.add_argument("--document_numbers", type=int, required=True, help="Number of documents to sample")
args = parser.parse_args()

dataset = args.dataset
prompt_type = args.prompt_type
task_type = args.task_type
document_number = args.document_numbers

filename = f"{task_type}_{document_number}K.json"
filepath = os.path.join("data", dataset, prompt_type, filename)

with open(filepath, 'r') as file:
    all_prompts = json.load(file)

results = {}


for time in tqdm(range(100)):
    input_prompt = all_prompts[str(time)][1]
    test_number = all_prompts[str(time)][0]

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": input_prompt}]

    response = chatgpt_client.chat.completions.create(
        model="gpt-4o",

        messages=messages,
        temperature=0,
        top_p=1
    )
    
    results[str(time)] = (test_number, response.choices[0].message.content)
    os.makedirs("results", exist_ok=True)

    ## write the results
    output_filename = f"gpt4o_{prompt_type}_{task_type}_{document_number}K.json"
    output_path = os.path.join("results", output_filename)

    with open(output_path, 'w') as file:
        json.dump(results, file)

