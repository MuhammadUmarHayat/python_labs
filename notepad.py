import tkinter as tk
from tkinter import filedialog, messagebox

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Notepad")
        self.root.geometry("800x600")

        # Add text area
        self.text_area = tk.Text(root, wrap='word', undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=1)

        # Initialize menu
        self.menu_bar = tk.Menu(root)
        root.config(menu=self.menu_bar)

        # File menu
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_notepad)

        # Edit menu
        edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo", command=self.undo_action)
        edit_menu.add_command(label="Redo", command=self.redo_action)
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=self.cut_text)
        edit_menu.add_command(label="Copy", command=self.copy_text)
        edit_menu.add_command(label="Paste", command=self.paste_text)
        edit_menu.add_command(label="Delete", command=self.delete_text)

        # Help menu
        help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

        # Track current file
        self.current_file = None

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.current_file = None

    def open_file(self):
        self.current_file = filedialog.askopenfilename(defaultextension=".txt",
                                                       filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
        if self.current_file:
            with open(self.current_file, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())

    def save_file(self):
        if not self.current_file:
            self.current_file = filedialog.asksaveasfilename(defaultextension=".txt",
                                                            filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
        if self.current_file:
            with open(self.current_file, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            messagebox.showinfo("Save", "File Saved Successfully!")

    def exit_notepad(self):
        self.root.quit()

    def undo_action(self):
        self.text_area.event_generate("<<Undo>>")

    def redo_action(self):
        self.text_area.event_generate("<<Redo>>")

    def cut_text(self):
        self.text_area.event_generate("<<Cut>>")

    def copy_text(self):
        self.text_area.event_generate("<<Copy>>")

    def paste_text(self):
        self.text_area.event_generate("<<Paste>>")

    def delete_text(self):
        self.text_area.delete(tk.SEL_FIRST, tk.SEL_LAST)

    def show_about(self):
        messagebox.showinfo("About", "Python Notepad Application using Tkinter.")

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    notepad = Notepad(root)
    root.mainloop()
