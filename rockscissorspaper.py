import tkinter, random
MainWindow=tkinter.Tk()
def Init():
        global MainWindow, Button0, Button1, Button2, label1, label2
        Button0=tkinter.Button(MainWindow, text="Камень")
        Button1=tkinter.Button(MainWindow, text="Ножницы")
        Button2=tkinter.Button(MainWindow, text="Бумага")
        label1=tkinter.Label(MainWindow)
        label2=tkinter.Label(MainWindow)
        for obj in Button0, Button1, Button2, label1, label2:
            obj.pack()
        for obj in Button0, Button1, Button2:
            obj.bind("<Button-1>", Game)
def Game(event):
        label1['text']="Computer showed"
        label2['text']=""
        click=event.widget
        str1="YOU ARE LOSER..."
        str2="YOU ARE WINNER!"
        if click == Button0:
            myturn = 0
        elif click == Button1:
            myturn = 1
        else:
            myturn =2

        compturn = random.randint(0,2)

        if compturn == 0:
            label1['text'] += " камень"
        elif compturn == 1:
            label1['text'] += " ножницы"
        else:
            label1['text'] += " бумага"

        if myturn==compturn:
            label2['text']="Ничья"
        elif myturn > compturn and myturn != 2:
            label2['text']=str1
        elif compturn > myturn and compturn != 2:
            label2['text']=str2
        elif myturn == 2:
            label2['text']=str2
        else:
            label2['text']=str1



Init()
MainWindow.mainloop()
