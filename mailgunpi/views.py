"""Contains application views.
"""


import json

from flask import Flask, redirect, render_template, jsonify, make_response, request, send_from_directory

from mailgunpi import app
from mailgunpi.config import UPLOAD_FOLDER
from mailgunpi.utils import get_events


@app.route('/', methods=['GET'])
def get_root():
    """Return"""
    domain = request.args.get('domain')
    if domain:
        # Fetch data from Mailgun API
        response = get_events(domain)
        json_response = response.json()
        events = json_response['items']
    else:
        events = []

    return render_template('index.html', events=events)


@app.route('/download', methods=['GET'])
def download():
    """Download file"""
    domain = request.args.get('domain')
    if not domain:
        return jsonify({"error": "Missing required arguments"})

    # Fetch data from Mailgun API
    response = get_events(domain)
    json_response = response.json()
    events = json_response['items']

    # Write JSON file
    filename = 'data.csv'
    json_file_path = './mailgunpi/tempfiles/{}'.format(filename)
    with open(json_file_path, 'w') as f:
        f.write(json.dumps(events))

    # Convert JSON file to CSV

    # Write to CSV file

    # Return CSV file
    return send_from_directory(directory=UPLOAD_FOLDER, filename=filename)
