# Software Name: Notepad_Plus
# Category: Tools_Utilities
# Description: Notepad Plus is a software application that provides an enhanced text editing experience. It includes features such as syntax highlighting, code indentation, search and replace functionality, and customizable themes. Notepad Plus allows users to create and edit text files with ease, making it a versatile tool for programmers, writers, and anyone who needs a powerful yet simple text editor.

import tkinter as tk
from tkinter import scrolledtext, Menu, filedialog, messagebox, ttk
import os

class NotepadPlus:
    def __init__(self, master):
        self.master = master
        master.title("Notepad Plus")
        master.geometry("800x600")

        self.filename = None
        self.default_font = ("Courier New", 12)
        self.current_font = self.default_font

        self.text_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, font=self.current_font)
        self.text_area.pack(expand=True, fill=tk.BOTH)

        self.create_menu()
        self.create_statusbar()

        self.bind_shortcuts()

    def create_menu(self):
        self.menubar = Menu(self.master)

        # File Menu
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
        filemenu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
        filemenu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        filemenu.add_command(label="Save As...", command=self.save_file_as)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.exit_app)
        self.menubar.add_cascade(label="File", menu=filemenu)

        # Edit Menu
        editmenu = Menu(self.menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=self.undo, accelerator="Ctrl+Z")
        editmenu.add_command(label="Redo", command=self.redo, accelerator="Ctrl+Y")
        editmenu.add_separator()
        editmenu.add_command(label="Cut", command=self.cut, accelerator="Ctrl+X")
        editmenu.add_command(label="Copy", command=self.copy, accelerator="Ctrl+C")
        editmenu.add_command(label="Paste", command=self.paste, accelerator="Ctrl+V")
        editmenu.add_command(label="Delete", command=self.delete, accelerator="Del")
        editmenu.add_separator()
        editmenu.add_command(label="Find", command=self.find, accelerator="Ctrl+F")
        editmenu.add_command(label="Replace", command=self.replace, accelerator="Ctrl+H")
        editmenu.add_separator()
        editmenu.add_command(label="Select All", command=self.select_all, accelerator="Ctrl+A")
        self.menubar.add_cascade(label="Edit", menu=editmenu)
        
        # Format Menu
        formatmenu = Menu(self.menubar, tearoff=0)
        formatmenu.add_command(label="Font...", command=self.change_font)
        self.menubar.add_cascade(label="Format", menu=formatmenu)

        # Help Menu
        helpmenu = Menu(self.menubar, tearoff=0)
        helpmenu.add_command(label="About Notepad Plus", command=self.show_about)
        self.menubar.add_cascade(label="Help", menu=helpmenu)

        self.master.config(menu=self.menubar)

    def create_statusbar(self):
        self.statusbar = ttk.Label(self.master, text="Ready", relief=tk.SUNKEN, anchor=tk.W)
        self.statusbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.update_status()

    def update_status(self):
        line, column = self.text_area.index(tk.INSERT).split(".")
        self.statusbar.config(text=f"Line: {int(line) + 1}, Column: {int(column) + 1}")
        self.master.after(100, self.update_status)

    def bind_shortcuts(self):
        self.master.bind("<Control-n>", self.new_file)
        self.master.bind("<Control-o>", self.open_file)
        self.master.bind("<Control-s>", self.save_file)
        self.master.bind("<Control-f>", self.find)
        self.master.bind("<Control-h>", self.replace)
        self.master.bind("<Control-a>", self.select_all)

    def new_file(self, event=None):
        self.filename = None
        self.text_area.delete("1.0", tk.END)
        self.master.title("Notepad Plus - New File")

    def open_file(self, event=None):
        options = {
            'defaultextension': '.txt',
            'filetypes': [('All files', '*.*'), ('Text files', '*.txt'), ('Python files', '*.py')],
            'title': 'Open file'
        }
        self.filename = filedialog.askopenfilename(**options)
        if self.filename:
            try:
                with open(self.filename, "r") as file:
                    self.text_area.delete("1.0", tk.END)
                    self.text_area.insert(tk.END, file.read())
                self.master.title(f"Notepad Plus - {os.path.basename(self.filename)}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file:\n{e}")

    def save_file(self, event=None):
        if self.filename:
            try:
                with open(self.filename, "w") as file:
                    file.write(self.text_area.get("1.0", tk.END))
                self.statusbar.config(text="File saved successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file:\n{e}")
        else:
            self.save_file_as()

    def save_file_as(self):
        options = {
            'defaultextension': '.txt',
            'filetypes': [('All files', '*.*'), ('Text files', '*.txt'), ('Python files', '*.py')],
            'title': 'Save as'
        }
        self.filename = filedialog.asksaveasfilename(**options)
        if self.filename:
            try:
                with open(self.filename, "w") as file:
                    file.write(self.text_area.get("1.0", tk.END))
                self.master.title(f"Notepad Plus - {os.path.basename(self.filename)}")
                self.statusbar.config(text="File saved successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file:\n{e}")

    def exit_app(self):
        if messagebox.askyesno("Confirm Exit", "Do you want to save before exiting?"):
            self.save_file()
        self.master.destroy()

    def undo(self):
        try:
            self.text_area.edit_undo()
        except tk.TclError:
            pass

    def redo(self):
        try:
            self.text_area.edit_redo()
        except tk.TclError:
            pass

    def cut(self):
        self.text_area.event_generate("<<Cut>>")

    def copy(self):
        self.text_area.event_generate("<<Copy>>")

    def paste(self):
        self.text_area.event_generate("<<Paste>>")

    def delete(self):
        self.text_area.delete(tk.SEL_FIRST, tk.SEL_LAST)

    def find(self, event=None):
        def search():
            text_to_find = find_entry.get()
            self.text_area.tag_remove('found', '1.0', tk.END)
            if text_to_find:
                start = '1.0'
                while True:
                    start = self.text_area.search(text_to_find, start, stopindex=tk.END)
                    if not start:
                        break
                    end = f'{start}+{len(text_to_find)}c'
                    self.text_area.tag_add('found', start, end)
                    start = end
                self.text_area.tag_config('found', background='yellow')

        find_dialog = tk.Toplevel(self.master)
        find_dialog.title("Find")
        find_label = tk.Label(find_dialog, text="Find:")
        find_label.grid(row=0, column=0, padx=5, pady=5)
        find_entry = tk.Entry(find_dialog, width=30)
        find_entry.grid(row=0, column=1, padx=5, pady=5)
        find_button = tk.Button(find_dialog, text="Find", command=search)
        find_button.grid(row=0, column=2, padx=5, pady=5)

    def replace(self, event=None):
        def replace_text():
            text_to_find = find_entry.get()
            text_to_replace = replace_entry.get()
            self.text_area.tag_remove('found', '1.0', tk.END)
            if text_to_find:
                start = '1.0'
                while True:
                    start = self.text_area.search(text_to_find, start, stopindex=tk.END)
                    if not start:
                        break
                    end = f'{start}+{len(text_to_find)}c'
                    self.text_area.delete(start, end)
                    self.text_area.insert(start, text_to_replace)
                    start = f'{start}+{len(text_to_replace)}c'

        replace_dialog = tk.Toplevel(self.master)
        replace_dialog.title("Replace")
        find_label = tk.Label(replace_dialog, text="Find:")
        find_label.grid(row=0, column=0, padx=5, pady=5)
        find_entry = tk.Entry(replace_dialog, width=30)
        find_entry.grid(row=0, column=1, padx=5, pady=5)
        replace_label = tk.Label(replace_dialog, text="Replace with:")
        replace_label.grid(row=1, column=0, padx=5, pady=5)
        replace_entry = tk.Entry(replace_dialog, width=30)
        replace_entry.grid(row=1, column=1, padx=5, pady=5)
        replace_button = tk.Button(replace_dialog, text="Replace All", command=replace_text)
        replace_button.grid(row=2, column=1, padx=5, pady=5)

    def select_all(self, event=None):
        self.text_area.tag_add(tk.SEL, "1.0", tk.END)
        self.text_area.mark_set(tk.INSERT, "1.0")
        self.text_area.see(tk.INSERT)
        return 'break'

    def show_about(self):
        messagebox.showinfo("About Notepad Plus", "Notepad Plus - A simple text editor\nCreated with Tkinter")
    
    def change_font(self):
        from tkinter import font
        
        def set_font():
            self.current_font = (font_family.get(), font_size.get())
            self.text_area.config(font=self.current_font)
            font_dialog.destroy()
        
        font_dialog = tk.Toplevel(self.master)
        font_dialog.title("Font")
        
        # Font Family
        font_family_label = tk.Label(font_dialog, text="Font Family:")
        font_family_label.grid(row=0, column=0, padx=5, pady=5)
        font_family = tk.StringVar()
        font_family.set(self.current_font[0])
        font_family_dropdown = ttk.Combobox(font_dialog, textvariable=font_family, values=font.families(), state="readonly")
        font_family_dropdown.grid(row=0, column=1, padx=5, pady=5)
        
        # Font Size
        font_size_label = tk.Label(font_dialog, text="Font Size:")
        font_size_label.grid(row=1, column=0, padx=5, pady=5)
        font_size = tk.IntVar()
        font_size.set(self.current_font[1])
        font_size_spinbox = tk.Spinbox(font_dialog, textvariable=font_size, from_=8, to=48, increment=2)
        font_size_spinbox.grid(row=1, column=1, padx=5, pady=5)
        
        # Apply Button
        apply_button = tk.Button(font_dialog, text="Apply", command=set_font)
        apply_button.grid(row=2, column=1, padx=5, pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    notepad = NotepadPlus(root)
    root.mainloop()