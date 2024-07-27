#imports
from tkinter import ttk
from tkinter import *
import sqlite3
import google.generativeai as genai
import os

#Model and API setup
genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')

#functions
def OPENAI_APICALL():
    prompt = user_data.get()
    response = model.generate_content(prompt)
   # output = Label(tab2, text = response.text, font = (20)).pack()
    print(response.text)
#app starts
window = Tk()

#tab creation
notebook = ttk.Notebook(window)
tab1 = Frame(notebook)
tab2 = Frame (notebook)
notebook.add(tab1, text = "HOME")
notebook.add(tab2,text = "HISTORY")
notebook.pack(fill="both", expand=True)
tab1.configure(background="white")
tab2.configure(background="white")


#window configuration
window.geometry("600x400")
window.maxsize(width=600,height=400)
window.minsize(width=600,height=400)
window.title("BodyGuru")
icon = PhotoImage(file="C:\\Users\\franc\\source\\repos\\BodyGuru\\BodyGuruImages\\icon.png")
window.iconphoto(True, icon)

#TAB-1
logo = PhotoImage(file = "C:\\Users\\franc\\source\\repos\\BodyGuru\\BodyGuruImages\\logo.png")
logo_txt = Label(tab1, image=logo, borderwidth=0).pack()
enter_txt = Label(tab1, text="Enter you're Question", font = ('Arial'), bg = 'White' ).pack()
user_data = Entry(tab1, font = (20))
user_data.pack()
submit = Button(tab1, text = "Submit", command=OPENAI_APICALL, padx = 10).pack()


#app ends
window.mainloop()

