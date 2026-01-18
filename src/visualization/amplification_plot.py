import matplotlib.pyplot as plt
import pandas as pd


def plot_amplification_index(
    amplification: pd.DataFrame,
    platform: str
) -> None:
    plt.figure(figsize=(8, 5))
    plt.barh(
        amplification["content type"],
        amplification["amplification_index"]
    )
    plt.axvline(1, linestyle="--")
    plt.xlabel("Amplification Index")
    plt.title(f"{platform}: Algorithmic Amplification by Content Type")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()
