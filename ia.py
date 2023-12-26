import random # Pour le choix aléatoire de la position de l'IA

def ia(board, signe): # Fonction qui fait jouer l'IA
    for i in range(3): # Pour chaque ligne et chaque colonne
        if board[i][0] == board[i][1] == signe and board[i][2] == 0: # Si les deux premiers éléments de la ligne sont identiques et différents de 0
            return 3 * i + 2 # Retourne la position de la case vide
        elif board[i][0] == board[i][2] == signe and board[i][1] == 0: # Si le premier et le dernier élément de la ligne sont identiques et différents de 0
            return 3 * i + 1 # Retourne la position de la case vide
        elif board[i][1] == board[i][2] == signe and board[i][0] == 0: # Si les deux derniers éléments de la ligne sont identiques et différents de 0
            return 3 * i # Retourne la position de la case vide

        if board[0][i] == board[1][i] == signe and board[2][i] == 0: # Si les deux premiers éléments de la colonne sont identiques et différents de 0
            return 6 + i # Retourne la position de la case vide
        elif board[0][i] == board[2][i] == signe and board[1][i] == 0: # Si le premier et le dernier élément de la colonne sont identiques et différents de 0
            return 3 + i # Retourne la position de la case vide
        elif board[1][i] == board[2][i] == signe and board[0][i] == 0: # Si les deux derniers éléments de la colonne sont identiques et différents de 0
            return i # Retourne la position de la case vide

    if board[0][0] == board[1][1] == signe and board[2][2] == 0: # Si les deux premiers éléments de la diagonale sont identiques et différents de 0
        return 8 # Retourne la position de la case vide
    elif board[0][0] == board[2][2] == signe and board[1][1] == 0: # Si le premier et le dernier élément de la diagonale sont identiques et différents de 0
        return 4 # Retourne la position de la case vide
    elif board[1][1] == board[2][2] == signe and board[0][0] == 0: # Si les deux derniers éléments de la diagonale sont identiques et différents de 0
        return 0 # Retourne la position de la case vide

    if board[0][2] == board[1][1] == signe and board[2][0] == 0: # Si les deux premiers éléments de la diagonale sont identiques et différents de 0
        return 6 # Retourne la position de la case vide
    elif board[0][2] == board[2][0] == signe and board[1][1] == 0: # Si le premier et le dernier élément de la diagonale sont identiques et différents de 0
        return 4 # Retourne la position de la case vide
    elif board[1][1] == board[2][0] == signe and board[0][2] == 0: # Si les deux derniers éléments de la diagonale sont identiques et différents de 0
        return 2 # Retourne la position de la case vide

    opponent_signe = "X" if signe == "O" else "O" # Récupère le signe de l'adversaire
    for i in range(3): # Pour chaque ligne et chaque colonne
        if board[i][0] == board[i][1] == opponent_signe and board[i][2] == 0: # Si les deux premiers éléments de la ligne sont identiques et différents de 0
            return 3 * i + 2 # Retourne la position de la case vide
        elif board[i][0] == board[i][2] == opponent_signe and board[i][1] == 0: # Si le premier et le dernier élément de la ligne sont identiques et différents de 0
            return 3 * i + 1 # Retourne la position de la case vide
        elif board[i][1] == board[i][2] == opponent_signe and board[i][0] == 0: # Si les deux derniers éléments de la ligne sont identiques et différents de 0
            return 3 * i # Retourne la position de la case vide

        if board[0][i] == board[1][i] == opponent_signe and board[2][i] == 0: # Si les deux premiers éléments de la colonne sont identiques et différents de 0
            return 6 + i # Retourne la position de la case vide
        elif board[0][i] == board[2][i] == opponent_signe and board[1][i] == 0: # Si le premier et le dernier élément de la colonne sont identiques et différents de 0
            return 3 + i # Retourne la position de la case vide
        elif board[1][i] == board[2][i] == opponent_signe and board[0][i] == 0: # Si les deux derniers éléments de la colonne sont identiques et différents de 0
            return i # Retourne la position de la case vide

    if board[0][0] == board[1][1] == opponent_signe and board[2][2] == 0: # Si les deux premiers éléments de la diagonale sont identiques et différents de 0
        return 8 # Retourne la position de la case vide
    elif board[0][0] == board[2][2] == opponent_signe and board[1][1] == 0: # Si le premier et le dernier élément de la diagonale sont identiques et différents de 0
        return 4 # Retourne la position de la case vide
    elif board[1][1] == board[2][2] == opponent_signe and board[0][0] == 0: # Si les deux derniers éléments de la diagonale sont identiques et différents de 0
        return 0 # Retourne la position de la case vide

    if board[0][2] == board[1][1] == opponent_signe and board[2][0] == 0: # Si les deux premiers éléments de la diagonale sont identiques et différents de 0
        return 6 # Retourne la position de la case vide
    elif board[0][2] == board[2][0] == opponent_signe and board[1][1] == 0: # Si le premier et le dernier élément de la diagonale sont identiques et différents de 0
        return 4 # Retourne la position de la case vide
    elif board[1][1] == board[2][0] == opponent_signe and board[0][2] == 0: # Si les deux derniers éléments de la diagonale sont identiques et différents de 0
        return 2 # Retourne la position de la case vide

    empty_positions = [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0] # Récupère les positions des cases vides
    if empty_positions: # Si il y a des cases vides
        return 3 * random.choice(empty_positions[0]) + random.choice(empty_positions[1]) # Retourne une position aléatoire

    return False # Retourne False si il n'y a plus de cases vides
