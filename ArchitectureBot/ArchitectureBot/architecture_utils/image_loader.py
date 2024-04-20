def get_image(folder_name: str):
    path = "images/" + folder_name + "/" + folder_name + ".jpg"
    with open(path, "rb") as image:
        return image
