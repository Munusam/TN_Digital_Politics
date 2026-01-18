import matplotlib.pyplot as plt
import pandas as pd


def plot_content_typology(distribution: pd.DataFrame) -> None:
    platforms = distribution["platform"].unique()

    for platform in platforms:
        subset = distribution[distribution["platform"] == platform]

        plt.figure(figsize=(8, 5))
        plt.barh(subset["content type"], subset["percentage"])
        plt.xlabel("Percentage (%)")
        plt.title(f"Political Content Types on {platform}")
        plt.tight_layout()
        plt.show()
