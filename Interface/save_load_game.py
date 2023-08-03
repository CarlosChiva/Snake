import pickle
from clases import clases
class Save_load_game():
    def __init__(self):
        pass
    def save_game(self, table):
        with open("games","wb") as file:
            pickle.dump(table,file)
        del file
    def load_game(self):
        try:
            with open("games", "rb") as games:
                lista_games = pickle.load(games)
                for i in lista_games:
                    print(i.score)
            return lista_games
        except:
            print("No hay partidas guardadas")