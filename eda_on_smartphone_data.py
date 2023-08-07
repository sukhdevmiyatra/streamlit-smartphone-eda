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
    st.write('Smartphone Data Overview')
    st.dataframe(df.head(10))  
    
    st.write('Smartphone Data Statistical Description')
    
    st.dataframe(df.describe())  
    
    st.title('In Depth Price To Performance Analysis')
    
    st.write('Smartphone Brands Vs Price Via Rating')
    
    bar_chart = px.bar(df, x='brand_name', y='price',color='rating')
    st.plotly_chart(bar_chart) 
    
    st.write('Processor Brand vs Price')
    
    fig1,ax1 = plt.subplots()
    sns.barplot(data=df,x='processor_brand',y='price',estimator=np.median,ax=ax1)
    plt.xticks(rotation='vertical')
    st.pyplot(fig1)
    
    st.write('Processor Cores vs Price')
    
    fig2,ax2 = plt.subplots()
    sns.barplot(data=df,x='num_cores',y='price',estimator=np.median,ax=ax2)
    st.pyplot(fig2)
    
    st.write('Processor Speed vs Price')
    
    fig3, ax3 = plt.subplots()
    sns.scatterplot(data=df, x='processor_speed', y='price', ax=ax3)
    st.pyplot(fig3)
    
    st.write('Cores And Operating System')
    
    st.dataframe(pd.crosstab(df['num_cores'],df['os'])) 
    
    st.write('Processor Screen Size vs Price')
    
    fig4,ax4 = plt.subplots()      
    sns.scatterplot(data=df,x='screen_size',y='price',ax=ax4)
    st.pyplot(fig4)
    
    st.write('Ir Blaster vs Price')
    
    fig5,ax5 = plt.subplots()    
    sns.barplot(data=df,x='has_ir_blaster',y='price',estimator=np.median,ax=ax5)
    st.pyplot(fig5)
    
    st.write('NFC vs Price')
    
    fig6,ax6 = plt.subplots()   
    sns.pointplot(data=df,x='has_nfc',y='price',estimator=np.median,ax=ax6)
    st.pyplot(fig6)
    
    st.write('5G vs Price')
    
    fig7,ax7 = plt.subplots()  
    sns.barplot(data=df,x='has_5g',y='price',estimator=np.median,ax=ax7)
    st.pyplot(fig7)  
    
  

elif menu == 'Top 10 Smartphone Brands By Value Count':
    
    st.write('Top 10 Smartphone Brands By Value Count')
    
    bar_chart = df['brand_name'].value_counts().head(10)      

    bar_chart_data = px.bar(bar_chart,text_auto=True)

    st.plotly_chart(bar_chart_data)
 
elif menu == 'Rating Overview':
    
    st.write('Rating Overview')
    
    st.pyplot(sns.displot(kind='hist',data=df,x='rating',kde=True))    
    
    st.write('Rating Price Analysis')
    
    st.plotly_chart(px.bar(df,x='rating',y='price'))   
    
    st.write('Rating Boxplot')
    
    fig, ax = plt.subplots()    
    sns.boxplot(data=df, x='rating', ax=ax)
    st.pyplot(fig)
   
elif menu == 'Processor Overview':   
    
    st.write('Processor Overview')   
  
    st.plotly_chart(px.pie(df, names='processor_brand'))
    
elif menu == 'Storage And Ram Overview':
   
   
    st.write('Storage And Ram Overview')
    
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
    
    st.write('Storage And Ram Overview')
    
    os_counts = df['os'].value_counts()
    labels = os_counts.index
    values = os_counts.values

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='percent+label')])

    fig.update_layout(title='Operating System Distribution', showlegend=True)

    st.plotly_chart(fig)
    
elif menu == 'Camera Overview':
    
    st.write('Numbers of Cameras')
    
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
    
    st.write('Extra Features') 
    
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
