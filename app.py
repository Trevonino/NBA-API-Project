from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

# SELECT team_name, position FROM common_player_info WHERE person_id = (SELECT id FROM player WHERE full_name = 'Bill Laimbeer');

def connect_to_db():
    conn = sqlite3.connect('basketball.sqlite')
    return conn


def get_players():
    players = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM player ORDER BY id;")
        rows = cur.fetchall()

        # convert row objects to dictionary
        for i in rows:
            player = {}
            player["id"] = i["id"]
            player["full_name"] = i["full_name"]
            player["first_name"] = i["first_name"]
            player["last_name"] = i["last_name"]
            player["is_active"] = i["is_active"]
            players.append(player)

    except:
        players = []

    return players


def get_player(fname, lname):
    players = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        print(fname)
        print(lname)
        cur.execute("SELECT * FROM player WHERE first_name LIKE ? AND last_name LIKE ? ORDER BY id;",
                    (fname, lname))
        rows = cur.fetchall()

        # convert row object to dictionary
        for i in rows:
            player = {}
            player["id"] = i["id"]
            player["full_name"] = i["full_name"]
            player["first_name"] = i["first_name"]
            player["last_name"] = i["last_name"]
            player["is_active"] = i["is_active"]
            players.append(player)

    except:
        players = []

    return players


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/api/players', methods=['GET'])
def api_get_players():
    return jsonify(get_players())


@app.route('/api/player', methods=['GET'])
def player():
    fname  = request.args.get('fname', '%')
    lname  = request.args.get('lname', '%')
    return jsonify(get_player(fname, lname))


if __name__ == '__main__':
    app.run()
