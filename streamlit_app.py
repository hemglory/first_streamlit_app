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
streamlit.dataframe(my_fruit_list)
