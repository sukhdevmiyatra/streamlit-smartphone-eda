# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import seaborn as sns
import streamlit as st
import plotly.express as px

# Load the dataset
df = pd.read_csv('smartphone_cleaned.csv')

# Set the page configuration for the Streamlit app
st.set_page_config(page_title='Smartphone Data Analysis')

# Create a sidebar menu for selecting different analysis options
st.sidebar.title('Smartphone Data Analysis Menu')
menu = st.sidebar.selectbox('Select One', [
    'Smartphone Data Overview', 
    'Top 10 Smartphone Brands By Value Count', 
    'Rating Overview', 
    'Processor Overview', 
    'Storage And Ram Overview', 
    'Operating System Overview', 
    'Camera Overview', 
    'Extra Features'
])

# Handle different menu options
if menu == 'Smartphone Data Overview':
    # Display a brief overview of the dataset
    st.write('Smartphone Data Overview')
    st.dataframe(df.head(10))
    
    # Display the statistical description of the dataset
    st.write('Smartphone Data Statistical Description')
    st.dataframe(df.describe())
    
    # Perform price to performance analysis using plots and charts
    st.title('In-Depth Price To Performance Analysis')
    
    # Bar chart showing smartphone brands vs. price via rating
    bar_chart = px.bar(df, x='brand_name', y='price', color='rating')
    st.plotly_chart(bar_chart)
    
    # Bar chart showing processor brand vs. price
    st.write('Processor Brand vs. Price')
    fig1, ax1 = plt.subplots()
    sns.barplot(data=df, x='processor_brand', y='price', estimator=np.median, ax=ax1)
    plt.xticks(rotation='vertical')
    st.pyplot(fig1)
    
    # Bar chart showing processor cores vs. price
    st.write('Processor Cores vs. Price')
    fig2, ax2 = plt.subplots()
    sns.barplot(data=df, x='num_cores', y='price', estimator=np.median, ax=ax2)
    st.pyplot(fig2)
    
    # Scatter plot showing processor speed vs. price
    st.write('Processor Speed vs. Price')
    fig3, ax3 = plt.subplots()
    sns.scatterplot(data=df, x='processor_speed', y='price', ax=ax3)
    st.pyplot(fig3)    
    
    # Scatter plot showing processor screen size vs. price
    st.write('Processor Screen Size vs. Price')
    fig4, ax4 = plt.subplots()
    sns.scatterplot(data=df, x='screen_size', y='price', ax=ax4)
    st.pyplot(fig4)
    
    # Bar chart showing infrared (IR) blaster vs. price
    st.write('IR Blaster vs. Price')
    fig5, ax5 = plt.subplots()
    sns.barplot(data=df, x='has_ir_blaster', y='price', estimator=np.median, ax=ax5)
    st.pyplot(fig5)
    
    # Point plot showing NFC (Near Field Communication) vs. price
    st.write('NFC vs. Price')
    fig6, ax6 = plt.subplots()
    sns.pointplot(data=df, x='has_nfc', y='price', estimator=np.median, ax=ax6)
    st.pyplot(fig6)
    
    # Bar chart showing 5G capability vs. price
    st.write('5G vs. Price')
    fig7, ax7 = plt.subplots()
    sns.barplot(data=df, x='has_5g', y='price', estimator=np.median, ax=ax7)
    st.pyplot(fig7)

# Handle the other menu options with different analysis types
elif menu == 'Top 10 Smartphone Brands By Value Count':
    # Display a bar chart of the top 10 smartphone brands based on value counts
    st.write('Top 10 Smartphone Brands By Value Count')
    bar_chart = df['brand_name'].value_counts().head(10)
    bar_chart_data = px.bar(bar_chart, text_auto=True)
    st.plotly_chart(bar_chart_data)

elif menu == 'Rating Overview':
    # Display rating-related overviews and analysis
    st.write('Rating Overview')
    
    # Histogram of smartphone ratings
    st.pyplot(sns.displot(kind='hist', data=df, x='rating', kde=True))
    
    # Bar chart showing rating vs. price
    st.write('Rating Price Analysis')
    st.plotly_chart(px.bar(df, x='rating', y='price'))
    
    # Box plot showing rating distribution
    st.write('Rating Boxplot')
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x='rating', ax=ax)
    st.pyplot(fig)
    
    # Cross-tabulation of cores and operating systems
    st.write('Cores And Operating System')
    st.dataframe(pd.crosstab(df['num_cores'], df['os']))

st.write('End of Analysis')
