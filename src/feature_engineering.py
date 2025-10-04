import pandas as pd
import os
from src.logger import logging
from src.exception import CustomException
import sys

def engineer_features(input_path="data/processed/wbdata_processed.csv",output_path="data/processed/features.csv"):
  try:
    logging.info("Starting Feature Engineering")

    df = pd.read_csv(input_path)
    df['date'] = pd.to_datetime(df['date'], errors='coerce', exact=False)
    df = df.dropna(subset=['date'])
    df['year'] = df['date'].dt.year

    df = df.sort_values(by=['country', 'year']).reset_index(drop = True)

    cols_to_fill = df.columns.difference(['country'])
    df[cols_to_fill] = df.groupby('country')[cols_to_fill].transform(lambda x: x.ffill().bfill())



    lag_features = ['gdp_growth', 'inflation', 'unemployment']
    for col in lag_features:
      df[f"{col}_lag1"] = df.groupby("country")[col].shift(1)

    for col in lag_features:
      df[f"{col}_roll3"] = df.groupby("country")[col].transform(lambda x: x.rolling(3, min_periods=1).mean())

    if "population" in df.columns and "gdp_percapita" not in df.columns:
      df['gdp_percapita'] = df['gdp_growth'] / df['population']

    df = df.dropna().reset_index(drop=True)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)

    logging.info(f"Feature Engineering Completed.")
    return df
  except Exception as e :
    logging.error("Error in Feature Engineering")
    raise CustomException(e, sys)
  

if __name__ == "__main__":
  df_features = engineer_features()
  logging.info(f"Features Shape: {df_features.shape}")
  logging.info(f"Sample Features:\n{df_features.head()}")  



  