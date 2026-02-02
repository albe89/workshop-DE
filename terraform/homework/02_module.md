# Homework 2: Workflow Orchestration - Answer Template

**Course:** Data Engineering Zoomcamp 2026  
**Email:** albe.tilo@gmail.com  
---

## Question 1
**Topic:** Yellow Taxi data uncompressed file size (2020-12)

**Answer:** 
- [-] 128.3 MiB
- [x] 134.5 MiB


**Explanation:** 
I check the size of the file in the bucket after the ingestion, but I also check the log in kestra after adding a - ls -lh {{render(vars.file)}} command, with the second method he give me 128.3mib
---

## Question 2
**Topic:** Rendered variable value for file

**Answer:** 
- [x] `green_tripdata_2020-04.csv`


**Explanation:** 
run it and this was the value
---

## Question 3
**Topic:** Yellow Taxi rows (all 2020 CSV files)

**Answer:** 
- [x] 24,648,499

**Explanation:** 
I did 2 queries in big query, one filtering the final table for only 2020 second with union of all intermediate table

---

## Question 4
**Topic:** Green Taxi rows (all 2020 CSV files)

**Answer:** 
- [x] 1,734,051

**Explanation:** 

I did 2 queries in big query, one filtering the final table for only 2020 second with union of all intermediate table

---

## Question 5
**Topic:** Yellow Taxi rows (March 2021)

**Answer:** 
- [x] 1,925,152

**Explanation:** 
details of table in BQ
---

## Question 6
**Topic:** Schedule trigger timezone configuration for New York

**Answer:** 
- [x] Add a timezone property set to America/New_York

**Explanation:** 
only solution possible, asked chatgpt for explanation
---


