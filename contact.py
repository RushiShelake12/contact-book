import tkinter as tk
from tkinter import messagebox

class ContactApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Management System")

        self.contacts = []

        # Labels
        tk.Label(self.master, text="Name:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self.master, text="Phone:").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(self.master, text="Email:").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(self.master, text="Address:").grid(row=3, column=0, padx=10, pady=5)

        # Entry Widgets
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        self.phone_entry = tk.Entry(self.master)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)
        self.email_entry = tk.Entry(self.master)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)
        self.address_entry = tk.Entry(self.master)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        # Buttons
        tk.Button(self.master, text="Add Contact", command=self.add_contact).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.master, text="View Contacts", command=self.view_contacts).grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(self.master, text="Search Contact", command=self.search_contact).grid(row=6, column=0, columnspan=2, pady=10)
        tk.Button(self.master, text="Update Contact", command=self.update_contact).grid(row=7, column=0, columnspan=2, pady=10)
        tk.Button(self.master, text="Delete Contact", command=self.delete_contact).grid(row=8, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Name and Phone are required fields.")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts found.")
        else:
            contact_list = "\n".join([f"{contact['Name']}: {contact['Phone']}" for contact in self.contacts])
            messagebox.showinfo("Contact List", contact_list)

    def search_contact(self):
        search_term = simpledialog.askstring("Search Contact", "Enter name or phone number:")
        if search_term:
            found_contacts = [contact for contact in self.contacts if search_term.lower() in contact['Name'].lower() or search_term in contact['Phone']]
            if found_contacts:
                contact_list = "\n".join([f"{contact['Name']}: {contact['Phone']}" for contact in found_contacts])
                messagebox.showinfo("Search Results", contact_list)
            else:
                messagebox.showinfo("Info", f"No contacts found for '{search_term}'.")

    def update_contact(self):
        # You can implement contact updating logic here based on your specific requirements.
        messagebox.showinfo("Info", "Update Contact functionality not implemented yet.")

    def delete_contact(self):
        # You can implement contact deletion logic here based on your specific requirements.
        messagebox.showinfo("Info", "Delete Contact functionality not implemented yet.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactApp(root)
    root.mainloop()