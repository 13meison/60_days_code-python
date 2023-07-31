import PySimpleGUI as sg

lebel1 = sg.Text('simple1 :')
input1 = sg.InputText()

lebel2 = sg.Text('simple1 :')
input2 = sg.InputText()

button = sg.Button('add')

window = sg.Window('Simple app', layout=[[lebel1, input1],
                                         [lebel2, input2],
                                         [button]])

window.read()
window.close()
