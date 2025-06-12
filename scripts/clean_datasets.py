import pandas as pd
from pathlib import Path

def clean_accommodation_facts(path: Path) -> pd.DataFrame:
    """Load and clean accommodation facts data."""
    df = pd.read_csv(path)

    # Standardize column names to snake_case
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # Convert numeric columns where appropriate
    num_cols = ["room_count", "stars", "bookingdotcom_review_score", "latitude", "longitude"]
    for col in num_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Drop rows without a bookingdotcom_id since this field is required for joins
    if "bookingdotcom_id" in df.columns:
        df = df.dropna(subset=["bookingdotcom_id"])

    return df

def clean_market_otb(path: Path) -> pd.DataFrame:
    """Load and clean market occupancy data."""
    df = pd.read_csv(path)
    df.columns = [col.strip().lower() for col in df.columns]

    if "stay_date" in df.columns:
        df["stay_date"] = pd.to_datetime(df["stay_date"])

    return df

def combine_rate_files(rates_dir: Path) -> pd.DataFrame:
    """Combine all daily rate csv files into a single DataFrame."""
    all_files = sorted(rates_dir.glob("rates_*.csv"))
    frames = []
    for file in all_files:
        frame = pd.read_csv(file)
        frame.columns = [c.strip().lower() for c in frame.columns]
        frames.append(frame)
    combined = pd.concat(frames, ignore_index=True)

    if "stay_date" in combined.columns:
        combined["stay_date"] = pd.to_datetime(combined["stay_date"])
    if "extract_date" in combined.columns:
        combined["extract_date"] = pd.to_datetime(combined["extract_date"])

    return combined

def main(data_dir: Path = Path("Data")) -> None:
    clean_dir = data_dir / "clean"
    clean_dir.mkdir(exist_ok=True)

    acc_path = data_dir / "accommodation_facts.csv"
    market_path = data_dir / "market_otb.csv"
    rates_dir = data_dir / "Rates"

    acc_df = clean_accommodation_facts(acc_path)
    acc_df.to_csv(clean_dir / "accommodation_facts_clean.csv", index=False)

    market_df = clean_market_otb(market_path)
    market_df.to_csv(clean_dir / "market_otb_clean.csv", index=False)

    rates_df = combine_rate_files(rates_dir)
    rates_df.to_csv(clean_dir / "rates_combined.csv", index=False)

if __name__ == "__main__":
    main()
