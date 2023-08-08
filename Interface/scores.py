import pickle
import datetime
class Scores():
    def __init__(self):
        self.scores = self.read_scores()
    def write_score(self, new_score):
        current_date = datetime.datetime.now()
        self.scores[current_date] = new_score

        with open("Scores", "wb") as file:
            pickle.dump(self.scores, file)
    
    def read_scores(self):
        try:
            with open("Scores", "rb") as file:
                scores = pickle.load(file)
            
        except FileNotFoundError:
            scores = {}
        return scores
        