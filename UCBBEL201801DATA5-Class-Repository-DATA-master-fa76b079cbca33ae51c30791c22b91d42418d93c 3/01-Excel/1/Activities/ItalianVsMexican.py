# Dependencies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
import seaborn
from scipy.stats import ttest_ind

# Yelp API Key
ykey_id = "1GwZyE0zIjSujpHtlMnodQ"
ykey_secret = ("mcTmghB48JIH0xoNWLldvsX9uIiOLQfdi0gR8LWdFt02lboCAF9vx"
               "SSd1MI0KtZ0")
ykey_access_token = ("gl6k6JmewUhzjMVBv0I2x4Bz_NRiEggSqjlGbTaejmbzvB"
                     "JXgI36FPgWoqBnEL9QQ6wU5H4h41dxPkxVjHFlawtH69m1"
                     "kcXQuHev5PuWBtcdBEAbdJR0HNl3d4tpWXYx")

# Import the census data into a Pandas DataFrame
census_pd = pd.read_csv("Census_Data.csv")

# Preview the data
census_pd.head()

# Sell all zip codes with a population over 1000 from a set of randomly
# selected list of 700 zip code locations
selected_zips = census_pd.sample(n=700)
selected_zips = selected_zips[selected_zips["Population"].astype(int) > 1000]

# Visualize
print(selected_zips.head())

# Show the total number of zip codes that met our population cut-off
print('Total number of zip codes that met our population cut-off:')
print(selected_zips.count())

# Show the average population of our representive sample set
print('Average population:')
print(selected_zips["Population"].mean())

# Show the average household income of our representive sample set
print('Average household income:')
print(selected_zips["Household Income"].mean())

# Show the average median age of our representive sample set
print('Average median age:')
print(selected_zips["Median Age"].mean())

# Create Two DataFrames to store the Italian and the Mexican Data
italian_data = pd.DataFrame()
mexican_data = pd.DataFrame()

# Setup the DataFrames to have appropriate columns
italian_data["Zip Code"] = ""
italian_data["Italian Review Count"] = ""
italian_data["Italian Average Rating"] = ""
italian_data["Italian Weighted Rating"] = ""

mexican_data["Zip Code"] = ""
mexican_data["Mexican Review Count"] = ""
mexican_data["Mexican Average Rating"] = ""
mexican_data["Mexican Weighted Rating"] = ""

# Include Yelp Token
headers = {"Authorization": "Bearer gl6k6JmewUhzjMVBv0I2x4Bz_NRiEggSqjlGbTaejmbzvBJXgI36FPgWoqBnEL9QQ6wU5H4h41dxPkxVjHFlawtH69m1kcXQuHev5PuWBtcdBEAbdJR0HNl3d4tpWXYx"}
counter = 0

# Loop through every zip code
for index, row in selected_zips.iterrows():

    # Add to counter
    counter = counter + 1

    # Create two endpoint URLs:
    url = "https://api.yelp.com/v3/businesses/search?term="
    target_url_italian = url + "Italian&location=%s" % (row["Zipcode"])
    target_url_mexican = url + "Mexican&location=%s" % (row["Zipcode"])

    # Print the URLs to ensure logging
    print(counter)
    print(target_url_italian)
    print(target_url_mexican)

    # Get the Yelp Reviews
    yelp_reviews_italian = requests.get(target_url_italian,
                                        headers=headers).json()
    yelp_reviews_mexican = requests.get(target_url_mexican,
                                        headers=headers).json()

    # Calculate the total reviews and weighted rankings
    italian_review_count = 0
    italian_weighted_review = 0

    mexican_review_count = 0
    mexican_weighted_review = 0

    try:

        # Loop through all records to calculate the review count and weighted
        # review value
        for business in yelp_reviews_italian["businesses"]:

            italian_review_count = (italian_review_count +
                                    business["review_count"])
            italian_weighted_review = (italian_weighted_review +
                                       business["review_count"] *
                                       business["rating"])

        for business in yelp_reviews_mexican["businesses"]:
            mexican_review_count = (mexican_review_count +
                                    business["review_count"])
            mexican_weighted_review = (mexican_weighted_review +
                                       business["review_count"] *
                                       business["rating"])

        # Append the data to the appropriate column of the data frames
        italian_data.set_value(index, "Zip Code", row["Zipcode"])
        italian_data.set_value(index, "Italian Review Count",
                               italian_review_count)
        italian_data.set_value(index, "Italian Average Rating",
                               italian_weighted_review / italian_review_count)
        italian_data.set_value(index, "Italian Weighted Rating",
                               italian_weighted_review)

        mexican_data.set_value(index, "Zip Code", row["Zipcode"])
        mexican_data.set_value(index, "Mexican Review Count",
                               mexican_review_count)
        mexican_data.set_value(index, "Mexican Average Rating",
                               mexican_weighted_review / mexican_review_count)
        mexican_data.set_value(index, "Mexican Weighted Rating",
                               mexican_weighted_review)

    except:
        print("Uh oh")


