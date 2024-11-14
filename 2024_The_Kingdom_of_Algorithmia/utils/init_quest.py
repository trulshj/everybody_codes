import pathlib


QUEST_NUMBER = int(input("Quest number: "))
DIRECTORY_NAME = f"quest_{QUEST_NUMBER:02}"

current_path = pathlib.Path('.')
print("Target is:", (current_path / DIRECTORY_NAME).absolute())

proceed = "?"
while proceed not in ["Y", "N", "y", "n", ""]:
    proceed = input("Proceed? [Y/n] ")

if proceed.lower() == "n":
    exit()

current_path = current_path / DIRECTORY_NAME
current_path.mkdir(exist_ok=True)

FILE_NAMES = [f"{DIRECTORY_NAME}.py", "part_1.txt", "part_2.txt", "part_3.txt"]

for file_name in FILE_NAMES:
    path = current_path / file_name
    path.touch(mode=644, exist_ok=True)
