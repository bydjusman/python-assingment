import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

# File to store data
DATA_FILE = "mindset_data.csv"

# Initialize or load data
def load_data():
    try:
        return pd.read_csv(DATA_FILE, parse_dates=["Date"])
    except FileNotFoundError:
        return pd.DataFrame(columns=["Date", "Mood", "Productivity", "Thought"])

# Save entry
def save_entry(mood, productivity, thought):
    new_entry = pd.DataFrame({
        "Date": [date.today()],
        "Mood": [mood],
        "Productivity": [productivity],
        "Thought": [thought]
    })
    data = load_data()
    data = pd.concat([data, new_entry], ignore_index=True)
    data.to_csv(DATA_FILE, index=False)

# Main App
st.title("🧠 Mindset Tracker")

st.subheader("Enter Today's Mindset")
mood = st.selectbox("How are you feeling today?", ["Happy", "Neutral", "Sad", "Stressed", "Excited"])
productivity = st.slider("Productivity Level (1 to 10)", 1, 10)
thought = st.text_area("Any thoughts or reflections?")

if st.button("Save Entry"):
    save_entry(mood, productivity, thought)
    st.success("Entry saved successfully!")

# Show past data
st.subheader("📊 Your Mindset History")
data = load_data()
if not data.empty:
    st.dataframe(data.sort_values("Date", ascending=False))

    # Mood Count
    st.subheader("Mood Trend")
    mood_counts = data["Mood"].value_counts()
    st.bar_chart(mood_counts)

    # Productivity trend
    st.subheader("Productivity Over Time")
    st.line_chart(data.set_index("Date")["Productivity"])
else:
    st.info("No entries yet. Start by adding today's mindset!")

    # Run project locally with the following command
    # streamlit run mindset_tracker.py
