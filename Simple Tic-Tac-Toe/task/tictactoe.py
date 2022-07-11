# write your code here
Enter_cells = '         '

def display(field):
    Enter_cells = field
    string = "---------" + '\n' + "|" + " " + Enter_cells[0] + " " + Enter_cells[1] + " " + Enter_cells[2] + " " + "|" + '\n' + "|" + " " + Enter_cells[3] + " " + Enter_cells[4] + " " + Enter_cells[5] + " " + "|" + '\n' + "|" + " " + Enter_cells[6] + " " + Enter_cells[7] + " " + Enter_cells[8] + " " + "|" + '\n' + "---------"
    return string

def horzontial(Enter_cells):
    first_line = Enter_cells[:3]
    if first_line == 'OOO':
        return 'O wins'
    elif first_line == 'XXX':
        return 'X wins'
    else:
        return None

def second_horzontial(Enter_cells):
    first_line = Enter_cells[3:6]
    if first_line == 'OOO':
        return 'O wins'
    elif first_line == 'XXX':
        return 'X wins'
    else:
        return None

def third_horzontial(Enter_cells):
    first_line = Enter_cells[6:]
    if first_line == 'OOO':
        return 'O wins'
    elif first_line == 'XXX':
        return 'X wins'
    else:
        return None

def result_from_horizontaal(field):
    aantal = 0
    if horzontial(field) != None:
        aantal += 1
    if second_horzontial(field) != None:
        aantal += 1
    if third_horzontial(field) != None:
        aantal += 1

    if aantal >= 2:
        return "Both"
    else:
        return horzontial(field) or second_horzontial(field) or third_horzontial(field)


def vertical(field):
    first_line = field[0::3]

    if first_line == 'OOO':
        return 'O wins'
    elif first_line == 'XXX':
        return 'X wins'
    else:
        return None

def second_vertical(field):
    second_line = field[1::3]

    if second_line == 'OOO':
        return 'O wins'
    elif second_line == 'XXX':
        return 'X wins'
    else:
        return None

def third_vertical(field):
    third_line = field[2::3]
    if third_line == 'OOO':
        return 'O wins'
    elif third_line == 'XXX':
        return 'X wins'
    else:
        return None

def result_from_vertical(field):
    aantal = 0
    if vertical(field) != None:
        aantal += 1
    if second_vertical(field) != None:
        aantal += 1
    if third_vertical(field) != None:
        aantal += 1

    if aantal >= 2:
        return "Both"
    elif vertical(field) or second_vertical(field) or third_vertical(field):
        return vertical(field) or second_vertical(field) or third_vertical(field)


def schuin(field):
    if field[0:9:4] == 'OOO' and field[2:7:2] == 'OOO' or field[0:9:4] == 'XXX' and field[2:7:2] == 'XXX':
        return "Both"

    if field[0:9:4] == 'OOO' or field[2:7:2] == 'OOO':
        return 'O wins'

    if field[0:9:4] == 'XXX' or field[2:7:2] == 'XXX':
        return 'X wins'


def Draw(field):
    if '_' not in field and result_from_vertical(field) == None and result_from_horizontaal(field) == None and schuin(field) == None:
        return "Draw"
    if hulpmiddel_1(field) != None:
        return hulpmiddel_1(field)



def hulpmiddel_1(field):
    aantal = 0
    if result_from_horizontaal(field) == 'Both':
        aantal += 1

    if result_from_vertical(field) == 'Both':
        aantal += 1

    if schuin == 'Both':
        aantal += 1

    if aantal >= 1:
        return "Impossible"

def Impossible(field):
    if hulpmiddel_1(field) != None:
        return hulpmiddel_1(field)
    elif result_from_vertical(field) != None or result_from_horizontaal(field) != None or schuin(field) != None:
        return result_from_vertical(field) or result_from_horizontaal(field) or schuin(field)

    x = field.count('X')
    o = field.count('O')
    if x - o == 1 or x == o or o - x == 1:
        return result_from_vertical(field) or result_from_horizontaal(field)
    elif x - o != 1 or x != o or o - x != 1:
        return 'Impossible'


