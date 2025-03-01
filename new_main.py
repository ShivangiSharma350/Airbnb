import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import product

airbnb = pd.read_csv('C:/Users/My/Downloads/Airbnb NYC 2019.csv')
#Data description and information
print(airbnb.describe())
print(airbnb.columns)
print(airbnb.info())

#To get count of null values in each column
print(airbnb.isnull().sum())

#Drop unnecessary columns
airbnb.drop(['latitude','longitude','last_review','reviews_per_month'],axis=1,inplace=True)

#To find which host and area has maximum host_countings
host_info = airbnb.groupby(['host_name','neighbourhood_group'])['calculated_host_listings_count'].max().reset_index()
print(host_info.sort_values('calculated_host_listings_count',ascending=False).head())

#To find which room and area has maximum price
room_info = airbnb.groupby(['room_type','neighbourhood_group'])['price'].max().reset_index()
room_info = room_info.sort_values(by='price',ascending=False).head(10)
print('The room and area which has maximum price are:\n',room_info)

room_type = []
room_dict = {}
for i in room_info['room_type']:
    room_type.append(i)
for i in room_type:
    room_dict[i] = room_type.count(i)

plt.bar(room_dict.keys(),room_dict.values(),color = 'blue',edgecolor='red')
plt.title('Room Type according to their price')
plt.xlabel('Room Type')
plt.ylabel('Count')
plt.show()

#To check reviews of different areas
area_review = airbnb.groupby('neighbourhood_group')['number_of_reviews'].max().reset_index()
print('Reviews of different areas:\n',area_review.sort_values('number_of_reviews',ascending=False))

plt.bar(area_review['neighbourhood_group'],area_review['number_of_reviews'],width=0.5,color='green',edgecolor='red')
plt.title('Reviews of area')
plt.xlabel('Area')
plt.ylabel('Reviews')
plt.show()

#To check reviews as per the price
price_review = airbnb.groupby('price')['number_of_reviews'].max().reset_index()
print('Reviews as per the price:\n',price_review.sort_values('number_of_reviews',ascending=False))

plt.scatter(price_review['price'],price_review['number_of_reviews'])
plt.title('Reviews in terms of price')
plt.xlabel('Price')
plt.ylabel('Reviews')
plt.show()

#to find out busiest host and the reason ?
busy_host = airbnb.groupby(["host_id","host_name","room_type"])["number_of_reviews"].max().reset_index()
busy_host = busy_host.sort_values(by="number_of_reviews",ascending=False).head(10)
print('Top 10 busiest hosts are:\n',busy_host)

plt.bar(busy_host['host_name'],busy_host['number_of_reviews'])
plt.title('Top 10 busy host')
plt.xlabel('Host name')
plt.ylabel('Reviews')
plt.show()

#To find highest charging host
high_charging_host = airbnb.groupby(['host_id','host_name','room_type'])['price'].max().reset_index()
high_charging_host = high_charging_host.sort_values(by='price',ascending=False).head(10)
print('Top 10 highest charging hosts are:\n',high_charging_host)

plt.bar(high_charging_host['host_name'],high_charging_host['price'],color='purple')
plt.title('Highest charging host')
plt.xlabel('Host name')
plt.ylabel('Price')
plt.show()


#To find traffic difference between different areas
traffic = airbnb.groupby(['neighbourhood_group','room_type'])['minimum_nights'].count().reset_index()
print('Traffic difference between different areas:\n',traffic)

plt.bar(traffic['room_type'],traffic['minimum_nights'],color='yellow',width=0.2)
plt.xlabel('Room type')
plt.ylabel('Minimum night count')
plt.title('Traffic based on minimum night count')
plt.show()

#To find the correlation between different variables
correl = airbnb.corr(method='pearson',numeric_only=True)
print('Correlation between different variables:\n',correl)
sns.heatmap(correl,annot=True)
plt.show()

#Room count in all over NYC according to different room types
ax=sns.countplot(y='room_type',hue='neighbourhood_group',data=airbnb)
total = len(airbnb['room_type'])
for p in ax.patches:
    percentage = '{:.1f}%'.format(100 * p.get_width()/total)
    x = p.get_x() + p.get_width()+ 0.02
    y = p.get_y() + p.get_height()/2
    ax.annotate(percentage,(x,y))
plt.xlabel('Room count')
plt.ylabel('Room type')
plt.title('Count of each room type in NYC')
plt.xticks(rotation=90)
plt.show()

