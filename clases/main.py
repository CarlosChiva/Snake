from Table import *

table = Table()
table.printTable()
control = input("Choose: ")
while not table.game_Over:
    table.controller(control)
    if table.game_Over:
        break
    table.printTable()
    control = input("Choose: ")
