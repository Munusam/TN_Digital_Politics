import pandas as pd


def interpret_results(
    insta_amp: pd.DataFrame,
    yt_amp: pd.DataFrame
) -> str:
    """
    Generates structured interpretation of algorithmic amplification.
    """

    insta_top = insta_amp.iloc[0]["content type"]
    yt_top = yt_amp.iloc[0]["content type"]

    interpretation = f"""
INTERPRETATION OF FINDINGS
--------------------------

1. Platform-Specific Political Visibility
Instagram algorithms disproportionately amplify '{insta_top}' political content,
indicating a preference for emotionally engaging and informal communication styles.

YouTube algorithms favor '{yt_top}' political content, highlighting the platform's
support for longer-form political discussion and interpretive narratives.

2. Algorithmic Mediation of Political Communication
The findings demonstrate that digital platforms do not operate as neutral channels.
Instead, algorithmic ranking systems selectively prioritize political narratives
that maximize engagement metrics.

3. Implications for Political Actors
Political parties and leaders are structurally incentivized to adapt their messaging
towards emotionally resonant, meme-based, or commentary-driven formats to achieve
greater visibility.

4. Implications for Democratic Discourse
Such algorithmic amplification may reduce the visibility of formal policy-oriented
communication, potentially reshaping public political understanding and voter attention.
"""

    return interpretation


def election_impact_conclusion() -> str:
    """
    Final conclusion answering the election impact question.
    """

    return """
FINAL CONCLUSION
----------------

Based on the analysis of political content on Instagram and YouTube, this study concludes
that social media platforms have the capacity to influence political communication in
Tamil Nadu through algorithmic amplification mechanisms.

While this study does not claim direct causality between social media engagement and voting
behavior, the preferential amplification of emotionally charged, satirical, and
commentary-based political content suggests that digital algorithms significantly shape
political visibility.

By influencing which political narratives gain prominence, social media platforms can
indirectly affect voter perception, agenda-setting, and political discourse. Therefore,
social media is likely to play an increasingly influential role in future Tamil Nadu
elections.
"""
