import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


conn = sqlite3.connect('/home/s0datik/Escritorio/Python/sql/Northwind.db')

# OBTENIENDO LOS 10 PRODUCTOS MAS RENTABLES
query = '''
    SELECT ProductName, SUM(Price * Quantity) as Revenue
    FROM OrderDetails od
    JOIN Products p ON p.ProductID = od.ProductID
    GROUP BY od.ProductID
    ORDER BY Revenue DESC
    LIMIT 10
'''

top_products = pd.read_sql_query(query,conn)

top_products.plot(x="ProductName",y="Revenue",kind="bar",figsize=(8,5),legend=False)

plt.title("10 Productos mas rentables")
plt.xlabel("Products")
plt.ylabel("Revenue")
plt.xticks(rotation=90)
plt.show()

#OBTENIENDO LOS 10 EMPLEADOS MAS EFECTIVOS

query2 = '''
    SELECT FirstName || ' ' || LastName as Employee, COUNT(*) as Total
    FROM Orders o
    JOIN Employees e 
    ON e.EmployeeID = o.EmployeeID
    GROUP BY o.EmployeeID
    ORDER BY Total DESC
    LIMIT 10
    '''

# Para despedir los 3 peores empleados
# ORDER BY Total ASC
# LIMIT 3


top_employees = pd.read_sql_query(query2,conn)

top_employees.plot(x="Employee",y="Total",kind="bar",figsize=(8,5),legend=False)

plt.title("10 Empleados mas efectivos") # LOS 3 EMPLEADOS QUE VENDIERON MENOS
plt.xlabel("Empleados")
plt.ylabel("Total vendidos")
plt.xticks(rotation=45)
plt.show()