import streamlit as st

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Slide, to extend graph.")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"Temperature for the next {days} days in Tirana")



