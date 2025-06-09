#  Step 1: Ek Naya Folder Banao (Project Folder)

#  Step 2: Ek Naya File Banao (mood_app.py)
#  mood_tracker file name ap kuch bhi rakh sakte ho app.py main.py mood_tracker xyz
 cd mood_tracker file me enter hoga

# Isme tum apna Streamlit ka code likhoge.
# Example code:

import streamlit as st

st.title("My First Streamlit App")
st.write("Welcome to my app!")


# Step 3: Virtual Environment Banao
 python -m venv venv 

# Step 4: Virtual Environment Activate Karo
 .\venv\Scripts\activate 

# Agar sahi se activate ho gaya, toh terminal me kuch aisa dikhai dega:
 (venv) C:\python-clasess\secure-data-encryption-system>

# Step 5: Zaroori Libraries Install Karo Install Streamlit:
 pip install streamlit

# file create kro requirements.txt 
# terminal per run kro req ki file khudi ban jaye gi

 pip freeze > requirements.txt 


# Step 6: App Run Karo
 streamlit run mood_app.py

# Ye browser open karega:
 http://localhost:8501

# Thanks for looking at my code.
 by-dj-Usman


