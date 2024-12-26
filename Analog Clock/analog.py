import tkinter as ui
import time
import math

window = ui.Tk()
window.title('Analog Clock')
window.geometry("900x900")


def update():
    hrs=int(time.strftime("%H"))
    mnt=int(time.strftime("%M"))
    scnd=int(time.strftime("%S"))

    sx=slen*math.sin(math.radians(scnd*6))+centerx
    sy=-1*slen*math.cos(math.radians(scnd*6))+centery
    canvas.coords(sechand,centerx,centery,sx,sy)

    mx=mlen*math.sin(math.radians(mnt*6))+centerx
    my=-1*mlen*math.cos(math.radians(mnt*6))+centery
    canvas.coords(mnthand,centerx,centery,mx,my)

    hx=hlen*math.sin(math.radians((hrs%12)*30))+centerx
    hy=-1*hlen*math.cos(math.radians((hrs%12)*30))+centery
    canvas.coords(hrshand,centerx,centery,hx,hy)
    print(hrs,mnt,scnd)

    window.after(1000,update)

canvas = ui.Canvas(window,width=900,height=900,bg="white")
canvas.pack(expand=True, fill=b"both")

bg=ui.PhotoImage(file="img/11.png")
canvas.create_image(450,410,image=bg)

centerx=450
centery=410
slen=280
mlen=215
hlen=180

sechand=canvas.create_line(400,450,480+slen,480+slen,width=3,fill='red')

mnthand=canvas.create_line(480,450,480+mlen,480+mlen,width=5,fill='black')

hrshand=canvas.create_line(480,450,480+hlen,480+hlen,width=10,fill='black')

update()

window.mainloop()