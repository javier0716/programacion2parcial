total_sueldo =float(input("Ingrese el total del sueldo: "))

if(total_sueldo > 7000):
    descuento = total_sueldo * 0.08
    print("Impuestos a pagar " + str (descuento))
else:
    print("No paga impuestos")
