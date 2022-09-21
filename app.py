
from flask import Flask, jsonify, render_template
from tide import *

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True



@app.route('/')
def index():
    """Date, Time and Heigh for each location"""
    cities= ['Half Moon Bay California', "Huntington Beach California", "Providence Rhode Island", "Wrightsville Beach North Carolina"]
    low_tide_data = []
    for city in cities:
        half_moon_tide = LowTide(city)
        tide = half_moon_tide.low_tide()['data']
        low_tide_data.append(tide)
    return render_template('index.html', low_tide_data=low_tide_data)




#________________________________SIMPLE API ROUTES______________________________________________________

"""API routes for for accessing low_tides data. Only Get requests are supported"""

@app.route('/halfmoon')
def half_moon():
    half_moon_tide = LowTide("Half Moon Bay California")
    tide = half_moon_tide.low_tide()['data']
    return jsonify(tide)

@app.route('/huntington')
def huntington():
    huntington_tide = LowTide("Huntington Beach California")
    tide = huntington_tide.low_tide()['data']
    return jsonify(tide)

@app.route('/providence')
def providence():
    providence_tide = LowTide("Providence Rhode Island")
    tide = providence_tide.low_tide()['data']
    return jsonify(tide)

@app.route('/wrightsville')
def wrightsville():
    wrightsville_tide = LowTide("Wrightsville Beach North Carolina")
    tide = wrightsville_tide.low_tide()['data']
    return jsonify(tide)


