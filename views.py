from flask import Blueprint, render_template, request, jsonify, redirect, url_for


import sys
sys.path.append('Snake_game')

# Import the module's functions
from Snake_game.main import main


views = Blueprint(__name__, 'views')


@views.route('/run-program')
def run_program():
    # Your Python program code goes here
    main()
    return render_template('index.html', main=main())

@views.route('/')
def home():
    return render_template('index.html', name="Joe")


@views.route('/profile')
def profile():
    return render_template('profile.html')

@views.route("/json")
def get_json():
    return jsonify({"name": "Joe", "age": 20})

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for('views.home'))
