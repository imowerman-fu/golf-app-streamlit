import streamlit as st
from utils.db import supabase

st.title("⛳ Enter Holes")

if "round_id" not in st.session_state or not st.session_state.round_id:
    st.warning("Create a round first.")
    st.stop()

hole_number = st.number_input("Hole", 1, 18)
par = st.selectbox("Par", [3, 4, 5])
score = st.number_input("Score", min_value=1)

if st.button("Add Hole"):
    supabase.table("holes").insert({
        "round_id": st.session_state.round_id,
        "hole_number": hole_number,
        "par": par,
        "score": score
    }).execute()

    st.success("Hole added!")