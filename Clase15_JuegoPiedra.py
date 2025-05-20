print("Hola! Vamos a Jugar piedra, papel o tijera")
print("¿Estás listo? ¡Pues vamos...!")

# Definir opciones válidas
opciones = ["Piedra", "Papel", "Tijera"]

# Ingresar nombres
usuario_1 = input("Ingrese su nombre (Jugador 1): ")
usuario_2 = input("Ingrese su nombre (Jugador 2): ")

# Ingresar jugadas
jugador_1 = input(f"{usuario_1}, escribe una opción (Piedra, Papel o Tijera): ").capitalize()
jugador_2 = input(f"{usuario_2}, escribe una opción (Piedra, Papel o Tijera): ").capitalize()

# Mostrar las elecciones
print(f"\n{usuario_1} eligió {jugador_1}")
print(f"{usuario_2} eligió {jugador_2}\n")

# Verificar si la entrada es válida
if jugador_1 not in opciones or jugador_2 not in opciones:
    print("❌ ¡Una de las opciones no es válida! Asegúrate de escribir Piedra, Papel o Tijera.")
else:
    # Empate
    if jugador_1 == jugador_2:
        print("😮 ¡Empate!")
    # Jugador 1 gana
    elif (jugador_1 == "Piedra" and jugador_2 == "Tijera") or \
         (jugador_1 == "Tijera" and jugador_2 == "Papel") or \
         (jugador_1 == "Papel" and jugador_2 == "Piedra"):
        print(f"🏆 El ganador es: {usuario_1}")
    else:
        print(f"🏆 El ganador es: {usuario_2}")
