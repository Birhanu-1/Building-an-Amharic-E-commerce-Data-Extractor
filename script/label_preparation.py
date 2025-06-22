


import re
import pandas as pd


def extract_product_price_location(text):
    # Convert to string safely (handle NaN or missing)
    if not isinstance(text, str):
        text = ''  # or str(text) if you want
    
    price_pattern = r'(\b\d{1,3}(?:,\d{3})*(?:\.\d+)?\s*(?:ETB|birr|\$|USD)?\b)'
    location_pattern = r'(?:in|at|from|located in|from)\s+([A-Z][a-zA-Z\s]+)'
    
    price_match = re.search(price_pattern, text, re.IGNORECASE)
    location_match = re.search(location_pattern, text, re.IGNORECASE)
    
    price = price_match.group(1).strip() if price_match else "N/A"
    location = location_match.group(1).strip() if location_match else "N/A"
    
    cutoffs = []
    if price_match:
        cutoffs.append(price_match.start())
    if location_match:
        cutoffs.append(location_match.start())
    cutoff = min(cutoffs) if cutoffs else len(text)
    
    product = text[:cutoff].strip()
    
    return product, price, location

def process_telegram_data_and_save_txt(input_csv, output_txt, text_column='clean_text'):
    df = pd.read_csv(input_csv)
    
    # Fill NaN in text column with empty string to avoid errors
    df[text_column] = df[text_column].fillna('')
    
    extracted = df[text_column].apply(extract_product_price_location)
    df[['product', 'price', 'location']] = pd.DataFrame(extracted.tolist(), index=df.index)
    
    with open(output_txt, 'w', encoding='utf-8') as f:
        for idx, row in df.iterrows():
            f.write(f"Message: {row[text_column]}\n")
            f.write(f"Product: {row['product']}\n")
            f.write(f"Price: {row['price']}\n")
            f.write(f"Location: {row['location']}\n")
            f.write("-" * 40 + "\n")
    
    print(f"Labeled messages saved to {output_txt}")

# Example usage
if __name__ == '__main__':
    input_file = '../data1/preprocessed_telegram_data.csv'
    output_file = '../data1/labeled_telegram_messages.txt'
    
    process_telegram_data_and_save_txt(input_file, output_file)