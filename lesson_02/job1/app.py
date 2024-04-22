import os

from flask import Flask, request

from settings import AUTH_TOKEN, APPLICATION_PORT
from sales_api.disk import save_to_disk_json
from sales_api.http import fetch_data

app = Flask(__name__)


@app.post("/")
def execute():
    input_data: dict = request.get_json()
    date: str = input_data.get('date')

    if not date:
        return {
            "message": "date parameter missed",
        }, 400

    raw_dir: str = input_data.get('raw_dir')

    if not raw_dir:
        raw_dir = os.path.join('./file_storage/raw', date)
    else:
        raw_dir = os.path.join('./file_storage/raw', raw_dir)

    save_to_disk_json(fetch_data(date, AUTH_TOKEN), raw_dir, date)

    return {
        "message": "Data retrieved successfully from API",
    }, 201


if __name__ == "__main__":
    app.run(debug=True, port=APPLICATION_PORT, host='0.0.0.0')
