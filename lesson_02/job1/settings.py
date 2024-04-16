import os

AUTH_TOKEN = os.environ.get('AUTH_TOKEN')
APPLICATION_PORT = os.environ.get('PORT')

if not AUTH_TOKEN:
    print("AUTH_TOKEN environment variable must be set")
    raise Exception("AUTH_TOKEN environment variable must be set")

if not APPLICATION_PORT:
    APPLICATION_PORT = 8081

BASE_URL = "https://fake-api-vycpfa6oca-uc.a.run.app/sales"