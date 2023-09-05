from .Game import Game
from .principal import Principal
from .view_score import ViewScore
from .load_games_view import Load_games_view
class Windows_provider():
    def __init__(self,root):
        self.root = root
        principal = Principal(self.root,self.change_windows)    
    def principal_window(self):
        principal = Principal(self.root,self.change_windows)    
    def game_window(self):
        game = Game(self.root,self.change_windows)
    def score_window(self):
        view_score = ViewScore(self.root,self.change_windows) 
    def load_game(self):
        view_score = Load_games_view(self.root,self.load_game_loaded) 
    def load_game_loaded(self,table):
        game = Game(self.root,self.change_windows,table=table)        
    def change_windows(self,name_window,table=None):
        match name_window:
                case "principal":
                    self.principal_window()
                case "game":
                    self.game_window()
                case "score":
                    self.score_window() 
                case "load_game":
                    self.load_game()