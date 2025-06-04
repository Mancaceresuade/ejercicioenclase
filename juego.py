import tkinter as tk
import random
import time

snake = [[100, 100], [90, 100], [80, 100]]  # Lista de coordenadas
direction = [10, 0]  # Movimiento en X e Y

def mover_snake(snake, direction):
    cabeza = [snake[0][0] + direction[0], snake[0][1] + direction[1]]
    snake.insert(0, cabeza)
    snake.pop()  # Elimina cola

def crecer_snake(snake):
    cola = snake[-1]
    snake.append(cola[:])  # Duplica último segmento

def hay_colision(snake):
    cabeza = snake[0]
    return cabeza in snake[1:]  # Colisión consigo misma


def crear_ventana():
    ventana = tk.Tk()
    ventana.title("Snake en Python sin clases")
    canvas = tk.Canvas(ventana, width=400, height=400, bg="black")
    canvas.pack()
    return ventana, canvas

def dibujar(canvas, snake, comida):
    canvas.delete("all")
    for x, y in snake:
        canvas.create_rectangle(x, y, x+10, y+10, fill="green")
    canvas.create_oval(comida[0], comida[1], comida[0]+10, comida[1]+10, fill="red")


comida = [random.randint(0, 39)*10, random.randint(0, 39)*10]

def actualizar_juego():
    global comida
    mover_snake(snake, direction)
    if snake[0] == comida:
        crecer_snake(snake)
        comida = [random.randint(0, 39)*10, random.randint(0, 39)*10]
    if hay_colision(snake):
        print("¡Perdiste!")
        return
    dibujar(canvas, snake, comida)
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
