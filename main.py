import tkinter as tk
from tkinter import ttk, messagebox
from database import connect_db


window = tk.Tk()

window.title("📚 Library Management System")
window.geometry("750x650")
window.configure(bg="#EAF2F8")


title = tk.Label(
    window,
    text="📚 Library Management System",
    font=("Arial", 22, "bold"),
    bg="#EAF2F8",
    fg="#1B4F72"
)

title.pack(pady=20)


def add_book():

    db = connect_db()
    cursor = db.cursor()

    sql = """
    INSERT INTO books(title, author, category, quantity)
    VALUES(%s,%s,%s,%s)
    """

    values = (
        title_entry.get(),
        author_entry.get(),
        category_entry.get(),
        quantity_entry.get()
    )

    cursor.execute(sql, values)

    db.commit()
    db.close()

    messagebox.showinfo(
        "Success ✅",
        "Book Added Successfully 📚"
    )


# Entry Style

label_font = ("Arial", 12, "bold")
entry_font = ("Arial", 12)


# Title

tk.Label(
    window,
    text="📖 Book Title",
    font=label_font,
    bg="#EAF2F8",
    fg="#1B4F72"
).pack()

title_entry = tk.Entry(
    window,
    font=entry_font,
    width=30
)
title_entry.pack(pady=5)


# Author

tk.Label(
    window,
    text="✍️ Author",
    font=label_font,
    bg="#EAF2F8",
    fg="#1B4F72"
).pack()

author_entry = tk.Entry(
    window,
    font=entry_font,
    width=30
)
author_entry.pack(pady=5)


# Category

tk.Label(
    window,
    text="📂 Category",
    font=label_font,
    bg="#EAF2F8",
    fg="#1B4F72"
).pack()

category_entry = tk.Entry(
    window,
    font=entry_font,
    width=30
)
category_entry.pack(pady=5)


# Quantity

tk.Label(
    window,
    text="🔢 Quantity",
    font=label_font,
    bg="#EAF2F8",
    fg="#1B4F72"
).pack()

quantity_entry = tk.Entry(
    window,
    font=entry_font,
    width=30
)
quantity_entry.pack(pady=5)


def view_books():

    db = connect_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM books")
    records = cursor.fetchall()

    for row in tree.get_children():
        tree.delete(row)

    for record in records:
        tree.insert("", tk.END, values=record)

    db.close()


# Table Style

style = ttk.Style()

style.configure(
    "Treeview",
    font=("Arial", 11),
    rowheight=30
)

style.configure(
    "Treeview.Heading",
    font=("Arial", 12, "bold")
)


tree = ttk.Treeview(
    window,
    columns=("ID", "Title", "Author", "Category", "Quantity"),
    show="headings",
    height=8
)


tree.heading("ID", text="🆔 ID")
tree.heading("Title", text="📖 Title")
tree.heading("Author", text="✍️ Author")
tree.heading("Category", text="📂 Category")
tree.heading("Quantity", text="🔢 Quantity")


tree.column("ID", width=50)
tree.column("Title", width=150)
tree.column("Author", width=120)
tree.column("Category", width=120)
tree.column("Quantity", width=80)


tree.pack(pady=20)


def update_book():

    db = connect_db()
    cursor = db.cursor()

    sql = """
    UPDATE books
    SET title=%s, author=%s, category=%s, quantity=%s
    WHERE book_id=%s
    """

    values = (
        title_entry.get(),
        author_entry.get(),
        category_entry.get(),
        quantity_entry.get(),
        id_entry.get()
    )

    cursor.execute(sql, values)

    db.commit()
    db.close()

    messagebox.showinfo(
        "Update ✅",
        "Book Updated Successfully 📚"
    )


def delete_book():

    db = connect_db()
    cursor = db.cursor()

    sql = "DELETE FROM books WHERE book_id=%s"

    value = (id_entry.get(),)

    cursor.execute(sql, value)

    db.commit()
    db.close()

    messagebox.showinfo(
        "Delete 🗑️",
        "Book Deleted Successfully"
    )


# Book ID

tk.Label(
    window,
    text="🆔 Book ID",
    font=("Arial",12,"bold"),
    bg="#EAF2F8",
    fg="#1B4F72"
).pack()

id_entry = tk.Entry(
    window,
    font=("Arial",12),
    width=30
)

id_entry.pack(pady=5)


# Button Style

button_font = ("Arial", 12, "bold")


add_button = tk.Button(
    window,
    text="➕ Add Book",
    command=add_book,
    font=button_font,
    bg="#27AE60",
    fg="white",
    width=20
)
add_button.pack(pady=5)


view_button = tk.Button(
    window,
    text="📚 View Books",
    command=view_books,
    font=button_font,
    bg="#3498DB",
    fg="white",
    width=20
)
view_button.pack(pady=5)


update_button = tk.Button(
    window,
    text="✏️ Update Book",
    command=update_book,
    font=button_font,
    bg="#F39C12",
    fg="white",
    width=20
)
update_button.pack(pady=5)


delete_button = tk.Button(
    window,
    text="🗑️ Delete Book",
    command=delete_book,
    font=button_font,
    bg="#E74C3C",
    fg="white",
    width=20
)
delete_button.pack(pady=5)


# Start Application

window.mainloop()