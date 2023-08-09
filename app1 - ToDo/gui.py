import functions
import PySimpleGUI as sg
import time
import os

"""
для создания exe файла надо все завернуть в env, установить в него все нужные библиотеки и pyinstaller
и ввести команду
pyinstaller --onefile --windowed --clean gui.py
"""
if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass
sg.theme('Black')
clock = sg.Text(key='clock')
label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip='Enter todo', key='todo')
add_button = sg.Button('Add')
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete', button_color='Yellow', key='Complete')
clear_button = sg.Button('Clear')
list_box = sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=(45, 10))
window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button],
                           [complete_button, clear_button]],
                   font=('Helvetcia', 20))

while True:
    event, values = window.read(timeout=10)
    window['clock'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))
    print(event)
    print(values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            if new_todo == '\n':
                pass
            else:
                todos.append(new_todo)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                print(todos)
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup('Please select an item first', font=('Helvetcia', 10))
        case 'todos':
            try:
                window['todo'].update(value=values['todos'][0])
            except IndexError:
                pass
        case 'Complete':
            if not values['todos']:
                continue
            else:
                todos = functions.get_todos()
                todo_to_complete = values['todos'][0]
                index = todos.index(todo_to_complete)
                todos.pop(index)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
        case 'Clear':
            functions.write_todos([])
            todos = functions.get_todos()
            window['todos'].update(values=todos)
window.close()
