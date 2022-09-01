import Table

table = Table.Table()
table.printTable()
control = input("Choose: ")
while control != 'q':
    table.controller(control)
    table.printTable()
    control = input("Choose: ")
