# Amsterdam Airbnb Market Analysis
### An end-to-end data pipeline project: Python · BigQuery · Power BI

## What this project is

This project is primarily a data engineering exercise. Starting from three raw CSV files downloaded from Inside Airbnb, I built a complete ETL pipeline: data cleaning and transformation in Python, cloud storage in Google BigQuery, and a multi-page analytical dashboard in Power BI.

The dataset covers Amsterdam listings as of September 2025 and includes approximately 10,000 listings, 3.8 million calendar rows, and 500,000 reviews.

## Dashboard

![Page 1](screenshots:s1.png)
![Page 2](screenshots:s2.png)
![Page 3](screenshots:s3.png)

## Tech Stack

- Python (pandas, google-cloud-bigquery)
- Google BigQuery
- Power BI Desktop

## Pipeline Architecture

Raw CSVs → Python cleaning script → BigQuery (3 tables: listings, calendar, reviews) → Power BI data model with relationships → Dashboard

## What the data says

Amsterdam's short-term rental market is heavily concentrated in the centre, but the most interesting story is elsewhere. Centrum-Oost leads in revenue potential with an average of around €60K per listing annually, followed by Centrum-West and Zuid — no surprises there.

What is surprising is Bijlmer-Oost. It sits at the bottom of the revenue ranking but records the highest occupancy rate in the city. The likely explanation is simple: there are very few listings in that area, so the ones that exist get booked almost by default. It's a supply constraint, not genuine excess demand — and it's worth noting as a limitation of reading occupancy rate in isolation.

On the question of price and quality, the data is pretty clear: above €500 per night, higher price does not correlate with higher review scores. Amsterdam's premium listings appear to sell on location and aesthetics rather than on delivering a measurably better guest experience.

The review trend over time tells the Covid story everyone lived through — a sharp collapse in 2020, a slow recovery through 2021 and 2022, and a full rebound by 2023 that continued growing into 2025.

## Limitations

The calendar dataset contains future availability windows, not historical booking records, so occupancy rate is estimated from availability flags rather than confirmed bookings. The dataset is also a single snapshot in time and does not reflect real-time market conditions.

## How to Run

1. Clone the repo
2. Add your Google Cloud service account key as `chiave.json` (excluded from version control)
3. Install dependencies: `pip install pandas google-cloud-bigquery pyarrow`
4. Run `clean_airbnb.py`
5. Dashboard screenshots available in the screenshots/ folder