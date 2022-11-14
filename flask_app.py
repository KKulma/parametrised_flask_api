from flask import Flask, jsonify, request

app = Flask(__name__)

games = [
    {'console': 'PS4',
     'name': 'Call of Duty'},
    {'console': 'XBox',
     'name': 'Lego Star Wars'},
    {'console': 'Nintendo',
     'name': 'Mario n64'},
    {'console': 'Nintendo',
     'name': 'Mario Maker'}
]

@app.route('/api/', methods=['GET'])
def get_games():
    console = request.args['console']
    results = []
    for game in games:
        if game['console'] == console:
            results.append(game)
    return jsonify(results)



app.run(debug=True, port=5001)