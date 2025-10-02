import wbdata
import pandas as pd
from datetime import datetime
from src import config
import src.logger as logging
from src.exception import CustomException
import sys

def fetch_wb_data(country="all", save=True):

  try:
    logging.info("Starting data fetch process...")

    start = datetime(config.START_YEAR, 1, 1)
    end = datetime(config.END_YEAR, 1, 1)

    df = wbdata.get_dataframe(
        config.INDICATORS,  
        country,
        (start, end)        
    )
    df.reset_index(inplace=True)
    logging.info("Data fetch process completed successfully.")

    if save:
      config.RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
      raw_file = config.RAW_DATA_DIR / "wbdata_raw.csv"
      df.to_csv(raw_file, index=False)
      logging.info(f"Raw data saved to {raw_file}")

    return df
  except Exception as e:
    logging.error("Error occurred while fetching data.")
    raise CustomException(e, sys)
  

if __name__ == "__main__":
    df = fetch_wb_data()
    logging.info(f"Fetched data shape: {df.shape}")
    logging.info(f"df.head():\n{df.head()}")

     