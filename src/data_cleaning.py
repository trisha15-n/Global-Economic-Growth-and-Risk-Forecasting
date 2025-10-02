import pandas as pd
from src import config
from src.logger import logging
from src.exception import CustomException
import sys

def clean_wb_data(raw_file=None, save=True):
  try:
    logging.info("Starting data clenaing.")

    if raw_file is None:
      raw_file = config.RAW_DATA_DIR / "wbdata_raw.csv"

    df = pd.read_csv(raw_file)
    logging.info(f"Raw data shape: {df.shape}")

    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors="coerce")
        logging.info("Converted 'date' column to datetime.")

    missing_before = df.isnull().sum().sum()
    df.dropna(inplace=True)
    missing_after = df.isnull().sum().sum()
    logging.info(f"Dropped rows with missing values. Missing before: {missing_before}, after: {missing_after}. New shape: {df.shape}")

    sort_cols = [col for col in ['country', 'date'] if col in df.columns]
    if sort_cols:
        df.sort_values(by=sort_cols, inplace=True)
        df.reset_index(inplace=True, drop=True)
        logging.info(f"Sorted data by columns: {sort_cols}")

    if save:
      config.PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
      processed_file = config.PROCESSED_DATA_DIR / "wbdata_processed.csv"
      df.to_csv(processed_file, index=False)
      logging.info(f"Cleaned data saved to {processed_file}")

    return df
  except Exception as e:
    logging.error("Error occurred during data cleaning.")
    raise CustomException(e, sys)

if __name__ == "__main__":
    df = clean_wb_data()
    logging.info(f"Cleaned data shape: {df.shape}")
    logging.info(f"df.head():\n{df.head()}")    