from flask import Flask, redirect
import querybot.query as query

app = Flask(__name__)

@app.route("/")
def hello_world():
    return redirect(query.get_install_team_map(), code=307)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4055, debug=True)