from pathlib import Path
import pandas as pd

# Get project root: .../TN_digital_politics
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

insta = pd.read_excel(DATA_DIR / "instagram.xlsx")
yt = pd.read_excel(DATA_DIR / "youtube.xlsx")

# Standardize column names
insta.columns = insta.columns.str.lower().str.replace(" ", "_")
yt.columns = yt.columns.str.lower().str.replace(" ", "_")

# Remove duplicates
insta.drop_duplicates(inplace=True)
yt.drop_duplicates(inplace=True)

# Handle missing values
insta.fillna(0, inplace=True)
yt.fillna(0, inplace=True)

# Save cleaned files back into data/
insta.to_csv(DATA_DIR / "instagram_clean.csv", index=False)
yt.to_csv(DATA_DIR / "youtube_clean.csv", index=False)

print("Cleaning done.")
