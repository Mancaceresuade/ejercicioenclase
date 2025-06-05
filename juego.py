import tkinter as tk
import random
import time

snake = [[100, 100], [90, 100], [80, 100]]
direction = [10, 0]

score = 0
start_time = time.time()
juego_activo = True

def mover_snake(snake, direction):
    cabeza = [snake[0][0] + direction[0], snake[0][1] + direction[1]]
    cabeza[0] %= 400
    cabeza[1] %= 400
    snake.insert(0, cabeza)

def hay_colision(snake):
    cabeza = snake[0]
    return cabeza in snake[1:]

def crear_ventana():
    ventana = tk.Tk()
    ventana.title("Snake en Python sin clases")
    canvas = tk.Canvas(ventana, width=400, height=400, bg="black")
    canvas.pack()
    try:
        fondo_img = tk.PhotoImage(file=r"ejercicioenclase/platense.png")
        canvas.fondo_img = fondo_img
        print("Imagen de fondo cargada correctamente.")
    except Exception as e:
        print("Error cargando la imagen de fondo:", e)
        canvas.fondo_img = None
    return ventana, canvas

comida = [random.randint(0, 39)*10, random.randint(0, 39)*10]

def dibujar(canvas, snake, comida, score, tiempo, mostrar_game_over=False):
    canvas.delete("all")
    if canvas.fondo_img is not None:
        canvas.create_image(200, 200, anchor="center", image=canvas.fondo_img)
    for x, y in snake:
        canvas.create_rectangle(x, y, x+10, y+10, fill="green")
    canvas.create_oval(comida[0], comida[1], comida[0]+10, comida[1]+10, fill="red")
    
    # Puntaje y tiempo en negro
    canvas.create_text(50, 10, fill="black", font=("Arial", 10), text=f"Score: {score}")
    canvas.create_text(350, 10, fill="black", font=("Arial", 10), text=f"Time: {tiempo}s")
    
    if mostrar_game_over:
        canvas.create_text(200, 200, fill="black", font=("Arial", 20, "bold"), text="¡Perdiste!")

def actualizar_juego():
    global comida, score, juego_activo
    if not juego_activo:
        return

    mover_snake(snake, direction)

    if snake[0] == comida:
        score += 1
        comida = [random.randint(0, 39)*10, random.randint(0, 39)*10]
    else:
        snake.pop()

    if hay_colision(snake):
        juego_activo = False
        print(f"¡Perdiste! Puntaje final: {score}")
        tiempo = int(time.time() - start_time)
        dibujar(canvas, snake, comida, score, tiempo, mostrar_game_over=True)
        return

    tiempo = int(time.time() - start_time)
    dibujar(canvas, snake, comida, score, tiempo)
    ventana.after(100, actualizar_juego)

def cambiar_direccion(event):
    global direction
    if event.keysym == "Up" and direction != [0, 10]:
        direction = [0, -10]
    elif event.keysym == "Down" and direction != [0, -10]:
        direction = [0, 10]
    elif event.keysym == "Left" and direction != [10, 0]:
        direction = [-10, 0]
    elif event.keysym == "Right" and direction != [-10, 0]:
        direction = [10, 0]

ventana, canvas = crear_ventana()
ventana.bind("<Key>", cambiar_direccion)
ventana.after(100, actualizar_juego)
ventana.mainloop()
