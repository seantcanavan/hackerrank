import sys
# Enter your code here. Read input from STDIN. Print output to STDOUT

import fileinput

notepad = ""

undo = (
    "operation",
    "value"
)

undo_actions = []


def delegate_operation(operation, value):
    if operation == "1":
        append_operation(value)
    elif operation == "2":
        delete_operation(int(value) - 1)
    elif operation == "3":
        print_operation(int(value) - 1)
    elif operation == "4":
        undo_operation()
    else:
        print("invalid value for operation")
        sys.exit(-1)


def append_operation(value):
    global notepad, undo_actions
    notepad = notepad + value
    undo_actions.insert(0, ("append", value))


def delete_operation(index):
    global notepad, undo_actions
    notepad = notepad[:index]
    undo_actions.insert(0, ("delete", index))


def print_operation(index):
    print(notepad[index])


def undo_operation():
    global undo_actions
    undo_action = undo_actions.pop()
    if undo[0] == "append":
        delete_operation(undo[1])
    elif undo[0] == "delete":
        append_operation(undo[1])


# remove the first line of input as we don't need it
# also, if we get 10 million lines of operations
# we don't want to have to check a boolean on every line
first_line = True
for line in fileinput.input():
    first_line = True
    fileinput.close()
    break

for line in fileinput.input():
    command = line.rstrip().split(" ")
    if len(command) == 2:
        delegate_operation(command[0], command[1])
    else:
        delegate_operation(command[0], -1)

print(notepad)
