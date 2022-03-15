consumo_energia = {
 'Coca Codo Sinclair': {
 'Quito': { 'consumos':(400, 432, 400, 432, 420, 432, 460, 432, 400, 432, 300 , 213),'tarifa': 65},
 'Guayaquil': { 'consumos': (120, 55, 32, 120, 75, 32, 150, 55, 32, 120, 97, 32),'tarifa': 84},
 },
 'Sopladora': {
 'Guayaquil':{ 'consumos': (310, 220, 321, 310, 220, 321, 310, 220, 321, 310, 220, 321),'tarifa':55},
 'Quito': { 'consumos': (400, 432, 587, 400, 432, 587, 400, 432, 587, 400, 432, 587),'tarifa': 79},
 'Loja': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
 },
}
informacion = {
 'costa': ('Guayaquil', 'Manta'),
 'sierra': ('Quito', 'Ambato', 'Loja'),
 'oriente': ('Tena', 'Nueva Loja')
}
#Coca Codo Sinclair
consumo_Cocacodo_energyQ=consumo_energia["Coca Codo Sinclair"]["Quito"]["consumos"]
consumo_Cocacodo_energyG=consumo_energia["Coca Codo Sinclair"]["Guayaquil"]["consumos"]
tarifa_Cocacodo_energyQ=consumo_energia["Coca Codo Sinclair"]["Quito"]["tarifa"]
tarifa_Cocacodo_energyG=consumo_energia["Coca Codo Sinclair"]["Guayaquil"]["tarifa"]
#Sopladera
consumo_Sopladora_energyG=consumo_energia["Sopladora"]["Guayaquil"]["consumos"]
consumo_Sopladora_energyQ=consumo_energia["Sopladora"]["Quito"]["consumos"]
consumo_Sopladora_energyL=consumo_energia["Sopladora"]["Loja"]["consumos"]
tarifa_Sopladora_energyG=consumo_energia["Sopladora"]["Guayaquil"]["tarifa"]
tarifa_Sopladora_energyQ=consumo_energia["Sopladora"]["Quito"]["tarifa"]
tarifa_Sopladora_energyL=consumo_energia["Sopladora"]["Loja"]["tarifa"]

opcion=1

def menu():
    print("<1> Consultar el total de MWh consumidos en una planta eléctrica")
    print("<2> Consultar información de plantas en una ciudad")
    print("<3> Consultar información de dinero recaudado en una región")
    print("<4> Salir")

#Solicite al usuario el nombre de una planta y de una ciudad y presente el total de
#megavatios de consumos para dicha ciudad en dicha planta
def opcion_1():
    print("Plantas de energía:\n-Coca Codo Sinclair\n-Sopladora")
    plant1=str(input("Ingrese el nombre de la planta de energía:"))
    print("....................................................................................")
    if plant1== "Coca Codo Sinclair":
        print("Ciudades en las que se encuentra Coca Codo Sinclair:\n-Quito\n-Guayaquil")
        city1=str(input("Ingrese la ciudad a evaluar:"))
        if city1=="Quito":
            consumo_totalCocaQ=0
            for cquito in consumo_Cocacodo_energyQ:
                consumo_totalCocaQ += cquito
            print("El consumo total de Coca Codo Sinclair en Quito es",consumo_totalCocaQ,"MWh")   
        elif city1=="Guayaquil":
            consumo_totalCocaG=0
            for cguayaquil in consumo_Cocacodo_energyG:
                consumo_totalCocaG += cguayaquil
            print("El consumo total de Coca Codo Sinclair en Guayaquil es",consumo_totalCocaG,"MWh")
        else:
            print("Datos erróneos, intente nuevamente ingresando datos correctos")

    elif plant1=="Sopladora":
        print("Ciudades en las que se encuentra Sopladora:\n-Guayaquil\n-Quito\n-Loja")
        city1=str(input("Ingrese la ciudad a evaluar:"))
        if city1=="Guayaquil":
            consumo_totalSoplaG=0
            for sguayaquil in consumo_Sopladora_energyG:
                consumo_totalSoplaG += sguayaquil
            print("El consumo total de Sopladora en Guayaquil es",consumo_totalSoplaG,"MWh") 
        elif city1=="Quito":
            consumo_totalSoplaQ=0
            for squito in consumo_Sopladora_energyQ:
                consumo_totalSoplaQ += squito
            print("El consumo total de Sopladora en Quito es",consumo_totalSoplaQ,"MWh")
        elif city1=="Loja":
            consumo_totalSoplaL=0
            for sloja in consumo_Sopladora_energyL:
                consumo_totalSoplaL += sloja
            print("El consumo de Sopladora en Loja es",consumo_totalSoplaL,"MWh")
        else:
            print("Datos erróneos, intente nuevamente ingresando datos correctos")
    else:
        print("Datos erróneos, intente nuevamente ingresando datos correctos")

