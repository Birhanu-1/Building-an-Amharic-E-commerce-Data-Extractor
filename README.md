# Building-an-Amharic-E-commerce-Data-Extractor

This project consists of two main tasks focusing on Ethiopian Telegram e-commerce channels data:

---
🔧 Setup Instructions
1. Clone the Repository
bash
git clone https://github.com/Birhanu-1/Building-an-Amharic-E-commerce-Data-Extractor.git
cd telegram-ner-labeling
2. Create a Virtual Environment (Recommended)
bash
python -m venv venv
source venv/bin/activate          # For macOS/Linux
venv\Scripts\activate             # For Windows
3. Install Dependencies
bash
pip install -r requirements.txt
🚀 How to Use
📥 Task 1: Ingest and Preprocess Telegram Data
Set up your Telegram API credentials in a .env file or config.py:

env
TG_API_ID=your_api_id
TG_API_HASH=your_api_hash
phone=+251XXXXXXXXX
Run the ingestion script:

bash
python ingest_telegram_data.py
📁 Preprocessed data is saved in the data/ folder.

📷 Media files are saved under data/photos/.

🏷️ Task 2: Label Dataset in CoNLL Format
Run the labeling script to tag messages for NER:

bash
python label_data.py
Output is saved as labeled_data.conll in CoNLL format.

You can adjust entity patterns in label_data.py.



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
