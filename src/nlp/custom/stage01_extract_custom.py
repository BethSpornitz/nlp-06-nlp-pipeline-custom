"""Stage 01: Extract HTML for the custom clinical fall-risk NLP pipeline.

Original author: Denise Case
Modified by: Beth Spornitz
Modification date: 2026-11


Source: arXiv abstract page configured in config_custom.py.
Sink: Raw HTML file configured as RAW_HTML_PATH.

Retrieves the HTML document, saves it locally, and returns
the content for validation and subsequent NLP processing.
"""
# ============================================================
# Section 1. Setup and Imports
# ============================================================

import logging
from pathlib import Path

from datafun_toolkit.logger import log_path
import requests

# ============================================================
# Section 2. Define Run Extract Function
# ============================================================


def run_extract(
    source_url: str,
    http_request_headers: dict,
    raw_html_path: Path,
    LOG: logging.Logger,
) -> str:
    """Extract HTML data from the web page and save it to a file.

    Args:
        source_url (str): The URL of the web page.
        http_request_headers (dict[str, str]): The HTTP request headers.
        raw_html_path (Path): The path to save the raw HTML file.
        LOG (logging.Logger): The logger instance.

    Returns:
        str: The extracted HTML content as a string.

    Raises:
        requests.HTTPError: If the HTTP request to the web page fails.
        requests.RequestException: For other types of request exceptions.
        ValueError: If the response content cannot be parsed as HTML.
    """
    LOG.info("========================")
    LOG.info("STAGE 01: EXTRACT starting... ")
    LOG.info("========================")

    LOG.info(f"EXTRACT: Fetching HTML from {source_url}")

    # Use the requests.get() function to make an HTTP GET request
    # to the source_url with the provided headers.
    response = requests.get(source_url, headers=http_request_headers, timeout=30)

    # Use the raise_for_status() method to check for HTTP errors
    # and raise an exception if the request was unsuccessful.
    response.raise_for_status()

    # Use the .text attribute of the response object to get the HTML content
    # and store it in a variable called html_content.
    html_content: str = response.text

    # Use the write_text() method of the raw_html_path to
    # save the raw HTML data to a file.
    # Specify the encoding as "utf-8" to ensure proper handling of special characters.
    raw_html_path.write_text(html_content, encoding="utf-8")

    # Use log.info() to log the source URL (a string).
    # Use a formatted string (f-string) to include the variable in the log message.
    LOG.info(f"SOURCE URL = {source_url}")

    # Use the privacy-conscious
    # log_path function to log the sink path.
    log_path(LOG, "SINK PATH", raw_html_path)

    # Return the extracted HTML content as a string.
    return html_content