def Game_not_finsed(field):
    if '_' in field and result_from_vertical(field) == None and  result_from_horizontaal(field) == None and schuin(field) == None:
        return "Game not finished"


def result_of_tictactoe(field):
    if result_from_vertical(field) != None:
        return result_from_vertical(field)

    elif result_from_horizontaal(field) != None:
        return result_from_horizontaal(field)

    elif schuin(Enter_cells) != None:
        return schuin(Enter_cells)




def place(positie):
    l = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
    ]
    play_board = Enter_cells
    place = l[int(positie[0])- 1][int(positie[-1])- 1]
    if play_board[place] != " ":
        return "This cell is occupied! Choose another one!"

def texing(positie, aantal):
    l = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
    ]
    place = l[int(positie[0])- 1][int(positie[-1])- 1]
    global Enter_cells
    if aantal % 2 == 0:
        string = Enter_cells[:place] + "O" + Enter_cells[place+1:]
    else:
        string = Enter_cells[:place] + "X" + Enter_cells[place+1:]
    Enter_cells = string
    return display(Enter_cells)


def ga_naar_de_slager():
    while True:
        field = input()
        if not field[0].isdigit() and not field[-1].isdigit() or not field[0].isdigit() or not field[-1].isdigit():
            print("> " + field)
            print("You should enter numbers!")
        elif not (1 <= int(field[0]) <= 3):
            print("> " + field)
            print("Coordinates should be from 1 to 3!")
        elif not (1 <= int(field[-1]) <= 3):
            print("> " + field)
            print("Coordinates should be from 1 to 3!")
        elif place(field) != None:
            print("> " + field)
            print(place(field))
        else:
            return field

def result():
    print(display('         '))
    aantal = 1
    while ' ' in Enter_cells:
        print(texing(ga_naar_de_slager(), aantal))
        aantal += 1
        if result_of_tictactoe(Enter_cells) != None:
            return result_of_tictactoe(Enter_cells)
    a=1
    return Draw(Enter_cells)
print(result())

def test():
    assert schuin('X___X___X') == 'X wins'
    assert schuin('__X_X_X__') == 'X wins'

    assert schuin('O___O___O') == 'O wins'
    assert schuin('__O_O_O__') == 'O wins'

    assert schuin('_'*9) is None


    assert result_from_horizontaal('OOO______') == 'O wins'
    assert result_from_horizontaal('______OOO') == 'O wins'

    assert result_from_horizontaal('XXX______') == 'X wins'
    assert result_from_horizontaal('______XXX') == 'X wins'


    assert result_from_vertical('X__X__X__') == "X wins"
    assert result_from_vertical('_X__X__X_') == "X wins"
    assert result_from_vertical('__X__X__X') == "X wins"

    assert result_from_vertical('O__O__O__') == "O wins"
    assert result_from_vertical('_O__O__O_') == "O wins"
    assert result_from_vertical('__O__O__O') == "O wins"

    assert Impossible('OO_XXX___') != "Impossible"
    assert Impossible('XO_XO_XO_') == "Impossible"
    assert Impossible('X'*9) == "Impossible"
    assert Impossible('_O_X__X_X') == "Impossible"
    assert resultaat_van_tictactoe('XO_XO_XOX') == "Impossible"


    assert Draw('XOXOOXXXO') == 'Draw'
    assert Draw('XXXOO__O_') != 'Draw'

    assert Game_not_finsed('XO_OOX_X_') == 'Game not finished'
    assert Game_not_finsed('OX_XXO_O_') == 'Game not finished'

    assert resultaat_van_tictactoe('XOXOOXXXO') == 'Draw'
    assert resultaat_van_tictactoe('XO_OOX_X_') == 'Game not finished'
    assert resultaat_van_tictactoe('_O_X__X_X') == 'Impossible'
