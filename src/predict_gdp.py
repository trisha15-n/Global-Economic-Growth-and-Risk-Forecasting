import pandas as pd
import os
import sys
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from src.logger import logging
from src.exception import CustomException

def train_gdp_model(input_path="data/processed/features_clustered.csv", output_model_path="models/rf_gdp_model.pkl"):
  try:
    logging.info("Starting GDP prediction model training")
    df = pd.read_csv(input_path)

    feature_cols = ["gdp_growth_lag1", 
            "inflation_lag1", "unemployment_lag1",
            "gdp_growth_roll3", "inflation_roll3", "unemployment_roll3",
            "gdp_percapita"]
    X = df[feature_cols]
    y = df["gdp_growth"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    
    logging.info(f"Model evaluation metrics: MSE={mse}, R2={r2}, MAE={mae}")

    os.makedirs(os.path.dirname(output_model_path), exist_ok=True)
    joblib.dump(model, output_model_path)
    logging.info(f"Model saved to {output_model_path}")

    return model, r2, mae, mse
  except Exception as e:
    logging.error("Error occurred during model training")
    raise CustomException(e, sys)

if __name__ == "__main__":
  model, r2, mae, mse = train_gdp_model()
  logging.info(f"Trained model R2: {r2}, MAE: {mae}, MSE: {mse}")
  import pandas as pd
  df = pd.read_csv("data/processed/features_clustered.csv")
  sample = df.head()[[
    "gdp_growth_lag1", "inflation_lag1", "unemployment_lag1",
        "gdp_growth_roll3", "inflation_roll3", "unemployment_roll3",
        "gdp_percapita"
  ]]
  pred = model.predict(sample)
  logging.info(f"Sample predictions: {pred}")
  
