"""Contains application views.
"""


import json

from flask import Flask, redirect, render_template, jsonify, make_response, request, send_from_directory

from json2csv import gen_outline, json2csv

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
        download_endpoint = '/download?domain={}'.format(domain)
    else:
        events = []
        download_endpoint = None

    return render_template('index.html', events=events, download_link=download_endpoint)


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

    mailgun_json = {
        "data": events
    }

    # Write JSON file
    filename = 'mailgun_json.json'

    json_file_path = './mailgunpi/tempfiles/{}'.format(filename)

    with open(json_file_path, 'w') as f:
        f.write(json.dumps(mailgun_json))


    temp_json_file = open(json_file_path, 'r')

    # Generate JSON map file
    outline = gen_outline.make_outline(json_file=temp_json_file, each_line=False, collection_key='data')

    # Store map file
    temp_outfile = 'temp.outfile.json'
    outfile = './mailgunpi/tempfiles/{}'.format(temp_outfile)
    with open(outfile, 'w') as f:
        json.dump(outline, f, indent=2, sort_keys=True)

    # Convert JSON file to CSV
    key_map_json = open(outfile)
    key_map = json.load(key_map_json)

    loader = json2csv.Json2Csv(key_map)

    file_json = open(json_file_path, 'r')
    loader.load(file_json)

    # Write to CSV file
    loader.write_csv(filename="./mailgunpi/tempfiles/test.csv")

    # Return CSV file
    return send_from_directory(directory=UPLOAD_FOLDER, filename='test.csv')
