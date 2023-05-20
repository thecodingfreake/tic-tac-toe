from tkinter import *
import random


def reset():
    button1.config(text='', bg='white',  command=lambda: click(button1))
    button2.config(text='', bg='white',  command=lambda: click(button2))
    button3.config(text='', bg='white',  command=lambda: click(button3))
    button4.config(text='', bg='white',  command=lambda: click(button4))
    button5.config(text='', bg='white',  command=lambda: click(button5))
    button6.config(text='', bg='white',  command=lambda: click(button6))
    button7.config(text='', bg='white',  command=lambda: click(button7))
    button8.config(text='', bg='white',  command=lambda: click(button8))
    button9.config(text='', bg='white',  command=lambda: click(button9))


def winner():
    if button1['text'] == button2['text'] == button3['text'] == 'x':
        print('you win')
    elif button1['text'] == button4['text'] == button7['text'] == 'x':
        print('you win')
    elif button1['text'] == button5['text'] == button9['text'] == 'x':
        print('you win')
    elif button2['text'] == button5['text'] == button8['text'] == 'x':
        print('you win')
    elif button3['text'] == button6['text'] == button9['text'] == 'x':
        print('you win')
    elif button3['text'] == button2['text'] == button7['text'] == 'x':
        print('you win')
    elif button1['text'] == button2['text'] == button3['text'] == 'x':
        print('you win')
    elif button3['text'] == button4['text'] == button5['text'] == 'x':
        print('you win')
    elif button6['text'] == button8['text'] == button9['text'] == 'x':
        print('you win')
    elif button1['text'] == button2['text'] == button3['text'] == 'o':
        print('you win')
    elif button1['text'] == button4['text'] == button7['text'] == 'o':
        print('you win')
    elif button1['text'] == button5['text'] == button9['text'] == 'o':
        print('you win')
    elif button2['text'] == button5['text'] == button8['text'] == 'o':
        print('you win')
    elif button3['text'] == button6['text'] == button9['text'] == 'o':
        print('you win')
    elif button3['text'] == button2['text'] == button7['text'] == 'o':
        print('you win')
    elif button1['text'] == button2['text'] == button3['text'] == 'o':
        print('you win')
    elif button3['text'] == button4['text'] == button5['text'] == 'o':
        print('you win')
    elif button6['text'] == button8['text'] == button9['text'] == 'o':
        print('you win')
    else:
        print('match tie')


def click(button):
    button = button
    player = 'x'
    computer = 'o'
    a = random.choice(choices)
    choices2 = [button1, button2, button3, button4, button5, button6, button7, button8, button9]
    choices2.remove(a)
    if a in result:
        choices2.remove(button)
        b = random.choice(choices2)
        b.config(text=computer, bg='yellow')
        button.config(text=player, bg='green')
        choices.remove(b)
        choices2.remove(b)
        result.add(b)
    elif a and button not in result:
        a.config(text=computer, bg='yellow')
        button.config(text=player, bg='green')
        choices.remove(a)
        choices.remove(button)
        result.add(a)
        result.add(button)


window = Tk()
button1 = Button(window, padx=40, pady=40, bg='white',  command=lambda: click(button1))
button2 = Button(window, padx=40, pady=40, bg='white', command=lambda: click(button2))
button3 = Button(window, padx=40, pady=40, command=lambda: click(button3), bg='white')
button4 = Button(window, padx=40, pady=40, command=lambda: click(button4), bg='white')
button5 = Button(window, padx=40, pady=40, command=lambda: click(button5), bg='white')
button6 = Button(window, padx=40, pady=40, command=lambda: click(button6), bg='white')
button7 = Button(window, padx=40, pady=40, command=lambda: click(button7), bg='white')
button8 = Button(window, padx=40, pady=40, command=lambda: click(button8), bg='white')
button9 = Button(window, padx=40, pady=40, command=lambda: click(button9), bg='white')
button10 = Button(window, padx=20, text='submit', pady=20, command=winner)
button11 = Button(window, padx=20, text='reset', pady=20, command=reset)
choices = [button1, button2, button3, button4, button5, button6, button7, button8, button9]
result = set()
button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)
button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)
button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
button10.grid(row=4, column=1)
button11.grid(row=4, column=2)
window.mainloop()
