import pickle
from clases import Table
class Save_load_game():
    def __init__(self):
        self.list_of_games : [Table] = self.__read_games() 
    def save_game(self, table):
        self.list_of_games.append(table)
        with open("games","wb") as file:
            pickle.dump(self.list_of_games,file)
        del file
    def __read_games(self):
        try:
            with open("games", "rb") as games:
                return pickle.load(games)
        except (FileNotFoundError, EOFError):
            print("No hay partidas guardadas")
            return []

    def get_scores(self):
        list_scores = {}
        for index, table in enumerate(self.list_of_games):
            user_index= index+1
            print(f"{user_index}------------{table.score}")
            list_scores[index] = table.score
    def load_game(self, number):
        return self.list_of_games[number-1]        