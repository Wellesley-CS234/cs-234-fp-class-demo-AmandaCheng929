
import streamlit as st
import pandas as pd
import plotly.express as px


data = pd.read_csv('all_movies_totalViews.csv')

st.set_page_config(layout="wide")

st.header('Movie Platforms & Wikipedia')

st.markdown("#### Introduction")
st.markdown("""
**Research question:**  How well do Wikipedia movie articles reflect the realities of movies on IMDb?

1) How well do *plot summaries* on Wikipedia showcase the genres of the movies as stated on IMDb?  
2) How well does *total pageview* reflect the performance of these movies on IMDb?
""")

st.markdown("#### Original Dataset")
st.write("This is a dataset found on Kaggle, containing the descriptions and performance of movies, with data collected during 2024.")
ori_data = pd.read_csv('oriData_short.csv')
st.dataframe(ori_data.head(10))

st.markdown("#### Processed Dataset")
st.write("""The main processing involves using the 'instance_of' and 'release_year' to find the correct wikipedia article page among potential wikipedia pages with similar names." 
This dataset only contains english-language movies with valid revenue information of 10+ user rating instances during 2024.
""")
st.dataframe(data.head(10))


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


text_data = pd.read_csv("title_genreclassed.csv")
st.markdown("#### A Sneak Peek into Progress for Text Classification and New Features")
st.dataframe(text_data.head(20))

st.markdown("#### Assumptions in this Study")
st.markdown("""
1) Data only contains 2024
2) Only considers english-language films
3) Only considers movies with 10+ number of ratings during 2024
""")