# Preview Italian Data
print(italian_data.head())

# Preview Mexican Data
print(mexican_data.head())

# Calculate summaries

print('Mexican Review Count')
print(mexican_data["Mexican Review Count"].sum())

print('Italian Review Count')
print(italian_data["Italian Review Count"].sum())

print('Average rating for Mexican restaurants')
print(mexican_data["Mexican Weighted Rating"].sum() /
      mexican_data["Mexican Review Count"].sum())

print('Average rating for Italian restaurants')
print(italian_data["Italian Weighted Rating"].sum() /
      italian_data["Italian Review Count"].sum())

# Combine Data Frames into a single Data Frame
combined_data = pd.merge(mexican_data, italian_data, on="Zip Code")
combined_data.head()

# Total Rating and Popularity "Wins"
combined_data["Rating Wins"] = np.where(combined_data["Mexican Average Rating"] > combined_data["Italian Average Rating"], "Mexican", "Italian")
combined_data["Review Count Wins"] = np.where(combined_data["Mexican Review Count"] > combined_data["Italian Review Count"], "Mexican", "Italian")

# View Combined Data
print(combined_data.head())

# Tally number of cities where one type wins on ratings over the other
print(combined_data["Rating Wins"].value_counts())

# Tally number of cities where one type wins on review counts over the other
print(combined_data["Review Count Wins"].value_counts())

# Model 1: Head-to-Head Review Counts
italian_summary = pd.DataFrame(
    {
        "Review Counts": italian_data["Italian Review Count"].sum(),
        "Rating Average": italian_data["Italian Average Rating"].mean(),
        "Review Count Wins": combined_data["Review Count Wins"].value_counts()["Italian"],
        "Rating Wins": combined_data["Rating Wins"].value_counts()["Italian"]
    }, index=["Italian"])

mexican_summary = pd.DataFrame(
    {
        "Review Counts": mexican_data["Mexican Review Count"].sum(),
        "Rating Average": mexican_data["Mexican Average Rating"].mean(),
        "Review Count Wins": combined_data["Review Count Wins"].value_counts()["Mexican"],
        "Rating Wins": combined_data["Rating Wins"].value_counts()["Mexican"]
    }, index=["Mexican"])

final_summary = pd.concat([mexican_summary, italian_summary])
print(final_summary)

# ----- #
# Plots #
# ----- #

# Plot Rating Average
plt.clf()
final_summary["Rating Average"].plot.bar()
plt.show()

# Plot Rating Wins
plt.clf()
final_summary["Rating Wins"].plot.bar()
plt.show()

# Plot Review Count
plt.clf()
final_summary["Review Counts"].plot.bar()
plt.show()

# Plot Review Count
plt.clf()
final_summary["Review Count Wins"].plot.bar()
plt.show()

# Histogram Italian Food (Ratings)
plt.figure()

# Subplot 1 (Italian)
plt.subplot(121)
combined_data["Italian Average Rating"].plot.hist(bins=[0, 0.5, 1, 1.5, 2, 2.5,
                                                        3, 3.5, 4, 4.5, 5.0],
                                                  color="blue", alpha=0.6)
plt.xlabel("Italian Restaurant Ratings")
plt.xlim([1, 5.0])
plt.ylim([0, 400])

# Subplot 2 (Mexican)
plt.subplot(122)
combined_data["Mexican Average Rating"].plot.hist(bins=[0, 0.5, 1, 1.5, 2, 2.5,
                                                        3, 3.5, 4, 4.5, 5.0],
                                                  color="red", alpha=0.6)
plt.xlabel("Mexican Retaurant Ratings")
plt.xlim([1, 5.0])
plt.ylim([0, 400])

# Show Plot
plt.show()

# -------------------- #
# Statistical analysis #
# -------------------- #

# Run a t-test on average rating and number of reviewers
mexican_ratings = combined_data["Mexican Average Rating"]
italian_ratings = combined_data["Italian Average Rating"]

mexican_review_counts = combined_data["Mexican Review Count"]
italian_review_counts = combined_data["Italian Review Count"]

# Run T-Test on Ratings
print(ttest_ind(mexican_ratings.values, italian_ratings.values))

# Run T-Test on Review Counts
print(ttest_ind(mexican_review_counts.values, italian_review_counts.values))
