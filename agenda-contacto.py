import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AGENDA DE CONTACTOS")
        self.root.geometry("650x480")
        self.root.resizable(False, False)

        # Persistencia de datos
        self.file_name = "agenda.json"
        self.agenda = self.load_data()

        self.setup_ui()
        self.populate_tree()

    def setup_ui(self):
        # Encabezados y entradas
        tk.Label(self.root, text="NOMBRE:", bg="#4A90E2", fg="white", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.input_name = tk.Entry(self.root, width=20, font=("Arial", 10))
        self.input_name.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.root, text="TELÉFONO:", bg="#4A90E2", fg="white", font=("Arial", 10, "bold")).grid(row=0, column=2, padx=10, pady=10, sticky="e")
        self.input_phone = tk.Entry(self.root, width=20, font=("Arial", 10))
        self.input_phone.grid(row=0, column=3, padx=10, pady=10)

        # Botones agrupados
        btn_frame = tk.Frame(self.root)
        btn_frame.grid(row=1, column=0, columnspan=4, pady=10)

        tk.Button(btn_frame, text="AÑADIR", bg="#4A90E2", fg="white", command=self.add).pack(side="left", padx=5)
        tk.Button(btn_frame, text="ACTUALIZAR", bg="#5BC0DE", fg="white", command=self.update_selected).pack(side="left", padx=5)
        tk.Button(btn_frame, text="BORRAR", bg="#D9534F", fg="white", command=self.remove_selected).pack(side="left", padx=5)
        tk.Button(btn_frame, text="LIMPIAR", bg="#777777", fg="white", command=self.clear_fields).pack(side="left", padx=5)

        # Treeview
        cols = ("id", "name", "phone")
        self.tree = ttk.Treeview(self.root, columns=cols, show="headings", height=18)
        
        self.tree.heading("id", text="ID")
        self.tree.heading("name", text="NOMBRE")
        self.tree.heading("phone", text="TELÉFONO")
        
        self.tree.column("id", width=50, anchor="center")
        self.tree.column("name", width=250, anchor="center")
        self.tree.column("phone", width=200, anchor="center")
        self.tree.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Evento para cargar datos al seleccionar
        self.tree.bind("<<TreeviewSelect>>", self.on_select)

        # Configurar redimensionado
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(2, weight=1)

    def load_data(self):
        if os.path.exists(self.file_name):
            try:
                with open(self.file_name, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return []
        return []

    def save_data(self):
        try:
            with open(self.file_name, "w", encoding="utf-8") as f:
                json.dump(self.agenda, f, indent=4, ensure_ascii=False)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar la agenda: {e}")

    def populate_tree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for contact in self.agenda:
            self.tree.insert("", "end", values=(contact["id"], contact["name"], contact["phone"]))

    def clear_fields(self):
        self.input_name.delete(0, tk.END)
        self.input_phone.delete(0, tk.END)

    def on_select(self, event):
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected, "values")
            self.input_name.delete(0, tk.END)
            self.input_name.insert(0, values[1])
            self.input_phone.delete(0, tk.END)
            self.input_phone.insert(0, values[2])

    def add(self):
        name = self.input_name.get().strip()
        phone = self.input_phone.get().strip()

        if not name or not phone:
            messagebox.showwarning("Campos Vacíos", "Debes rellenar todos los campos")
            return
        if not phone.isdigit() or len(phone) < 9:
            messagebox.showwarning("Teléfono Inválido", "El teléfono debe contener solo dígitos y tener al menos 9 caracteres.")
            return

        # Verificar duplicados
        for c in self.agenda:
            if c["name"].lower() == name.lower() and c["phone"] == phone:
                messagebox.showwarning("Duplicado", "Ya existe un contacto con ese nombre y teléfono")
                return

        max_id = max([c["id"] for c in self.agenda], default=0)
        new_id = max_id + 1

        self.agenda.append({"id": new_id, "name": name, "phone": phone})
        self.save_data()
        self.populate_tree()
        self.clear_fields()
        messagebox.showinfo("Éxito", "Contacto añadido correctamente")

    def remove_selected(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Selección", "Selecciona un contacto de la lista para eliminarlo.")
            return

        values = self.tree.item(selected, "values")
        if messagebox.askyesno("Confirmar", f"¿Estás seguro de eliminar a {values[1]}?"):
            target_id = int(values[0])
            self.agenda = [c for c in self.agenda if c["id"] != target_id]
            self.save_data()
            self.tree.delete(selected)
            self.clear_fields()
            messagebox.showinfo("Éxito", "Contacto eliminado correctamente.")

    def update_selected(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Selección", "Selecciona un contacto de la lista para actualizarlo.")
            return

        name = self.input_name.get().strip()
        phone = self.input_phone.get().strip()

        if not name or not phone:
            messagebox.showwarning("Campos Vacíos", "Debes rellenar todos los campos.")
            return

        target_id = int(self.tree.item(selected, "values")[0])
        for i, c in enumerate(self.agenda):
            if c["id"] == target_id:
                self.agenda[i]["name"] = name
                self.agenda[i]["phone"] = phone
                break

        self.save_data()
        self.populate_tree()
        self.clear_fields()
        messagebox.showinfo("Éxito", "Contacto actualizado correctamente.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()