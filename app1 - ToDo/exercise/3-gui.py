import PySimpleGUI as sg

label_feet = sg.Text('Enter feet :')
input_feet = sg.InputText(key='feet')

label_inches = sg.Text('Enter inches :')
input_inches = sg.InputText(key='inches')

button = sg.Button('Convert')
output = sg.Text(key='output')

button_exit = sg.Button('Exit')

window = sg.Window('Convertor app',
                   layout=[[label_feet, input_feet],
                           [label_inches, input_inches],
                           [button, output, button_exit]],
                   font=('Helvetcia', 20))


def converter(feet, inches):
    meters = ((int(feet) * 30.48) + (int(inches) * 2.54)) / 100
    return meters


while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Convert':
            try:
                meters = converter(values['feet'], values['inches'])
                meters = str(meters) + ' m'
                window['output'].update(value=meters)
            except:
                sg.popup("enter a value")
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break
        case _:
            break
window.close()
