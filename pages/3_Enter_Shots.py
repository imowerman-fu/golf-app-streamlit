import streamlit as st
from utils.db import supabase

st.title("🎯 Enter Shots")

if "round_id" not in st.session_state:
    st.warning("Create a round first.")
    st.stop()

# get holes for dropdown
holes = supabase.table("holes") \
    .select("*") \
    .eq("round_id", st.session_state.round_id) \
    .execute().data

hole_map = {f"Hole {h['hole_number']}": h["id"] for h in holes}

hole_choice = st.selectbox("Hole", list(hole_map.keys()))
shot_number = st.number_input("Shot #", min_value=1)
club = st.text_input("Club")
distance = st.number_input("Distance (yards)", min_value=0)
direction = st.selectbox("Direction", ["left", "center", "right"])

if st.button("Add Shot"):
    supabase.table("shots").insert({
        "hole_id": hole_map[hole_choice],
        "shot_number": shot_number,
        "club": club,
        "distance": distance,
        "direction": direction
    }).execute()

    st.success("Shot added!")