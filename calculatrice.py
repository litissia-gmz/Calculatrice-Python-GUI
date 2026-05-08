import tkinter as tk
from tkinter import messagebox

def on_click(button_text):
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            messagebox.showerror("Erreur", "Calcul invalide")
            entry.delete(0, tk.END)
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

root = tk.Tk()
root.title("Calculatrice - L2 Info Angers")
root.geometry("300x400")

entry = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief="flat", justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    action = lambda x=button: on_click(x)
    tk.Button(root, text=button, width=5, height=2, font=("Arial", 14),
              command=action).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()