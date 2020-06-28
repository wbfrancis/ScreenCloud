import os
from flask import Flask, request, jsonify, abort, render_template, Response, flash, redirect, url_for
from sqlalchemy import exc
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# db_drop_and_create_all()
# ENDPOINTS FOR RECIPES
# #####################

@app.route('/scripts')
def get_preuploaded_scripts():
    preuploaded_script_data = {
        "id": -1,
        "title": "",
        "author": "",
        "characterNames": []
    }

    return jsonify({
        "success": True,
        "scripts": preuploaded_script_data
    })

@app.route('/scripts', methods=['POST'])
def upload_script():
    script_object = {}
    characterNames = []

    return jsonify({
        "success": True,
        "scriptObject": script_object,
        "characterNames": characterNames
    })

# script_id=-1, script_obj=None, whole_script=False, action_lines=False, characters=[]
@app.route('/clouds', methods=['POST'])
def generate_clouds():
    clouds = []
    return jsonify({
        "success": True,
        "clouds": clouds
    })

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'error': 404,
        'message': 'resource not found'
    }), 404


@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "bad request"
    }), 400