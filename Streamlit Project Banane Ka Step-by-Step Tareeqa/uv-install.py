# Step 1: uv install karein (agar pehle se nahi hai)
pip install uv

# Phir check karein:
uv --version

# Output kuch aisa hona chahiye:
1.0.0

 #Step 2: Virtual Environment banaayein (optional but recommended)

 python -m venv venv
.\venv\Scripts\activate       # activate karein

uv init .
#pyproject.toml file banata hai —
#yeh Python project metadata aur dependencies store karne ke liye use hoti hai

# Step 3: uv se Streamlit install karein
uv pip install streamlit

# Step 4: uv se Streamlit run karein
uv streamlit run main.py

# Extra Tip: Requirements save karna ho toh:
uv pip freeze > requirements.txt

