import matplotlib.pyplot as plt
import pandas as pd


def plot_engagement_by_content_type(summary: pd.DataFrame, metric: str, platform: str):
    plt.figure(figsize=(8, 5))
    plt.barh(summary["content type"], summary[f"avg_{metric}"])
    plt.xlabel(metric.replace("_", " ").title())
    plt.title(f"{platform}: {metric.replace('_', ' ').title()} by Content Type")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()
