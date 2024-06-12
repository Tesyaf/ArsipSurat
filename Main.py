import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Basic Window")
root.geometry("300x200")

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20)

# Run the application
root.mainloop()
