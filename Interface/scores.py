import pickle
import datetime
class Scores():
    def __init__(self):
        self.scores = self.__read_scores()
        print(self.scores)
        print("------------------------------------")
    def write_score(self, new_score):
        current_date = datetime.datetime.now()
        self.scores[current_date] = new_score

        with open("Interface/Scores", "wb") as file:
            pickle.dump(self.scores, file)
    
    def __read_scores(self):
        try:
            with open("Interface/Scores", "rb") as file:
                scores = pickle.load(file)
        except FileNotFoundError:
            scores = {}
        return scores
    def __get_sorted_scores(self):
        sorted_scores = sorted(self.scores.items(), key=lambda x: x[1], reverse=True)
        print(dict(sorted_scores))
        return dict(sorted_scores)
    def get_scores(self):
        return self.__get_sorted_scores() 