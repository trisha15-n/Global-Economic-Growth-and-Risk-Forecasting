import pandas as pd
import os
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from src.logger import logging
from src.exception import CustomException
import sys

def cluster_countries(input="data/processed/features.csv",
                      output="data/processed/features_clustered.csv",
                      n_clusters=3):
  try:
    logging.info("Starting country clustering process")
    df = pd.read_csv(input)
    clustering_features = ["gdp_growth_roll3", "inflation_roll3", "unemployment_roll3", "gdp_percapita"]
    X = df[clustering_features]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['cluster'] = kmeans.fit_predict(X_scaled)

    cluster_map = {0: "Stable", 1: "Emerging", 2: "Fragile"}
    df['cluster_label'] = df['cluster'].map(cluster_map)

    os.makedirs(os.path.dirname(output), exist_ok=True)
    df.to_csv(output, index=False)
    logging.info(f"Clustering completed and saved to {output}")
    return df
  except Exception as e:
    logging.error("Error occurred during country clustering")
    raise CustomException(e, sys)
  
if __name__ == "__main__":
  df_clustered = cluster_countries() 
  logging.info(f"Sample clusters:\n{df_clustered[['country','year','cluster_label']].head()}")
  logging.info(f"Clustered dataset shape: {df_clustered.shape}")
        