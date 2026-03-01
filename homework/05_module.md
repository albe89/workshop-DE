## Homework 5 – Answers

1. **Pipeline structure**  
   Answer: `.bruin.yml and pipeline/ with pipeline.yml and assets/`  
   Explanation: Bruin requires `.bruin.yml` at the project root and a `pipeline/` folder containing `pipeline.yml` plus the `assets/` directory.

2. **Materialization strategy**  
   Answer: `time_interval - incremental based on a time column`  
   Explanation: `time_interval` is designed to delete and re‑insert data only for the specified time window based on a time key.

3. **Overriding taxi_types**  
   Answer: `bruin run --var 'taxi_types=["yellow"]'`  
   Explanation: Pipeline variables are overridden with `--var` using JSON syntax for the value.

4. **Run asset with downstream dependencies**  
   Answer: `bruin run ingestion/trips.py --downstream`  
   Explanation: You point to the asset file and use `--downstream` to execute it and all dependent assets.

5. **Quality check for non‑NULL timestamps**  
   Answer: `name: not_null`  
   Explanation: The `not_null` check enforces that a column (like `pickup_datetime`) never contains NULLs.

6. **View dependency graph**  
   Answer: `bruin lineage`  
   Explanation: `bruin lineage` visualizes upstream and downstream asset dependencies for your pipeline.

7. **First run on new DuckDB database**  
   Answer: `--full-refresh`  
   Explanation: `--full-refresh` recreates tables from scratch, which is recommended for the first pipeline run.

