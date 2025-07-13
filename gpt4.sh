datasets=("Ref-Long-A")
prompt_types=("before")
task_types=("multi_stars_hard")
document_numbers=("24")

for dataset in "${datasets[@]}"
do
  for prompt in "${prompt_types[@]}"
  do
    for task in "${task_types[@]}"
    do
      for doc_num in "${document_numbers[@]}"
      do
        python3 gpt4o.py \
          --dataset "$dataset" \
          --prompt_type "$prompt" \
          --task_type "$task" \
          --document_numbers "$doc_num"
      done
    done
  done
done