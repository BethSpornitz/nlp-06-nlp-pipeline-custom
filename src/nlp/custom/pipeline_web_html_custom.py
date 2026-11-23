"""Run the custom EVTAL pipeline for clinical fall-risk research.

Original author: Denise Case
Modified by: Beth Spornitz
Modification date: 2026-11

Source: https://arxiv.org/abs/2510.20714

EVTAL: Extract, Validate, Transform, Analyze, Load.

Run from the project root:
    uv run python -m nlp.custom.pipeline_web_html_custom
"""

import logging

from datafun_toolkit.logger import get_logger, log_header, log_path

from nlp.custom.config_custom import (
    DATA_PATH,
    HTTP_REQUEST_HEADERS,
    PAGE_URL,
    PROCESSED_CSV_PATH,
    PROCESSED_PATH,
    RAW_HTML_PATH,
    RAW_PATH,
    ROOT_PATH,
)
from nlp.custom.stage01_extract_custom import run_extract
from nlp.custom.stage02_validate_custom import run_validate
from nlp.custom.stage03_transform_custom import run_transform
from nlp.custom.stage04_analyze_custom import run_analyze
from nlp.custom.stage05_load_custom import run_load

LOG: logging.Logger = get_logger("CI", level="DEBUG")


def main() -> None:
    """Execute the custom clinical fall-risk EVTAL pipeline."""
    log_header(LOG, "Module 6: CUSTOM CLINICAL FALL-RISK EVTAL PIPELINE")
    LOG.info("START CUSTOM PIPELINE")

    RAW_PATH.mkdir(parents=True, exist_ok=True)
    PROCESSED_PATH.mkdir(parents=True, exist_ok=True)

    log_path(LOG, "ROOT_PATH", ROOT_PATH)
    log_path(LOG, "DATA_PATH", DATA_PATH)
    log_path(LOG, "RAW_PATH", RAW_PATH)
    log_path(LOG, "PROCESSED_PATH", PROCESSED_PATH)

    # EXTRACT
    html_content = run_extract(
        source_url=PAGE_URL,
        http_request_headers=HTTP_REQUEST_HEADERS,
        raw_html_path=RAW_HTML_PATH,
        LOG=LOG,
    )

    # VALIDATE
    validated_soup = run_validate(
        html_content=html_content,
        LOG=LOG,
    )

    # TRANSFORM
    df = run_transform(
        soup=validated_soup,
        LOG=LOG,
    )

    # ANALYZE
    run_analyze(
        df=df,
        LOG=LOG,
    )

    # LOAD
    run_load(
        df=df,
        processed_csv_path=PROCESSED_CSV_PATH,
        LOG=LOG,
    )

    LOG.info("========================")
    LOG.info("Custom pipeline executed successfully!")
    LOG.info("========================")


if __name__ == "__main__":
    main()
