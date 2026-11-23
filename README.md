# nlp-06-nlp-pipeline-custom

[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](pyproject.toml)
[![CI](https://github.com/BethSpornitz/nlp-06-nlp-pipeline-custom/actions/workflows/ci-python-zensical.yml/badge.svg)](https://github.com/BethSpornitz/nlp-06-nlp-pipeline-custom/actions/workflows/ci-python-zensical.yml)
[![Documentation](https://img.shields.io/badge/docs-site-blue?logo=github)](https://BethSpornitz.github.io/nlp-06-nlp-pipeline-custom/)

[![uv managed](https://img.shields.io/badge/uv-managed-DE5FE9)](https://docs.astral.sh/uv/)
[![ty type checked](https://img.shields.io/badge/ty-type_checked-2F80ED)](https://docs.astral.sh/ty/)
[![Zensical docs](https://img.shields.io/badge/Zensical-docs-purple)](https://zensical.org/)
[![MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

> A reproducible natural language processing pipeline for analyzing vocabulary patterns in academic research on clinical fall-risk assessment.

## Project Overview

**Author:** Beth Spornitz
**Date:** 2026 November
**Course:** Web Mining and Applied NLP — Project 06

This project demonstrates a complete natural language processing (NLP) pipeline for retrieving, cleaning, analyzing, and interpreting text from academic web documents.

The project builds on techniques introduced in earlier course modules, including web extraction, text preprocessing, structured data transformation, and visualization.

It extends the Extract, Validate, Transform, Load (EVTL) architecture by adding an explicit Analyze stage.

The resulting architecture is **Extract, Validate, Transform, Analyze, Load (EVTAL)**.

The repository includes the instructor's original example pipeline and a separate custom implementation that analyzes an academic paper related to clinical fall-risk assessment.

The custom project investigates how stopword removal affects token frequencies, vocabulary diversity, and the interpretation of text.

Project configuration and dependencies are managed through [pyproject.toml](pyproject.toml).

## Original Example Project

The original example was developed by Denise Case for the Web Mining and Applied NLP course.

**Original repository:** [nlp-06-nlp-pipeline](https://github.com/denisecase/nlp-06-nlp-pipeline)

**Original source:** [Agents of Chaos — arXiv 2602.20021](https://arxiv.org/abs/2602.20021)

The example demonstrates an integrated NLP pipeline that retrieves an academic paper's abstract page from arXiv.

The pipeline extracts bibliographic metadata, cleans and tokenizes the abstract, calculates vocabulary measures, generates visualizations, and saves the processed results.

The original Python files are preserved in `src/nlp/` to maintain a working reference implementation.

## Technical Modification to the Original Example

I modified `src/nlp/stage04_analyze.py` to display the 15 most frequent tokens instead of 20. This produces a more focused frequency chart and terminal summary.

The modified pipeline ran successfully, and the underlying text statistics remained unchanged. The original example and my separate clinical fall-risk implementation are both retained in this repository.

## Custom Project: Clinical Fall-Risk Assessment

### Research Document

The custom project analyzes the academic paper:

**An Interpretable Data-Driven Approach to Optimizing Clinical Fall Risk Assessment**

**Source:** [arXiv 2510.20714](https://arxiv.org/abs/2510.20714)

This paper was selected during Module 5 and is reused in Module 6 to extend the earlier HTML extraction work into a complete NLP analysis.

The topic is relevant to healthcare quality improvement and patient safety.

### Analytical Question

**How does stopword removal affect the vocabulary patterns and interpretation of an academic paper about clinical fall-risk assessment?**

The analysis examines the frequency and diversity of words in the paper's abstract.

Two preprocessing approaches are compared:

1. **Stopwords removed:** Common stopwords are excluded to emphasize potentially meaningful vocabulary.
2. **Stopwords retained:** Common stopwords remain in the text to provide a comparison of token frequencies and vocabulary measures.

The comparison examines how preprocessing decisions influence the resulting analysis.

### Project Objectives

The custom project uses an EVTAL pipeline to:

- Retrieve and preserve the academic paper's HTML.
- Validate the expected HTML structure.
- Extract the title, authors, abstract, and document metadata.
- Clean and tokenize the abstract using spaCy.
- Calculate total and unique token counts.
- Calculate type-token ratios.
- Identify frequently occurring tokens.
- Generate token frequency charts and word clouds.
- Compare results with and without stopword removal.
- Save structured data and visualization artifacts.
- Interpret the vocabulary patterns and limitations of the analysis.

## Data

Both the original and custom projects retrieve academic paper abstract pages from arXiv.

The source documents contain bibliographic and textual information, including:

- Paper title.
- Authors.
- Abstract text.
- Subject categories.
- Submission information.
- arXiv identifier.

The pipeline preserves the original HTML and transforms the extracted information into structured, analysis-ready data.

The custom implementation uses separate output filenames to prevent its results from overwriting the instructor's example artifacts.

## Methods and Approach

The project uses a modular Python pipeline organized into five stages.

### Stage 1: Extract

Requests retrieves the HTML document from arXiv.

The original HTML is preserved for inspection and reproducibility.

### Stage 2: Validate

BeautifulSoup parses the HTML document.

The validation stage checks for required elements before the data is transformed.

### Stage 3: Transform

The pipeline extracts document metadata and processes the abstract text using spaCy.

Text preprocessing includes tokenization, normalization, punctuation filtering, and configurable stopword removal.

Derived NLP features include:

- Raw abstract word count.
- Cleaned token count.
- Unique token count.
- Type-token ratio.
- Author count.

The **type-token ratio (TTR)** is calculated as:

`TTR = unique token count / total token count`

The ratio provides a basic measure of vocabulary diversity.

### Stage 4: Analyze

The Analyze stage uses token frequency distributions to identify recurring vocabulary.

The analysis includes:

- Frequency counts using Python's `Counter`.
- Horizontal bar charts of frequently occurring tokens.
- Word clouds showing relative word frequency.
- Comparison of token counts and type-token ratios across preprocessing approaches.

The stopword comparison evaluates how removing common words changes the patterns visible in the results.

### Stage 5: Load

Pandas organizes the processed data into a structured dataset.

The pipeline saves the results to CSV files and preserves the generated visualizations.

Execution information is recorded through logging.

## Preprocessing Comparison

The custom project compares two approaches to processing the same academic abstract.

| Feature | Stopwords Removed | Stopwords Retained |
|---|---|---|
| Source document | Clinical fall-risk paper | Clinical fall-risk paper |
| Tokenization | spaCy | spaCy |
| Text normalization | Applied | Applied |
| Punctuation filtering | Applied | Applied |
| Stopword filtering | Applied | Not applied |
| Token frequency analysis | Included | Included |
| Type-token ratio | Calculated | Calculated |
| Visualizations | Generated | Generated |

This comparison isolates stopword removal as the primary preprocessing difference.

The analysis considers whether removing common words improves the visibility of topic-related vocabulary or eliminates information that may be meaningful.

## Project Structure

The original example files are preserved in `src/nlp/`.

Custom processing files are organized separately in `src/nlp/custom/`.

```text
nlp-06-nlp-pipeline-custom/
├── README.md
├── pyproject.toml
├── zensical.toml
├── src/
│   └── nlp/
│       ├── __init__.py
│       ├── config.py
│       ├── pipeline_web_html.py
│       ├── stage01_extract.py
│       ├── stage02_validate.py
│       ├── stage03_transform.py
│       ├── stage04_analyze.py
│       ├── stage05_load.py
│       └── custom/
│           ├── __init__.py
│           ├── config_custom.py
│           ├── pipeline_web_html_custom.py
│           ├── stage01_extract_custom.py
│           ├── stage02_validate_custom.py
│           ├── stage03_transform_custom.py
│           ├── stage04_analyze_custom.py
│           └── stage05_load_custom.py
├── data/
│   ├── raw/
│   └── processed/
├── docs/
├── tests/
└── .github/
    └── workflows/
```

The original and custom pipelines use separate configuration values and output filenames.

## Run the Project

Follow the [Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/) to prepare the development environment.

Open the repository in VS Code and run commands from the project root.

### Run the Original Example

```powershell
uv run python -m nlp.pipeline_web_html
```

### Run the Custom Pipeline

```powershell
uv run python -m nlp.custom.pipeline_web_html_custom
```

The custom pipeline processes the clinical fall-risk assessment paper and supports the two preprocessing approaches used in the comparison.

## Results and Visualizations

The pipelines produce structured datasets, execution logs, and visualizations.

### Original Example Outputs

- `project.log` — pipeline execution log.
- `data/raw/case_raw.html` — original HTML.
- `data/processed/case_processed.csv` — processed dataset.
- `data/processed/case_top_tokens.png` — token frequency chart.
- `data/processed/case_wordcloud.png` — word cloud.

### Custom Project Outputs

The custom project uses the following output naming convention:

- `data/raw/fall_risk_raw.html`
- `data/processed/fall_risk_processed.csv`
- `data/processed/fall_risk_top_tokens.png`
- `data/processed/fall_risk_wordcloud.png`

Additional comparison outputs distinguish between stopwords-removed and stopwords-retained processing.

The final analytical results, visualizations, and interpretations are presented in the [project documentation](https://BethSpornitz.github.io/nlp-06-nlp-pipeline-custom/).

## Interpretation and Limitations

The analysis examines whether the most frequently occurring tokens reflect the topic of clinical fall-risk assessment and how preprocessing affects those patterns.

Token frequencies provide information about recurring vocabulary but do not independently establish the meaning or importance of a term.

Type-token ratios provide a measure of vocabulary diversity but can be influenced by document length and preprocessing decisions.

The analysis is limited to the abstract of one academic paper. Its vocabulary patterns may not represent the entire article or the broader clinical research literature.

Additional limitations include potential information loss during cleaning and the inability of simple frequency counts to capture context, negation, or relationships between words.

Detailed findings and comparisons are documented in `docs/index.md`.

## Verification

Run the automated tests:

```powershell
uv run python -m pytest
```

Run linting, formatting, and type checks:

```powershell
uv run ruff check . --fix
uv run ruff format .
uv run ty check
```

Build the documentation:

```powershell
uv run python -m zensical build
```

These checks support reproducibility and help identify implementation problems.

## Project Documentation

The project documentation is published using Zensical and GitHub Pages.

**Hosted documentation:** [Module 6 Custom Project Documentation](https://BethSpornitz.github.io/nlp-06-nlp-pipeline-custom/)

The documentation presents the analytical question, data source, preprocessing methods, NLP features, visualizations, results, interpretation, and limitations.

Additional background about traditional NLP and language models is available in [NLP Evolution](docs/nlp-evolution.md).

## CI/CD and GitHub Actions

The repository includes GitHub Actions for continuous integration and documentation deployment.

- [CI: Python and Documentation Checks](https://github.com/BethSpornitz/nlp-06-nlp-pipeline-custom/actions/workflows/ci-python-zensical.yml)
- [CD: Documentation Deployment](https://github.com/BethSpornitz/nlp-06-nlp-pipeline-custom/actions/workflows/deploy-zensical.yml)

These workflows support automated project verification and publication.

## Developer Reference

Follow the [Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/) for detailed setup instructions and troubleshooting.

### Initialize and Update the Python Environment

Run each command from the VS Code terminal:

```powershell
uvx pup-clean --delete
uv self update
uv python pin 3.14
uv python install
uv lock --upgrade
uv sync
uv audit
```

### Set Up and Run Git Hooks

```powershell
uvx prek install --force
uvx prek update --freeze --cooldown-days 7

git add -A
uvx prek run --all-files
# Repeat if changes were made
uvx prek run --all-files
```

### Run Common Chores

```powershell
uv run ruff check . --fix
uv run ruff format .

uv run ty check
uv run python -m pytest
uv run python -m zensical build
```

### Git Add-Commit-Push to GitHub

After making useful changes, save the work to GitHub.

```powershell
git add -A
git commit -m "describe your changes in quotes"
git push -u origin main
```

## Developer Notes

- Use the **UP ARROW** and **DOWN ARROW** in the terminal to scroll through previous commands.
- Use **CTRL+F** to find text within a file.
- Preserve the instructor's original working example files.
- Keep custom code and configuration in `src/nlp/custom/`.
- Verify outputs and visualizations before documenting analytical findings.

## Developer Tools

- [uv](https://docs.astral.sh/uv/) — Python environments and dependencies.
- [Ruff](https://docs.astral.sh/ruff/) — Python linting and formatting, configured in [.ruff.toml](.ruff.toml).
- [ty](https://docs.astral.sh/ty/) — Python type checking.
- [pytest](https://docs.pytest.org/) — automated testing, configured in [.pytest.toml](.pytest.toml).
- [prek](https://prek.j178.dev/) — Git hooks and automated checks, configured in [prek.toml](prek.toml).
- [Zensical](https://zensical.org/) — documentation generation, configured in [zensical.toml](zensical.toml).
- [Requests](https://requests.readthedocs.io/) — HTTP requests.
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) — HTML parsing.
- [spaCy](https://spacy.io/) — linguistic text processing.
- [Pandas](https://pandas.pydata.org/) — structured data processing.
- [Matplotlib](https://matplotlib.org/) — data visualization.
- [WordCloud](https://amueller.github.io/word_cloud/) — vocabulary visualization.

## Links

- [Custom GitHub Repository](https://github.com/BethSpornitz/nlp-06-nlp-pipeline-custom)
- [Hosted Documentation](https://BethSpornitz.github.io/nlp-06-nlp-pipeline-custom/)
- [Original Instructor Repository](https://github.com/denisecase/nlp-06-nlp-pipeline)
- [Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/)
- [Citation](CITATION.cff)
- [License](LICENSE)
