# Software Name: Notify_Me
# Category: Development
# Description: Notify Me is a development software application that helps developers stay updated on the latest news and updates related to their programming languages, frameworks, and libraries of interest. It provides a user-friendly interface where developers can select their favorite topics and sources. The application then aggregates and displays relevant articles, blog posts, tutorials, and release notes in a centralized feed, allowing developers to stay informed and up-to-date with the latest developments in their field.

import feedparser
import tkinter as tk
from tkinter import ttk
import webbrowser

class NotifyMeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Notify Me")

        self.topics = {
            "Python": [
                "https://www.python.org/blogs/rss/",
                "https://realpython.com/atom.xml"
            ],
            "JavaScript": [
                "https://www.javascripttutorial.net/feed/"
            ],
            "React": [
                "https://reactjs.org/feed.xml"
            ]
        }

        self.selected_topics = []
        self.news_feed = []

        self.setup_ui()

    def setup_ui(self):
        # Topic Selection
        self.topic_label = ttk.Label(self.root, text="Select Topics:")
        self.topic_label.pack(pady=5)

        self.topic_frame = ttk.Frame(self.root)
        self.topic_frame.pack()

        self.topic_checkboxes = {}
        for topic in self.topics:
            var = tk.BooleanVar()
            checkbox = ttk.Checkbutton(self.topic_frame, text=topic, variable=var,
                                         command=lambda t=topic, v=var: self.toggle_topic(t, v.get()))
            checkbox.pack(side=tk.LEFT, padx=5)
            self.topic_checkboxes[topic] = var

        # Fetch News Button
        self.fetch_button = ttk.Button(self.root, text="Fetch News", command=self.fetch_news)
        self.fetch_button.pack(pady=10)

        # News Feed Display
        self.news_label = ttk.Label(self.root, text="News Feed:")
        self.news_label.pack()

        self.news_listbox = tk.Listbox(self.root, width=80, height=20, font=("Arial", 10))
        self.news_listbox.pack(padx=10, pady=5)
        self.news_listbox.bind("<Double-Button-1>", self.open_news_article)

        self.status_label = ttk.Label(self.root, text="")
        self.status_label.pack(pady=5)

    def toggle_topic(self, topic, is_selected):
        if is_selected and topic not in self.selected_topics:
            self.selected_topics.append(topic)
        elif not is_selected and topic in self.selected_topics:
            self.selected_topics.remove(topic)

    def fetch_news(self):
        self.news_feed = []
        self.news_listbox.delete(0, tk.END)
        self.status_label.config(text="Fetching news...")

        for topic in self.selected_topics:
            for url in self.topics[topic]:
                try:
                    feed = feedparser.parse(url)
                    for entry in feed.entries:
                        self.news_feed.append({
                            "title": entry.title,
                            "link": entry.link,
                            "topic": topic
                        })
                except Exception as e:
                    print(f"Error fetching feed from {url}: {e}")
                    self.status_label.config(text=f"Error fetching feed from {url}: {e}")
                    return

        self.news_feed.sort(key=lambda x: x["title"])

        for item in self.news_feed:
            self.news_listbox.insert(tk.END, f"[{item['topic']}] {item['title']}")

        self.status_label.config(text="News fetched successfully.")

    def open_news_article(self, event):
        try:
            index = self.news_listbox.curselection()[0]
            url = self.news_feed[index]["link"]
            webbrowser.open_new(url)
        except IndexError:
            pass  # No item selected

if __name__ == "__main__":
    root = tk.Tk()
    app = NotifyMeApp(root)
    root.mainloop()