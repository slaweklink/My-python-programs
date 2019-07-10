# shows a window in which the user has to log in with the correct password

import PySimpleGUI as sg


text = sg.PopupGetText("Input your password", "Password check")

if text == "Robot1":
    sg.Popup("Result: " + text + " is correct")
else:
    sg.Popup("Wrong password!")
