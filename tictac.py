import tkinter as tk
from functools import partial


def center_window(window, width=500, height=500):
    """
    Функция центрирует окно на экране.
    """
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f'{width}x{height}+{x}+{y}')

def on_button_click_x():
    # Создаем новое окно
    current_window = tk.Toplevel(root)
    current_window.title("Окно X")

    # Устанавливаем цвет фона серым
    current_window.config(bg='gray')

    # Центрируем и изменяем размер окна
    center_window(current_window, 1000, 800)

    btn1_text = tk.StringVar()
    # Создаем кнопку в новом окне
    btn1 = tk.Button(current_window, textvariable=btn1_text, command=partial(on_button_clicked, btn1_text), pady=100,padx=150, anchor="nw")# justify="left")
    btn1.pack(anchor=tk.NW)
    button = tk.Button(current_window, command=on_button_clicked, pady=100, padx=150, anchor="nw")  # justify="left")
    button.pack(anchor=tk.NW)
    button = tk.Button(current_window, command=on_button_clicked, pady=100, padx=150, anchor="nw")  # justify="left")
    button.pack(anchor=tk.NW)
    button = tk.Button(current_window, command=on_button_clicked, pady=135, padx=150, anchor="nw")
    button.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    button = tk.Button(current_window, command=on_button_clicked, pady=135, padx=150, anchor="nw")
    button.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

def on_button_click_y():
    # Создаем новое окно
    current_window = tk.Toplevel(root)
    current_window.title("Окно Y")

    # Устанавливаем цвет фона серым
    current_window.config(bg='gray')

    # Центрируем и изменяем размер окна
    center_window(current_window, 1000, 800)

    # Создаем надпись в новом окне



def on_button_clicked(btn_text, *args):
    print(f"Кнопка нажата! {btn_text=}")
    btn_text.set('X')


# Создаем главное окно
root = tk.Tk()

# Устанавливаем цвет фона серым
# или не серым
root.config(bg='gray')

# Центрируем и изменяем размер главного окна
center_window(root, 1000, 800)

# Создаем кнопку X с крупным шрифтом
button_x = tk.Button(root, text="X", command=on_button_click_x, width=10, height=2, font=("Helvetica", 120))

# Создаем надпись с инструкциями
label_x = tk.Label(root, text="выбери за кого играеш!", font=("Helvetica", 40))

# Создаем кнопку Y с крупным шрифтом
button_y = tk.Button(root, text="Y", command=on_button_click_y, width=10, height=2, font=("Helvetica", 120))

# Устанавливаем отступ между виджетами при размещении их в окне
button_x.pack(pady=20)
button_y.pack(pady=20)
label_x.pack()

root.mainloop()
