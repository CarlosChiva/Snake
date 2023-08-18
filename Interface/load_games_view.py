import tkinter
from save_load_game import Save_load_game
from Game import Game

class Load_games_view():
    root:tkinter
    def __init__(self, root):
        self.root = root 
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        # main frame
        self.main_frame = tkinter.Frame(self.root, bg="green")
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        # Configurar cómo las filas y columnas dentro de main_frame se expanden
        self.main_frame.grid_rowconfigure(0, weight=0)  # No necesitamos que la primera fila dentro de main_frame expanda
        self.main_frame.grid_rowconfigure(1, weight=1)  # Queremos que la segunda fila dentro de main_frame expanda
        self.main_frame.grid_columnconfigure(0, weight=1)
        
        
        self.etiqueta_titulo = tkinter.Label(self.main_frame, text="Games", font=("Helvetica", 16, "bold"),bg="green")
        self.etiqueta_titulo.grid(row=0, column=0, columnspan=2, pady=20,sticky="n")
        self.lista_scores = tkinter.Listbox(self.main_frame, font=("Helvetica", 12), width=30)
        self.lista_scores.grid(row=1, column=0, columnspan=2, padx=10, pady=100,sticky="n")
        self.lista_scores.config(justify=tkinter.CENTER)
        self.games = Save_load_game()
        self.list_games= self.games.get_scores()
        for index,value in enumerate(self.list_games.values()):
            user_index = index +1
            self.lista_scores.insert(tkinter.END,f"{user_index}---{value}")
        self.lista_scores.bind("<Button-1>",self.print_selection)
    def print_selection(self,event):    
        selected_index = self.lista_scores.nearest(event.y)
        self.load_selected_game(self.games.list_of_games[selected_index])
        #selected_item = self.lista_scores.get(selected_index)
        #print(f"index:---{selected_index} item:----{selected_item}")
    def load_selected_game(self,table):
        game = Game(self.root,table)            