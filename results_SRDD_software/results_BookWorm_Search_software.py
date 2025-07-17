# Software Name: BookWorm_Search
# Category: Reference_Books
# Description: BookWorm Search is a software application that helps users easily search for books in their personal libraries or online. It provides a simple and intuitive interface where users can enter the title, author, or keywords related to the book they are searching for. The software then displays matching results with relevant book details such as title, author, summary, and cover image. Users can click on a book to view more information and add it to their reading list. BookWorm Search aims to simplify the process of finding and accessing books.

import tkinter as tk
from tkinter import ttk
import json
import requests
from PIL import Image, ImageTk
from io import BytesIO

class BookWormSearch:
    def __init__(self, root):
        self.root = root
        self.root.title("BookWorm Search")

        self.search_label = ttk.Label(root, text="Search:")
        self.search_label.grid(row=0, column=0, padx=5, pady=5)

        self.search_entry = ttk.Entry(root, width=30)
        self.search_entry.grid(row=0, column=1, padx=5, pady=5)

        self.search_button = ttk.Button(root, text="Search", command=self.search_books)
        self.search_button.grid(row=0, column=2, padx=5, pady=5)

        self.results_tree = ttk.Treeview(root, columns=("Title", "Author", "Summary"), show="headings")
        self.results_tree.heading("Title", text="Title")
        self.results_tree.heading("Author", text="Author")
        self.results_tree.heading("Summary", text="Summary")
        self.results_tree.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        self.results_tree.bind("<Double-1>", self.show_book_details)

        self.book_details_window = None

        # Placeholder book data (replace with your data source)
        self.book_data = [
            {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "summary": "A classic fantasy adventure.", "cover_url": "https://m.media-amazon.com/images/I/71jLBXtWJWL._AC_UF1000,1000_QL80_.jpg"},
            {"title": "Pride and Prejudice", "author": "Jane Austen", "summary": "A romantic novel set in 19th century England.", "cover_url": "https://images-na.ssl-images-amazon.com/images/I/71Q1IuGjroL.jpg"},
            {"title": "1984", "author": "George Orwell", "summary": "A dystopian novel about totalitarianism.", "cover_url": "https://m.media-amazon.com/images/I/71w3oU-bJQL._AC_UF1000,1000_QL80_.jpg"},
        ]


    def search_books(self):
        search_term = self.search_entry.get().lower()
        self.results_tree.delete(*self.results_tree.get_children()) # Clear previous results

        for book in self.book_data:
            if search_term in book["title"].lower() or \
               search_term in book["author"].lower() or \
               search_term in book["summary"].lower():
                self.results_tree.insert("", tk.END, values=(book["title"], book["author"], book["summary"]))

    def show_book_details(self, event):
        selected_item = self.results_tree.selection()
        if not selected_item:
            return

        book_title = self.results_tree.item(selected_item[0])['values'][0]
        book = next((b for b in self.book_data if b["title"] == book_title), None)

        if not book:
            return

        if self.book_details_window:
            self.book_details_window.destroy()

        self.book_details_window = tk.Toplevel(self.root)
        self.book_details_window.title(book["title"])

        title_label = ttk.Label(self.book_details_window, text=f"Title: {book['title']}")
        title_label.grid(row=0, column=0, padx=5, pady=5)

        author_label = ttk.Label(self.book_details_window, text=f"Author: {book['author']}")
        author_label.grid(row=1, column=0, padx=5, pady=5)

        summary_label = ttk.Label(self.book_details_window, text=f"Summary: {book['summary']}", wraplength=300)
        summary_label.grid(row=2, column=0, padx=5, pady=5)

        try:
            response = requests.get(book["cover_url"])
            response.raise_for_status()
            image_data = BytesIO(response.content)
            img = Image.open(image_data)
            img = img.resize((150, 200), Image.LANCZOS)  # Resize for display
            self.photo = ImageTk.PhotoImage(img)  # Keep a reference to prevent garbage collection
            cover_label = ttk.Label(self.book_details_window, image=self.photo)
            cover_label.grid(row=3, column=0, padx=5, pady=5)
        except (requests.exceptions.RequestException, FileNotFoundError):
            cover_label = ttk.Label(self.book_details_window, text="Cover Image Not Available")
            cover_label.grid(row=3, column=0, padx=5, pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = BookWormSearch(root)
    root.mainloop()