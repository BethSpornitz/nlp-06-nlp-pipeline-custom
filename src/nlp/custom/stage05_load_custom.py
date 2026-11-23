"""Stage 05: Load processed clinical fall-risk NLP results.

Author: Beth Spornitz
Date: 2026-11

Source: Pandas DataFrame containing both preprocessing versions.
Sink: data/processed/fall_risk_processed.csv

The CSV includes the original abstract features and the additional
metrics comparing stopwords removed versus stopwords retained.

The instructor's original CSV-writing logic is preserved.
"""

# ============================================================
# Section 1. Setup and Imports
# ============================================================

import logging
from pathlib import Path

from datafun_toolkit.logger import log_path
import pandas as pd

# ============================================================
# Section 2. Define Run Load Function
# ============================================================


def run_load(
    df: pd.DataFrame,
    processed_csv_path: Path,
    LOG: logging.Logger,
) -> None:
    """Write DataFrame to CSV sink.

    Args:
        df (pd.DataFrame): The DataFrame to write.
        processed_csv_path (Path): The path to save the processed CSV file.
        LOG (logging.Logger): The logger instance.

    Returns:
        None (just writes to the sink)
    """
    LOG.info("========================")
    LOG.info("STAGE 05: LOAD starting...")
    LOG.info("========================")

    df.to_csv(processed_csv_path, index=False)

    # Use the privacy-conscious
    # log_path function to log the sink path.
    log_path(LOG, "SINK PATH", processed_csv_path)
