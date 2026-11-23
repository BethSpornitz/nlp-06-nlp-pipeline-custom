"""Stage 04: Analyze clinical fall-risk vocabulary and stopword effects.

Author: Beth Spornitz
Date: 2026-11

Source: Analysis-ready Pandas DataFrame from the Transform stage.
Sink: Four visualizations saved to data/processed/.

======================================================================
THE ANALYST WORKFLOW: Analyze means look, not just calculate
======================================================================

Engineered features become more useful when we visualize them.

This stage uses the instructor's frequency-chart and word-cloud
techniques to compare two versions of the same research abstract:

    1. Stopwords removed
    2. Stopwords retained

Both versions use the same source text, lowercase normalization,
and punctuation filtering. Only stopword removal differs.

======================================================================
PURPOSE AND ANALYTICAL QUESTIONS
======================================================================

Purpose:
    Compare how stopword removal affects vocabulary patterns and
    interpretation of a clinical fall-risk research abstract.

Analytical Questions:
    - Which tokens occur most frequently in each version?
    - How do token counts and unique token counts differ?
    - How does the type-token ratio change?
    - Do the word clouds emphasize different vocabulary?
    - Which approach better highlights the clinical subject matter?

Outputs:
    - fall_risk_top_tokens.png
    - fall_risk_wordcloud.png
    - fall_risk_top_tokens_with_stopwords.png
    - fall_risk_wordcloud_with_stopwords.png
"""

# ============================================================
# Section 1. Setup and Imports
# ============================================================

from collections import Counter
import logging
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud

from nlp.custom.config_custom import (
    TOP_TOKENS_PATH,
    TOP_TOKENS_WITH_STOPWORDS_PATH,
    WORDCLOUD_PATH,
    WORDCLOUD_WITH_STOPWORDS_PATH,
)

# ============================================================
# Section 2. Define Helper Functions
# ============================================================


def _plot_top_tokens(
    tokens: list[str],
    top_n: int,
    output_path: Path,
    title: str,
    LOG: logging.Logger,
) -> None:
    """Plot a horizontal bar chart of the most frequent tokens.

    Args:
        tokens: List of tokens from the cleaned abstract.
        top_n: Maximum number of tokens to display.
        output_path: Location where the chart will be saved.
        title: Chart title.
        LOG: Logger instance.
    """
    # Counter maps each token to its frequency.
    # most_common() returns the highest-frequency tokens.
    counter = Counter(tokens)
    most_common = counter.most_common(top_n)

    if not most_common:
        LOG.warning("No tokens to plot: %s", title)
        return

    # Separate words and counts for plotting.
    words, counts = zip(*most_common, strict=False)

    # Reverse the order so the most frequent token appears at the top.
    _, ax = plt.subplots(figsize=(10, 6))

    ax.barh(
        list(reversed(words)),
        list(reversed(counts)),
        color="steelblue",
    )

    ax.set_xlabel("Frequency")
    ax.set_title(title)

    # Prevent chart labels from being clipped.
    plt.tight_layout()

    # Save the figure and release memory.
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=150)
    plt.close()

    LOG.info("  Saved bar chart to %s", output_path)


def _plot_wordcloud(
    text: str,
    output_path: Path,
    title: str,
    LOG: logging.Logger,
) -> None:
    """Generate and save a word cloud from cleaned text.

    Word size reflects token frequency.

    Args:
        text: Space-joined cleaned tokens.
        output_path: Location where the image will be saved.
        title: Word-cloud title.
        LOG: Logger instance.
    """
    if not text or text == "unknown":
        LOG.warning("No text available for word cloud: %s", title)
        return

    # Disable WordCloud's automatic stopword removal.
    # WHY: Stage 3 already controls whether stopwords are removed.
    # Allowing WordCloud to filter them again would invalidate
    # the comparison between the two preprocessing approaches.
    #
    # collocations=False also prevents WordCloud from combining
    # frequent word pairs into separate display entries.
    wc = WordCloud(
        width=800,
        height=400,
        background_color="white",
        max_words=80,
        colormap="viridis",
        stopwords=set(),
        collocations=False,
    ).generate(text)

    _, ax = plt.subplots(figsize=(12, 6))

    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    ax.set_title(title, fontsize=14)

    plt.tight_layout()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=150)
    plt.close()

    LOG.info("  Saved word cloud to %s", output_path)


# ============================================================
# Section 3. Define Run Analyze Function
# ============================================================


