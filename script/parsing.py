

import pandas as pd
from collections import Counter
import json



# --- Step 1: Load labeled text ---
file_path = "../data1/labeled_telegram_messages.txt"
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

# --- Step 2: Parse into sentence-level structure ---
sentences = []
current_sentence = []

for line in lines:
    if line.strip() == "":
        if current_sentence:
            sentences.append(current_sentence)
            current_sentence = []
    else:
        parts = line.strip().split()
        if len(parts) == 2:
            current_sentence.append((parts[0], parts[1]))
        else:
            current_sentence.append((parts[0], "O"))

if current_sentence:
    sentences.append(current_sentence)

print("\U0001F9BE Total sentences:", len(sentences))
print("\U0001F50E Example:", sentences[0])

# --- Step 3: Save as CoNLL-style text ---
with open("../data1/amharic_ner_data_conll.txt", "w", encoding="utf-8") as f:
    for sentence in sentences:
        for word, tag in sentence:
            f.write(f"{word}\t{tag}\n")
        f.write("\n")
print("\u2705 Saved as amharic_ner_data_conll.txt")

# --- Step 4: Optional tag distribution ---
all_tags = [tag for sentence in sentences for _, tag in sentence]
tag_counts = Counter(all_tags)
print("\U0001F4CA Tag distribution:", tag_counts)

# --- Step 5: Optional JSON format for Hugging Face datasets ---
ner_json = []
for sentence in sentences:
    words = [word for word, tag in sentence]
    tags = [tag for word, tag in sentence]
    ner_json.append({"tokens": words, "tags": tags})

with open("../data1/amharic_ner_dataset.json", "w", encoding="utf-8") as f:
    json.dump(ner_json, f, ensure_ascii=False, indent=2)

print("\U0001F4E6 Saved Hugging Face style NER dataset.")
