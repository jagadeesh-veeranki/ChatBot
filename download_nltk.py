import os
import nltk

local_dir = os.path.join(os.getcwd(), 'nltk_data')
if not os.path.exists(local_dir):
    os.makedirs(local_dir)

nltk.data.path.append(local_dir)

print(f"Downloading NLTK data to {local_dir}...")

try:
    nltk.download('punkt', download_dir=local_dir)
    nltk.download('punkt_tab', download_dir=local_dir)
    nltk.download('wordnet', download_dir=local_dir)
    nltk.download('averaged_perceptron_tagger', download_dir=local_dir)
    print("Download complete.")
except Exception as e:
    print(f"Error downloading NLTK data: {e}")
