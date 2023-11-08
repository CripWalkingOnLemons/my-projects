import tkinter as tk

class ItemTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Item Tracker")
        
        self.item_list = []
        self.total_cost = 0.0
        
        self.name_label = tk.Label(root, text="Item Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()
        
        self.cost_label = tk.Label(root, text="Item Cost:")
        self.cost_label.pack()
        self.cost_entry = tk.Entry(root)
        self.cost_entry.pack()
        
        self.add_button = tk.Button(root, text="Add Item", command=self.add_item)
        self.add_button.pack()
        
        self.remove_button = tk.Button(root, text="Remove Item", command=self.remove_selected_item)
        self.remove_button.pack()
        
        self.item_listbox = tk.Listbox(root)
        self.item_listbox.pack()
        
        self.total_label = tk.Label(root, text="Total Cost:")
        self.total_label.pack()
        self.total_display = tk.Label(root, text="")
        self.total_display.pack()
        
    def add_item(self):
        item_name = self.name_entry.get()
        item_cost = self.cost_entry.get()
        
        if item_name and item_cost:
            try:
                item_cost = float(item_cost)
                self.item_list.append((item_name, item_cost))
                self.total_cost += item_cost
                self.item_listbox.insert(tk.END, f"{item_name} - ${item_cost:.2f}")
                self.name_entry.delete(0, tk.END)
                self.cost_entry.delete(0, tk.END)
                self.update_total_display()
            except ValueError:
                tk.messagebox.showerror("Invalid Cost", "Please enter a valid numeric cost.")
        else:
            tk.messagebox.showerror("Missing Data", "Please enter both item name and cost.")
    
    def remove_selected_item(self):
        selected_item = self.item_listbox.curselection()
        if selected_item:
            index = selected_item[0]
            item_name, item_cost = self.item_list[index]
            self.item_list.pop(index)
            self.total_cost -= item_cost
            self.item_listbox.delete(index)
            self.update_total_display()

    def update_total_display(self):
        self.total_display.config(text=f"Total Cost: ${self.total_cost:.2f}")
    
if __name__ == "__main__":
    root = tk.Tk()
    app = ItemTracker(root)
    root.mainloop()
