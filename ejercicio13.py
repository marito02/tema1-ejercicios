# 1.13 Realiza un programa que siga las siguientes instrucciones:
#    • Crea un conjunto llamado usuarios con los usuarios Marta, David, Elvira, Juan y Marcos
#    • Crea un conjunto llamado administradores con los administradores Juan y Marta.
#    • Borra al administrador Juan del conjunto de administradores.
#    • Añade a Marcos como un nuevo administrador, pero no lo borres del conjunto de usuarios.
#    • Muestra todos los usuarios por pantalla de forma dinámica, además debes indicar cada usuario es administrador o no.

usuarios = ["Marta","David","Elvira","Juan","Marcos"]
administradores = ["Marta","Juan"]
nuevos_administradores=[administradores.append("Marta")]
nuevos_administradores.append("Marcos")
for i in usuarios:
    print(f"{i} es un usuario")
    for j in nuevos_administradores:
        print(f"{j} es un adminitrador")

