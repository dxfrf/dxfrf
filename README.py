import tkinter as tk


def center_window(root, width=500, height=500):
  """
  This function centers the root window on the screen.
  """
  screen_width = root.winfo_screenwidth()
  screen_height = root.winfo_screenheight()

  x = (screen_width - width) // 2
  y = (screen_height - height) // 2

  root.geometry(f'{width}x{height}+{x}+{y}')

def on_button_click_x():


  root.config(bg='gray')
  current_window: tk = tk.Tk()
  current_window.title("Initial Window")
  root.destroy()
  current_window.geometry('1000x800')

  button = Button(root, text="Click Me", command=button_clicked)

  button.pack()



  current_window.mainloop()


def on_button_click_y():
  current_window: tk = tk.Tk()
  current_window.title("Initial Window")
  root.destroy()
  current_window.geometry('1000x800')

  current_window.mainloop()

  # Center and resize the window
  center_window(root, 1000, 800)
  """
  This function prints a message when the Y button is clicked.
  """
  label_x = tk.Label(root, text="выбери за кого играеш!", font=("Helvetica", 40))

# Create the main windw
root = tk.Tk()

# Set the background color to gray
root.config(bg='gray')

# Center and resize the window
center_window(root, 1000, 800)

# Create the X button with a large font
button_x = tk.Button(root, text="X", command=on_button_click_x, width=10, height=2, font=("Helvetica", 120))

# Create a label with instructions
label_x = tk.Label(root, text="выбери за кого играеш!", font=("Helvetica", 40))

# Create the Y button with a large font
button_y = tk.Button(root, text="0", command=on_button_click_y, width=10, height=2, font=("Helvetica", 120))

# Add padding between buttons when placing them in the window
button_x.pack(pady=20)
button_y.pack(pady=20)
label_x.pack()

root.mainloop()

