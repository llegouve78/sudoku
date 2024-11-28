import os
import numpy as np
import ast

def est_valide(matrice, i, j, k):
    bloc_x, bloc_y = 3 * (i // 3), 3 * (j // 3)
    return (
        k not in matrice[i, :]  # Vérifie la ligne
        and k not in matrice[:, j]  # Vérifie la colonne
        and k not in matrice[bloc_x:bloc_x+3, bloc_y:bloc_y+3]  # Vérifie le bloc 3x3
    )

# Résolution par backtracking
def resoudre_sudoku(matrice):
    for i in range(9):
        for j in range(9):
            if matrice[i, j] == 0:  # Trouver une case vide
                for k in range(1, 10):  # Essayer tous les chiffres de 1 à 9
                    if est_valide(matrice, i, j, k):
                        matrice[i, j] = k  # Placer le chiffre
                        if resoudre_sudoku(matrice):  # Appel récursif
                            return True
                        matrice[i, j] = 0  # Annuler le choix (backtrack)
                return False  # Aucune solution possible pour cette case
    return True  


def main():
    name = os.getenv('MY_SUDOKU', '000')
    print(f"MY_IN={name}\n")
    
    result = [[int(char) for char in name[i:i+9]] for i in range(0, len(name) - 1, 9)]

    #list_array = ast.literal_eval(result)
    #print(f"MY_RES={list_array}\n")
    
  
    
    matrice = np.array(result)
    #greeting = f"Source, \n{matrice}"
    #print(greeting)
    
    resoudre_sudoku(matrice)

    
    print(f"MY_OUTPUT={str(matrice).replace("'","").replace("[","").replace("]","").replace("\n","")}\n")
    #print(greeting)
    

        
if __name__ == "__main__":
    main()                          

