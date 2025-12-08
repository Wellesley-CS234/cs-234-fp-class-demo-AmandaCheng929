
import streamlit as st
import pandas as pd
import plotly.express as px


data = pd.read_csv('all_movies_totalViews.csv')

st.set_page_config(layout="wide")

st.header('Movie Platforms & Wikipedia')


choice = st.selectbox(
    'Select Variable', ['rating','popularity','revenue']
)
if choice == 'rating':
  st.write(f'Showing movie ratings and their wikipedia pageviews')
  chart_data = data
elif choice == 'popularity':
  st.write(f'Showing movie popularity and their wikipedia pageviews')
  chart_data = data
else:
  chart_data = data[data['revenue']!=0]
  st.write(f'Showing movie revenue and their wikipedia pageviews')


# #st.write(chart_data.head())
# st.scatter_chart(data=chart_data, x=choice, y='total_pageview', x_label = choice, y_label='wikipedia pageview')
# # st.line_chart(data=chart_data, x='month-day', y='z_score', color='year', x_label = 'Time', y_label='Z_score\nCC Pageviews')

fig = px.scatter(data, x=choice, y="total_pageview", hover_data=["title"])  # 👈 add z here

st.plotly_chart(fig, use_container_width=True)