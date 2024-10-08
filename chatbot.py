from tkinter import *
import json
import random

# Load responses from JSON file
def load_responses():
    with open('responses.json', 'r') as file:
        return json.load(file)

# Function to handle sending messages
def send(event=None):
    user_input = e.get().strip().lower()  # Normalize input
    if user_input:  # Only send if there's input
        txt.insert(END, "\nYou -> " + user_input)
        e.delete(0, END)

        response = responses.get(user_input, ["Sorry, I didn't understand that."])
        txt.insert(END, "\nBot -> " + random.choice(response))

# Function to clear the chat window
def clear_chat():
    txt.delete('1.0', END)

# Load responses from the JSON file
responses = load_responses()

# Setting up the main window
root = Tk()
root.title("Simple Chatbot")
root.geometry("400x500")

# Creating the chat window with a scrollbar
frame = Frame(root)
frame.pack(padx=10, pady=10)

txt = Text(frame, bg="light grey", wrap=WORD)
scrollbar = Scrollbar(frame, command=txt.yview)
txt.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)
txt.pack(side=LEFT, fill=BOTH, expand=True)

# Creating the entry box for user input
e = Entry(root, width=80)
e.pack(padx=10, pady=10)

# Binding the Enter key to the send function
e.bind("<Return>", send)

# Creating the send button
send_button = Button(root, text="Send", command=send)
send_button.pack(side=LEFT, padx=5)

# Creating a clear button
clear_button = Button(root, text="Clear", command=clear_chat)
clear_button.pack(side=RIGHT, padx=5)

root.mainloop()
