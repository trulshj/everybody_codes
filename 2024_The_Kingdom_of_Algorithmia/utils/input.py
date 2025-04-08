from pathlib import Path


def get_input_path(quest: int, part: int):
    BASE_PATH = Path(
        "/Users/trulshj/dev/everybody_codes/2024_The_Kingdom_of_Algorithmia/inputs")
    return BASE_PATH / f"quest_{quest:02}" / f"part_{part}.txt"


def read_input(quest: int, part: int) -> str:
    file_path = get_input_path(quest, part)
    with open(file_path) as f:
        return f.read()


def readlines_input(quest: int, part: int) -> list[str]:
    file_path = get_input_path(quest, part)
    with open(file_path) as f:
        return f.readlines()
