import streamlit as st
from utils.db import supabase
from datetime import date

st.title("➕ Enter Round")

if "round_id" not in st.session_state:
    st.session_state.round_id = None

round_date = st.date_input("Date", date.today())
course = st.text_input("Course Name")

if st.button("Save Round"):
    res = supabase.table("rounds").insert({
        "date": str(round_date),
        "course_name": course
    }).execute()

    st.session_state.round_id = res.data[0]["id"]

    st.success("Round saved!")