"""Configuration for the custom clinical fall-risk NLP pipeline.

Author: Beth Spornitz
Date: 2026-11

Source: arXiv paper 2510.20714

Stores the source URL, HTTP headers, and output paths for
the custom Extract, Validate, Transform, Analyze, Load
(EVTAL) pipeline.
"""

from pathlib import Path

# ============================================================
# WEB DOCUMENT CONFIGURATION
# ============================================================

PAGE_URL: str = "https://arxiv.org/abs/2510.20714"

HTTP_REQUEST_HEADERS: dict = {
    "User-Agent": "Mozilla/5.0 (educational-use; web-mining-course)"
}

# ============================================================
# PATH CONFIGURATION
# ============================================================

ROOT_PATH: Path = Path.cwd()
DATA_PATH: Path = ROOT_PATH / "data"

RAW_PATH: Path = DATA_PATH / "raw"
PROCESSED_PATH: Path = DATA_PATH / "processed"

# Custom output files
RAW_HTML_PATH: Path = RAW_PATH / "fall_risk_raw.html"

PROCESSED_CSV_PATH: Path = PROCESSED_PATH / "fall_risk_processed.csv"

TOP_TOKENS_PATH: Path = PROCESSED_PATH / "fall_risk_top_tokens.png"

WORDCLOUD_PATH: Path = PROCESSED_PATH / "fall_risk_wordcloud.png"

# Visualization outputs with stopwords retained
TOP_TOKENS_WITH_STOPWORDS_PATH: Path = (
    PROCESSED_PATH / "fall_risk_top_tokens_with_stopwords.png"
)

WORDCLOUD_WITH_STOPWORDS_PATH: Path = (
    PROCESSED_PATH / "fall_risk_wordcloud_with_stopwords.png"
)
