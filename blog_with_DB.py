import tkinter as tk
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect('blog_posts.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL
)
''')
conn.commit()

def add_post():
    title = title_entry.get()
    content = content_text.get("1.0", tk.END).strip()
    
    if title and content:
        cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (title, content))
        conn.commit()
        messagebox.showinfo("Success", "Post added successfully!")
        view_posts()
        clear_fields()
    else:
        messagebox.showerror("Error", "Title and content cannot be empty.")

def edit_post():
    selected_post_id = post_listbox.curselection()
    if not selected_post_id:
        messagebox.showerror("Error", "No post selected.")
        return
    
    post_id = post_listbox.get(selected_post_id[0]).split(" - ")[0]  
    title = title_entry.get()
    content = content_text.get("1.0", tk.END).strip()
    
    if title and content:
        cursor.execute("UPDATE posts SET title = ?, content = ? WHERE id = ?", (title, content, post_id))
        conn.commit()
        messagebox.showinfo("Success", "Post updated successfully!")
        view_posts()
        clear_fields()
    else:
        messagebox.showerror("Error", "Title and content cannot be empty.")

def delete_post():
    selected_post_id = post_listbox.curselection()
    if not selected_post_id:
        messagebox.showerror("Error", "No post selected.")
        return
    
    post_id = post_listbox.get(selected_post_id[0]).split(" - ")[0]  
    cursor.execute("DELETE FROM posts WHERE id = ?", (post_id,))
    conn.commit()
    messagebox.showinfo("Success", "Post deleted successfully!")
    view_posts()  

def view_posts():
    post_listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    
    for post in posts:
        post_listbox.insert(tk.END, f"{post[0]} - {post[1]}")

def clear_fields():
    title_entry.delete(0, tk.END)
    content_text.delete("1.0", tk.END)

def load_post_for_edit(event):
    selected_post_id = post_listbox.curselection()
    if not selected_post_id:
        return
    
    post_id = post_listbox.get(selected_post_id[0]).split(" - ")[0] 
    cursor.execute("SELECT title, content FROM posts WHERE id = ?", (post_id,))
    post = cursor.fetchone()
    
    title_entry.delete(0, tk.END)
    content_text.delete("1.0", tk.END)
    
    if post:
        title_entry.insert(tk.END, post[0])
        content_text.insert(tk.END, post[1])

root = tk.Tk()
root.title("Simple Blogging Platform")

title_label = tk.Label(root, text="Blog Post Title:")
title_label.pack()
title_entry = tk.Entry(root, width=50)
title_entry.pack()

content_label = tk.Label(root, text="Blog Post Content:")
content_label.pack()
content_text = tk.Text(root, height=10, width=50)
content_text.pack()

add_button = tk.Button(root, text="Add Post", command=add_post)
add_button.pack(pady=5)

edit_button = tk.Button(root, text="Edit Post", command=edit_post)
edit_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Post", command=delete_post)
delete_button.pack(pady=5)

post_listbox = tk.Listbox(root, width=50, height=10)
post_listbox.pack(pady=5)

view_button = tk.Button(root, text="View Posts", command=view_posts)
view_button.pack(pady=5)

post_listbox.bind("<Double-1>", load_post_for_edit)

view_posts()
root.mainloop()
conn.close()
