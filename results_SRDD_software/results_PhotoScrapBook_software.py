# Software Name: PhotoScrapBook
# Category: Family_Kids
# Description: PhotoScrapBook is a software application that allows families to create digital scrapbooks of their precious memories. Users can upload and organize photos, add captions and notes, and customize the layout and design of each page. The app also offers a variety of templates, stickers, and decorative elements to enhance the visual appeal of the scrapbook. Families can share their scrapbooks with each other, preserving and reliving their cherished moments.

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk

class PhotoScrapBook:
    def __init__(self, master):
        self.master = master
        master.title("PhotoScrapBook")

        self.photos = []
        self.captions = {}
        self.current_page = 0
        self.templates = ["Template 1", "Template 2", "Template 3"]  # Example templates
        self.stickers = ["Sticker 1", "Sticker 2", "Sticker 3"]  # Example stickers

        # UI elements
        self.photo_label = tk.Label(master, text="No Photo Selected")
        self.photo_label.pack()

        self.caption_label = tk.Label(master, text="Caption:")
        self.caption_label.pack()
        self.caption_entry = tk.Entry(master)
        self.caption_entry.pack()

        self.add_photo_button = tk.Button(master, text="Add Photo", command=self.add_photo)
        self.add_photo_button.pack()

        self.next_button = tk.Button(master, text="Next", command=self.next_page)
        self.next_button.pack()

        self.prev_button = tk.Button(master, text="Previous", command=self.prev_page)
        self.prev_button.pack()

        self.template_label = tk.Label(master, text="Select Template:")
        self.template_label.pack()
        self.template_combo = ttk.Combobox(master, values=self.templates)
        self.template_combo.pack()

        self.sticker_label = tk.Label(master, text="Select Sticker:")
        self.sticker_label.pack()
        self.sticker_combo = ttk.Combobox(master, values=self.stickers)
        self.sticker_combo.pack()

        self.apply_template_button = tk.Button(master, text="Apply Template", command=self.apply_template)
        self.apply_template_button.pack()

        self.apply_sticker_button = tk.Button(master, text="Apply Sticker", command=self.apply_sticker)
        self.apply_sticker_button.pack()

        self.save_button = tk.Button(master, text="Save Scrapbook", command=self.save_scrapbook)
        self.save_button.pack()

        self.load_button = tk.Button(master, text="Load Scrapbook", command=self.load_scrapbook)
        self.load_button.pack()

        self.update_page()

    def add_photo(self):
        filename = filedialog.askopenfilename(initialdir=".", title="Select a photo",
                                              filetypes=(("Image files", "*.jpg *.jpeg *.png"), ("all files", "*.*")))
        if filename:
            self.photos.append(filename)
            self.captions[filename] = ""
            self.update_page()

    def next_page(self):
        if self.current_page < len(self.photos) - 1:
            self.current_page += 1
            self.update_page()

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.update_page()

    def update_page(self):
        if self.photos:
            photo_path = self.photos[self.current_page]
            try:
                img = Image.open(photo_path)
                img = img.resize((300, 300), Image.LANCZOS)  # Resize for display
                self.photo_image = ImageTk.PhotoImage(img)
                self.photo_label.config(image=self.photo_image)
                self.photo_label.image = self.photo_image
                self.caption_entry.delete(0, tk.END)
                self.caption_entry.insert(0, self.captions.get(photo_path, ""))  # Get caption or default to ""

            except FileNotFoundError:
                messagebox.showerror("Error", "Image file not found.")
                self.photos.pop(self.current_page) # Remove missing file from list.
                if not self.photos:
                     self.photo_label.config(text="No Photo Selected")
                     self.caption_entry.delete(0, tk.END)
                     self.current_page = 0
                else:
                    self.current_page = min(self.current_page, len(self.photos)-1) #adjust if page was last
                    self.update_page()

        else:
            self.photo_label.config(text="No Photo Selected")
            self.caption_entry.delete(0, tk.END)

    def apply_template(self):
        selected_template = self.template_combo.get()
        if selected_template:
            messagebox.showinfo("Template Applied", f"Template '{selected_template}' applied to the current page.")
        else:
            messagebox.showinfo("Warning", "No template selected.")

    def apply_sticker(self):
        selected_sticker = self.sticker_combo.get()
        if selected_sticker:
            messagebox.showinfo("Sticker Applied", f"Sticker '{selected_sticker}' applied to the current page.")
        else:
            messagebox.showinfo("Warning", "No sticker selected.")

    def save_scrapbook(self):
         for i,photo_path in enumerate(self.photos):
            self.captions[photo_path] = self.caption_entry.get()
         filepath = filedialog.asksaveasfilename(defaultextension=".txt",
                                           filetypes=[("Text file", "*.txt"), ("All files", "*.*")])
         if filepath:
            try:
                with open(filepath, "w") as f:
                    f.write(str({"photos":self.photos, "captions":self.captions}))
                messagebox.showinfo("Success", "Scrapbook saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Error saving scrapbook: {e}")


    def load_scrapbook(self):
        filepath = filedialog.askopenfilename(defaultextension=".txt",
                                          filetypes=[("Text file", "*.txt"), ("All files", "*.*")])
        if filepath:
            try:
                with open(filepath, "r") as f:
                    data = eval(f.read()) #Danger eval is bad, needs safe json alternative.
                    self.photos = data["photos"]
                    self.captions = data["captions"]
                    self.current_page = 0
                    self.update_page()
                messagebox.showinfo("Success", "Scrapbook loaded successfully!")

            except (FileNotFoundError, KeyError, SyntaxError) as e:
               messagebox.showerror("Error", f"Error loading scrapbook: {e}")



root = tk.Tk()
my_gui = PhotoScrapBook(root)
root.mainloop()