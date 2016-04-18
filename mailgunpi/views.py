"""Contains application views.
"""


from flask import Flask, render_template, jsonify, make_response, request

from mailgunpi import app
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
        events = None

    return render_template('index.html', events=events)
