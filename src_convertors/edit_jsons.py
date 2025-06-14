import os
import json
import csv
import unicodedata

# Normalize function to ensure consistency
def normalize(s):
    return unicodedata.normalize('NFC', s.strip())

# Load metadata CSV into dictionary
def load_metadata(meta_csv_path):
    meta = {}
    with open(meta_csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            key = normalize(row['filename'])
            meta[key] = {field: normalize(value) for field, value in row.items()}
    return meta

# Patch JSON files
def patch_json_folder(json_folder, meta_dict):
    for root, dirs, files in os.walk(json_folder):
        for filename in files:
            if filename.endswith('.json'):
                json_path = os.path.join(root, filename)
                with open(json_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                base_filename = normalize(os.path.splitext(filename)[0])

                if base_filename in meta_dict:
                    metadata = meta_dict[base_filename]

                    # Top-level metadata for legacy tools
                    data['meta'] = metadata

                    # Sentence-level metadata for Tsakorpus search/filtering
                    for sentence in data.get("sentences", []):
                        sent_meta = sentence.get("meta", {})
                        for k, v in metadata.items():
                            if k not in sent_meta:
                                sent_meta[k] = v
                        sentence["meta"] = sent_meta

                    print(f"✅ Updated top-level and sentence-level metadata for {filename}")
                else:
                    print(f"⚠️  No metadata found for {filename}")

                with open(json_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    meta_csv_path = 'corpus/meta.csv'
    json_folder = 'corpus/json'

    meta_dict = load_metadata(meta_csv_path)
    patch_json_folder(json_folder, meta_dict)
