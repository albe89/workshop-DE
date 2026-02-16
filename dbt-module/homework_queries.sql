-- ============================================
-- Homework 4 - Analytics Engineering
-- Data Engineering Zoomcamp 2026
-- ============================================


-- ============================================================
-- Question 3
-- Count of records in fct_monthly_zone_revenue
-- Expected answer: 12,184
-- ============================================================

SELECT COUNT(*) AS total_records
FROM prod.fct_monthly_zone_revenue;



-- ============================================================
-- Question 4
-- Zone with highest revenue for Green taxis in 2020
-- Expected answer: East Harlem North
-- ============================================================

SELECT
    pickup_zone,
    revenue_month,
    service_type,
    revenue_monthly_total_amount,
    total_monthly_trips
FROM prod.fct_monthly_zone_revenue
WHERE service_type = 'Green'
  AND YEAR(revenue_month) = 2020
ORDER BY revenue_monthly_total_amount DESC
LIMIT 5;



-- ============================================================
-- Question 5
-- Total trips for Green taxis in October 2019
-- Expected answer: 384,624
-- ============================================================

SELECT COUNT(*) AS total_trips
FROM prod.int_trips
WHERE service_type = 'Green'
  AND YEAR(pickup_datetime) = 2019
  AND MONTH(pickup_datetime) = 10;



-- ============================================================
-- Question 6
-- Count of records in stg_fhv_tripdata
-- (dispatching_base_num IS NOT NULL filter applied in staging)
-- Expected answer: 43,244,693
-- ============================================================

SELECT COUNT(*) AS total_records
FROM prod.stg_fhv_tripdata;
