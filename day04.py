with open(file='data.txt') as file:
    numbers = list(map(int, file.read().split("\n")[0].split(",")))
with open(file='data.txt') as file:
    data = file.read().split("\n")
    bingo_boards = []
    board_template = []

    for line in data[2:]:
        test = [int(char) for char in line.split(" ") if char]
        if not test:  # new board
            bingo_boards.append(board_template)
            board_template = []
        else:
            board_template.append(test)


    def check_board_for_number(number):
        for r, row in enumerate(board):
            for c, col in enumerate(row):
                if board[r][c] == number:
                    board[r][c] = "X"
                    return


    def check_row_and_col():
        for row in board:
            if row.count("X") == 5:
                return True

        for c in range(len(board[0])):
            col_string = ""
            for r in range(len(board)):
                col_string += str(board[r][c])

            if col_string.count("X") == 5:
                return True

        return False


    def calculate_winning_board():
        total_sum = 0
        for r, row in enumerate(board):
            for c, col in enumerate(row):
                if board[r][c] != "X":
                    total_sum += board[r][c]

        return total_sum

    winning_boards = {}
    for number in numbers:
        for index, board in enumerate(bingo_boards):
            if index not in winning_boards:
                check_board_for_number(number)
                if check_row_and_col():
                    winning_boards[index] = number * calculate_winning_board()

    print(winning_boards)
