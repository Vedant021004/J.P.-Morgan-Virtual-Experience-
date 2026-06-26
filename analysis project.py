import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd



headers = {
    "User-Agent": "Mozilla/5.0"
}

all_names = []
all_prices = []
all_description = []
all_stars = []
all_reviews = []

for page in range(1, 3):
    url = f"https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={page}"

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    data = soup.find_all("a", class_="title")
    data2 = soup.find_all("h4", class_="price")
    data3 = soup.find_all("p", class_="description")
    rating = soup.find_all("p", attrs={"data-rating": True})
    data4 = soup.find_all("p", class_ = "review-count")

    for item in data:
        all_names.append(item.text.strip())

    for rate in data2:
        all_prices.append(rate.text.strip())

    for description in data3:
        all_description.append(description.text.strip())  

    for stars in rating:
        all_stars.append(stars["data-rating"])

    for feedback in data4:
        all_reviews.append(feedback.text.strip())    


for name, price, description, rating, review in zip(
    all_names,
    all_prices,
    all_description,
    all_stars,
    all_reviews
):
    print(f"""
Name        : {name}
Price       : {price}
Description : {description}
Rating      : {rating}
Reviews     : {review}
{'-'*60}
""")        


# print("Names")
# for name in all_names:
#     print(name)

# print("\nPrices")
# for price in all_prices:
#     print(price)

# print("\nDescription")
# for details in all_description:
#     print(details)

# print("\nRating")    
# for review in all_stars:
#     print(review)

# print("\nFeedback")
# for new in all_reviews:
#     print(new)


# Data Cleaning 

df = pd.DataFrame({
    "Name": all_names,
    "Price": all_prices,
    "Description": all_description,
    "Rating": all_stars,
    "Reviews": all_reviews
})

print(df.head())

df["Price"] = df["Price"].str.replace("$", "", regex=False)
df["Price"] = df["Price"].astype(float)

# Line Graph
plt.figure(figsize=(10,5))

plt.plot(df["Name"], df["Price"], marker="o")

plt.xticks(rotation=90)

plt.grid(True)

plt.show()


# Bar Graph
plt.figure(figsize=(10,5))

plt.bar(df["Name"], df["Price"])

plt.xticks(rotation=90)

plt.show()


# Pie Chart
rating_count = df["Rating"].value_counts()

plt.figure(figsize=(6,6))

plt.pie(
    rating_count,
    labels=rating_count.index,
    autopct="%1.1f%%"
)

plt.title("Rating Distribution")

plt.show()


# Price vs review

plt.figure(figsize=(8,5))

plt.scatter(df["Reviews"], df["Price"])

plt.xlabel("Reviews")
plt.ylabel("Price")

plt.title("Reviews vs Price")

plt.grid(True)

plt.show()