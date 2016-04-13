"""Contains application views.
"""

from mailgunpi import app


@app.route('/', methods=['GET'])
def get_root():
    return 'MailgunPI'
