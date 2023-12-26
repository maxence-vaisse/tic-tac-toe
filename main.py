import tkinter as tk
from tkinter import messagebox # Pour afficher des messages d'erreur
from ia import ia # Importe la fonction ia() du fichier ia.py

fenetre = tk.Tk() # Crée la fenêtre
fenetre.title("Tic Tac Toe") # Donne un titre à la fenêtre

game_mode = tk.IntVar() # Variable qui contient le mode de jeu (0 = Joueur contre Joueur, 1 = Joueur contre IA)

def create_board(): # Fonction qui crée le plateau de jeu
    for i in range(3): # Pour chaque ligne
        for j in range(3): # Pour chaque colonne
            button = tk.Button(fenetre, text="", font=("Comic Sans MS", 50), height=1, width=4, bg="yellow", command=lambda row=i, col=j: handle_click(row, col)) # Crée un bouton
            button.grid(row=i, column=j, sticky="nsew") # Place le bouton dans la fenêtre

create_board() # Crée le plateau de jeu

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # Crée une liste qui contient le plateau de jeu
current_player = 1 # Variable qui contient le joueur actuel (1 = Joueur 1, 2 = Joueur 2)

def handle_click(row, col): # Fonction qui est appelée quand un joueur clique sur un bouton
    global current_player # Permet de modifier la variable current_player

    if board[row][col] == 0: # Si la case est vide
        if current_player == 1: # Si c'est au tour du joueur 1
            board[row][col] = "X" # Met un X dans la case
            current_player = 2 # Passe au joueur 2
        else: # Si c'est au tour du joueur 2
            board[row][col] = "O" # Met un O dans la case
            current_player = 1 # Passe au joueur 1

        button = fenetre.grid_slaves(row=row, column=col)[0] # Récupère le bouton qui a été cliqué
        button.config(text=board[row][col]) # Change le texte du bouton

        check_for_winner() # Vérifie si un joueur a gagné

        if not check_for_winner(): # Si personne n'a gagné
            if game_mode.get() == 1: # Si le mode de jeu est Joueur contre IA
                play_ia() # L'IA joue

def play_ia(): # Fonction qui fait jouer l'IA
    global current_player # Permet de modifier la variable current_player

    ia_move = ia(board, "O") # Récupère le coup que l'IA va jouer

    if ia_move is not False: # Si l'IA peut jouer
        row, col = divmod(ia_move, 3) # Convertit le coup de l'IA en coordonnées

        if board[row][col] == 0: # Si la case est vide
            board[row][col] = "O" # Met un O dans la case
            current_player = 1 # Passe au joueur 1

            button = fenetre.grid_slaves(row=row, column=col)[0] # Récupère le bouton qui a été cliqué
            button.config(text=board[row][col]) # Change le texte du bouton

            check_for_winner() # Vérifie si un joueur a gagné

def check_for_winner(): # Fonction qui vérifie si un joueur a gagné
    winner = None # Variable qui contient le joueur qui a gagné

    for row in board: # Pour chaque ligne
        if row.count(row[0]) == len(row) and row[0] != 0: # Si tous les éléments de la ligne sont identiques et différents de 0
            winner = row[0] # Le joueur qui a gagné est le premier élément de la ligne
            break # Arrête la boucle

    for col in range(len(board)): # Pour chaque colonne
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0: # Si tous les éléments de la colonne sont identiques et différents de 0
            winner = board[0][col] # Le joueur qui a gagné est le premier élément de la colonne
            break # Arrête la boucle

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0: # Si tous les éléments de la diagonale sont identiques et différents de 0
        winner = board[0][0] # Le joueur qui a gagné est le premier élément de la diagonale
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0: # Si tous les éléments de la diagonale sont identiques et différents de 0
        winner = board[0][2] # Le joueur qui a gagné est le premier élément de la diagonale

    if all([all(row) for row in board]) and winner is None: # Si toutes les cases sont remplies et qu'il n'y a pas de gagnant
        winner = "Egalité" # Il y a égalité

    if winner: # Si un joueur a gagné
        declare_winner(winner) # Affiche un message de fin de partie

def declare_winner(winner): # Fonction qui affiche un message de fin de partie
    if winner == "Egalité": # Si il y a égalité
        message = "Match nul ! " # Message de fin de partie
    else: # Si un joueur a gagné
        message = f"Joueur {winner} a gagné la partie ! " # Message de fin de partie

    answer = messagebox.askyesno("Fin de partie", message + "Voulez-vous relancer une partie ?") # Affiche un message de fin de partie et demande si on veut relancer une partie

    if answer: # Si on veut relancer une partie
        reset_board() # Réinitialise le plateau de jeu
    else: # Si on ne veut pas relancer une partie
        fenetre.quit() # Ferme la fenêtre

def reset_board(): # Fonction qui réinitialise le plateau de jeu
    global board, current_player # Permet de modifier les variables board et current_player
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # Réinitialise le plateau de jeu
    current_player = 1 # Réinitialise le joueur actuel

    for i in range(3): # Pour chaque ligne
        for j in range(3): # Pour chaque colonne
            button = fenetre.grid_slaves(row=i, column=j)[0] # Récupère le bouton
            button.config(text="") # Réinitialise le texte du bouton

def set_game_mode(mode): # Fonction qui change le mode de jeu
    game_mode.set(mode) # Change le mode de jeu
    reset_board() # Réinitialise le plateau de jeu

menu_bar = tk.Menu(fenetre) # Crée la barre de menu
fenetre.config(menu=menu_bar) # Ajoute la barre de menu à la fenêtre

options_menu = tk.Menu(menu_bar, tearoff=0) # Crée le menu Options
menu_bar.add_cascade(label="Options de jeu", menu=options_menu) # Ajoute le menu Options à la barre de menu

game_mode_menu = tk.Menu(options_menu, tearoff=0) # Crée le menu Mode de jeu
options_menu.add_cascade(label="Mode de jeu", menu=game_mode_menu) # Ajoute le menu Mode de jeu au menu Options

game_mode_menu.add_radiobutton(label="Joueur contre Joueur", variable=game_mode, value=0, command=lambda: set_game_mode(0)) # Ajoute un bouton radio au menu Mode de jeu
game_mode_menu.add_radiobutton(label="Joueur contre IA", variable=game_mode, value=1, command=lambda: set_game_mode(1)) # Ajoute un bouton radio au menu Mode de jeu

fenetre.mainloop() # Lance la fenêtre
