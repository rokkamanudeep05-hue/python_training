import json
from pathlib import Path


DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)


def load_data(filename):
    file_path = DATA_DIR / filename

    if not file_path.exists():
        return []

    try:
        with file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError(
                f"{filename} must contain a JSON list."
            )

        return data

    except json.JSONDecodeError as error:
        raise ValueError(
            f"{filename} contains invalid JSON."
        ) from error


def save_data(filename, data):
    file_path = DATA_DIR / filename
    temp_path = file_path.with_suffix(".tmp")

    with temp_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    temp_path.replace(file_path)