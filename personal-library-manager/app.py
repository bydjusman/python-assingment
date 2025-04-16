import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="📚 Personal Library Manager")

st.title("📚 Personal Library Manager")
st.subheader("Manage your books with ease!")

# Check if the file exists
file_path = "library.csv"
if not os.path.exists(file_path):
    df = pd.DataFrame(columns=["Title", "Author", "Genre", "Year"])
    df.to_csv(file_path, index=False)

# Load Data
df = pd.read_csv(file_path)

st.header("➕ Add a New Book")

with st.form("add_book_form"):
    title = st.text_input("Title")
    author = st.text_input("Author")
    genre = st.selectbox("Genre", ["Fiction", "Non-fiction", "Sci-Fi", "Fantasy", "Mystery", "Other"])
    year = st.number_input("Year Published", min_value=0, max_value=2100, step=1)
    submitted = st.form_submit_button("Add Book")

    if submitted and title and author:
        new_book = pd.DataFrame([[title, author, genre, year]], columns=df.columns)
        df = pd.concat([df, new_book], ignore_index=True)
        df.to_csv(file_path, index=False)
        st.success("Book added successfully!")
        st.rerun()

st.header("📖 Your Book Collection")
st.dataframe(df, use_container_width=True)

st.header("🗑️ Delete a Book")

if not df.empty:
    book_to_delete = st.selectbox("Select a book to delete", df["Title"])
    if st.button("Delete Book"):
        df = df[df["Title"] != book_to_delete]
        df.to_csv(file_path, index=False)
        st.success("Book deleted successfully!")
        st.rerun()
else:
    st.info("No books to delete.")
