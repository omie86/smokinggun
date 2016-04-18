"""Contains application views.
"""


from flask import Flask, render_template, jsonify, make_response, request

from mailgunpi import app


@app.route('/', methods=['GET'])
def get_root():
    return render_template('index.html')
