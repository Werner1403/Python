import os
from flask import Flask, render_template, request, send_file, send_from_directory
from flask_restful import Api
from sspes_rest import sspes_stats, player_stats

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']
        os.remove('SSPES/sspes.json')
        f.save('SSPES/sspes.json')  
        return render_template("Acknowledgement.html", name = f.filename)
    
@app.route('/download')
def download_file():
	path = "sspes.json"
	return send_file(path, as_attachment=True)

api.add_resource(sspes_stats, '/stats')
api.add_resource(player_stats, '/player/<string:p>')

app.run(debug=True)