import streamlit as st
import pandas as pd
from datetime import datetime

# Inställningar för appen
st.set_page_config(page_title="Höglanda Hästgård", page_icon="🐎")

st.title("🌿 Höglanda Hästgård")
st.markdown("Välkommen till stallets egna app!")

# Meny i sidofältet
menu = ["Veckoschema", "Paddockbokning", "Hästaktivitet", "Foderstater", "Logga Strö/Pellets"]
choice = st.sidebar.selectbox("Meny", menu)

# --- FLIK: VECKOSCHEMA ---
if choice == "Veckoschema":
    st.header("📅 Veckoschema")
    st.info("Här ser du veckans pass.")
    # Här kan vi lägga in koden som läser direkt från ditt Google Sheet
    st.write("Måndag: Utsläpp - Jennifer & Lars")

# --- FLIK: PADDOCKBOKNING ---
elif choice == "Paddockbokning":
    st.header("🏟️ Paddockbokning")
    with st.form("paddock_form"):
        date = st.date_input("Välj datum")
        time = st.time_input("Välj tid")
        rider = st.text_input("Ditt namn")
        type_box = st.selectbox("Typ av bokning", ["Ensam (Röd)", "Ok att rida bredvid (Grön)", "Träning (Gul)"])
        submitted = st.form_submit_button("Boka")
        if submitted:
            st.success(f"Bokat för {rider} kl {time}!")

# --- FLIK: LOGGA STRÖ ---
elif choice == "Logga Strö/Pellets":
    st.header("📦 Logga förbrukning")
    with st.form("stro_form"):
        name = st.text_input("Namn")
        item = st.radio("Vad har du tagit?", ["Stallströ", "Stallpellets"])
        amount = st.number_input("Antal säckar", min_value=1, step=1)
        if st.form_submit_button("Spara logg"):
            st.success(f"Sparat: {amount} st {item} på {name}")

# --- FLIK: FODERSTATER ---
elif choice == "Foderstater":
    st.header("🐴 Foderstater")
    st.table(pd.DataFrame({
        'Häst': ['Stella', 'Balder'],
        'Morgon': ['2kg Hö', '3kg Hö'],
        'Lunch': ['1kg Hö', '2kg Hö'],
        'Kväll': ['3kg Hö', '4kg Hö']
    }))
