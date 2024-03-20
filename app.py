from flask import Flask, request, jsonify, session
import sqlite3
import math
import Flask.Helper as helper
import random
import json
import Flask.solver as solver
from Flask.gather import Gather
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import traceback
import sqlite3
import uuid
import secrets
from flask_cors import CORS
from extensions import socketio

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
CORS(app, supports_credentials=True)
socketio.init_app(app)


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username and password:
        session['username'] = username
        session['password'] = password
        print(session)
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/solve-SBC', methods=['POST'])
def solveSBC():
    players = solver.load_players_from_database()
    data = request.get_json()
    formationJson = data.get('formation', [])
    json = data.get('criteria')
    
    best_squad = solver.solve_sbc(formationJson,players, json)
    print(f"this is the best squad {best_squad}")
    
    players_list = [
        {
            "name": player.name,
            "rating": player.rating,
            "club": player.club,
            "nation": player.nation,
            "league": player.league,
        } for player in best_squad
    ]
    response = {
        "best_squad": players_list
    }
    return jsonify(response)



@app.route('/scrape', methods=['POST'])
def scrape_data():
    print(session)
    username = session.get('username')  # Retrieve username from session
    password = session.get('password')  # Retrieve password from session
    if not username or not password:
        return jsonify({"status": "Error", "message": "User not logged in"}), 401
    try:
        gather_instance = Gather()
        is_2FA_needed = gather_instance.is_2FA(username, password)
        print(f"this is the is 2FA needed {is_2FA_needed}")
        #gather_instance.driver.quit()
        if is_2FA_needed:
            print('sending status to front end that we need 2FA')
            return jsonify({"status": "2FA Required", "message": "2FA verification needed"}), 200
        else:
            gather_instance.scrape_without_2FA(username, password)
            return jsonify({"status": "Success", "message": "Scraping complete"}), 200
        
    except Exception as e:
        response = {"status": "Error", "message": str(e)}
    return jsonify(response)


@app.route('/submit-2FA', methods=['POST'])
def submit_2FA():
    print("in submitting 2FA")
    data = request.get_json()
    username = session.get('username')
    password = session.get('password')
    code = data.get('code')

    if not username or not password or not code:
        return jsonify({"status": "Error", "message": "Missing credentials or 2FA code"}), 400
    
    try:
        gather_instance = Gather()
        print("scraping with code")
        # Use the provided 2FA code to proceed with the scraping process
        gather_instance.scrape_user_club(username, password, code)
        print("scraped with code")
        return jsonify({"status": "Success", "message": "Scraping after 2FA complete"}), 200
    except Exception as e:
        return jsonify({"status": "Error", "message": str(e)}), 500



@app.route('/logout')
def logout():
    # Remove user_id from session
    session.pop('user_id', None)
    # You can add more session keys to clear if needed
    return jsonify({"status": "Success", "message": "Logged out successfully"})



if __name__ == '__main__':
    socketio.run(app, debug=True)