#Solicite al usuario el nombre de una ciudad y presente un nuevo diccionario cuyas claves
#son los nombres de las plantas generadoras y el valor es el total megavatios que cada
#planta le ha dado a ciudad. Si la planta no entrega energía a la ciudad entonces esa planta
#no debería aparecer en el nuevo diccionario
def opcion_2():
    plants_energy={
        "Guayaquil":("Coca Codo Sinclair","Sopladora"),
        "Quito":("Coca Codo Sinclair","Sopladora"),
        "Loja":("Sopladora")
    }
    
    plants_guayaquil=plants_energy["Guayaquil"]
    plants_quito=plants_energy["Quito"]
    plants_loja=plants_energy["Loja"]

    print("A continuación se muestran las ciudades:\n-Guayaquil\n-Quito\n-Loja")
    city2=str(input("Ingrese el nombre de la ciudad a evaluar:"))
    if city2=="Guayaquil":
        print("En esta ciudad funcionan las siguientes plantas:",plants_guayaquil)
        print("Coca Codo Sinclair ha entregado",sum(consumo_Cocacodo_energyG),"MWh de energía y Sopladora entregó",sum(consumo_Sopladora_energyG),"MWh de energía")
    elif city2=="Quito":
        print("En esta ciudad funcionan las siguientes plantas:",plants_quito)
        print("Coca Codo Sinclair ha entregado",sum(consumo_Cocacodo_energyQ),"MWh de energía y Sopladora entregó",sum(consumo_Sopladora_energyQ),"MWh de energía")
    elif city2=="Loja":
        print("En esta ciudad funcionan las siguientes plantas:",plants_loja)
        print("Sopladora ha entregado",sum(consumo_Sopladora_energyL),"MWh de energía")
    else:
        print("Datos erróneos, intente nuevamente ingresando datos correctos")

        
# Solicite el nombre de una región al usuario y presente cuento dinero ha recaudado la región Sierra

def opcion_3():
    print("Regiones:\n-Costa\n-Sierra\n-Oriente")
    region1=str(input("Ingrese el nombre de la Región a evalúar:"))
    if region1=="Costa":
        dinero_CostaCocaG=sum(consumo_Cocacodo_energyG)*tarifa_Cocacodo_energyG
        dinero_CostaSoplaG=sum(consumo_Sopladora_energyG)*tarifa_Sopladora_energyG
        print("En esta región se ha recaudado $",(dinero_CostaCocaG+dinero_CostaSoplaG))
    elif region1=="Sierra":
        dinero_SierraCocaQ=sum(consumo_Cocacodo_energyQ)*tarifa_Cocacodo_energyQ
        dinero_SierraSoplaQ=sum(consumo_Sopladora_energyQ)*tarifa_Sopladora_energyQ
        dinero_SierraSoplaL=sum(consumo_Sopladora_energyL)*tarifa_Sopladora_energyL
        print("En esta región se ha recaudado $",dinero_SierraCocaQ+dinero_SierraSoplaQ+dinero_SierraSoplaL)
    elif region1=="Oriente":
        print("No se han registrado plantas de energía en esta región aún")
    else:
        print("Datos erróneos, intente nuevamente ingresando datos correctos")
        

while opcion!=0:
    menu()
    opcion=int(input("Eliga una opción:"))
    print(".............................................................................")
    if opcion ==1:
        opcion_1()
        print("..........................................................................")
    elif opcion==2:
        opcion_2()
        print("..........................................................................")
    elif opcion==3:
        opcion_3()
        print("..........................................................................")
    elif opcion==4:
        print("Programa finalizado...")
        exit()
        
