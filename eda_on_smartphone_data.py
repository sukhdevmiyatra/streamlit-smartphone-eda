import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import seaborn as sns
import streamlit as st
import plotly.express as px


df = pd.read_csv('smartphone_cleaned.csv')


st.set_page_config(page_title='Smartphone Data Analysis')


st.sidebar.title('Smartphone Data Analysis Menu')

menu = st.sidebar.selectbox('Select One',['Smartphone Data Overview','Top 10 Smartphone Brands By Value Count','Rating Overview','Processor Overview','Storage And Ram Overview','Operating System Overview','Camera Overview','Extra Features'])


if menu == 'Smartphone Data Overview':
    st.title('Smartphone Data Overview')
   
    st.dataframe(df.head())  
    st.write('It shows the first 5 rows of the smartphone dataset')
             
    st.title('Smartphone Data Statistical Description')
    
    st.dataframe(df.describe())  

    st.write('It shows the some basic stats like the average price, highest, lowest, etc')
    
    st.title('In Depth Price To Performance Analysis')
    
    st.write('Smartphone Brands Vs Price Via Rating')    
    
    
    bar_chart = px.bar(df, x='brand_name', y='price',color='rating')
    st.plotly_chart(bar_chart)
    st.write("We see a cool bar chart that compares smartphone brands based on their prices and colors them according to their ratings. Looks like higher-rated phones are generally more expensive.")
    
    
    st.title('Processor Brand vs Price')
    
    fig1,ax1 = plt.subplots()
    sns.barplot(data=df,x='processor_brand',y='price',estimator=np.median,ax=ax1)
    plt.xticks(rotation='vertical')
    st.pyplot(fig1)
  
    st.title('Processor Cores vs Price')
    
    fig2,ax2 = plt.subplots()
    sns.barplot(data=df,x='num_cores',y='price',estimator=np.median,ax=ax2)
    st.pyplot(fig2)
    st.write("Another bar chart shows the median price of smartphones for different processor brands.")
    
    st.title('Processor Speed vs Price')
    
    fig3, ax3 = plt.subplots()
    sns.scatterplot(data=df, x='processor_speed', y='price', ax=ax3)
    st.pyplot(fig3)
    st.write("There are graphs for processor cores and speed vs. price too.")    
    
    st.title('Processor Screen Size vs Price')
    
    fig4,ax4 = plt.subplots()      
    sns.scatterplot(data=df,x='screen_size',y='price',ax=ax4)
    st.pyplot(fig4)
    st.write("There is a scatter plot showing how screen size affects the price.")
    
    
    st.title('Ir Blaster vs Price')
    
    fig5,ax5 = plt.subplots()    
    sns.barplot(data=df,x='has_ir_blaster',y='price',estimator=np.median,ax=ax5)
    st.pyplot(fig5)    
    
    
    st.title('NFC vs Price')
    
    fig6,ax6 = plt.subplots()   
    sns.pointplot(data=df,x='has_nfc',y='price',estimator=np.median,ax=ax6)
    st.pyplot(fig6)
    
    st.title('5G vs Price')
    
    fig7,ax7 = plt.subplots()  
    sns.barplot(data=df,x='has_5g',y='price',estimator=np.median,ax=ax7)
    st.pyplot(fig7)
    st.write("charts show the median price of phones with or without IR blaster, NFC, and 5G, so we can see if these features influence the price.")  

    st.title("Inferences:")
    st.write("- Higher-rated phones tend to be more expensive.")
    st.write("- Phones with certain processor brands might have different price ranges.")
    st.write("- The number of cores and processor speed doesn't seem to have a big impact on the price.")
    st.write("- Phones with larger screens tend to be pricier.")
    st.write("- Some features like IR blaster, NFC, and 5G can affect the price.")
    
  

elif menu == 'Top 10 Smartphone Brands By Value Count':
    
    st.title('Top 10 Smartphone Brands By Value Count')
    
    st.write('This one gives us the most popular smartphone brands in the dataset.')
    
    bar_chart = df['brand_name'].value_counts().head(10)      

    bar_chart_data = px.bar(bar_chart,text_auto=True)

    st.plotly_chart(bar_chart_data)
 
