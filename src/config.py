from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent[1]
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

OUTPUTS = BASE_DIR / "outputs"
MODELS_DIR = OUTPUTS / "models"
TABLEAU_DIR = OUTPUTS / "tableau"

for p in [DATA_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR, OUTPUTS, MODELS_DIR, TABLEAU_DIR]:
    p.mkdir(parents=True, exist_ok=True)

INDICATORS = {
    "NY.GDP.MKTP.KD.ZG": "gdp_growth",        
    "FP.CPI.TOTL.ZG": "inflation",          
    "SL.UEM.TOTL.ZS": "unemployment",       
    "SE.PRM.ENRR": "school_enrollment",     
    "SP.POP.TOTL": "population",            
    "NY.GDP.PCAP.KD": "gdp_percapita"
    }

START_YEAR = 2000
END_YEAR = 2023
