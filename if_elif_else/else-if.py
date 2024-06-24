ingreso_mensual = 81000#10k 500, 12000k
gasto_mensual = 80000

#if anidados y else if (elif)

if ingreso_mensual > 10000:#10k
    if ingreso_mensual - gasto_mensual < 0:
        print("Estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Bien pa, estas bien")
    else: 
        print("bro!!, estas gastando mucho dinero, hay que ver sí te alcanza")
    
elif ingreso_mensual > 1000:
    print("Estas  bien en latinoamérica")
    
elif ingreso_mensual > 500:
    print("Estas bien en Colombia")
    
elif ingreso_mensual > 200:
    print("Estas bien en venezuela")
    
else:
    print("Sos pobre")