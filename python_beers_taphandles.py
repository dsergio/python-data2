######
#
# Sample Python Project
# Author: David Sergio
#
# beer/breweries dataset: https://www.kaggle.com/nickhould/craft-cans
# taphandles dataset: https://www.taphandles.com/en/ready-made/pub-style
#
######

import numpy as np
import pandas as pd
# import matplotlib as plt
import matplotlib.pyplot as plt
from numpy import nan


# read data from CSV
#
beers = pd.read_csv(".\\beers\\beers.csv", encoding="ISO-8859-1")
breweries = pd.read_csv(".\\beers\\breweries.csv", encoding="ISO-8859-1")
taphandles = pd.read_csv(".\\taphandles\\pubstyle-taphandles.csv", encoding="ISO-8859-1")


# Print first 10 rows of each dataset
# Describe dataset
#
print(beers.head(10))
print("\n\n")
print(beers.describe())
print("\n\n")

print(breweries.head(10))
print("\n\n")
print(breweries.describe())
print("\n\n")

print(taphandles.head(10))
print("\n\n")
print(taphandles.describe())
print("\n\n")


# Missing Data
# 
for col in beers.columns: 
	beers[col] = beers[col].replace("", nan)
	beers[col] = beers[col].replace(" ", nan)
	beers[col] = beers[col].replace("NA", nan)
	beers[col] = beers[col].replace("?", nan)
for col in breweries.columns: 
	breweries[col] = breweries[col].replace("", nan)
	breweries[col] = breweries[col].replace(" ", nan)
	breweries[col] = breweries[col].replace("NA", nan)
	breweries[col] = breweries[col].replace("?", nan)
for col in taphandles.columns: 
	taphandles[col] = taphandles[col].replace("", nan)
	taphandles[col] = taphandles[col].replace(" ", nan)
	taphandles[col] = taphandles[col].replace("NA", nan)
	taphandles[col] = taphandles[col].replace("?", nan)

print("beers missing data:")
print(beers.isnull().sum())
print("\n\n")

print("breweries missing data:")
print(breweries.isnull().sum())
print("\n\n")

print("taphandles missing data:")
print(taphandles.isnull().sum())
print("\n\n")


# Histograms, multiple plots
# 
hist1 = plt.figure()
ax1 = hist1.add_subplot(1, 1, 1)
n, bins, patches = ax1.hist(beers['abv'])
ax1.set_xlabel('ABV')
ax1.set_ylabel('Frequency')

hist2 = plt.figure()
ax2 = hist2.add_subplot(1, 1, 1)
n, bins, patches = ax2.hist(taphandles['price'])
ax2.set_xlabel('Price')
ax2.set_ylabel('Frequency')

hist1.savefig("histograms\\beers_abv_hist.png")
hist2.savefig("histograms\\taphandles_pubstyle_price_hist.png")



# Histograms, only one plot
# 
# plt.hist(beers['abv'])
# plt.title("Beers ABV Histogram")
# plt.xlabel("ABV")
# plt.ylabel("Frequency")
# plt.savefig("histograms2\\beers_abv_hist.png")

# Histograms, only one plot
# 
# plt.hist(taphandles['price'])
# plt.title("Taphandles pub-style Price Histogram")
# plt.xlabel("Price")
# plt.ylabel("Frequency")
# plt.savefig("histograms2\\taphandles_pubstyle_price_hist.png")

