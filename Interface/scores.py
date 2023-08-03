import pickle

class Scores():
    def __init__(self):
        self.scores = self.read_scores()
    def write_score(self, new_score):
        self.scores.append(new_score)
        self.scores.sort(reverse=True)  # Ordenar los puntajes en orden descendente
        with open("Scores", "wb") as file:
            pickle.dump(self.scores, file)
    
    def read_scores(self):
        try:
            with open("Scores", "rb") as ficheroApertura:
                scores = pickle.load(ficheroApertura)
            return scores
        except FileNotFoundError:
            return []
        except pickle.UnpicklingError:
            print("Error al leer el archivo. Se creará uno nuevo.")
            return []