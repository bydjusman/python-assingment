import tkinter as tk
from tkinter import ttk, messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO
import webbrowser

class HollywoodMoviesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hollywood Movies Collection")
        self.root.geometry("1000x700")
        
        self.api_key = "your_omdb_api_key"  # 🔑 Paste your OMDb API key here
        self.base_url = "http://www.omdbapi.com/"
        
        self.create_widgets()
        
    def create_widgets(self):
        search_frame = ttk.Frame(self.root)
        search_frame.pack(pady=10)
        
        ttk.Label(search_frame, text="Search Movie:").pack(side=tk.LEFT, padx=5)
        self.search_entry = ttk.Entry(search_frame, width=40)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        
        search_btn = ttk.Button(search_frame, text="Search", command=self.search_movies)
        search_btn.pack(side=tk.LEFT, padx=5)
        
        filter_frame = ttk.Frame(self.root)
        filter_frame.pack(pady=5)
        
        ttk.Label(filter_frame, text="Filter by:").pack(side=tk.LEFT)
        self.filter_var = tk.StringVar()
        filters = ["All", "New Releases", "Classics", "Action", "Comedy", "Drama"]
        for f in filters:
            ttk.Radiobutton(filter_frame, text=f, variable=self.filter_var, 
                            value=f.lower().replace(" ", "_")).pack(side=tk.LEFT, padx=5)
        self.filter_var.set("all")
        
        self.movies_frame = ttk.Frame(self.root)
        self.movies_frame.pack(fill=tk.BOTH, expand=True)
        
        self.display_sample_movies()
        
    def display_sample_movies(self):
        for widget in self.movies_frame.winfo_children():
            widget.destroy()
        
        sample_movies = [
            {"Title": "The Shawshank Redemption", "Year": "1994", "Poster": "https://m.media-amazon.com/images/M/MV5BNDE3ODcxYzMtY2YzZC00NmNlLWJiNDMtZDViZWM2MzIxZDYwXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_SX300.jpg"},
            {"Title": "The Dark Knight", "Year": "2008", "Poster": "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SX300.jpg"},
            {"Title": "Inception", "Year": "2010", "Poster": "https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SX300.jpg"},
            {"Title": "Pulp Fiction", "Year": "1994", "Poster": "https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI5MjljXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg"},
            {"Title": "Avengers: Endgame", "Year": "2019", "Poster": "https://m.media-amazon.com/images/M/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzQ2NzM@._V1_SX300.jpg"},
            {"Title": "The Godfather", "Year": "1972", "Poster": "https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg"}
        ]
        
        for i, movie in enumerate(sample_movies):
            self.display_movie(movie, i)

    def display_movie(self, movie, index):
        row = index // 3
        col = index % 3
        
        movie_frame = ttk.Frame(self.movies_frame)
        movie_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
        
        try:
            response = requests.get(movie["Poster"])
            img_data = response.content
            img = Image.open(BytesIO(img_data))
            img = img.resize((150, 220), Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            
            poster_label = ttk.Label(movie_frame, image=photo)
            poster_label.image = photo
            poster_label.pack()
            
            poster_label.bind("<Button-1>", lambda e, m=movie: self.show_movie_details(m))
        except:
            no_image_label = tk.Label(movie_frame, text="No Image Available", width=20, height=10)
            no_image_label.pack()
            no_image_label.bind("<Button-1>", lambda e, m=movie: self.show_movie_details(m))
        
        ttk.Label(movie_frame, text=movie["Title"], wraplength=150, justify="center").pack()
        ttk.Label(movie_frame, text=f"({movie['Year']})", foreground="gray").pack()
    
    def search_movies(self):
        query = self.search_entry.get()
        if not query:
            messagebox.showwarning("Warning", "Please enter a search term")
            return
            
        params = {
            "s": query,
            "apikey": self.api_key,
            "type": "movie"
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            data = response.json()
            
            if data.get("Response") == "True":
                for widget in self.movies_frame.winfo_children():
                    widget.destroy()
                
                for i, movie in enumerate(data["Search"]):
                    self.display_movie(movie, i)
            else:
                messagebox.showerror("Error", data.get("Error", "No movies found"))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch data: {str(e)}")
    
    def show_movie_details(self, movie):
        details_window = tk.Toplevel(self.root)
        details_window.title(movie["Title"])
        details_window.geometry("600x400")
        
        params = {
            "t": movie["Title"],
            "y": movie.get("Year", ""),
            "apikey": self.api_key,
            "plot": "full"
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            details = response.json()
            
            if details.get("Response") == "True":
                main_frame = ttk.Frame(details_window)
                main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
                
                left_frame = ttk.Frame(main_frame)
                left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5)
                
                try:
                    response = requests.get(details["Poster"])
                    img_data = response.content
                    img = Image.open(BytesIO(img_data))
                    img = img.resize((200, 300), Image.LANCZOS)
                    photo = ImageTk.PhotoImage(img)
                    
                    poster_label = ttk.Label(left_frame, image=photo)
                    poster_label.image = photo
                    poster_label.pack()
                except:
                    tk.Label(left_frame, text="No Image Available", width=25, height=15).pack()
                
                right_frame = ttk.Frame(main_frame)
                right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)
                
                ttk.Label(right_frame, text=details["Title"], font=("Arial", 16, "bold")).pack(anchor="w")
                ttk.Label(right_frame, text=f"Year: {details.get('Year', 'N/A')}").pack(anchor="w")
                ttk.Label(right_frame, text=f"Rated: {details.get('Rated', 'N/A')}").pack(anchor="w")
                ttk.Label(right_frame, text=f"Runtime: {details.get('Runtime', 'N/A')}").pack(anchor="w")
                ttk.Label(right_frame, text=f"Genre: {details.get('Genre', 'N/A')}").pack(anchor="w")
                ttk.Label(right_frame, text=f"Director: {details.get('Director', 'N/A')}").pack(anchor="w")
                ttk.Label(right_frame, text=f"Actors: {details.get('Actors', 'N/A')}").pack(anchor="w")
                
                plot_frame = ttk.LabelFrame(right_frame, text="Plot")
                plot_frame.pack(fill=tk.X, pady=5)
                plot_text = tk.Text(plot_frame, wrap=tk.WORD, height=6, width=40)
                plot_text.insert(tk.END, details.get("Plot", "N/A"))
                plot_text.config(state=tk.DISABLED)
                plot_text.pack(fill=tk.BOTH, expand=True)
                
                if details.get("imdbID"):
                    imdb_btn = ttk.Button(right_frame, text="View on IMDb", 
                        command=lambda: webbrowser.open(f"https://www.imdb.com/title/{details['imdbID']}/"))
                    imdb_btn.pack(pady=5)
            else:
                messagebox.showerror("Error", details.get("Error", "Could not fetch details"))
                details_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch details: {str(e)}")
            details_window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = HollywoodMoviesApp(root)
    root.mainloop()
