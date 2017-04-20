import tkinter, random

MainWindow=tkinter.Tk()
def Tod0():
    global MainWindow, title, TruBut, DaBut, outback
    title=tkinter.Label(MainWindow, text="Truth or dare")
    TruBut=tkinter.Button(MainWindow, text="Truth")
    DaBut=tkinter.Button(MainWindow, text="Dare")
    outback=tkinter.Label(MainWindow)
    for i in title, TruBut, DaBut, outback:
        i.pack()
    for i in TruBut, DaBut:
        i.bind("<Button-1>", Tod)
def Tod (event):
    click=event.widget
    choice=random.randint(0,3)
    if click==TruBut:
        if choice == 0:
            outback['text']="What is your biggest fear?"
        elif choice == 1:
            outback['text']="If you knew the world was about to end, what would you do?"
        elif choice == 2:
            outback['text']="What was the worst day of your life?"
        else:
            outback['text']="If you were food what would you be and how would you like to be eaten?"
    else:
        if choice == 0:
            outback['text']="Do the worm."
        elif choice == 1:
            outback['text']="Eat half a stick of butter."
        elif choice == 2:
            outback['text']="Act like a pig."
        else:
            outback['text']="Blindfolded, spin around 15 times and walk down the street and back."
Tod0()

MainWindow.mainloop()