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



