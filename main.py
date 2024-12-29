import requests
import tkinter as tk
from tkinter import ttk

def check_rate():
    listbox.delete(0, tk.END)
    rate1 = rate2_entry.get() + '.'
    rate2 = '1' + rate1_entry.get()
    rates = requests.get(f"https://{rate1}rate.sx/{rate2}")
    if rates.status_code == 200:
        for rate in rates:
            listbox.insert(tk.END, f'1 ' + rate2[1:] + ' = ' + str(rate)[2:-3] + ' ' + rate1[:-1])
    else:
        listbox.insert(tk.END, "Error")

window = tk.Tk()
window.title('Currency Check App')
window.geometry('300x300')
window.resizable(True, True)

frame = ttk.Frame(window, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

ttk.Label(frame, text='1st currency')
rate1_entry = ttk.Entry(frame, width=30)
rate1_entry.grid(row=0, column=1)
rate1_entry.insert(0, 'usd')


ttk.Label(frame, text='2nd currency')
rate2_entry = ttk.Entry(frame, width=30)
rate2_entry.grid(row=1, column=1)
rate2_entry.insert(0, 'eur')


ttk.Button(frame, text='Check rate', command=check_rate).grid(row=2, column=0, columnspan=2)

listbox = tk.Listbox(window, width=50, height=15)
listbox.grid(row=3, column=0, columnspan=2)

window.mainloop()