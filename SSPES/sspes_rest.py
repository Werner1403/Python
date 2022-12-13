from flask import jsonify
from flask_restful import Resource
import json

class sspes_stats(Resource):
    def get(self):
        with open('SSPES/sspes.json', 'r') as f:
            data = json.load(f)
            pd = json.dumps(data["players"], indent=4)
            return pd

class player_stats(Resource):
    def get(self, p):
        with open('SSPES/sspes.json', 'r') as f:
            data = json.load(f)
            if p in data["players"]:
                return json.dumps(data["players"][p], indent=4)
            else:
                return {"Message" : "not found"}