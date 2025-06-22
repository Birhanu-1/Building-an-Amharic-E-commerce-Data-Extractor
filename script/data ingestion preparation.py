import os
import zipfile
import pandas as pd
import re
import json
from pathlib import Path
from datetime import datetime
import emoji




# --- Step 1: Define paths ---
BASE_DIR = Path("../data1")
ZIP_PATH = BASE_DIR / "photos.zip"
IMAGES_DIR = BASE_DIR / "photos"
DATA_FILE = BASE_DIR / "telegram_data.csv"

# --- Step 2: Unzip images ---
if not IMAGES_DIR.exists():
    with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
        zip_ref.extractall(IMAGES_DIR)
    print("Images extracted.")
else:
    print("Images already extracted.")

# --- Step 3: Load Telegram data ---
try:
    df = pd.read_csv(DATA_FILE)
except:
    df = pd.read_json(DATA_FILE, lines=True)

df = df.rename(columns=str.lower)
print("Loaded messages:", df.shape)
print(df.head())

# --- Step 4: Normalize Amharic text ---
def clean_amharic(text):
    if not isinstance(text, str):
        return ""
    text = emoji.replace_emoji(text, replace='')
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text

#df["clean_text"] = df["text"].apply(clean_amharic)
df["clean_text"] = df["message"].apply(clean_amharic)

df["has_image"] = df["media path"].apply(lambda x: os.path.exists(IMAGES_DIR / str(x)) if pd.notna(x) else False)

# --- Step 5: Export cleaned data ---
df_filtered = df[["id", "clean_text", "media path", "has_image"]]
df_filtered.to_csv("../data1/preprocessed_telegram_data.csv", index=False)
print("Saved to /data1/preprocessed_telegram_data.csv")

# --- Step 6: Optional stats ---
price_mentions = df["clean_text"].str.contains(r"(ብር|\d+\s*birr|\d+\s*ብር)", na=False)
location_mentions = df["clean_text"].str.contains(r"(አዲስ\s?አበባ|ቦሌ|መገናኛ)", na=False)

print("Messages with price mentions:", price_mentions.sum())
print("Messages with location mentions:", location_mentions.sum())
