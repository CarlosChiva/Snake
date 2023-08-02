import pickle

class Scores():
    scores = []
    def __init__(self):
        self.scores = self.read_scores()
    def write_score(self,new_score):
        self.scores.append(new_score)
        with open("Scores","wb") as file:
            pickle.dump(self.scores,file)
        del file
    def read_scores(self):
     try:
        with open("Scores", "rb") as ficheroApertura:
            lista_strings = pickle.load(ficheroApertura)
            lista_enteros = [int(num) for num in lista_strings]  # Convertir los strings a enteros
            list_score = sorted(lista_enteros)  # Ordenar los números enteros
        return list_score
     except:
        return []