# data_extraction.py

import csv
import requests
import boto3

class DataExtractor:
    """A utility class for extracting data from different sources."""

    def __init__(self):
        # Initialize any attributes or resources here
        pass

    # def extract_from_csv(self, file_path):
    #     """Extract data from a CSV file and return a list of dictionaries."""
    #     data = []
    #     with open(file_path, "r") as csv_file:
    #         reader = csv.DictReader(csv_file)
    #         for row in reader:
    #             data.append(row)
    #     return data

    # def extract_from_api(self, url, params=None):
    #     """Extract data from an API and return a JSON object."""
    #     response = requests.get(url, params=params)
    #     response.raise_for_status()
    #     data = response.json()
    #     return data

    # def extract_from_s3(self, bucket_name, key):
    #     """Extract data from an S3 bucket and return a bytes object."""
    #     s3 = boto3.client("s3")
    #     response = s3.get_object(Bucket=bucket_name, Key=key)
    #     data = response["Body"].read()
    #     return data

    



