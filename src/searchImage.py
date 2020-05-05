import os


def search_image(folder, img):
    def wrapper():
        game_folder = os.path.dirname(__file__)
        return os.path.join(f'{game_folder}/Media/{folder}', f'{img}')

    return wrapper()