elif menu == 'Rating Overview':
    
    st.title('Rating Overview')
    st.write("We can see a histogram of smartphone ratings, so we know how they are distributed.")
    
    st.pyplot(sns.displot(kind='hist',data=df,x='rating',kde=True))    
    
    st.title('Rating Price Analysis')
    st.write("A bar chart shows the relationship between phone ratings and prices. Higher-rated phones tend to be more expensive.")
    st.plotly_chart(px.bar(df,x='rating',y='price'))   
    
    st.title('Rating Boxplot')
    st.write("There's also a box plot to see the spread and outliers in ratings.")
    
    fig, ax = plt.subplots()    
    sns.boxplot(data=df, x='rating', ax=ax)
    st.pyplot(fig)
   
elif menu == 'Processor Overview':   
    
    st.title('Processor Overview')
    st.write('A simple pie chart shows the distribution of different processor brands used in smartphones.')  
  
    st.plotly_chart(px.pie(df, names='processor_brand'))
    
elif menu == 'Storage And Ram Overview':
   
   
    st.title('Storage And Ram Overview')

    st.write('The pie charts tell us the percentage distribution of different RAM capacities and internal memory sizes used in smartphones.')
    
    ram_capacity_counts = df['ram_capacity'].value_counts()
    labels = ram_capacity_counts.index
    values = ram_capacity_counts.values

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='percent+label')])

    fig.update_layout(title='RAM Capacity Distribution', showlegend=True)
    st.plotly_chart(fig)
    
    internal_memory_counts = df['internal_memory'].value_counts()
    labels = internal_memory_counts.index
    values = internal_memory_counts.values

    fig2 = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='percent+label')])

    fig2.update_layout(title='Internal Memory Distribution', showlegend=True)
    st.plotly_chart(fig2)
    
elif menu == 'Operating System Overview':
    
    st.title('Operating System Overview')
    st.write('This pie chart shows the distribution of different operating systems used in smartphones.')
    
    os_counts = df['os'].value_counts()
    labels = os_counts.index
    values = os_counts.values

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='percent+label')])

    fig.update_layout(title='Operating System Distribution', showlegend=True)

    st.plotly_chart(fig)
    
elif menu == 'Camera Overview':
    
    st.title('Numbers of Cameras')
    st.write('One pie chart shows the distribution of the total number of rear and front cameras used in smartphones.')
    st.write('Another pie chart tells us about the distribution of primary camera megapixels.')
    
    camera_counts = (df['num_rear_cameras'] + df['num_front_cameras']).value_counts()
    labels = camera_counts.index
    values = camera_counts.values

    fig1 = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='percent+label')])

    fig1.update_layout(title='Numbers of Cameras Distribution', showlegend=True)

    st.plotly_chart(fig1)
    
    
    labels = df['primary_camera_rear']
    values = df['primary_camera_front']

    fig2 = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='percent+label')])

    fig2.update_layout(title='Cameras Megapixels', showlegend=True)

    st.plotly_chart(fig2)
    
elif menu == 'Extra Features':
    
    st.title('Extra Features') 
    st.write('The pie charts show the distribution of features like fast charging, refresh rate, and extended memory availability in smartphones.') 
    
    fast_charging =  df['fast_charging_available'].value_counts()
    labels = fast_charging.index
    values = fast_charging.values

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='percent+label')])

    fig.update_layout(title='Fast Charing Distribution', showlegend=True)

    st.plotly_chart(fig)
    
    refresh_rate =  df['refresh_rate'].value_counts()
    labels = refresh_rate.index
    values = refresh_rate.values

    fig1 = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='percent+label')])

    fig1.update_layout(title='Refresh Rate Distribution', showlegend=True)

    st.plotly_chart(fig1)    
    
    
    extended_memory =  df['extended_memory_available'].value_counts() 
    labels = extended_memory.index
    values = extended_memory.values

    fig2 = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='percent+label')])

    fig2.update_layout(title='Extended Memory Distribution', showlegend=True)

    st.plotly_chart(fig2) 
