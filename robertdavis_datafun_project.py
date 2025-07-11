# robertdavis_datafun_project.py

import json
import pandas as pd
import requests
from utils_logger import logger


def fetch_json_and_save():
    """Fetch data from a sample API and save it to a local file."""
    url = "https://jsonplaceholder.typicode.com/posts"
    logger.info("Fetching data from API...")
    try:
        response = requests.get(url)
        logger.info(f"Status code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            output_file = "data/web_data.json"
            with open(output_file, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
            logger.info("Success! Saving content to data folder.")
        else:
            logger.warning("Failed to fetch data.")
    except Exception as e:
        logger.error(f"Error fetching data: {e}")


def process_csv_file(filepath):
    """Read and summarize a CSV file."""
    logger.info(f"Reading CSV file: {filepath}")
    try:
        df = pd.read_csv(filepath)
        logger.info(f"CSV data:\n{df}")
        summary = df.describe(include='all')
        logger.info(f"CSV summary:\n{summary}")
    except Exception as e:
        logger.error(f"Error reading CSV file: {e}")


def process_excel_file(filepath):
    """Read and summarize an Excel file."""
    logger.info(f"Reading Excel file: {filepath}")
    try:
        df = pd.read_excel(filepath)
        logger.info(f"Excel data:\n{df}")
        summary = df.describe()
        logger.info(f"Excel summary:\n{summary}")
    except Exception as e:
        logger.error(f"Error reading Excel file: {e}")


def process_json_file(filepath):
    """Read and display JSON file content."""
    logger.info(f"Reading JSON file: {filepath}")
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
            logger.info(f"JSON data:\n{data}")
            logger.info(f"Number of records: {len(data)}")
    except Exception as e:
        logger.error(f"Error reading JSON file: {e}")


def process_text_file(filepath):
    """Read and display lines in a text file."""
    logger.info(f"Reading text file: {filepath}")
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            lines = file.readlines()
            logger.info(f"Line count: {len(lines)}")
            for i, line in enumerate(lines):
                logger.info(f"Line {i+1}: {line.strip()}")
    except Exception as e:
        logger.error(f"Error reading text file: {e}")


def main():
    logger.info("Starting main function")

    # Fetch JSON data from web and save
    fetch_json_and_save()

    # Local file processing
    process_csv_file("data/sample_data.csv")
    process_excel_file("data/scores.xlsx")
    process_json_file("data/sample.json")
    process_text_file("data/story.txt")

    logger.info("All processing complete")


if __name__ == "__main__":
    main()
