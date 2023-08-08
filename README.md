Smartphone Data Analysis

This repository contains a data analysis application for smartphones. The app, built with Streamlit, enables users to explore diverse aspects of smartphones, including price, ratings, processor details, camera specifications, and additional features.
Setup and Installation

You can now access the app through your browser at (https://app-smartphone-eda.streamlit.app/).
Features
Smartphone Data Overview

This section provides an overview of the smartphone dataset, showcasing the first 10 rows and basic statistical descriptions.
In-Depth Price-To-Performance Analysis

This comprehensive analysis delves into the relationship between smartphone brands, prices, ratings, processor information, operating systems, screen size, and various extra features. The analysis includes bar charts, scatter plots, and data tables to aid in understanding the nuances of the smartphone market.
Top 10 Smartphone Brands By Value Count

A bar chart highlights the top 10 most popular smartphone brands based on their occurrences in the dataset.
Rating Overview

This section visualizes the distribution of smartphone ratings using a histogram and a box plot, offering insights into the overall rating trends.
Processor Overview

A pie chart illustrates the distribution of different processor brands used in smartphones, providing an overview of the processor landscape.
Storage and RAM Overview

Pie charts present the percentage distribution of RAM capacities and internal memory sizes, shedding light on the storage specifications of smartphones.
Operating System Overview

This pie chart displays the distribution of different operating systems used in smartphones, giving an overview of OS preferences among smartphone users.
Camera Overview

Pie charts showcase the distribution of the total number of rear and front cameras used in smartphones and the distribution of primary camera megapixels.
Extra Features

This section uses pie charts to illustrate the distribution of features like fast charging, refresh rate, and extended memory availability in smartphones.
Inferences.

From the analysis, we can draw the following inferences:

    Higher-rated phones tend to be more expensive.
    The choice of processor brand may influence the price range.
    The number of cores and processor speed do not significantly impact the price.
    Phones with larger screens generally command higher prices.
    The presence of certain features like IR blaster, NFC, and 5G can influence the price of smartphones.

To further validate our findings, hypothesis testing can be conducted on the price variance across different processor brands and the effect of features like IR blaster on smartphone prices.
Data Source

The smartphone dataset (smartphone_cleaned.csv) utilized in this analysis is available in the repository.
Libraries Used
    
    Pandas
    NumPy
    Matplotlib
    Plotly
    Seaborn
    Streamlit
