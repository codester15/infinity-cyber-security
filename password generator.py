import string
import secrets
import tkinter as tk

def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

def generate_and_display_password():
    password_length = int(length_entry.get())
    password = generate_password(password_length)
    print("Generated password:", password)  # Print the generated password in command prompt
    password_display.config(state="normal")  # Allow modification of password_display widget
    password_display.delete(0, tk.END)
    password_display.insert(0, password)
    password_display.config(state="readonly")  # Disable modification of password_display widget

# Create the main application window
app = tk.Tk()
app.title("Password Generator")

# Create GUI elements
length_label = tk.Label(app, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)

length_entry = tk.Entry(app)
length_entry.grid(row=0, column=1, padx=10, pady=10)

generate_button = tk.Button(app, text="Generate Password", command=generate_and_display_password)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

password_display = tk.Entry(app, state="readonly")
password_display.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
app.mainloop()
