import pandas as pd


def compute_amplification_index(
    df: pd.DataFrame,
    metric: str
) -> pd.DataFrame:
    """
    Computes algorithmic amplification index by content type.
    """
    baseline = df[metric].median()

    amplification = (
        df.groupby("content type")[metric]
        .mean()
        .reset_index(name=f"avg_{metric}")
    )

    amplification["amplification_index"] = (
        amplification[f"avg_{metric}"] / baseline
    )

    amplification = amplification.sort_values(
        by="amplification_index", ascending=False
    )

    return amplification
