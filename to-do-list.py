import tkinter as tk

class TodoListGUI:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List")

        # Create task list box
        self.task_listbox = tk.Listbox(master, selectmode=tk.EXTENDED, height=15, width=50)
        self.task_listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create "Delete" button
        self.delete_button = tk.Button(master, text="Delete Selected", command=self.delete_task, height=2, width=15)
        self.delete_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Create "Clear All" button
        self.clear_button = tk.Button(master, text="Clear All", command=self.clear_tasks, height=2, width=15)
        self.clear_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Create task entry
        self.new_task_entry = tk.Entry(master, width=50)
        self.new_task_entry.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)
        self.new_task_entry.bind("<Return>", self.add_task)

        # Create "Add" button
        self.add_button = tk.Button(master, text="Add", command=self.add_task, height=2, width=10)
        self.add_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Bind right click with right control to select multiple tasks
        self.task_listbox.bind("<Button-3><Control-Button-1>", self.select_task)

        # Bind left click and drag to move task
        self.task_listbox.bind("<Button-1>", self.start_move_task)
        self.task_listbox.bind("<B1-Motion>", self.move_task)
        self.task_listbox.bind("<ButtonRelease-1>", self.end_move_task)

        # Initialize variables for moving tasks
        self.moving_task = False
        self.start_index = None

        # Create "Show" button
        self.show_button = tk.Button(master, text="Show", command=self.show_task, height=2, width=15)
        self.show_button.pack(side=tk.LEFT, padx=10, pady=10)


    def show_task(self):
      selection = self.task_listbox.curselection()
      if len(selection) > 0:
        task = self.task_listbox.get(selection[0])
        new_window = tk.Toplevel(self.master)
        new_window.title("Selected Task")
        task_label = tk.Label(new_window, text=task, justify="left", wraplength=300)
        task_label.pack(padx=10, pady=10)


    def add_task(self, event=None):
        task = self.new_task_entry.get()
        if task != "":
            self.task_listbox.insert(tk.END, task)
            self.new_task_entry.delete(0, tk.END)

    def delete_task(self):
        selection = self.task_listbox.curselection()
        if len(selection) > 0:
            for i in reversed(selection):
                self.task_listbox.delete(i)

    def clear_tasks(self):
        self.task_listbox.delete(0, tk.END)

    def select_task(self, event):
        self.task_listbox.selection_clear(0, tk.END)
        index = self.task_listbox.nearest(event.y)
        self.task_listbox.selection_set(index)

    def start_move_task(self, event):
        selection = self.task_listbox.curselection()
        if len(selection) == 1:
            self.moving_task = True
            self.start_index = selection[0]

    def move_task(self, event):
        if self.moving_task:
            index = self.task_listbox.nearest(event.y)
            if index != self.start_index:
                task = self.task_listbox.get(self.start_index)
                self.task_listbox.delete(self.start_index)
                if index > self.start_index:
                    index -= 1
                self.task_listbox.insert(index, task)
                self.task_listbox.selection_clear(0, tk.END)
                self.task_listbox.selection_set(index)
                self.start_index = index

   
    def end_move_task(self, event):
        self.moving_task = False

root = tk.Tk()

my_gui = TodoListGUI(root)
root.mainloop()
