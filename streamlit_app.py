# streamlit_app.py

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="3-Bedroom Energy Dashboard", layout="centered")

st.title("3-Bedroom House Energy Dashboard")
st.write("This dashboard shows sample energy usage per room.")

# Sample data: energy usage per room in kWh
rooms = ["Living Room", "Kitchen", "Master Bedroom", "Bedroom 2", "Bedroom 3"]
energy_usage = np.random.randint(5, 30, size=len(rooms))  # random sample data

data = pd.DataFrame({
    "Room": rooms,
    "Energy Usage (kWh)": energy_usage
})

st.subheader("Current Energy Usage per Room")
st.table(data)

st.subheader("Energy Usage Chart")
st.bar_chart(data.set_index("Room"))

st.subheader("Summary")
st.write(f"Total Energy Usage: {data['Energy Usage (kWh)'].sum()} kWh")
st.write(f"Average Energy Usage per Room: {data['Energy Usage (kWh)'].mean():.1f} kWh")

st.info("This is sample data. You can replace it with real energy readings for your project.")
