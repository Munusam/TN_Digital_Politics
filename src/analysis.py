from pathlib import Path
import pandas as pd

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

insta = pd.read_csv(DATA_DIR / "instagram_clean.csv")
yt = pd.read_csv(DATA_DIR / "youtube_clean.csv")

# Create engagement_rate here as well
insta["engagement_rate"] = (insta["likes"] + insta["comments"]) / insta["followers"]
yt["engagement_rate"] = (yt["likes"] + yt["comments"]) / yt["views"]

print("\nInstagram Engagement:")
print(insta.groupby("content_type")[["likes", "comments", "engagement_rate"]].mean())

print("\nYouTube Engagement:")
print(yt.groupby("content_type")[["views", "likes", "comments", "engagement_rate"]].mean())
