from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Inicializar el tablero y puntuaciones
board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"
scores = {"X": 0, "O": 0}

@app.route('/')
def index():
    return render_template('index.html', scores=scores)

@app.route('/move', methods=['POST'])
def move():
    global current_player
    data = request.json
    row, col = data['row'], data['col']

    if board[row][col] == "":
        board[row][col] = current_player
        winner = check_winner()
        if winner:
            scores[winner] += 1  # Incrementar la puntuación del ganador
            return jsonify({"board": board, "winner": winner, "scores": scores})
        current_player = "O" if current_player == "X" else "X"
    return jsonify({"board": board, "winner": None, "scores": scores})

@app.route('/reset', methods=['POST'])
def reset():
    global board, current_player
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    return jsonify({"board": board, "scores": scores})

def check_winner():
    # Comprobar filas, columnas y diagonales
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    
    return None

if __name__ == '__main__':
    app.run(debug=True)
