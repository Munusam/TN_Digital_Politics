import pandas as pd


def compute_instagram_engagement(df: pd.DataFrame) -> pd.DataFrame:
    insta = df[df["platform"] == "Instagram"].copy()

    insta["total_engagement"] = insta["likes"] + insta["comments"]
    insta["engagement_rate"] = insta["total_engagement"] / insta["followers"]

    return insta


def compute_youtube_engagement(df: pd.DataFrame) -> pd.DataFrame:
    yt = df[df["platform"] == "YouTube"].copy()

    yt["total_engagement"] = yt["likes"] + yt["comments"]
    yt["comment_intensity"] = yt["comments"] / yt["views"]

    return yt


def aggregate_by_content_type(df: pd.DataFrame, metric: str) -> pd.DataFrame:
    summary = (
        df.groupby("content type")[metric]
        .mean()
        .reset_index(name=f"avg_{metric}")
        .sort_values(by=f"avg_{metric}", ascending=False)
    )

    return summary
