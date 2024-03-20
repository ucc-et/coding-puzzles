
# class BingoFinder:
#     def __init__(self):
#         self.drawnNumbers = []
#         self.boards = [] #List where every element is a board --> every element is a 2d-list
#         self.lastCheckedNum = 0

#         self.getBingoSeries()
#         self.getBoards()
        
#         for number in self.drawnNumbers:
#             for boardIndex in range(len(self.boards)):
#                 self.lastCheckedNum = int(number)
#                 if self.checkIfNumberOnBoard(boardIndex, number):
#                     if self.checkIfBoardWins(boardIndex):
#                         sum = self.sumAllNonMarked(boardIndex)
#                         print(sum)
#                         print("Part 1: ", sum*self.lastCheckedNum)
#                         print(self.lastCheckedNum)
#                         self.printBoard(boardIndex)
#                         return

#     def getBingoSeries(self):
#         # put the first line of the input into a list
#         with open('input.txt') as bingo:
#             firstLine = bingo.readline()
#             currentNum = ""
#             for i in firstLine:
#                 if i == ",":
#                     self.drawnNumbers.append(currentNum)
#                     currentNum = ""
#                 elif i == firstLine[len(firstLine)-1]:
#                     self.drawnNumbers.append(currentNum)
#                     break
#                 else:
#                     currentNum += i

#     def getBoards(self):
#         # put the bingo boards into the boards list
#         currentBoard = []
#         boardLine = []
#         number = ""
#         numbersInRow = 0
#         linesInBoard = 0
#         fileInput = []
#         row = 0

#         with open('input.txt') as bingo:
#             fileInput = bingo.readlines()
#             fileInput = fileInput[2:len(fileInput)-1]
#             # \n break line
#             # x y z \n --> line of board
#             # \n board done
#         for line in fileInput:
#             if line == "\n":
#                 pass
#             else:
#                 newLine = line[:-2]
#                 # line contains bingo board values
#                 for character in newLine:
#                     # character
#                     if numbersInRow == 5:
#                         # already 5 numbers in line
#                         numbersInRow = 0
#                         currentBoard.append(boardLine)
#                         boardLine = []
#                         linesInBoard += 1
#                     elif linesInBoard == 5:
#                         # already 5 lines from the board
#                         linesInBoard = 0
#                         self.boards.append(currentBoard)
#                         currentBoard = []
#                     else:
#                         # normal num
#                         if character == " ":
#                             # character is space
#                             if number != "":
#                                 numbersInRow += 1
#                                 boardLine.append(number)
#                                 number = ""
#                         else:
#                             number += character

#     def printBoard(self, boardIndex):
#         for i in self.boards[boardIndex]:
#             print(i)
#         print("-------------")

#     def checkIfNumberOnBoard(self, boardIndex, number):
#         numberOnBoard = 0
#         for row in range(len(self.boards[boardIndex])):
#             for column in range(len(self.boards[boardIndex][row])):
#                 if number == self.boards[boardIndex][row][column]:
#                     self.markNumber(boardIndex, row, column)
#                     numberOnBoard += 1
#         if numberOnBoard != 0:
#             return True
#         return False

#     def markNumber(self, boardIndex, row, column):
#         # mark the number on the board if its on
#         self.boards[boardIndex][row][column] = "O"
#         return

#     def checkIfBoardWins(self, boardIndex):
#         # check if the board won
#         for lineIndex in range(len(self.boards[boardIndex])):
#             for columnIndex in range(len(self.boards[boardIndex][lineIndex])):
#                 if self.boards[boardIndex][lineIndex][columnIndex] == "O":
#                     if lineIndex == 0:
#                         if self.checkUpperLine(boardIndex, columnIndex):
#                             return True
#                     elif lineIndex == len(self.boards[boardIndex])-1:
#                         if self.checkBottomLine(boardIndex,  columnIndex):
#                             return True
#                     else:
#                         if self.checkMiddle(boardIndex, lineIndex, columnIndex):
#                             return True
#         return False
    
#     def checkUpperLine(self, boardIndex, columnIndex):
#         board = self.boards[boardIndex]

#         if board[0][0] + board[0][1] + board[0][2] + board[0][3] + board[0][4] == "OOOOO":
#             return True
#         elif board[0][columnIndex] + board[1][columnIndex] + board[2][columnIndex] + board[3][columnIndex] + board[4][columnIndex] == "OOOOO":
#             return True
#         return False

#     def checkBottomLine(self, boardIndex, columnIndex):
#         board = self.boards[boardIndex]

#         if board[4][0] + board[4][1] + board[4][2] + board[4][3] + board[4][4] == "OOOOO":
#             return True
#         elif board[0][columnIndex] + board[1][columnIndex] + board[2][columnIndex] + board[3][columnIndex] + board[4][columnIndex] == "OOOOO":
#             return True
#         return False

