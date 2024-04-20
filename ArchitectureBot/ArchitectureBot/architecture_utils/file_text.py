def get_text(file_name: str) -> str:
    path = "text/" + file_name + ".txt"
    with open(path, "r", encoding="utf-8") as file:
        text = "".join(file.readlines())
        return text
