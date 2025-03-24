import time
import tkinter as tk
import random

import pandas as pd
data = pd.read_csv("data/french_words.csv")
data = data.to_dict(orient="records")
def next_card():
    global random_word
    random_word = random.choice(data)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=random_word["French"], fill="black")
    canvas.itemconfig(image, image=old_image)
    window.after(3000, generate)
def generate():
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=random_word["English"], fill="white")
    canvas.itemconfig(image, image=new_image)
    window.after(3000, next_card)


def accepted():
    global data
    data.remove(random_word)
    df = pd.DataFrame(data)
    df.to_csv("data/french_words.csv", index=False)
    pd.DataFrame([random_word]).to_csv("data/learned_words.csv", mode="a", index=False, header=False)
    next_card()

BACKGROUND_COLOR = "#B1DDC6"
window = tk.Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
canvas = tk.Canvas(width=800, height=526)
new_image = tk.PhotoImage(file="images/card_back.png")
old_image = tk.PhotoImage(file="images/card_front.png")
image = canvas.create_image(400, 263, image=old_image)
language = canvas.create_text(400, 150, text="", fill='black', font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", fill='black', font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

cross = tk.PhotoImage(file="images/wrong.png")
button_cross = tk.Button(image=cross, highlightthickness=0, bd=0, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, command=next_card)
button_cross.grid(column=0, row=1)

right = tk.PhotoImage(file="images/right.png")
button_right = tk.Button(image=right, highlightthickness=0, bd=0, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, command=accepted)
button_right.grid(column=1, row=1)
next_card()
window.mainloop()

