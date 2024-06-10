from functions import get_todos, write_todos
import time

now =time.strftime("%b %d, %y %H:%M:%S")
print("It is "+now)

todos = get_todos()

while True:
    user_action = input('type add or show, edit, complete or exit ')
    user_action = user_action.strip()


    if user_action.startswith('add'):
        todo = user_action[4:]+'\n'

        todo = todo.title()
        todo = todo.strip(" ")
        todos.append(todo)

        write_todos(todos)

    elif user_action.startswith('show') or user_action.startswith('display'):

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f'{index+1}. {item}')

    elif user_action.startswith('edit'):
        try:
            choice = int(user_action[5:])
            choice = choice - 1

            todos = get_todos()

            new_todo = input('enter edit: ')
            todos[choice] = new_todo + "\n"

            write_todos(todos)

        except ValueError:
            print('your command is not valid.')
            print('edit should be followed by a number')

    elif user_action.startswith('complete'):
        try:
            choice = int(user_action[9:])

            todos = get_todos()

            choice = choice - 1
            todo_to_remove = todos[choice].strip('\n')
            todos.pop(choice)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)

        except IndexError:
            print('there is no item with that number')
        except:
            print('complete should be followed by a number')

    elif user_action.startswith('exit'):
        break
    else:
        print("incorrect command")

print("bye")
