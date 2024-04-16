import os

APPLICATION_PORT = os.environ.get('PORT')

if not APPLICATION_PORT:
    APPLICATION_PORT = 8082
