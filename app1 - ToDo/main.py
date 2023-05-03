from functions import get_todos, write_todos

while True:
    user_action = input('Type add, show, edit, complete or exit: ').strip() + '\n'

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo)

        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()
        # print([item.strip('\n') for item in todos])
        for index, i in enumerate(todos):
            i = i.strip('\n')
            print(f'{index + 1}-{i}')
            # print(f'{index + 1}-{i}'[0:-1])

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            todos = get_todos()
            todos[number - 1] = input('Type new action todo: ') + '\n'
            write_todos(todos)
        except ValueError:
            print('Your command is not valid.')
            continue
        except IndexError:
            print("There is no item with that number ")
            continue

    elif user_action.startswith('clean'):
        todos = []
        write_todos(todos)
        print('Todos cleaned')

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)
            write_todos(todos)
            print(f'Todo {todo_to_remove} was removed from the list')
        except IndexError:
            print("There is no item with that number ")
            continue
        except ValueError:
            print("There is no item with that number ")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print('Unknown action')
        break
