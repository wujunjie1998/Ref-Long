import json
import pdb
import re
import numpy as np
import os

evaluate_model = "gpt4o"
dataset = "Ref-Long-A"
prompt_types = ["before"]
task_types = ["multi_stars_hard"]
document_numbers = ["24"]

def extract_numbers_from_string(input_string):
    # Step 1: Check if "Document" is in the string
    if "Document" not in input_string:
        # return ""  # Return empty if "Document" is not found
        return ' '

    # Step 2: Extract part of string after "Document"
    try:
        # Extract the substring from 'Document' until the end or first newline
        relevant_part = input_string.split("Document", 1)[1].split('\n', 1)[0]

        # Find all numbers in the relevant part of the string
        numbers = re.findall(r'\d+', relevant_part)

        # Join the numbers with commas and return the result
        return ','.join(numbers)

    except IndexError:
        return ""  # In case there is no valid part after "Document"

def calculate_f1_score(prediction, ground_truth):
    prediction_set = set(prediction)
    ground_truth_set = set(ground_truth)

    true_positives = len(prediction_set.intersection(ground_truth_set))
    precision = true_positives / len(prediction_set) if prediction_set else 0
    recall = true_positives / len(ground_truth_set) if ground_truth_set else 0

    if precision + recall == 0:
        return 0  # Avoid division by zero
    f1_score = 2 * (precision * recall) / (precision + recall)
    return f1_score

for prompt in prompt_types:
    for task in task_types:
        for doc_num in document_numbers:

            result_list = []
            prediction_filename = f"{evaluate_model}_{prompt}_{task}_{doc_num}K.json"
            prediction_path = os.path.join("results", prediction_filename)

            with open(prediction_path, 'r') as file:
                multi = json.load(file)

            answer_filename = f"{task}_{doc_num}K_answers.json"
            answer_path = os.path.join("data", dataset, "answers", answer_filename)

            with open(answer_path, 'r') as file:
                multi_answers = json.load(file)

            correct_num = 0
            all_num = 0
            f1_scores = []

            for key in multi.keys():
                # string = multi[key][1]
                string = extract_numbers_from_string(multi[key][1])
                # Use regular expression to find all numbers in the string
                numbers = re.findall(r'\d+', string)

                # Convert the extracted numbers to integers
                numbers = list(map(int, numbers))
                answers = multi_answers[key][1]

                # calculate f1 score
                f1_scores.append(calculate_f1_score(numbers, answers))

                ## calculate accuracy and overlap percentage
                same_items = set(numbers) == set(answers)

                if same_items == True:
                    correct_num += 1
                all_num += 1

            print(task + " " + doc_num + "K Acc: " + str(correct_num / all_num))
            print(task + " " + doc_num + "K F1: " + str(np.array(f1_scores).mean()))
            print("\n")