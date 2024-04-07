import os
import json

from typing import List, Dict, Any


def save_to_disk_json(data: List[Dict[str, Any]], raw_dir: str, date: str) -> None:
    print(os.path.join(raw_dir.replace('//', '/'), f"{date}.json"))
    os.makedirs(raw_dir, exist_ok=True)
    with open(os.path.join(raw_dir, f"{date}.json"), "w") as file:
        json.dump(data, file)
        file.close()
