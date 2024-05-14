"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    count_x = sum(row.count(X) for row in board)
    count_o = sum(row.count(O) for row in board)

    if count_x == count_o:
        return X  # Próximo a jogar é o jogador "X"
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    acoes_possiveis = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                acoes_possiveis.add((i,j))
    return acoes_possiveis


def result(board, action):
    acoesp = actions(board)

    if action not in acoesp:
        raise Exception("Not valid Action")

    i, j = action
    if board[i][j] is not None:
        raise Exception("Cell already occupied")

    # Faça uma cópia profunda do tabuleiro manualmente
    boardR = [row[:] for row in board]

    if player(board) == X:
        boardR[i][j] = X
    else:
        boardR[i][j] = O

    return boardR


def winner(board):
    # Verifica vitória nas linhas
    for row in board:
        if row.count("X") == 3:
            return "X"
        elif row.count("O") == 3:
            return "O"

    # Verifica vitória nas colunas
    for col in range(3):
        if all(board[row][col] == "X" for row in range(3)):
            return "X"
        elif all(board[row][col] == "O" for row in range(3)):
            return "O"

    # Verifica vitória nas diagonais
    if all(board[i][i] == "X" for i in range(3)) or all(board[i][2 - i] == "X" for i in range(3)):
        return "X"
    elif all(board[i][i] == "O" for i in range(3)) or all(board[i][2 - i] == "O" for i in range(3)):
        return "O"

    # Se não houver vencedor, retorna None
    return None


def terminal(board):
    # Verifica se há um vencedor
    if winner(board) is not None:
        return True

    # Verifica se todas as células foram preenchidas
    if all(cell is not None for row in board for cell in row):
        return True

    # Se nenhum dos casos acima for verdadeiro, o jogo ainda está em andamento
    return False


def utility(board):
    winner_player = winner(board)

    if winner_player == "X":
        return 1
    elif winner_player == "O":
        return -1
    else:
        return 0


def minimax(board):
    current_player = player(board)

    if terminal(board):
        return None

    if current_player == X:
        _, move = max_value(board)
    else:
        _, move = min_value(board)

    return move


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = -math.inf
    best_move = None

    for action in actions(board):
        new_board = result(board, action)
        value, _ = min_value(new_board)

        if value > v:
            v = value
            best_move = action

    return v, best_move


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = math.inf
    best_move = None

    for action in actions(board):
        new_board = result(board, action)
        value, _ = max_value(new_board)

        if value < v:
            v = value
            best_move = action

    return v, best_move
