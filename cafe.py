import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

root = tk.Tk()
root.title("Cafe")

# Променлива за сметката
total = 0
items = []

bill_generated = False

# Функция за добавяне на стока към сметката
def add_item(item_name, item_price):
    global total, bill_generated
    total += item_price
    items.append((item_name, item_price))
    update_bill()
    bill_generated = False

# Функция за изчистване на цялата сметка
def clear_bill():
    global total, bill_generated
    total = 0
    items.clear()
    update_bill()
    bill_generated = False

# Функция за генериране на сметка
def generate_bill():
    global bill_generated
    if items:  # Проверяваме дали има добавени продукти
        bill_text.config(state="normal")
        bill_text.insert(tk.END, "--------------------------\n")
        bill_text.insert(tk.END, f"Total: {total:.2f} leva\n")
        bill_text.config(state="disabled")
        bill_generated = True
    else:
        messagebox.showinfo("Информация", "Добавете продукти към сметката първо.")

# Функция за обновяване на сметката
def update_bill():
    bill_text.config(state="normal")
    bill_text.delete(1.0, tk.END)
    for item_name, item_price in items:
        bill_text.insert(tk.END, f"{item_name}: {item_price:.2f} leva\n")
    total_label.config(text=f"Total: {total:.2f} leva")
    bill_text.config(state="disabled")


style = ttk.Style()
style.configure('TButton', padding=(10, 5), font=('Helvetica', 12))
style.configure('TLabel', font=('Helvetica', 12))


buttons_frame = ttk.Frame(root)
buttons_frame.pack()

coffee_button = ttk.Button(buttons_frame, text="Espresso (4.50 leva)", command=lambda: add_item("Espresso", 4.50))
americano_button = ttk.Button(buttons_frame, text="Americano (4.50 leva)", command=lambda: add_item("Americano", 4.50))
mocaccino_button = ttk.Button(buttons_frame, text="Mocaccino (4.50 leva)", command=lambda: add_item("Mocaccino", 4.50))
tea_button = ttk.Button(buttons_frame, text="Tea (2.00 leva)", command=lambda: add_item("Tea", 2.00))
pancakes_button = ttk.Button(buttons_frame, text="Pancakes (6.00 leva)", command=lambda: add_item("Pancakes", 6.00))
eggs_button = ttk.Button(buttons_frame, text="Eggs Benedict (8.50 leva)", command=lambda: add_item("Eggs Benedict", 8.50))
cheesecake_button = ttk.Button(buttons_frame, text="Cheesecake (7.80 leva)", command=lambda: add_item("Cheesecake", 7.80))
strawberry_button = ttk.Button(buttons_frame, text="Strawberry Mousse (8.50 leva)", command=lambda: add_item("Strawberry Mousse", 8.50))

clear_button = ttk.Button(root, text="Clear Bill", command=clear_bill)
generate_button = ttk.Button(root, text="Generate Bill", command=generate_bill)


# Позициониране на бутоните в рамката
coffee_button.grid(row=0, column=0, padx=5, pady=5)
americano_button.grid(row=0, column=1, padx=5, pady=5)
mocaccino_button.grid(row=0, column=2, padx=5, pady=5)
tea_button.grid(row=0, column=3, padx=5, pady=5)
pancakes_button.grid(row=1, column=0, padx=5, pady=5)
eggs_button.grid(row=1, column=1, padx=5, pady=5)
cheesecake_button.grid(row=1, column=2, padx=5, pady=5)
strawberry_button.grid(row=1, column=3, padx=5, pady=5)

# Позициониране на бутоните извън рамката
clear_button.pack()
generate_button.pack()

# Създаване на текстово поле за сметка
bill_text = tk.Text(root, height=10, width=30, state="disabled")
bill_text.pack()

# Текстово поле за общата сума
total_label = ttk.Label(root, text="Total: 0.00 leva")
total_label.pack()

root.mainloop()
