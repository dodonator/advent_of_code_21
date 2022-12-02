import requests
from pathlib import Path
import datetime


def load_session_key(filename):
    filepath = Path(filename)
    with filepath.open("r") as stream:
        session_key = stream.read()
    return session_key


def download_input_data(year: int, day: int) -> Path:

    input_url = f"https://adventofcode.com/{year}/day/{day}/input"
    output_file = f"input_{year}-12-{day:0>2}.txt"

    output_path = Path(output_file)
    if output_path.exists():
        return output_path

    session_key = load_session_key("session_key.txt")
    req = requests.get(input_url, cookies={"session": session_key})

    if not output_path.exists():
        output_path.touch()

    text = req.text

    with output_path.open("w") as stream:
        stream.write(text)

    return output_path


def create_code_file(year: int, day: int) -> Path:
    template_path = Path("template.py")
    output_path = Path(f"{year}-12-{day:0>2}.py")

    if output_path.exists():
        return output_path

    with template_path.open("r") as stream:
        template = stream.read()

    content = template.format(year=year, day=day)

    with output_path.open("w") as stream:
        stream.write(content)

    return output_path


def init(year: int, day: int):
    data_path = download_input_data(year, day)
    code_path = create_code_file(year, day)
    print(f"input data: {data_path}")
    print(f"code path: {code_path}")


if __name__ == "__main__":
    today = datetime.date.today()
    year = today.year
    day = today.day
    init(year, day)
