# Import needed Python modules
import tkinter as tk
import random

# Create a list of fun answers
responses = [
    "Absolutely... if you're wearing socks.",
    "Nope. Not even in an alternate universe.",
    "Ask your cat. It knows.",
    "Yes, but only on Tuesdays.",
    "The moon says maybe.",
    "I consulted a squirrel. It's a yes.",
    "Your toaster disagrees.",
    "Try again after eating a banana.",
    "The vibes are off. Try later.",
    "Yes, but chaos will follow.",
    "No, unless you juggle flaming pineapples.",
    "I flipped a coin. It landed on its edge.",
    "The prophecy says... LOL no.",
    "Only if you dance first.",
    "Yes but tell no one.",
    "No, but it will be funny.",
    "Ask again when Mercury isn't retrograde.",
    "Sure, if you believe in unicorns.",
    "The answer is hidden in your laundry pile.",
    "I would say yes, but the ducks are watching.",
]

# Map keywords to emojis
emoji_map = {
    "yes": "😄",
    "no": "😬",
    "maybe": "🤔",
    "chaos": "🔥",
    "cat": "🐱",
    "squirrel": "🐿️",
    "moon": "🌙",
    "prophecy": "📜",
    "unicorns": "🦄",
    "ducks": "🦆"
}

# Track if the answer was shown
answered = False

# Store last three answers
history = []

# Handle Submit button click
def submit_question():
    global answered
    question = entry.get()
    if question.strip() and not answered:
        # Pick a random response
        response = random.choice(responses)
        result.config(text=response)
        answered = True

        show_emoji(response)

        update_history(response)

        fill_meter()

        submit_btn.pack_forget()
        reset_btn.pack(pady=10)

# Handle Reset button click
def reset_question():
    global answered
    entry.delete(0, tk.END)
    result.config(text="")
    emoji_label.config(text="")
    meter_var.set(0)
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

# Show emoji based on response
def show_emoji(response):
    for word, emoji in emoji_map.items():
        if word in response.lower():
            emoji_label.config(text=emoji)
            return
    emoji_label.config(text="🎱")

# Update response history display
def update_history(response):
    history.insert(0, response)
    if len(history) > 3:
        history.pop()
    history_text = "\n".join(history)
    history_label.config(text=history_text)

# Fill fortune meter randomly
def fill_meter():
    meter_var.set(random.randint(2, 100))

# Create main window
root = tk.Tk()
root.title("Wild Magic 8-Ball")
root.geometry("600x520")
root.configure(bg="#f0f0f0")

# Create top input section
top_frame = tk.Frame(root, bg="#f0f0f0")
top_frame.pack(pady=20)

# Add 8 ball icon
icon_label = tk.Label(top_frame, text="🎱", font=("Arial", 24), bg="#f0f0f0")
icon_label.pack()

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
result = tk.Label(result_frame, text="", font=("Arial", 13), fg="purple", wraplength=460, justify="center", bg="#f0f0f0")
result.pack()

# Add emoji reaction label
emoji_label = tk.Label(result_frame, text="", font=("Arial", 24), bg="#f0f0f0")
emoji_label.pack(pady=5)

# Add fortune meter
meter_var = tk.IntVar()
meter = tk.Scale(result_frame, from_=0, to=100, orient="horizontal", variable=meter_var, length=300, label="Fortune Meter", bg="#f0f0f0", state="disabled")
meter.pack(pady=5)

# Create bottom button section
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack()

# Add Submit button
submit_btn = tk.Button(button_frame, text="Submit", font=("Arial", 12), command=submit_question, state="disabled")
submit_btn.pack(pady=10)

# Add Reset button
reset_btn = tk.Button(button_frame, text="Ask another Question", font=("Arial", 12), command=reset_question)
reset_btn.pack_forget()

# Create history section
history_frame = tk.Frame(root, bg="#f0f0f0")
history_frame.pack(pady=10)

# Add history label
tk.Label(history_frame, text="History:", font=("Arial", 12), bg="#f0f0f0").pack()
history_label = tk.Label(history_frame, text="", font=("Arial", 11), bg="#f0f0f0", justify="left")
history_label.pack()

# Starts the app loop
root.mainloop()
