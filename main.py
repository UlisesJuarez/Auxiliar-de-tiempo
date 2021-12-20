from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
AZULADO="#3E8E7E"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repeticiones=0
tiempo=None

# ---------------------------- TIMER RESET ------------------------------- # 
def resetear_contador():
    global repeticiones
    repeticiones=0
    ventana.after_cancel(tiempo)
    canvas.itemconfig(contadorTxt,text="00:00")
    timer.config(text="Temporizador")
    check.config(text="")



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def empezar_contador():
    global repeticiones
    repeticiones+=1
    segundos_trabajando=WORK_MIN*60
    descanso_corto_seg=SHORT_BREAK_MIN*60
    descanso_largo_seg=LONG_BREAK_MIN*60

    disminuir_contador(segundos_trabajando)
    if repeticiones%8==0:
        disminuir_contador(descanso_largo_seg)
        timer.config(text="Descanso",fg=RED)
    elif repeticiones%2==0:
        disminuir_contador(descanso_corto_seg)
        timer.config(text="Descanso",fg=PINK)
    else:
        disminuir_contador(segundos_trabajando)
        timer.config(text="Trabajando",fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def disminuir_contador(contador):
    minutos=math.floor(contador/60)
    segundos=contador%60
    if  segundos<10:
        segundos=f"0{segundos}"
    canvas.itemconfig(contadorTxt,text=f"{minutos}:{segundos}")
    if contador>0:
        global tiempo
        tiempo=ventana.after(1000,disminuir_contador,contador-1)
    else:
        empezar_contador()
        marca=""
        for i in range(math.floor(repeticiones/2)):
            marca+="✔"
        check.config(text=marca)



# ---------------------------- UI SETUP ------------------------------- #
ventana=Tk()
ventana.title("Tomate")
ventana.config(padx=100,pady=50,bg=YELLOW)


canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomate=PhotoImage(file="day 28 dynamic typing/tomato.png")
canvas.create_image(100,112,image=tomate)
contadorTxt=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


timer=Label(text="Timer",font=("Arial",35,"bold"))
timer.config(bg=YELLOW,fg=AZULADO)
timer.grid(column=1,row=0)

empezar=Button(text="Empezar",highlightthickness=0,command=empezar_contador)
empezar.config(bg=YELLOW,fg=AZULADO,font=(FONT_NAME,10,"bold"))
empezar.grid(column=0,row=2)

resetear=Button(text="Resetear",highlightthickness=0,command=resetear_contador)
resetear.config(bg=YELLOW,fg=AZULADO, font=(FONT_NAME,10,"bold"))
resetear.grid(column=2,row=2)

check=Label(bg=YELLOW,fg=AZULADO, font=(FONT_NAME,12,"bold"))
check.grid(column=1,row=3)

ventana.mainloop()  