from tkinter import *

root = Tk()
root.geometry("1920x1080")


# TODO Have switch button that switches plus minus between category and adding a person
# TODO Make a have plus minus buttons go through a function that sends them to a function based on the "mode" via switch
# TODO have lists allow you to bring over names from list

def set_screen():
    global screenElem
    screenElem = [
        Button(root, text="+"),
        Button(root, text="-"),
        Button(root, text="switch")
    ]
    listElem = [
        [
            Entry(root), # TODO make it have a textvariable to say category
            Entry(root) # TODO make it have a textvariable to say placeholder name
        ]
    ]
    set_grid()


def set_grid():
    screenElem[0].grid(row=0, column=0)
    screenElem[1].grid(row=0, column=1)
    screenElem[2].grid(row=0, column=2)


root.title("Ranker")
set_screen()

root.mainloop()