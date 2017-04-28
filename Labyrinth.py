import tkinter, random

MainWindow = tkinter.Tk()

def check ():
    canvas.itemconfig(circle, fill='PaleTurquoise1', outline='PaleTurquoise1')
    canvas.create_polygon([0, 0], [0, 550], 550, 550, 550, 0, fill='PaleTurquoise1')
    

def paint (event):
    j=0
    canvas.coords(circle, event.x-20, event.y-20, event.x+20, event.y+20)
    if event.y > -1 and event.y<41 and event.x<20 or event.x>80 and event.x<550 and event.y > -1 and event.y<41 or event.x<41 or event.y>510 or event.x>510 or (event.x>200 and event.x<260 and event.y>310 and event.y<460) or  (event.x>200 and event.x<465 and event.y>420 and event.y<480):
        check()
    elif event.x>75 and event.x<135 and event.y>75 and event.y<330 or event.x>75 and event.x<260 and event.y>290 and event.y<350:
        check()
    elif event.x>330 and event.x<390 and event.y>260 and event.y<420 or event.x>430 and event.x<530 and event.y>335 and event.y<395:
        check()
    elif event.x>205 and event.x<390 and event.y>200 and event.y<260 or event.x>205 and event.x<265 and event.y>0 and event.y<260:
        check()
    elif event.x>205 and event.x<460 and event.y>80 and event.y<140 or event.x>380 and event.x<460 and event.y>80 and event.y<220:
        check()
    else:
        canvas.itemconfig(circle, fill='SteelBlue2', outline='SteelBlue2')




canvas = tkinter.Canvas(MainWindow, background='PaleTurquoise1', width=550, height=550)
canvas.pack()

color = ['midnight blue', 'light coral', 'Pale violet red', 'Sea green', 'green yellow', 'midnight blue', 'medium orchid']
i = random.randint(0, 6)

circle = canvas.create_oval(25, 25, 65, 65, fill='SteelBlue2', outline='SteelBlue2')

line1 = canvas.create_rectangle([0, 0], [20, 550], fill=color[i], outline=color[i])
line2 = canvas.create_rectangle([360, 0], [100, 20], fill=color[i], outline=color[i])
line3 = canvas.create_rectangle([0, 550], [550, 530], fill=color[i], outline=color[i])
line4 = canvas.create_rectangle([550, 550], [530, 0], fill=color[i], outline=color[i])
line5 = canvas.create_rectangle([550, 0], [360, 20], fill=color[i], outline=color[i])

border1 = canvas.create_rectangle([95, 95], [115, 310], fill=color[i], outline=color[i])
border2 = canvas.create_rectangle([95, 310], [240, 330], fill=color[i], outline=color[i])
border3 = canvas.create_rectangle([220, 330], [240, 440], fill=color[i], outline=color[i])
border4 = canvas.create_rectangle([220, 440], [445, 460], fill=color[i], outline=color[i])
border5 = canvas.create_rectangle([350, 440], [370, 240], fill=color[i], outline=color[i])
border6 = canvas.create_rectangle([550, 375], [450, 355], fill=color[i], outline=color[i])
border7 = canvas.create_rectangle([370, 240], [245, 220], fill=color[i], outline=color[i])
border8 = canvas.create_rectangle([245, 240], [225, 0], fill=color[i], outline=color[i])
border9 = canvas.create_rectangle([225, 100], [440, 120], fill=color[i], outline=color[i])
border10 = canvas.create_rectangle([440, 100], [420, 200], fill=color[i], outline=color[i])


But = tkinter.Button(MainWindow, text="FINISH", bg=color[i], fg='white')
But.pack()
But.place(x=270, y=50)

canvas.bind('<Motion>', paint)





MainWindow.mainloop()
