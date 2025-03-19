'''

Una universidad ofrece un descuento a los estudiantes que dependen del  estrato y la
edad. 

- Si el estrato es 1 y su edad es menor a 18 el descuento será del 20% sobre el valor
de la matrícula. 

-Si el estrato es 1 y alumnos tiene 18 o mas años, el descuento será
del 10% 

si el estrato es 2 y la edad es 18 años o mas, el descuento sera del 5%.

'''
'''
precio_m = int(input("Ingrese el precio de la matricula: "))
edad = int(input("Ingrese su edad: "))
estrato = (input("Ingrese su estrato: "))

if edad < 18 and estrato == 1:
      precio_final = precio_m - (precio_m * 0.2)
      print("El precio final es: ", precio_final)

elif edad >= 18 and estrato == 1:
      precio_final = precio_m - (precio_m * 0.15)
      print("El precio final es: ", precio_final)

elif edad < 18 and estrato == 2:
      precio_final = precio_m - (precio_m * 0.1)
      print("El precio final es: ", precio_final)

elif edad >= 18 and estrato == 2:
      precio_final = precio_m - (precio_m * 0.05)
      print("El precio final es: ", precio_final)
else:
      print("No tiene descuento")'
'''


precio_m = int(input("Ingrese el precio de la matricula: "))
edad = int(input("Ingrese su edad: "))
estrato = input("Ingrese su estrato: ")


if edad < 18 and estrato == "1":
      descuento = precio_m * 0.20
      precio_final = precio_m - descuento
      print("El precio final es: ", precio_final)
elif edad >= 18 and estrato == "1":
      descuento = precio_m * 0.15
      precio_final = precio_m - descuento
      print("El precio final es: ", precio_final)
elif edad < 18 and estrato == "2":
      descuento = precio_m * 0.10
      precio_final = precio_m - descuento
      print("El precio final es: ", precio_final)
elif edad >= 18 and estrato == "2":
      descuento = precio_m * 0.05
      precio_final = precio_m - descuento
      print("El precio final es: ", precio_final)
else:
      print("No tiene descuento")