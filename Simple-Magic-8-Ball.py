# Import needed Phyton modules
import tkinter as tk
import random

# Create a list of fun answers
responses = [
    "Absolutely... if you're wearing socks.",
    "Nope. Not even in an alternative universe.",
    "Ask your cat. It knows.",
    "Yes, but only on Tuesdays.",
    "The moon says maybe.",
    "I consulted a squirrel. It's a yes.",
    "Your toaster disagrees.",
    "Try again after eating a banana.",
    "The vibes are off. Try later.",
    "Yes, but chaos will follow.",
    "No, unless you juggle flamming pineapples.",
    "I flipped a coin. It landed on its edge.",
    "The prophecy says... LOL no.",
    "Only if you dance first.",
    "Yes but tell no one.",
    "No, but it will be funny.",
    "Ask again when Mercury isn't retrograde.",
    "Sure, if you believe in unicorns.",
    "The answer is hidden in your laundry pile",
    "I would say yes, but the ducks are watching.",
]

# Track if the answer was shown
answered = False

# Handle Submit button click
def submit_question():
    global answered
    question = entry.get()
    if question.strip() and not answered:
            result.config(text=random.choice(responses))
            answered=True
            submit_btn.pack_forget()
            reset_btn.pack(pady=10)

# Handle Reset butoon click
def reset_question():
    global answered
    entry.delete(0, tk.END)
    result.config(text="")
    answered = False
    reset_btn.pack_forget()
    submit_btn.pack(pady=10)
    submit_btn.config(state="disabled")

# Enable Submit while typing
def on_type(event):
     if entry.get().strip():
          submit_btn.config(state="normal")
     else:
          submit_btn.config(state="disabled")

# Create main window
root = tk.Tk()
root.title("Simple Magic 8 Ball")
root.geometry("500x320")
root.configure(bg="#f0f0f0")

# Create top input section
top_frame = tk.Frame(root, bg="#f0f0f0")
top_frame.pack(pady=20)

# Add question prompt label
tk.Label(top_frame, text="Ask a yes/no question:", font=("Arial", 14), bg="#f0f0f0").pack()

# Add question entry box
entry = tk.Entry(top_frame, width=50, font=("Arial", 13))
entry.pack(pady=8)
entry.bind("<KeyRelease>", on_type)  # Pressing Enter triggers the answer

# Create middle answer section
result_frame = tk.Frame(root, bg="#f0f0f0")
result_frame.pack(pady=15)

# Add answer display label
result= tk.Label(root, text="", font=("Arial", 13), fg="purple", wraplength=460, justify="center", bg="#f0f0f0" )
result.pack()

# Create bottom button section
button_frame=tk.Frame(root, bg="#f0f0f0")
button_frame.pack()

# Add Submit button
submit_btn= tk.Button(button_frame, text="Submit", font=("Arial", 12),command=submit_question, state="disabled")
submit_btn.pack(pady=10)

#Add Reset button
reset_btn = tk.Button(button_frame, text="Ask another Question", font=("Arial", 12), command=reset_question)
reset_btn.pack_forget()

# Starts the app loop
root.mainloop()