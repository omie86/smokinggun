"""Application endpoints that communicate with Mailgun API.
"""


import copy

from flask import make_response, jsonify, request

from mailgunpi import app
from mailgunpi.models import RESPONSE_MODEL
from mailgunpi.utils import get_events


@app.route('/api/v1/mailgun/events', methods=['GET'])
def get_json_events():
    """Return Mailgun API response"""
    domain = request.args.get('domain')
    if not domain:
        response_document = copy.deepcopy(RESPONSE_MODEL)
        response_document['status'] = 'No domain provided'
        return jsonify(response_document)

    # Fetch data from Mailgun API
    response = get_events(domain)
    json_response = response.json()
    items = json_response['items']

    # Build response JSON document
    response_document = copy.deepcopy(RESPONSE_MODEL)
    response_document['domain'] = domain
    response_document['total'] = len(items)
    response_document['items'] = items

    return jsonify(response_document)
