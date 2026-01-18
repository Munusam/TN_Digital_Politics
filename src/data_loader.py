import pandas as pd
from pathlib import Path


DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def load_instagram_data() -> pd.DataFrame:
    df = pd.read_excel(DATA_DIR / "data.xlsx")
    df.columns = df.columns.str.lower().str.strip()
    df["platform"] = "Instagram"
    return df


def load_youtube_data() -> pd.DataFrame:
    df = pd.read_excel(DATA_DIR / "you.xlsx")
    df.columns = df.columns.str.lower().str.strip()
    df["platform"] = "YouTube"
    return df


def load_combined_data() -> pd.DataFrame:
    insta = load_instagram_data()
    yt = load_youtube_data()
    return pd.concat([insta, yt], ignore_index=True)
