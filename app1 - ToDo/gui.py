import functions
import PySimpleGUI as sg


label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip='Enter todo')
add_button = sg.Button('Add')
checkbox = sg.Checkbox('123')
radio = sg.Radio('Yes', 2)

window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button, checkbox, radio]])
window.read()
window.close()



