# Building-an-Amharic-E-commerce-Data-Extractor

This project consists of two main tasks focusing on Ethiopian Telegram e-commerce channels data:

---
## 🔧 **Setup Instructions**

### **1. Clone the Repository**

```bash
git clone https://github.com/your-username/telegram-ner-labeling.git
cd telegram-ner-labeling
```

### **2. Create a Virtual Environment (Recommended)**

```bash
python -m venv venv
source venv/bin/activate          # For macOS/Linux
venv\Scripts\activate             # For Windows
```

### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

---

## 🚀 **How to Use**

### 📥 **Task 1: Ingest and Preprocess Telegram Data**

1. Configure your Telegram API credentials in a `.env` file:

```env
TG_API_ID=your_api_id
TG_API_HASH=your_api_hash
phone=+251XXXXXXXXX
```

2. Run the ingestion script:

```bash
python ingest_telegram_data.py
```

- **Preprocessed data:** saved in the `data/` folder  
- **Downloaded media:** stored in `data/photos/`

---

### 🏷️ **Task 2: Label Dataset in CoNLL Format**

Label product, price, and location entities in Amharic messages:

```bash
python label_data.py
```

- **Output:** `labeled_data.conll`  
- Adjust patterns in `label_data.py` to fine-tune labeling logic
## Task 3: Fine-Tune NER Model
## 🔧 Setup Instructions
Use Google Colab or any GPU-enabled environment.

## Install required libraries:
pip install transformers datasets evaluate seqeval pandas
## Ensure your labeled CoNLL-format data is converted to a Python dictionary like:
data = {
    "tokens": [["በአዲስ", "አበባ"]],
    "ner_tags": [[0, 1, 2, 3]]  # Use correct tag IDs
}
Load and tokenize using a pre-trained model (e.g. Davlan/afroxlmr-base or bert-tiny-amharic).

## Fine-tune with Hugging Face Trainer:
from transformers import Trainer, TrainingArguments
## Save the model locally after training:

trainer.save_model("./amharic-ner-model")
## Task 4: Model Comparison & Selection
## 🔧 Setup Instructions
## Train and save multiple models (XLM-Roberta, mBERT, DistilBERT).

## Evaluate with seqeval:
pip install seqeval evaluate
#  Compare on:
 F1 Score
 Training time
 Inference speed

## Generate plots with:

import matplotlib.pyplot as plt
Choose the best model and log your selection rationale (e.g., accuracy vs resource trade-offs).

## Task 5: Model Interpretability
## 🔧 Setup Instructions
## Install interpretable libraries:
pip install shap lime
Use a small sample (e.g., "በአዲስ አበባ አሸንፏል") for testing.

## Run SHAP for transformer models:

 import shap
 Use LIME for local prediction insights:
 from lime.lime_text import LimeTextExplainer
## Generate report:

  SHAP plot
  LIME feature importance
  Save in .json or .html

## Task 6: Vendor Scorecard
## 🔧 Setup Instructions
## Prepare your local scraped CSV with columns:

mathematica
Channel Title, Channel Username, ID, Message, Date
## Install necessary libraries:

pip install pandas

## Update your script to rename and parse:
vendor_df.rename(columns={
    'Channel Title': 'vendor_id',
    'Message': 'text',
    'Date': 'timestamp',
    'ID': 'views'
}, inplace=True)
## Extract metrics:

   -- Avg. Views
   -- Posts/Week
   -- Avg. Price (ETB)
   -- Top Product
   -- Lending Score

### Generate a scorecard:

pd.DataFrame([...]).to_csv("vendor_scorecard.csv")




