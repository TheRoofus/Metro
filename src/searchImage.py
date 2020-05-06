import os


def search_image(folder, img):
    def wrapper():
        game_folder = os.path.dirname(__file__)
        print(game_folder)
        return os.path.join(f'{game_folder}/resources/{folder}', f'{img}')

    return wrapper()
