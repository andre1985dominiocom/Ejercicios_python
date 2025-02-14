#Se requiere un algoritmo que decida si un empleado tiene derecho al auxilio de transporte. Se
#conoce que todos los empleados que devengan un salario menor o igual a dos salarios mínimos
#legales tienen derecho a este rubro.

#Variables
salario=1400000

salario_empleados=int(input("Ingresar el salario del empleado : "))


if salario_empleados <= salario*2:
    print("Derecho auxilio de transporte : ")

else:
    print("Sin derecho auxilio de transporte : ")


