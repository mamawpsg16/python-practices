import tkinter as tk

def main():
    root = Application()
    root.mainloop()

class Application(tk.Tk):
    def __init__(self):
        super().__init__()  # Initialize the base class (tk.Tk)
        self.title("Simple Shit")
        
        # Allow the frame to expand when the window is resized
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        frame = InputFrame(self)
        frame.grid(row=0, column=0, sticky="nsew")

class InputFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent) 

        # Configure the frame's layout to allow expansion
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)  # Button doesn't need to expand
        self.rowconfigure(1, weight=1)  # Make the listbox expandable vertically

        self.entry = tk.Entry(self)
        self.entry.grid(row=0, column=0, sticky="ew")
        self.entry.bind("<Return>", self.add_to_list)

        self.button_add = tk.Button(self, text="Add", command=self.add_to_list, width=10)
        self.button_add.grid(row=0, column=1, padx=(10, 0))

        self.button_clear = tk.Button(self, text="Clear", command=self.clear_list, width=10)
        self.button_clear.grid(row=0, column=2, padx=(5, 0))

        self.list_box = tk.Listbox(self)
        self.list_box.grid(row=1, column=0, columnspan=3, sticky="nsew", pady=10)

    def add_to_list(self, event=None):
        self.text = self.entry.get()
        if self.text:
            self.list_box.insert(tk.END, self.text)
            self.entry.delete(0, tk.END)

    def clear_list(self, event=None):
        if self.list_box.size():
            self.list_box.delete(0, tk.END)

if __name__ == "__main__":
    main()
