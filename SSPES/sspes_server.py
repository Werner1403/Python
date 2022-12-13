from flask import Flask, render_template
from flask_restful import Api
from sspes_rest import sspes_stats, player_stats

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return render_template('index.html')

api.add_resource(sspes_stats, '/stats')
api.add_resource(player_stats, '/player/<string:p>')

app.run(debug=True)