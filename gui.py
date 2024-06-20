import functions
import FreeSimpleGUI as sg

lable =sg.Text("Type in a To-Do")
input_box =sg.InputText(tooltip="Enter To-Do", key="todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")

window = sg.Window("My To-Do App",
                   layout=[[lable], [input_box, add_button], [edit_button, complete_button]],
                   font=('Helvetica', 20))
while True:
    event, values =window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] +"\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()
