# Module 3 Homework – Data Warehousing & BigQuery

CREATE OR REPLACE EXTERNAL TABLE `de-workshop-485417.homework3.yellow_tripdata_external`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://homework-03-alberto/yellow_tripdata_2024-*.parquet']
);

CREATE OR REPLACE TABLE `de-workshop-485417.homework3.yellow_tripdata_non_partitioned` AS
SELECT *
FROM `de-workshop-485417.homework3.yellow_tripdata_external`;

## Question 1: Counting records
Answer: 20,332,093

SELECT COUNT(*) 
FROM `de-workshop-485417.homework3.yellow_tripdata_external`;

## Question 2: Data read estimation
Answer: 0 MB for the External Table and 155.12 MB for the Materialized Table

-- Query on External Table
SELECT COUNT(DISTINCT PULocationID) 
FROM `de-workshop-485417.homework3.yellow_tripdata_external`;

-- Query on Materialized Table
SELECT COUNT(DISTINCT PULocationID) 
FROM `de-workshop-485417.homework3.yellow_tripdata_non_partitioned`;

## Question 3: Understanding columnar storage
Answer: BigQuery is a columnar database and scans only the columns requested in the query. Selecting more columns increases the amount of data read.

## Question 4: Counting zero fare trips
Answer: 8,333

SELECT COUNT(*)
FROM `de-workshop-485417.homework3.yellow_tripdata_non_partitioned`
WHERE fare_amount = 0;

## Question 5: Partitioning and clustering strategy
Answer: Partition by tpep_dropoff_datetime and Cluster on VendorID.

CREATE OR REPLACE TABLE `de-workshop-485417.homework3.yellow_tripdata_partitioned_clustered`
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID AS
SELECT * FROM `de-workshop-485417.homework3.yellow_tripdata_non_partitioned`;

## Question 6: Partition benefits
Answer: 310.24 MB for non-partitioned table and 26.84 MB for the partitioned table

-- Query on Materialized Table
SELECT DISTINCT VendorID
FROM `de-workshop-485417.homework3.yellow_tripdata_non_partitioned`
WHERE DATE(tpep_dropoff_datetime) BETWEEN '2024-03-01' AND '2024-03-15';

-- Query on Partitioned Table
SELECT DISTINCT VendorID
FROM `de-workshop-485417.homework3.yellow_tripdata_partitioned_clustered`
WHERE DATE(tpep_dropoff_datetime) BETWEEN '2024-03-01' AND '2024-03-15';

## Question 7: External table storage
Answer: GCP Bucket

## Question 8: Clustering best practices
Answer: False

## Question 9: Understanding table scans
Answer: 0 MB  
Explanation: BigQuery uses table metadata (cached statistics) to retrieve the total row count without scanning the actual column data.

SELECT COUNT(*) 
FROM `de-workshop-485417.homework3.yellow_tripdata_non_partitioned`;
