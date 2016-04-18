"""Application endpoints that communicate with Mailgun API.
"""


from flask import make_response, jsonify
import requests

from mailgunpi import app


@app.route('/api/v1/mailgun/events', methods=['GET'])
def get_events():
    """Return Mailgun API response"""
    data = {
        'status': 200,
        'total': 0,
        'items': []
    }

    return jsonify(data)


@app.route('/api/v1/mailgun/events/<domain_name>', methods=['GET'])
def get_domain_events(domain_name):
    """Return events resource for domain"""
    response = get_events(domain_name)
    json_response = response.json()
    items = json_response['items']

    data = {
        'status': 200,
        'total': len(items),
        'items': items
    }

    return jsonify(data)


def get_events(domain_name):
    domain = "https://api.mailgun.net/v3/{}/events".format(domain_name)
    return requests.get(
        domain,
        auth=("api", app.config["MAILGUN_API_KEY"]),
        params={"begin"       : "Sun, 3 Apr 2016 09:00:00 -0000",
                "ascending"   : "yes",
                "limit"       :  25,
                "pretty"      : "yes"})
