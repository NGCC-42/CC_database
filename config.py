# config.py

from pathlib import Path
import os

# -----------------------------
# PATHS
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
IMAGES_DIR = DATA_DIR / "Images"
PARQUET_DIR = DATA_DIR / "parquet"
EXPORT_DIR = BASE_DIR / "exports"

# -----------------------------
# STREAMLIT SETTINGS
# -----------------------------
APP_TITLE = "Club Cannon Database"
APP_ICON = IMAGES_DIR / "club-cannon-icon-black.png"
LAYOUT = "wide"
SIDEBAR_STATE = "collapsed"


# -----------------------------
# DATE CONSTANTS
# -----------------------------
MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

MONTHS_ALL_OPTION = ["All"] + MONTHS
YEARS = [2022, 2023, 2024, 2025, 2026]
MONTHS_X = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# -----------------------------
# ENVIRONMENT SETTINGS
# -----------------------------
ENV = os.getenv("ENV", "development")
DEBUG = ENV == "development"





"""
bom_cost_jet = {'Pro Jet': 290.86, 'Quad Jet': 641.43, 'Micro Jet': 243.57, 'Cryo Clamp': 166.05}
bom_cost_control = {'The Button': 141.07, 'Shostarter': 339.42, 'Shomaster': 667.12}
bom_cost_hh = {'8FT - No Case': 143.62, '8FT - Travel Case': 219.06, '15FT - No Case': 153.84, '15FT - Travel Case': 231.01}
bom_cost_hose = {'2FT MFD': 20.08, '3.5FT MFD': 22.50, '5FT MFD': 24.25, '5FT STD': 31.94, '5FT DSY': 31.84, '5FT EXT': 33.24, '8FT STD': 32.42, '8FT DSY': 34.52, '8FT EXT': 34.82, '15FT STD': 43.55, '15FT DSY': 46.47, '15FT EXT': 46.77, '25FT STD': 59.22, '25FT DSY': 61.87, '25FT EXT': 62.17, '35FT STD': 79.22, '35FT DSY': 81.32, '35FT EXT': 81.62, '50FT STD': 103.57, '50FT EXT': 105.97, '100FT STD': 183.39}
bom_cost_acc = {'CC-AC-CCL': 29.17, 'CC-AC-CTS': 6.70, 'CC-F-DCHA': 7.15, 'CC-F-HEA': 6.86, 'CC-AC-RAA': 11.94, 'CC-AC-4PM': 48.12, 'CC-F-MFDCGAJIC': 7.83, ' CC-AC-CGAJIC-SET': 5.16, 'CC-AC-CGAJIC-SET': 5.16, 'CC-AC-CGAJIC-SET - 1': 5.16, 'CC-CTC-20': 10.92, 'CC-CTC-50': 19.36, 'CC-AC-TC': 89.46, 'CC-VV-KIT': 29.28, 
                'CC-RC-2430': 847, 'CC-AC-LA2': 248.10, 'CC-SW-05': 157.24, 'CC-NPTC-06-STD': 10.99, 'CC-NPTC-10-DSY': 18.90, 'CC-NPTC-15-DSY': 27.08, 'CC-NPTC-25-DSY': 39.37}
bom_cost_mfx = {'MagicFX Commander': 355.73, 'Magic FX Smoke Bubble Blaster': 3328.63, 'MagicFX ARM SFX SAFETY TERMINATOR': 12.50, 'MagicFX Device Updater': 38.37, 'MagicFX PSYCO2JET': 1158.63, 'MagicFX Red Button': 61.23, 'MagicFX Replacement Keys': 7.27, 
                'MagicFX SFX Safety ARM Controller': 616.13, 'MagicFX SPARXTAR': 1623.63, 'MagicFX Sparxtar powder': 19.84, 'MagicFX StadiumBlaster': 2893.56, 'MagicFX StadiumBlower': 2858.90, 'MagicFX StadiumShot III': 2321.13, 'MagicFX SuperBlaster II': 1468.63, 
                'MagicFX Swirl Fan II': 1406.63, 'MagicFX Switchpack II': 448.73, 'MFX-AC-SBRV': 328.68, 'MFX-E2J-230': 3282.40, 'MFX-E2J-2LFA': 97, 'MFX-E2J-5LFCB': 128, 'MFX-E2J-F-ID': 30.45, 'MFX-E2J-F-OD': 37.92, 'MFX-E2J-FC': 673.48, 'MFX-E2J-FEH-1M': 46, 'MFX-E2J-FEH-2M': 69, 
                'MFX-E2J-OB': 46, 'MFX-ECO2JET-BKT': 193, 'MFX-SS3-RB': 136.13}
"""