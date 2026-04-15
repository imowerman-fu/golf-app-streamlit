import streamlit as st
import pandas as pd
from utils.db import supabase

st.title("📊 Analytics")

if "round_id" not in st.session_state:
    st.warning("Create a round first.")
    st.stop()

holes = supabase.table("holes") \
    .select("*") \
    .eq("round_id", st.session_state.round_id) \
    .execute().data

if not holes:
    st.info("No data yet.")
    st.stop()

df = pd.DataFrame(holes)

total_score = df["score"].sum()
total_par = df["par"].sum()

st.metric("Total Score", total_score)
st.metric("To Par", total_score - total_par)

st.bar_chart(df.set_index("hole_number")["score"])