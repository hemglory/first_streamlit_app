import streamlit
streamlit.title('My parents new healthy diner')
streamlit.header('DINNER MENU')
streamlit.text('🥣 Avakaya Pachadi')
streamlit.text('🥗 Gongura Pachadi')
streamlit.text('🥑 Maagaya Pachadi')
streamlit.text('🍞 Avocado Pachadi')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)
# Display the frutiyvice response on the page
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

