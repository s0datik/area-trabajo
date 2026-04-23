import tkinter as tk
from tkinter import messagebox
import json


def cargar_inventario():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def guardar_inventario(inventario):
    with open("data.json", "w") as file:
        json.dump(inventario, file, indent=4)

class SistemaVenta:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Venta con Inventario")
        self.inventario = cargar_inventario()

        #! Variables de control
        self.nombre_var = tk.StringVar()
        self.precio_var = tk.DoubleVar()
        self.cantidad_var = tk.IntVar()

        #! Crear widgets
        self.crear_widgets()

    def crear_widgets(self):
        #! Etiquetas y entradas
        tk.Label(self.root, text="Nombre del Producto:").grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.nombre_var).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Precio:").grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.precio_var).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Cantidad:").grid(row=2, column=0, padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.cantidad_var).grid(row=2, column=1, padx=10, pady=5)

        #! Botones
        tk.Button(self.root, text="Agregar Producto", command=self.agregar_producto).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Mostrar Inventario", command=self.mostrar_inventario).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Realizar Venta", command=self.realizar_venta).grid(row=5, column=0, columnspan=2, pady=10)

    def agregar_producto(self):
        nombre = self.nombre_var.get()
        precio = self.precio_var.get()
        cantidad = self.cantidad_var.get()

        if nombre and precio > 0 and cantidad > 0:
            if nombre in self.inventario:
                self.inventario[nombre]["cantidad"] += cantidad
            else:
                self.inventario[nombre] = {"precio": precio, "cantidad": cantidad}
            guardar_inventario(self.inventario)
            messagebox.showinfo("Éxito", f"Producto '{nombre}' agregado al inventario.")
        else:
            messagebox.showwarning("Error", "Por favor, ingrese datos válidos.")

    def mostrar_inventario(self):
        if not self.inventario:
            messagebox.showinfo("Inventario", "El inventario está vacío.")
            return

        inventario_texto = "\n".join(
            [f"{nombre}: Precio=${datos['precio']}, Cantidad={datos['cantidad']}" for nombre, datos in self.inventario.items()]
        )
        messagebox.showinfo("Inventario", inventario_texto)

    def realizar_venta(self):
        nombre = self.nombre_var.get()
        cantidad = self.cantidad_var.get()

        if nombre in self.inventario and cantidad > 0:
            if self.inventario[nombre]["cantidad"] >= cantidad:
                self.inventario[nombre]["cantidad"] -= cantidad
                guardar_inventario(self.inventario)
                messagebox.showinfo("Venta", f"Venta realizada: {cantidad} unidades de '{nombre}'.")
            else:
                messagebox.showwarning("Error", f"No hay suficiente stock de '{nombre}'.")
        else:
            messagebox.showwarning("Error", "Producto no encontrado o cantidad inválida.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaVenta(root)
    root.mainloop()