# datafun-03-analytics
# datafun-03-analytics

## Overview
This project demonstrates setting up a professional Python analytics environment, including creating a virtual environment, managing dependencies, and pushing code to GitHub.

## Project Structure
- `.venv/` - virtual environment (ignored by Git)
- `README.md` - this file
- `.gitignore` - defines files to be ignored
- `requirements.txt` - manages external dependencies
- `main.py` - main script file

## Dependencies
- `requests` - for making HTTP requests

## Setup Notes
- Virtual environment activated
- Used Git for version control
# DataFun-03-Analytics

## 📊 Project Overview

This project demonstrates basic data analytics skills using Python. It includes fetching data from the web, processing various file types (CSV, Excel, JSON, and TXT), and logging the output using a reusable logger.

## 👤 Author

**Name:** Robert Davis  
**Course:** Data Analytics with Python  
**Module:** Project 3 - Python Data Project  

---

## 🔧 Technologies Used

- Python 3.11+
- `requests` (for web API requests)
- `pandas` (for CSV and Excel processing)
- `openpyxl` (Excel backend)
- `json` (JSON parsing)
- Built-in `logging` module
- VS Code + GitHub + virtual environment (.venv)

---

## 📁 Project Structure

datafun-03-analytics/
├── data/
│ ├── posts.json # Fetched web API JSON
│ ├── sample_data.csv # Sample CSV data
│ ├── scores.xlsx # Sample Excel file
│ ├── sample.json # Sample JSON file
│ └── story.txt # Sample plain text file
├── utils_logger.py # Reusable logger setup
├── robertdavis_datafun_project.py # Main Python script
├── project.log # Log file for tracing execution
├── requirements.txt # Project dependencies
└── README.md # Project documentation

---

## 📥 Data Sources

- `posts.json`: Fetched using a web API (https://jsonplaceholder.typicode.com/posts)
- `sample_data.csv`: Sample student name, state, and score
- `scores.xlsx`: Excel version of the same data
- `sample.json`: Simple labeled animal records
- `story.txt`: A small fictional story written in plain text

---

## 🧠 What I Learned

- How to make web requests using `requests`
- How to load and summarize data with `pandas`
- The use of different data types (CSV, Excel, JSON, TXT)
- Writing modular, well-logged code using a reusable logger
- The value of structured logging over print statements
- How to work inside a Python virtual environment (.venv)

---
.