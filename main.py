import os
import nympy as py

def main():
    name = os.getenv('INPUT_NAME', 'World')
    greeting = f"Hello, {name}"
    with open(os.getenv('GITHUB_OUTPUT'), 'a') as output_file:
        output_file.write(f"greeting={greeting}\n")
        
if __main__== "__main__":
    main()
                          

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

resoudre_sudoku(matrice)