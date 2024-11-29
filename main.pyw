import tkinter as tk
import requests
from tkinter import ttk, messagebox


def ziskej_kurz(from_currency, to_currency):
    api_key = '' # insert yours api on https://www.exchangerate-api.com/
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}"

    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            return data['conversion_rate']
        else:
            messagebox.showerror("Chyba", "Nepodařilo se načíst směnný kurz.")
            return None
    except Exception as e:
        messagebox.showerror("Chyba", f"Došlo k chybě: {e}")
        return None


def prevod(event=None): 
    from_currency = from_currency_combobox.get()
    to_currency = to_currency_combobox.get()
    amount = amount_entry.get()

    if not amount or not amount.replace('.', '', 1).isdigit():
        messagebox.showwarning("Upozornění", "Zadejte platnou částku.")
        return

    amount = float(amount)
    kurz = ziskej_kurz(from_currency, to_currency)

    if kurz is not None:
        converted_amount = amount * kurz
        result_label.config(text=f"{amount} {from_currency} je {converted_amount:.2f} {to_currency}")

root = tk.Tk()
root.title("Převod měn")
root.geometry("400x300")  
root.config(bg="#f0f0f0")  

input_frame = tk.Frame(root, bg="#f0f0f0", padx=10, pady=10)
input_frame.pack(pady=20)

from_currency_label = tk.Label(input_frame, text="Zadejte měnu, ze které chcete převést:", bg="#f0f0f0")
from_currency_label.grid(row=0, column=0, padx=5, pady=5)

from_currency_combobox = ttk.Combobox(input_frame, values=["EUR", "USD", "CZK"], width=10)
from_currency_combobox.set("EUR")  
from_currency_combobox.grid(row=0, column=1, padx=5, pady=5)

to_currency_label = tk.Label(input_frame, text="Zadejte měnu, do které chcete převést:", bg="#f0f0f0")
to_currency_label.grid(row=1, column=0, padx=5, pady=5)

to_currency_combobox = ttk.Combobox(input_frame, values=["CZK", "EUR", "USD"], width=10)
to_currency_combobox.set("CZK") 
to_currency_combobox.grid(row=1, column=1, padx=5, pady=5)

amount_label = tk.Label(input_frame, text="Zadejte částku:", bg="#f0f0f0")
amount_label.grid(row=2, column=0, padx=5, pady=5)

amount_entry = tk.Entry(input_frame, width=15)
amount_entry.grid(row=2, column=1, padx=5, pady=5)

convert_button = tk.Button(root, text="Převést", command=prevod, bg="#4CAF50", fg="white", font=("Arial", 12), padx=10, pady=5)
convert_button.pack(pady=10)

result_label = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 12))
result_label.pack(pady=10)

root.bind('<Return>', prevod)

amount_entry.focus()

root.mainloop()
