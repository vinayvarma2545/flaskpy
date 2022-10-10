from flask import Flask
from healthcheck import HealthCheck

app = Flask (__name__)

health = HealthCheck()

# hello
app.add_url_rule('/healthcheck', 'healthcheck', view_func=lambda: health.run())
