#Se requiere un algoritmo que decida si un empleado tiene derecho al auxilio de transporte. Se
#conoce que todos los empleados que devengan un salario menor o igual a dos salarios mínimos
#legales tienen derecho a este rubro.

#Imprimir título
print("Programa para calcular el auxilio de transporte: ")

#Definir el valor del salario minimo legal
salary = 1400000

#Solicitar el salario del empleado
employee_salary = float(input("Ingresar el salario del empleado: "))

#Se utiliza condicionnates para comparar el salaro de los empleados
if employee_salary <= 2 * salary:
    print("Derecho auxilio de transporte.")
else:
    print("Sin derecho auxilio de transporte. ")
