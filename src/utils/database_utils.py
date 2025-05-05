import os
import duckdb


def spin_down_database(con, output_folder, splits):
    """
    Spins down the DuckDB database into Parquet files after verifying the server state.

    Args:
        con (duckdb.DuckDBPyConnection): Active DuckDB connection.
        output_folder (str): Folder to save the Parquet files.
        splits (dict): Dictionary of dataset splits (e.g., {'train': 'train.csv', 'test': 'test.csv'}).
    """
    # Verify the state of the database server
    if con is None or not isinstance(con, duckdb.DuckDBPyConnection):
        raise ValueError("Invalid or inactive DuckDB connection.")

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Export each table to a Parquet file
    for split_name in splits.keys():
        parquet_file = os.path.join(
            output_folder, f"{split_name}_data.parquet")
        con.execute(
            f"COPY {split_name}_data TO '{parquet_file}' (FORMAT PARQUET)")
        print(f"Exported {split_name}_data to {parquet_file}.")

    print("Database successfully spun down to Parquet files.")
