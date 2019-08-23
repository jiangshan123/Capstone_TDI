# Customer-friendly ML clustering tool
Capstone project working with Retina AI company. 

## Small business is HUGE
According to data from the Census Bureau’s Annual Survey of Entrepreneurs, there were 5.6 million employer firms in the United States in 2016.

● Firms with fewer than 20 workers made up 89.0 percent of those business.

● Employ 50% of all private sector employees

● Pay 45% of the total U.S. private payrolls

<img src="https://github.com/jiangshan123/Capstone_TDI/blob/master/images/SmallBusiness.png" width="480">

Add in the number of nonemployer businesses – there were 24.8 million in 2016 (latest data) – then the share of U.S. businesses with less than 20 workers increases to 98.0 percent.

<img src="https://github.com/jiangshan123/Capstone_TDI/blob/master/images/websites.png" width="240">

More and more small businesses are having their own websites or websites on eBay/Amazon/Taobao. However, the scales of the businesses prevent them from hiring a professional data analyst. Our goal is to build a customer-friendly clustring tool that can help small business owners understand their customers using machine learning.

### Goal
Clustering is a difficult problem because there isn't a good way to evaluate how "good" clusters are. We would like to have a tool that lets users add / subtract / re-weight features and visualize the resulting clusters, so they can interactively visualize what a "good" cluster is. Due to some business issues and flexibility of the package, need to write the python package from scratch.

### Delivery
Cluster customers (using K-means or DTs) using purchase history and browsing behavior where an end-user may prioritize (add weight) or eliminate features using a web-app front-end.

## Data Source
* Demo Data can be found here: https://github.com/jiangshan123/Capstone_TDI/blob/master/data/user_data_rui_liu.csv

* Demo data is a CSV file with some anonymized user data. The data corresponds to customers who purchase hair care products. Each row is a user (with a corresponding user_id) and there are 88759 users. The table contains 109 columns, or features, where user_id is considered a feature.

* There is no transaction data, but we summarize customers' transaction history using lifetime total revenue (LTR). This is the column in the dataset with label "predicted_future_ltr_10yr". Also included are revenue (total revenue so far) and purchases (total number of orders so far).

* There are also user-profile questions that were provided via an online Quiz. The 109 columns include categorical data that has been one-hot-encoded. 

## Data Wrangling
Data Cleanning pipline: [Capstone_TDI](https://github.com/jiangshan123/Capstone_TDI/blob/master/notebooks/data_wrangling.ipynb) project.
* Setup: load packages/setup path
* Load Demo Data
* Deal with missing data
* Deal with string data using Labelencode
* Preliminary statistical data analysis
* Data Visualization
* Save cleaned Data
## Heroku website
https://kmeans-web.herokuapp.com/ 
