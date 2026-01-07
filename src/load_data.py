from pathlib import Path
import pandas as pd

# This file → .../TN_digital_politics/src/load_data.py
# parent → .../TN_digital_politics/src
# parent.parent → .../TN_digital_politics
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

insta = pd.read_excel(DATA_DIR / "instagram.xlsx")
yt = pd.read_excel(DATA_DIR / "youtube.xlsx")

print(insta.head())
print(yt.head())


print(insta.columns)
print(yt.columns)
print(insta.info())
print(yt.info())
