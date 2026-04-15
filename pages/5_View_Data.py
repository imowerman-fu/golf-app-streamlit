import streamlit as st
from utils.db import supabase

st.title("📁 View Data")

rounds = supabase.table("rounds").select("*").execute().data

st.subheader("Rounds")
st.dataframe(rounds)

holes = supabase.table("holes").select("*").execute().data

st.subheader("Holes")
st.dataframe(holes)