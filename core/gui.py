import tkinter as tk
from tkinter import ttk, messagebox
from client import send_data


def submit_callback():
    """
    Callback function to handle the submit button click event.
    """
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    age = entry_age.get()
    gender = combobox_gender.get().lower()
    print(gender)

    data = {"first_name": first_name, "last_name": last_name, "age": age, "gender": gender}

    response = send_data(data)
    messagebox.showinfo("Response", response)


root = tk.Tk()
root.title("Client")

label_first_name = tk.Label(root, text="First Name:")
label_first_name.grid(row=0, column=0)
entry_first_name = tk.Entry(root)
entry_first_name.grid(row=0, column=1)

label_last_name = tk.Label(root, text="Last Name:")
label_last_name.grid(row=1, column=0)
entry_last_name = tk.Entry(root)
entry_last_name.grid(row=1, column=1)

label_age = tk.Label(root, text="Age:")
label_age.grid(row=2, column=0)
entry_age = tk.Entry(root)
entry_age.grid(row=2, column=1)

label_gender = tk.Label(root, text="Gender:")
label_gender.grid(row=3, column=0)
gender_values = ("Male", "Female")
combobox_gender = ttk.Combobox(root, values=gender_values, state="readonly")
combobox_gender.grid(row=3, column=1)

submit_button = tk.Button(root, text="Submit", command=submit_callback)
submit_button.grid(row=4, columnspan=2)

root.mainloop()
