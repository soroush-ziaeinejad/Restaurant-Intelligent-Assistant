import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

with open(ROOT / "configs/config.yaml", encoding="utf-8") as f:
    CFG = yaml.safe_load(f)

RAW = ROOT / CFG["paths"]["raw"]
INTERMEDIATE = ROOT / CFG["paths"]["intermediate"]
PROCESSED = ROOT / CFG["paths"]["processed"]