def run_analyze(
    df: pd.DataFrame,
    LOG: logging.Logger,
    output_dir: Path = Path("data/processed"),
    top_n: int = 20,
) -> None:
    """Analyze both preprocessing versions and create visualizations.

    Args:
        df: Analysis-ready DataFrame from Transform.
        LOG: Logger instance.
        output_dir: Directory for visualization outputs.
        top_n: Maximum number of tokens shown in each bar chart.
    """
    LOG.info("========================")
    LOG.info("STAGE 04: ANALYZE starting...")
    LOG.info("========================")

    output_dir.mkdir(parents=True, exist_ok=True)

    if df.empty:
        raise ValueError("Analyze stage received an empty DataFrame.")

    # Ensure the comparison fields exist before analysis.
    required_columns = [
        "tokens",
        "token_count",
        "unique_token_count",
        "type_token_ratio",
        "tokens_with_stopwords",
        "token_count_with_stopwords",
        "unique_token_count_with_stopwords",
        "type_token_ratio_with_stopwords",
    ]

    missing_columns = [
        column for column in required_columns if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(f"Missing required Analyze columns: {missing_columns}")

    # ============================================================
    # Phase 4.1: Extract tokens and summary statistics
    # ============================================================

    LOG.info("========================")
    LOG.info("PHASE 4.1: Extract tokens and summary statistics")
    LOG.info("========================")

    # This pipeline processes one research abstract.
    row = df.iloc[0]

    title: str = str(row.get("title", "unknown"))

    # Version 1: Stopwords removed
    tokens_str: str = str(row["tokens"])
    tokens: list[str] = tokens_str.split() if tokens_str else []

    token_count: int = int(row["token_count"])
    unique_token_count: int = int(row["unique_token_count"])
    type_token_ratio: float = float(row["type_token_ratio"])

    # Version 2: Stopwords retained
    tokens_with_stopwords_str: str = str(row["tokens_with_stopwords"])

    tokens_with_stopwords: list[str] = (
        tokens_with_stopwords_str.split() if tokens_with_stopwords_str else []
    )

    token_count_with_stopwords: int = int(row["token_count_with_stopwords"])

    unique_token_count_with_stopwords: int = int(
        row["unique_token_count_with_stopwords"]
    )

    type_token_ratio_with_stopwords: float = float(
        row["type_token_ratio_with_stopwords"]
    )

    abstract_word_count: int = int(row.get("abstract_word_count", 0))
    author_count: int = int(row.get("author_count", 0))

    LOG.info("  Paper: %s", title)
    LOG.info("  Abstract word count (raw): %s", abstract_word_count)
    LOG.info("  Author count: %s", author_count)

    LOG.info("STOPWORD COMPARISON:")
    LOG.info(
        "  Tokens without stopwords: %s",
        token_count,
    )
    LOG.info(
        "  Tokens with stopwords: %s",
        token_count_with_stopwords,
    )
    LOG.info(
        "  Unique tokens without stopwords: %s",
        unique_token_count,
    )
    LOG.info(
        "  Unique tokens with stopwords: %s",
        unique_token_count_with_stopwords,
    )
    LOG.info(
        "  TTR without stopwords: %.4f",
        type_token_ratio,
    )
    LOG.info(
        "  TTR with stopwords: %.4f",
        type_token_ratio_with_stopwords,
    )

    # Confirm that stored token counts match the token lists.
    if len(tokens) != token_count:
        raise ValueError(
            "Stopwords-removed token count does not match the stored token list."
        )

    if len(tokens_with_stopwords) != token_count_with_stopwords:
        raise ValueError(
            "Stopwords-retained token count does not match the stored token list."
        )

    # ============================================================
    # Phase 4.2: Frequency distributions - bar charts
    # ============================================================

    LOG.info("========================")
    LOG.info("PHASE 4.2: Token frequency comparison")
    LOG.info("========================")

    # First chart: Stopwords removed
    _plot_top_tokens(
        tokens=tokens,
        top_n=top_n,
        output_path=TOP_TOKENS_PATH,
        title=f"Top {top_n} Tokens (Stopwords Removed): {title}",
        LOG=LOG,
    )

    # Second chart: Stopwords retained
    _plot_top_tokens(
        tokens=tokens_with_stopwords,
        top_n=top_n,
        output_path=TOP_TOKENS_WITH_STOPWORDS_PATH,
        title=f"Top {top_n} Tokens (Stopwords Retained): {title}",
        LOG=LOG,
    )

    # ============================================================
    # Phase 4.3: Word clouds
    # ============================================================

    LOG.info("========================")
    LOG.info("PHASE 4.3: Word cloud comparison")
    LOG.info("========================")

    # First word cloud: Stopwords removed
    _plot_wordcloud(
        text=tokens_str,
        output_path=WORDCLOUD_PATH,
        title=f"Word Cloud (Stopwords Removed): {title}",
        LOG=LOG,
    )

    # Second word cloud: Stopwords retained
    _plot_wordcloud(
        text=tokens_with_stopwords_str,
        output_path=WORDCLOUD_WITH_STOPWORDS_PATH,
        title=f"Word Cloud (Stopwords Retained): {title}",
        LOG=LOG,
    )

    # ============================================================
    # Phase 4.4: Log top tokens for inline comparison
    # ============================================================

    LOG.info("========================")
    LOG.info("PHASE 4.4: Top token summaries")
    LOG.info("========================")

    # Stopwords removed
    counter = Counter(tokens)
    top_tokens = counter.most_common(top_n)

    LOG.info("TOP TOKENS: STOPWORDS REMOVED")
    for rank, (word, count) in enumerate(top_tokens, start=1):
        LOG.info("  %3d. %-30s %s", rank, word, count)

    # Stopwords retained
    counter_with_stopwords = Counter(tokens_with_stopwords)
    top_tokens_with_stopwords = counter_with_stopwords.most_common(top_n)

    LOG.info("TOP TOKENS: STOPWORDS RETAINED")
    for rank, (word, count) in enumerate(
        top_tokens_with_stopwords,
        start=1,
    ):
        LOG.info("  %3d. %-30s %s", rank, word, count)

    # ============================================================
    # Phase 4.5: Summarize the comparison
    # ============================================================

    LOG.info("========================")
    LOG.info("PHASE 4.5: Comparison summary")
    LOG.info("========================")

    tokens_removed = token_count_with_stopwords - token_count

    unique_tokens_removed = unique_token_count_with_stopwords - unique_token_count

    LOG.info(
        "  Tokens removed by stopword filtering: %s",
        tokens_removed,
    )
    LOG.info(
        "  Difference in unique token counts: %s",
        unique_tokens_removed,
    )

    LOG.info(
        "  TTR (stopwords removed): %.4f",
        type_token_ratio,
    )
    LOG.info(
        "  TTR (stopwords retained): %.4f",
        type_token_ratio_with_stopwords,
    )

    LOG.info("Sink: visualizations saved to data/processed/")
    LOG.info("Analysis complete.")
