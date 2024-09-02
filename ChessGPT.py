import chess

board = chess.Board()

def generate_legal_moves_from_square(square):
    legal_moves = []
    for move in board.generate_legal_moves():
        if (move.from_square == square):
            legal_moves.append(move)
    return legal_moves

def square_input():
    return chess.parse_square(input("enter a square: "))

def move_input():
    return chess.Move.from_uci(input("enter a move: "))

# null move
# board.push(chess.Move.null())

# legal move check
# board.is_legal(move)

# move from uci
# chess.Move.from_uci('a1a3')

"""
A8 B8 C8 D8 E8 F8 G8 H8
A7 B7 C7 D7 E7 F7 G7 H7
A6 B6 C6 D6 E6 F6 G6 H6
A5 B5 C5 D5 E5 F5 G5 H5
A4 B4 C4 D4 E4 F4 G4 H4
A3 B3 C3 D3 E3 F3 G3 H3
A2 B2 C2 D2 E2 F2 G2 H2
A1 B1 C1 D1 E1 F1 G1 H1
"""

while (True):
    legal_moves = []
    while (len(legal_moves) == 0):
        square = square_input()
        legal_moves = generate_legal_moves_from_square(square)
    for move in legal_moves:
        print(move)
    move = move_input()
    board.push(move)
    print(board)
