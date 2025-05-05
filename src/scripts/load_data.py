import os
import duckdb
from src.utils.database_utils import spin_down_database


def main():
    DATASET_URL = os.getenv("DATASET_URL")
    if not DATASET_URL:
        raise ValueError("DATASET_URL environment variable is not set.")

    splits = {'train': 'train.csv', 'test': 'test.csv'}
    database_folder = "./src/database"
    os.makedirs(database_folder, exist_ok=True)
    database_path = os.path.join(database_folder, "prompts_database.duckdb")

    # Create DB
    con = duckdb.connect(database=database_path)

    # Load train and test datasets to DB
    for split_name, split_file in splits.items():
        hf_url = f"{DATASET_URL}{split_file}"
        con.execute(
            f"CREATE TABLE {split_name}_data AS SELECT * FROM read_csv_auto('{hf_url}', strict_mode=false, null_padding=true, ignore_errors=true)")
        print(f"Successfully loaded {split_name} dataset.")

    # Verify loaded data
    for split_name in splits.keys():
        result = con.execute(
            f"SELECT COUNT(*) FROM {split_name}_data").fetchall()
        print(f"Loaded {result[0][0]} rows into {split_name}_data.")

    # Close DB connection
    con.close()
    spin_down_database(con, database_folder, splits)
    print(
        f"DuckDB database saved to {database_path} and spun down to Parquet files.")


if __name__ == "__main__":
    main()
