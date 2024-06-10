import functions
import FreeSimpleGUI as sg

lable =sg.Text("Type in a To-Do")
input_box =sg.InputText(tooltip="Enter To-Do")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")

window = sg.Window("My To-Do App",layout=[[lable], [input_box, add_button], [edit_button, complete_button]])
window.read()
window.close()
