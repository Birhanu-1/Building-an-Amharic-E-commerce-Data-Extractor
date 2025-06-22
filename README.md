# Building-an-Amharic-E-commerce-Data-Extractor
# Telegram Ethiopian E-Commerce Data Processing & Labeling

This project consists of two main tasks focusing on Ethiopian Telegram e-commerce channels data:

---

## Task 1: Data Ingestion and Data Preprocessing

**Goal:**  
Set up a data ingestion system to fetch messages (text, images, documents) from at least 5 Ethiopian Telegram e-commerce channels and prepare the raw data for entity extraction.

**Steps:**

- Identify and connect to relevant Ethiopian Telegram channels using a custom scraper.
- Implement a message ingestion system to collect data in real-time as it is posted.
- Preprocess text data by:
  - Tokenizing
  - Normalizing
  - Handling Amharic-specific linguistic features
- Clean and structure data into a unified format separating metadata (sender, timestamp) from message content.
- Store the preprocessed data in a structured format (e.g., CSV, JSON) for further analysis and labeling.

---

## Task 2: Label a Subset of Dataset in CoNLL Format

**Goal:**  
Label a subset (30-50 messages) of the dataset’s "Message" column using the CoNLL format for Named Entity Recognition (NER) focusing on Amharic text.

**Entity Types & Labels:**

| Entity   | Description                                 | Labels         |
|----------|---------------------------------------------|----------------|
| Product  | Product names (e.g., "Baby bottle")          | B-Product, I-Product |
| Location | Places (e.g., "Addis Abeba", "Bole")         | B-LOC, I-LOC    |
| Price    | Price expressions (e.g., "ዋጋ 1000 ብር")         | B-PRICE, I-PRICE|
| Outside  | Tokens not part of any entity                 | O              |

**CoNLL Format:**  
- One token per line followed by its entity label separated by space/tab.
- Blank lines separate messages.

**Example snippet:**

ዋጋ B-PRICE
1000 I-PRICE
ብር I-PRICE
በ O
Addis B-LOC
Abeba I-LOC
ላይ O
ታገዳለች O

Baby B-Product
bottle I-Product
ለ O
ልጆች O



**Output:**  
Save the labeled messages in a plain text `.txt` file in the CoNLL format.

---

## Dependencies

- Python 3.7+
- Telegram scraping libraries (e.g., Telethon)
- NLP libraries for Amharic text preprocessing (optional)

---

## Usage Notes

- For Task 1, you may use Telethon or other Telegram APIs to scrape and ingest channel messages.
- For Task 2, manual annotation or a semi-automated approach can be used to label entities in the extracted messages.
- The labeled dataset will help train or fine-tune NER models for Amharic e-commerce text.

---

Feel free to reach out for help with:

- Writing Telegram scrapers for Ethiopian channels
- Amharic text preprocessing techniques
- Creating scripts to convert labeled data into CoNLL format