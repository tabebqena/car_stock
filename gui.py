from tkinter import DISABLED, END, NORMAL, Listbox, Tk, Toplevel, ttk

from constants import stock_line_fields
from logics import validate_car_dict
from stock_manager import (add_car_to_stock, create_short_name,
                           delete_car_from_stock, get_all, load_stock_data,
                           update_stock_car)

top_window = None
listbox: Listbox = None
msg_view: ttk.Label = None
cars = []


def clean_msg_view():
    msg_view.config(text="")


def item_selected(event):
    clean_msg_view()
    activate_buttons()


def activate_buttons():
    button_names = [".buttons.show_btn", ".buttons.update_btn", ".buttons.delete_btn"]
    for name in button_names:
        top_window.nametowidget(name)["state"] = NORMAL


def deactivate_buttons():
    button_names = [".buttons.show_btn", ".buttons.update_btn", ".buttons.delete_btn"]
    for name in button_names:
        top_window.nametowidget(name)["state"] = DISABLED


def _get_selected_index():
    selected = listbox.curselection()
    if len(selected) == 0:
        msg_view.config(text="Please select car first !", foreground="red")
        return None
    return selected[0]


def update_car(car_index, data):
    clean_msg_view()
    result = update_stock_car(car_index, data)
    if result:
        msg_view.config(text="Car updated successfully!", foreground="green")
    fill_cars_list()
    

def add_car(index, data):
    clean_msg_view()
    result = add_car_to_stock(data)
    if result:
        msg_view.config(text="Car Added successfully!", foreground="green")
    fill_cars_list()
    

def show_update_window(car_index, short_name, car, fields, btn_txt, submit_func):
    win = Toplevel(top_window, name="update")
    win.geometry("500x460")
    ttk.Label(win, text=short_name).pack(fill="x")
    entries_frame = ttk.Frame(win, padding=10, name="entries")
        
    for i, field_name in enumerate(fields):
        field_label = ttk.Label(entries_frame, text=field_name, width=10)
        value_entry = ttk.Entry(entries_frame, name=field_name, width=30)
        value_entry.insert(0, str(car.get(field_name, "")))
        field_label.grid(column=0, row=i + 1)
        value_entry.grid(column=1, row=i + 1)
    entries_frame.pack(fill="x")
    state_label = ttk.Label(win)
    state_label.pack(fill="x")

    btn_frame = ttk.Frame(win, padding=10)
    btn_frame.pack(fill="x")

    def handle_button_press():
        data = {}
        for field_name in fields:
            entry_name = ".update.entries." + field_name
            entry = top_window.nametowidget(entry_name)
            data[field_name] = entry.get()
        error = validate_car_dict(data)
        if error:
            state_label.config(text=error, foreground="red")
            return
        submit_func(car_index, data)
        win.destroy()

    ttk.Button(btn_frame, text=btn_txt, command=handle_button_press).pack()

    win.mainloop()


def handle_add_btn():
    clean_msg_view()
    show_update_window(None, "Add New Car", {}, stock_line_fields, "Add", add_car)


def handle_update_btn():
    clean_msg_view()
    car_index = _get_selected_index()
    if car_index is not None:
        short_name = listbox.get(car_index)
        car = cars[car_index]
        show_update_window(
            car_index, short_name, car, stock_line_fields, "Update", update_car
        )




def handle_show_btn():
    clean_msg_view()
    car_index = _get_selected_index()
    if car_index is not None:
        short_name = listbox.get(car_index)
        car = cars[car_index]
        win = Toplevel(top_window)
        win.geometry("400x400")
        ttk.Label(win, text=short_name,  anchor="center", ).pack(fill="x")
        entries_frame = ttk.Frame(win, padding=10)
        
        for i, field_name in enumerate(stock_line_fields):
            field_label = ttk.Label(entries_frame, text=field_name, width=12)
            value_label = ttk.Label(entries_frame,   anchor="center", width=25, text=car.get(field_name))
            field_label.grid(column=0, row=i)
            value_label.grid(column=1, row=i)
        entries_frame.pack(fill="x")

        ttk.Button(win, text="Ok", command=win.destroy).pack()
        win.mainloop()
        
        

def handle_delete_btn():
    clean_msg_view()
    car_index = _get_selected_index()
    confirm_win = None

    def on_confirmed():
        confirm_win.destroy()
        delete_car_from_stock(car_index)
        fill_cars_list()

    if car_index is not None:
        confirm_win = Toplevel(top_window)
        confirm_win.geometry("200x250")
        ttk.Label(
            confirm_win, text="Ary you sure , You want to delete this car permanently?", wraplength=180
        ).pack()
        ttk.Button(confirm_win, text="Delete", command=on_confirmed).pack()
        confirm_win.mainloop()


def fill_cars_list():
    global cars
    cars = get_all()
    listbox.delete(0, END)  # clear listbox
    for i, car in enumerate(cars):
        short_name = create_short_name(car)
        listbox.insert(i, short_name)
    deactivate_buttons()


def build_window():
    global top_window, listbox, msg_view
    top_window = Tk()
    top_window.geometry("600x520")
    lbl = ttk.Label(top_window, text="Cars Shop")
    listbox = Listbox(top_window, width=580, justify="center", borderwidth=2)
    listbox.bind("<<ListboxSelect>>", item_selected)
    frame = ttk.Frame(top_window, padding=10, name="buttons")
    add_btn = ttk.Button(frame, text="Add", command=handle_add_btn, name="add_btn")
    show_btn = ttk.Button(
        frame,
        text="Show",
        command=handle_show_btn,
        state=DISABLED,
        name="show_btn",
    )
    update_btn = ttk.Button(
        frame,
        text="Update",
        command=handle_update_btn,
        state=DISABLED,
        name="update_btn",
    )
    delete_btn = ttk.Button(
        frame,
        text="Delete",
        command=handle_delete_btn,
        state=DISABLED,
        name="delete_btn",
    )

    lbl.pack()
    listbox.pack()
    #
    add_btn.grid(column=0, row=0)
    show_btn.grid(column=1, row=0)
    update_btn.grid(column=2, row=0)
    delete_btn.grid(column=3, row=0)
    frame.pack()

    msg_view = ttk.Label(
        top_window,
    )
    msg_view.pack()


if __name__ == "__main__":
    build_window()
    load_stock_data()
    fill_cars_list()
    top_window.mainloop()
