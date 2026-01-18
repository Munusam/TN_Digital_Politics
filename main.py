from src.interpretation import (
    interpret_results,
    election_impact_conclusion
)

from src.data_loader import load_combined_data
from src.content_typology import content_type_distribution
from src.engagement_metrics import (
    compute_instagram_engagement,
    compute_youtube_engagement,
    aggregate_by_content_type
)
from src.amplification_index import compute_amplification_index
from src.visualization.content_typology_plot import plot_content_typology
from src.visualization.engagement_plots import plot_engagement_by_content_type
from src.visualization.amplification_plot import plot_amplification_index


def main():
    df = load_combined_data()

    # STEP 1: Content Typology
    typology = content_type_distribution(df)
    print("\n=== CONTENT TYPOLOGY DISTRIBUTION ===\n")
    print(typology)
    plot_content_typology(typology)

    # STEP 2: Engagement Metrics
    insta = compute_instagram_engagement(df)
    yt = compute_youtube_engagement(df)

    insta_engagement = aggregate_by_content_type(insta, "engagement_rate" )
    yt_engagement = aggregate_by_content_type(yt, "comment_intensity" )

    print("\n=== INSTAGRAM ENGAGEMENT RATE ===\n")
    print(insta_engagement)

    print("\n=== YOUTUBE COMMENT INTENSITY ===\n")
    print(yt_engagement)

    plot_engagement_by_content_type(insta_engagement, "engagement_rate", "Instagram")
    plot_engagement_by_content_type(yt_engagement, "comment_intensity", "YouTube")

    # STEP 3: Algorithmic Amplification
    insta_amp = compute_amplification_index(insta, "engagement_rate")
    yt_amp = compute_amplification_index(yt, "comment_intensity")

    print("\n=== INSTAGRAM AMPLIFICATION INDEX ===\n")
    print(insta_amp)

    print("\n=== YOUTUBE AMPLIFICATION INDEX ===\n")
    print(yt_amp)

    plot_amplification_index(insta_amp, "Instagram")
    plot_amplification_index(yt_amp, "YouTube")

    # STEP 4: Interpretation & Conclusion
    print(interpret_results(insta_amp, yt_amp))
    print(election_impact_conclusion())


if __name__ == "__main__":
    main()
