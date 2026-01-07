from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RESULTS_DIR = BASE_DIR / "results" / "figures"

# Make sure results/figures exists
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

insta = pd.read_csv(DATA_DIR / "instagram_clean.csv")
yt = pd.read_csv(DATA_DIR / "youtube_clean.csv")

# Engagement rate
insta["engagement_rate"] = (insta["likes"] + insta["comments"]) / insta["followers"]
yt["engagement_rate"] = (yt["likes"] + yt["comments"]) / yt["views"]

# Plot engagement by content type
insta.groupby("content_type")["engagement_rate"].mean().plot(
    kind="bar", title="Instagram Engagement by Content Type"
)
plt.tight_layout()
plt.savefig(RESULTS_DIR / "insta_engagement.png")
plt.clf()

yt.groupby("content_type")["engagement_rate"].mean().plot(
    kind="bar", title="YouTube Engagement by Content Type"
)
plt.tight_layout()
plt.savefig(RESULTS_DIR / "yt_engagement.png")
plt.clf()

print("EDA done. Figures saved to results/figures/")
