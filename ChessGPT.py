import dotenv
import os
import json
import random

from openai import OpenAI

import chess

dotenv.load_dotenv()

board = chess.Board()
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def get_completion_content():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a genius tactician that describes your moves in a verbose comedic way within JSON. You are the black side in a chess game with the user." + get_cheat_message() + ". An example of uci is [e2e4]."},
            {"role": "user", "content": "The following is the current board state in FEN: " + board.fen() + "\n Give me you're next move and a nonsense explanation for all moves done in the following format, where uci is a list: {uci: [...], explanation: ...}."}
        ],
        response_format={"type": "json_object"}
    )
    return completion.choices[0].message.content

def get_cheat_message():
    if (random.randint(0, 3) == 0):
        return "You are allowed to cheat by moving multiple pieces by giving them in a list"
    else:
        return ""

def generate_legal_moves_from_square(square):
    legal_moves = []
    for move in board.generate_legal_moves():
        if (move.from_square == square):
            legal_moves.append(move)
    return legal_moves

def square_input():
    return chess.parse_square(input("enter a square: ").strip().lower())

def move_input():
    return chess.Move.from_uci(input("enter a move: ").strip().lower())

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
    print("")
    content = json.loads(get_completion_content())

    for uci in content["uci"]:
        print(uci)
        board.set_piece_at(chess.parse_square(uci[2:4]), board.remove_piece_at(chess.parse_square(uci[0:2])))
    board.push(chess.Move.null())
    print(content["explanation"])
    print(board)
    print("")