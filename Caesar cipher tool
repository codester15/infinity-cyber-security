import tkinter as tk

def encrypt_text():
    plaintext = plaintext_entry.get()
    shift = int(shift_entry.get())
    encrypted_text = ''.join(chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + shift) % 26 + 97) if char.islower() else char for char in plaintext)
    encrypted_text_var.set(encrypted_text)

def decrypt_text():
    ciphertext = ciphertext_entry.get()
    shift = int(shift_entry.get())
    decrypted_text = ''.join(chr((ord(char) - 65 - shift) % 26 + 65) if char.isupper() else chr((ord(char) - 97 - shift) % 26 + 97) if char.islower() else char for char in ciphertext)
    decrypted_text_var.set(decrypted_text)

# Create main window
root = tk.Tk()
root.title("Caesar Cipher Tool")

# Plaintext entry
plaintext_label = tk.Label(root, text="Plaintext:")
plaintext_label.grid(row=0, column=0, padx=5, pady=5)
plaintext_entry = tk.Entry(root)
plaintext_entry.grid(row=0, column=1, padx=5, pady=5)

# Shift entry
shift_label = tk.Label(root, text="Shift:")
shift_label.grid(row=1, column=0, padx=5, pady=5)
shift_entry = tk.Entry(root)
shift_entry.grid(row=1, column=1, padx=5, pady=5)

# Encrypt button
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.grid(row=2, column=0, padx=5, pady=5)

# Decrypt button
decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_text)
decrypt_button.grid(row=2, column=1, padx=5, pady=5)

# Encrypted text display
encrypted_text_var = tk.StringVar()
encrypted_text_label = tk.Label(root, text="Encrypted Text:")
encrypted_text_label.grid(row=3, column=0, padx=5, pady=5)
encrypted_text_entry = tk.Entry(root, textvariable=encrypted_text_var, state='readonly')
encrypted_text_entry.grid(row=3, column=1, padx=5, pady=5)

# Ciphertext entry
ciphertext_label = tk.Label(root, text="Ciphertext:")
ciphertext_label.grid(row=4, column=0, padx=5, pady=5)
ciphertext_entry = tk.Entry(root)
ciphertext_entry.grid(row=4, column=1, padx=5, pady=5)

# Decrypted text display
decrypted_text_var = tk.StringVar()
decrypted_text_label = tk.Label(root, text="Decrypted Text:")
decrypted_text_label.grid(row=5, column=0, padx=5, pady=5)
decrypted_text_entry = tk.Entry(root, textvariable=decrypted_text_var, state='readonly')
decrypted_text_entry.grid(row=5, column=1, padx=5, pady=5)

# Start the Tkinter event loop
root.mainloop()
