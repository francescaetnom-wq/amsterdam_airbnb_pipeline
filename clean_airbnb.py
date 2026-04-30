import pandas as pd

listings = pd.read_csv('listings.csv')
calendar = pd.read_csv('calendar.csv')
reviews = pd.read_csv('reviews.csv')

print(listings.shape)
print(calendar.shape)
print(reviews.shape)

print(listings.columns.tolist())
print(calendar.head())
print(reviews.head())

print(calendar[calendar['available'] == 't'].head())

print(calendar['price'].isna().sum())
print(calendar['available'].value_counts())
print(listings['price'].head(10))

listings['price'] = listings['price'].str.replace('$', '', regex=False).str.replace(',', '', regex=False)
listings['price'] = pd.to_numeric(listings['price'], errors='coerce')
listings = listings.dropna(subset=['price'])
listings = listings[listings['price'] < 2000]
print(listings['price'].describe())

listings_clean = listings[['id', 'neighbourhood_cleansed', 'room_type', 'price', 'review_scores_rating', 'number_of_reviews', 'availability_365']]
print(listings_clean.head())

listings_clean.to_csv('listings_clean.csv', index=False)

calendar_clean = calendar[['listing_id', 'date', 'available']]
calendar_clean.to_csv('calendar_clean.csv', index=False)
print('done')

reviews_clean = reviews[['listing_id', 'date', 'reviewer_id']]
reviews_clean.to_csv('reviews_clean.csv', index=False)
print('done')

from google.cloud import bigquery
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/francesca/Desktop/amsterdam housing analysis/chiave.json'

client = bigquery.Client(project='luminous-lambda-483816-p2')

table_id = 'luminous-lambda-483816-p2.amsterdam_airbnb.calendar_clean'

job = client.load_table_from_dataframe(calendar_clean, table_id)
job.result()
print('calendar caricato')

table_id = 'luminous-lambda-483816-p2.amsterdam_airbnb.reviews_clean'
job = client.load_table_from_dataframe(reviews_clean, table_id)
job.result()
print('reviews caricato')

print(reviews['date'].min())
print(reviews['date'].max())
