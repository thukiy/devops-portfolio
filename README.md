# devops-portfolio

A small Python command-line program, built as the final project for the
CDS212 DevOps module at FH Graubünden. The project grows every week with
DevOps topics such as testing, CI/CD and containers.

## Prerequisites

- Python 3.10 or newer
- Git

## Installation / Setup

```bash
git clone https://github.com/thukiy/devops-portfolio.git
cd devops-portfolio
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Usage

```bash
devops-portfolio
# Hello, World!

devops-portfolio Thuki
# Hello, Thuki!
```

Without installing, you can also run it directly:

```bash
PYTHONPATH=src python3 -m devops_portfolio Thuki
# Hello, Thuki!
```
