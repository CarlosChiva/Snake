import pickle
from clases import clases
class Save_load_game():
    def __init__(self):
        self.list_of_games : [clases.Table] = self.__read_games() 
    def save_game(self, table):
        with open("games","wb") as file:
            self.list_of_games.append(table)
            pickle.dump(table,file)
        del file
    def __read_games(self):
        try:
            with open("games", "rb") as games:
                self.list_of_games = pickle.load(games)
            return self.list_of_games
        except:
            print("No hay partidas guardadas")

    def get_scores(self):
        list_scores = {}
        for index, score in self.list_of_games:
            list_scores[index] = score.score