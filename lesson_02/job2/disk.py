import json
import os

import fastavro

from avro_schema import SCHEMA


def read_and_save_to_avro(file_name: str, raw_dir: str, stg_dir: str) -> None:
    with open(raw_dir + "/" + file_name, 'r') as f:
        data = json.load(f)

        if not os.path.exists(stg_dir):
            os.makedirs(stg_dir)

        with open(stg_dir + f'/{file_name.split(".")[0]}.avro', 'wb') as out:
            fastavro.writer(out, SCHEMA, data)
