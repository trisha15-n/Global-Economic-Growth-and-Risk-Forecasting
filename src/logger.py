import logging
from pathlib import Path
from datetime import datetime


PROJECT_ROOT = Path(__file__).resolve().parent.parent
LOGS_DIR = PROJECT_ROOT / "logs"
LOGS_DIR.mkdir(parents=True, exist_ok=True)

log_file = LOGS_DIR / f"app_{datetime.now().strftime('%Y_%m_%d')}.log"

logging.basicConfig(
    filename=log_file,  
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)    

def info(msg):
    logging.info(msg)

def error(msg):
    logging.error(msg)