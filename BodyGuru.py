#imports
from tkinter import ttk
from tkinter import *
import sqlite3
import google.generativeai as genai
import os

# SQL connect
conn = sqlite3.connect('HISTORY.db')
c = conn.cursor()

# Model and API setup
genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to update history tab
def update_history():
    history.delete('1.0', END)  # Clear existing content
    c.execute("SELECT * FROM conversations")
    data = c.fetchall()
    for item in data:
        history.insert(END, "QUESTION:\n")
        history.insert(END, item[0] + "\n\n\n")
        history.insert(END, "ANSWER:\n")
        history.insert(END, item[1] + "\n\n")

# Function to handle API call and insert into DB
def OPENAI_APICALL():
    prompt = user_data.get()
    response = model.generate_content(prompt)
    output_text = response.text
    text_output.insert(END, output_text)
    user_data.delete(0, END)
    # SQL insert
    c.execute("INSERT INTO conversations (prompt, reply) VALUES (?, ?)", (prompt, output_text))
    conn.commit()  # Commit the changes
    update_history()  # Update the history tab

# App starts
window = Tk()

# Tab creation
notebook = ttk.Notebook(window)
tab1 = Frame(notebook)
tab2 = Frame(notebook)
notebook.add(tab1, text="HOME")
notebook.add(tab2, text="HISTORY")
notebook.pack(fill="both", expand=True)
tab1.configure(background="white")
tab2.configure(background="white")

# Window configuration
window.geometry("600x400")
window.minsize(width=800, height=600)
window.title("BodyGuru")
icon = PhotoImage(file="C:\\Users\\franc\\source\\repos\\BodyGuru\\BodyGuruImages\\icon.png")
window.iconphoto(True, icon)

# TAB-1
logo = PhotoImage(file="C:\\Users\\franc\\source\\repos\\BodyGuru\\BodyGuruImages\\logo.png")
logo_txt = Label(tab1, image=logo, borderwidth=0).pack()
enter_txt = Label(tab1, text="Enter your Question", font=('Arial', 20, 'bold'), bg='White').pack(pady=40, padx=10)
user_data = Entry(tab1, font=(20), width=40)
user_data.pack(pady=10, padx=10)
submit = Button(tab1, text="SUBMIT", command=OPENAI_APICALL, padx=10, bg='black', fg='red', bd=0, font=('bold')).pack(pady=40, padx=10)
text_output = Text(tab1, wrap=WORD, height=10, width=90, relief=SOLID, font=('Arial', 10, 'bold'))
text_output.pack(side=LEFT, padx=10, pady=10, fill=BOTH, expand=True)
scrollbar = Scrollbar(tab1, command=text_output.yview)
scrollbar.pack(side=RIGHT, fill=Y)
text_output.config(yscrollcommand=scrollbar.set)

# TAB-2
history = Text(tab2, relief=SOLID, font=('Arial', 10, 'bold'))
history.pack(fill=BOTH, expand=True)

# Initial load of history
update_history()

# App ends
window.mainloop()


