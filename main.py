from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
word_choice = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
    library = data.to_dict("records")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    library = data.to_dict("records")


def flip():

    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(title_txt, text="English", fill="white")
    canvas.itemconfig(word_txt, text=word_choice["English"], fill="white")


def new_word():

    global word_choice, change, library

    window.after_cancel(change)
    word_choice = random.choice(library)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(title_txt, text="French", fill="black")
    canvas.itemconfig(word_txt, text=word_choice["French"], fill="black")

    change = window.after(3000, flip)


def save_word():
    global library

    library.remove(word_choice)
    new_lib = pandas.DataFrame(library)
    new_lib.to_csv("data/words_to_learn.csv", index=False)
    new_word()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
change = window.after(3000, flip)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
cross = PhotoImage(file="images/wrong.png")
tick = PhotoImage(file="images/right.png")

canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
cross_button = Button(window, image=cross, highlightthickness=0, padx=50, command=new_word)
cross_button.grid(row=1, column=0)

tick_button = Button(window, image=tick, highlightthickness=0, padx=50, command=save_word)
tick_button.grid(row=1, column=1)

# card text
title_txt = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_txt = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

new_word()

window.mainloop()

