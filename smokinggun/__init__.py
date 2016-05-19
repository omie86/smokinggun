from flask import Flask


app = Flask(__name__, static_url_path='', static_folder='static', instance_relative_config=True)
app.config.from_object('smokinggun.config')
app.config.from_pyfile('config.py', silent=True)


from smokinggun.mailgunclient import MailgunClient

api_key = app.config['MAILGUN_API_KEY']
base_url = app.config['MAILGUN_API_BASE_URL']

mg = MailgunClient(api_key, base_url)


from smokinggun import views
