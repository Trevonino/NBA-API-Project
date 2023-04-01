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
        cur.execute("SELECT * FROM player WHERE LOWER(first_name) LIKE LOWER(?) AND LOWER(last_name) LIKE LOWER(?) ORDER BY id",
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


def get_stats(player_id):
    info = []
    try:
        conn = connect_to_db()
        print('we connect')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        print('we try to run command')
        cur.execute("SELECT * FROM common_player_info WHERE person_id = ?;",
                    (player_id,))
        print('we get a row')
        row = cur.fetchone()
        print('we get a row')
        info.append(row["display_first_last"])
        info.append(row["birthdate"])
        info.append(row["team_name"])
        info.append(row["team_city"])
        info.append(row["height"])
        info.append(row["weight"])
        info.append(row["position"])
        info.append(row["from_year"])
        info.append(row["to_year"])
        info.append(row["draft_round"])
        info.append(row["draft_number"])
        print(row["display_first_last"])

    except:
        info = []
        print(player_id)

    return info


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/api/players', methods=['GET'])
def api_get_players():
    return jsonify(get_players())


@app.route('/api/player', methods=['GET'])
def player():
    fname = request.args.get('fname', '%')
    lname = request.args.get('lname', '%')
    return jsonify(get_player(fname, lname))


@app.route('/api/info', methods=['GET'])
def info():
    id = request.args.get('id', '%')
    return jsonify(get_stats(id))


if __name__ == '__main__':
    app.run()
