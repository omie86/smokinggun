"""Application endpoints that communicate with Mailgun API.
"""


from flask import make_response, jsonify

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