#     def checkMiddle(self, boardIndex, lineIndex, columnIndex):
#         board = self.boards[boardIndex]

#         if board[lineIndex][0] + board[lineIndex][1] + board[lineIndex][2] + board[lineIndex][3] + board[lineIndex][4] == "OOOOO":
#             return True
#         elif board[0][columnIndex] + board[1][columnIndex] + board[2][columnIndex] + board[3][columnIndex] + board[4][columnIndex] == "OOOOO":
#             return True
#         return False

#     def sumAllNonMarked(self, boardIndex):
#         # take the sum of all non marked
#         sum = 0
#         line = []
#         board = self.boards[boardIndex]
#         for lines in range(len(board)):
#             for column in range(len(board[lines])):
#                 if board[lines][column] != "O":
#                     line.append(board[lines][column])

#         for i in range(len(line)):
#             if line[i] != "O":
#                 sum += int(line[i])
#         return sum


# a = BingoFinder()


def get_input(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]


def make_boards(data):
    drawn_numbers = data[0].split(',')
    playing_boards = data[1:]
    parsed_boards = {}

    # Making the boards
    x, y = -1, -1
    for line in range(len(playing_boards)):
        if len(playing_boards[line]) == 0:
            x += 1
            parsed_boards[x] = {}
            for i in range(5):
                parsed_boards[x][i] = []
        else:   
            for num in playing_boards[line].split(" "):
                if num.isdigit():
                    parsed_boards[x][y].append(num)
        y += 1
        if y % 5 == 0:
            y = 0 

    return drawn_numbers, parsed_boards

def part_1(drawn_numbers, parsed_boards):
    # Drawing numbers
    playing = True
    while playing == True:
        for drawn in range(len(drawn_numbers)):
            x, y = 0, 0
            for board, board_values_dict in parsed_boards.items():
                for columns, rows in board_values_dict.items():
                    z = 0
                    for number in rows:
                        if drawn_numbers[drawn] == rows[z]:
                            rows[z] = 100
                            if rows.count(100) == 5 or int(board_values_dict[0][z]) + int(board_values_dict[1][z]) + int(board_values_dict[2][z]) + int(board_values_dict[3][z]) + int(board_values_dict[4][z]) == 500:
                                result = 0
                                last = int(number)
                                for col, row in board_values_dict.items():
                                    for num in row:
                                        if int(num) != 100:
                                            result += int(num)
                                print("Part 1: ", result * last)
                                print(f"Board {board} complete")
                                playing = False
                                break
                            
                            if playing == False:
                                break
                        z += 1
                    if playing == False:
                        break
                    y += 1
                    if y % 5 == 0:
                        y = 0
                if playing == False:
                    break
                x += 1
                if x % 5 == 0:
                    x = 0
            if playing == False:
                break
        break

def part_2(drawn_numbers, parsed_boards):
    # Drawing numbers
    def solve(drawn_numbers, parsed_boards):
        playing = True
        while playing == True:
            d = -1
            for drawn in range(len(drawn_numbers)):
                d += 1
                x, y = 0, 0
                for board, board_values_dict in parsed_boards.items():
                    for columns, rows in board_values_dict.items():
                        z = 0
                        for number in rows:
                            if drawn_numbers[drawn] == rows[z]:
                                rows[z] = 100
                                if rows.count(100) == 5 or int(board_values_dict[0][z]) + int(board_values_dict[1][z]) + int(board_values_dict[2][z]) + int(board_values_dict[3][z]) + int(board_values_dict[4][z]) == 500:
                                    result = 0
                                    last = int(number)
                                    for col, row in board_values_dict.items():
                                        for num in row:
                                            if int(num) != 100:
                                                result += int(num)
                                    part2 = result * last
                                    # print(f"Board {board} complete")
                                    playing = False
                                    break
                                
                                if playing == False:
                                    break
                            z += 1
                        if playing == False:
                            break
                        y += 1
                        if y % 5 == 0:
                            y = 0
                    if playing == False:
                        break
                    x += 1
                    if x % 5 == 0:
                        x = 0
                if playing == False:
                    break
            break
            
        del parsed_boards[board]    
        return drawn_numbers[d:], parsed_boards, part2
    
    # print(f"drawn numbers: {len(drawn_numbers)}, boards: {len(parsed_boards)}")
    while len(parsed_boards) > 0:
        drawn_numbers, parsed_boards, solution = solve(drawn_numbers, parsed_boards)
        # print(f"drawn numbers: {len(drawn_numbers)}, boards: {len(parsed_boards)}")
    print("Part 2: ", solution)
    

if __name__ == '__main__':
    data = get_input('input.txt')
    d, l = make_boards(data)
    part_1(d, l)
    d, l = make_boards(data)
    part_2(d, l)