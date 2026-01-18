import pandas as pd


def content_type_distribution(df: pd.DataFrame) -> pd.DataFrame:
    """
    Computes platform-wise distribution of political content types.
    """
    distribution = (
        df.groupby(["platform", "content type"])
        .size()
        .reset_index(name="post_count")
    )

    distribution["percentage"] = (
        distribution.groupby("platform")["post_count"]
        .transform(lambda x: round(100 * x / x.sum(), 2))
    )

    return distribution
