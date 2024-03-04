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


app = Flask(__name__)
import secrets
app.secret_key = secrets.token_hex(16)
CORS(app, supports_credentials=True)


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
        gather_instance.scrape_user_club(username, password)
        response = {"status": "Success", "message": "Scraping Complete"}
    except Exception as e:
        response = {"status": "Error", "message": str(e)}
    finally:
        gather_instance.driver.quit()
    
    return jsonify(response)



@app.route('/logout')
def logout():
    # Remove user_id from session
    session.pop('user_id', None)
    # You can add more session keys to clear if needed
    return jsonify({"status": "Success", "message": "Logged out successfully"})



if __name__ == '__main__':
    app.run()