from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Variável que seta que o programa está rodando
is_running = False

# Variável que guarda as repetições do pomodoro
reps = 0

# Variável para controle do tempo
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    # Cancela o timer
    window.after_cancel(timer)

    # Habilita o botão start
    start_button.config(state=NORMAL)

    # Reseta o texto do tomate
    canvas.itemconfig(timer_text, text="00:00")

    # Reseta o texto acima do tomate
    title_label.config(text="TIMER")

    # Reseta as marcações
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():

    # Desabilita o botão Start
    start_button.config(state=DISABLED)

    # Variável global que registra as repetições do pomodoro
    global reps

    reps += 1

    # Variáveis de tempo do pomodoro
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 9:
        reset_timer()
    elif reps % 8 == 0:
        # Inicia a contagem regressiva e altera o texto
        count_down(long_break_sec)
        title_label.config(text="BREAK", fg=GREEN)
    elif reps %2 == 0:
        # Inicia a contagem regressiva e altera o texto
        count_down(short_break_sec)
        title_label.config(text="BREAK", fg=PINK)
    else:
        # Inicia a contagem regressiva e altera o texto
        count_down(work_sec)
        title_label.config(text="WORK", fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    # Ajustes da contagem de tempo
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec == 0:
        count_sec = "00"

    if int(count_sec) < 10 and int(count_sec) > 0:
        count_sec = f"0{count_sec}"

    # Muda o texto em frente à imagem
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
   
    # Se não estiver em zero, a cada segundo diminui 1
    if count > 0:
        # Permite acessar a variável global
        global timer
        # Variável que possui a quantidade de segundos
        timer = window.after(1, count_down, count-1)
    else:
        start_timer()

        marks = ""
        work_sessions = math.floor(reps/2)

        for _ in range(work_sessions):
            marks += "✔️"
            check_marks.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

# Cria a janela
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Coloca a imagem no fundo da janela
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=r"Dia-28-Tkinter-DynamicTyping-Pomodoro\tomato.png")
canvas.create_image(100, 112, image=tomato_img)
# Cria o timer
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Cria o label de cima
title_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

# Cria os botões
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Cria os checkmarks
check_marks = Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

# Impede que a janela seja fechada
window.mainloop()