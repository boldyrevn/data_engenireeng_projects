import tkinter as tk


def move_processing(event):
    global player
    global winner
    x = event.x
    y = event.y
    if 100 <= x < 600 and 100 <= y < 600 and winner == -1:
        i = (y - 100) // 50
        j = (x - 100) // 50
        if cells[i][j] == -1:
            cells[i][j] = player
            print_player_move(i, j)
            winner = check_winner(i, j)
            player = int(not player)
            print_game_condition()


def print_player_move(i, j):
    if player == 0:
        field.create_oval((105 + 50 * j, 105 + 50 * i), (145 + 50 * j, 145 + 50 * i), outline='red', width=2)
    else:
        field.create_line((105 + 50 * j, 105 + 50 * i), (145 + 50 * j, 145 + 50 * i), fill='blue', width=2)
        field.create_line((105 + 50 * j, 145 + 50 * i), (145 + 50 * j, 105 + 50 * i), fill='blue', width=2)


def print_game_condition():
    field.create_rectangle((10, 10), (690, 90), fill='white', outline='white')
    if winner == -1:
        if player == 0:
            field.create_text((350, 50), text='Current player is NOUGHT', font='Verdana 14')
        else:
            field.create_text((350, 50), text='Current player is CROSS', font='Verdana 14')
    else:
        if winner == 0:
            field.create_text((350, 50), text='NOUGHT is the Winner!', font='Verdana 14')
        else:
            field.create_text((350, 50), text='CROSS is the Winner!', font='Verdana 14')


def check_winner(cell_row, cell_column):
    # check the cell column
    cells_count = 0
    for row in range(10):
        if cells[row][cell_column] == player:
            cells_count += 1
        else:
            cells_count = 0
        if cells_count == 5:
            x1, y1 = 125 + 50 * cell_column, 125 + 50 * (row - 4)
            x2, y2 = x1, 125 + 50 * row
            field.create_line((x1, y1), (x2, y2), fill='black', width=2)
            return player
    # check the cell row
    cells_count = 0
    for column in range(10):
        if cells[cell_row][column] == player:
            cells_count += 1
        else:
            cells_count = 0
        if cells_count == 5:
            x1, y1 = 125 + 50 * (column - 4), 125 + 50 * cell_row
            x2, y2 = 125 + 50 * column, y1
            field.create_line((x1, y1), (x2, y2), fill='black', width=2)
            return player
    # check the cell main diagonal
    cells_count = 0
    offset = min(cell_row, cell_column)
    row, column = cell_row - offset, cell_column - offset
    while row < 10 and column < 10:
        if cells[row][column] == player:
            cells_count += 1
        else:
            cells_count = 0
        if cells_count == 5:
            x1, y1 = 125 + 50 * (column - 4), 125 + 50 * (row - 4)
            x2, y2 = 125 + 50 * column, 125 + 50 * row
            field.create_line((x1, y1), (x2, y2), fill='black', width=2)
            return player
        row += 1
        column += 1
    # check the cell side diagonal
    cells_count = 0
    offset = min(cell_row, (9 - cell_column))
    row, column = cell_row - offset, cell_column + offset
    while row < 10 and column > -1:
        if cells[row][column] == player:
            cells_count += 1
        else:
            cells_count = 0
        if cells_count == 5:
            x1, y1 = 125 + 50 * (column + 4), 125 + 50 * (row - 4)
            x2, y2 = 125 + 50 * column, 125 + 50 * row
            field.create_line((x1, y1), (x2, y2), fill='black', width=2)
            return player
        row += 1
        column -= 1
    return -1


def make_grid():
    for i in range(11):
        field.create_line((100, 100 + 50 * i), (600, 100 + 50 * i), fill='black')  # make horizontal lines
        field.create_line((100 + 50 * i, 100), (100 + 50 * i, 600), fill='black')  # make vertical lines


def restart(event):
    global winner
    global player
    global cells
    cells = [[-1] * 10 for i in range(10)]
    player = 0  # nought if 0; cross if 1
    winner = -1
    field.create_rectangle((0, 0), (700, 700), fill='white', outline='white')
    make_grid()
    print_game_condition()


cells = [[-1] * 10 for i in range(10)]
player = 0  # nought if 0; cross if 1
winner = -1

root = tk.Tk()

field = tk.Canvas(width=700, height=700, background='white')
reset_button = tk.Button(text='Restart', width=13, height=3, font='Verdana 16')

field.pack()
reset_button.pack(padx=10, pady=20)

make_grid()
print_game_condition()

field.bind('<Button-1>', move_processing)
reset_button.bind('<Button-1>', restart)

root.mainloop()
