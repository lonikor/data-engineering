import json
import os

import fastavro


def read_and_save_to_avro(file_name: str, raw_dir: str, stg_dir: str) -> None:
    with open(raw_dir + "/" + file_name, 'r') as f:
        data = json.load(f)

        if not os.path.exists(stg_dir):
            os.makedirs(stg_dir)

        schema = {
            'doc': 'A sales reading.',
            'name': 'Sales',
            'namespace': 'test',
            'type': 'record',
            'fields': [
                {'name': 'client', 'type': 'string'},
                {'name': 'purchase_date', 'type': 'string'},
                {'name': 'product', 'type': 'string'},
                {'name': 'price', 'type': 'long'},
            ],
        }

        with open(stg_dir + f'/{file_name.split(".")[0]}.avro', 'wb') as out:
            fastavro.writer(out, schema, data)
