import os

from flask import Flask, request
from settings import APPLICATION_PORT

from disk import read_and_save_to_avro

app = Flask(__name__)


@app.post("/")
def execute():
    input_data: dict = request.get_json()
    raw_dir: str = input_data.get('raw_dir')
    stg_dir: str = input_data.get('stg_dir')

    if not raw_dir:
        return {
            "message": "raw_dir parameter missed",
        }, 400

    formatted_raw_dir = ('./file_storage/raw/' + f'{raw_dir}').replace('//', '/')

    if not os.path.isdir(formatted_raw_dir):
        return {
            "message": "raw_dir does not exists",
        }, 400

    if not stg_dir:
        stg_dir = './file_storage/stg/' + f'{raw_dir}'
    else:
        stg_dir = './file_storage/stg/' + f'{stg_dir}'

    formatted_stg_dir = stg_dir.replace('//', '/')

    dir_content = os.listdir(formatted_raw_dir)

    if len(dir_content) == 0:
        return {
            "message": "raw_dir is empty",
        }, 400

    file_name = dir_content[0]

    read_and_save_to_avro(file_name, formatted_raw_dir, formatted_stg_dir)

    return {
        "success": "File saved successfully",
    }, 201


if __name__ == "__main__":
    app.run(debug=True, port=APPLICATION_PORT, host='0.0.0.0')
