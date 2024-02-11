# data = {'one': 'two', 'two': 'three', 'three': 'four', 'four': 'one'}
# x = data['three']
#
# for y in range(len(data)):
#     x = data[x]
#
# print(y)
#
#
# def mystery_function(lst):
#     if len(lst) == 0:
#         return []
#     if len(lst) == 1:
#         return lst
#     return mystery_function(lst[1:]) + [lst[0]]
#
#
# original_list = [1, 2, 3, 4, 5]
# result = mystery_function(original_list)
# print("Original list:", original_list)
# print("Result:", result)
#
# list = [[1, 2, 3, 4]]
# result = 1

# for i in range(1):
#     result *= 10
#     for j in range(1):
#         list[i][j] *= result
# print(list)

# for i in range(1):
#     print(i)
#     print('*', end="", sep='-')
# else:
#     print('*')

  #----------NE MODIFIEZ PAS LE CODE AU DESSUS DE CETTE LIGNE, IL SERA REINITIALISE LORS DE l'EXECUTION----------

# obj_list is already sorted
# def graph_matrix_to_list(m):
#     new_m = []
#     for i in range(len(m)):
#         for j in range(i):
#             print(m[i][j])
#             if m[i][j]:
#                 new_m.append(m[m.index(i)][m.index(j)])
#             else:
#                 continue
#     return []
#
# #----------NE MODIFIEZ PAS LE CODE EN DESSOUS DE CETTE LIGNE, IL SERA REINITIALISE LORS DE l'EXECUTION----------
#
# l = [[False, True, True], [ True, False, False], [ True, True, False]]
# print(graph_matrix_to_list(l))

# ----------NE MODIFIEZ PAS LE CODE AU DESSUS DE CETTE LIGNE, IL SERA REINITIALISE LORS DE l'EXECUTION----------
# class Color:
#
#     def __new__(cls, r, g, b):
#         # pour créer une nouvelle instance :
#         # color = super().__new__(cls)
#         rgb = (r,g,b)
#         return rgb


# ----------NE MODIFIEZ PAS LE CODE EN DESSOUS DE CETTE LIGNE, IL SERA REINITIALISE LORS DE l'EXECUTION----------

#
# color_bicycle1 = Color(255, 0, 0)
# color_bicycle2 = Color(255, 0, 0)
# color_bicycle3 = Color(0, 100, 200)
# print(color_bicycle1.rgb)  # doit être un tuple (255, 0, 0)
# print(color_bicycle1 is color_bicycle2)  # doit être True
# print(color_bicycle1 is color_bicycle3)  # doit être False
#

# def mex(in_list):
#     for i in in_list:
#         k = (min(sorted(in_list)) + 1)
#         if k not in in_list:
#             return k
#         else:
#             return i + 1
#
# print(mex([1, 3, 0, 4, 1]))

class Personne():
    def __init__(self, nom):
        self.nom = nom

    def vous_faites_quoi(self):
        return f"{self.nom} ne fait rien."

    def comment_vous_vous_appelez(self):
        return f"Je m'appelle {self.nom}."

#----------NE MODIFIEZ PAS LE CODE AU DESSUS DE CETTE LIGNE, IL SERA REINITIALISE LORS DE l'EXECUTION----------

# class Etudiant:
#     def __init__(self, nom):
#         super(Personne).__init__(nom)
#     def vous_faites_quoi(self):
#         return f"{self.nom}  fait son devoir."
#
#
# #----------NE MODIFIEZ PAS LE CODE EN DESSOUS DE CETTE LIGNE, IL SERA REINITIALISE LORS DE l'EXECUTION----------
#
# mary = Personne("Mary")
# mary.comment_vous_vous_appelez()
#
# betty = Etudiant("Betty")
# betty.comment_vous_vous_appelez()


# def sum_subset(N, L):
#     if N == sum(L)
#     print(sum(L))
#     return N == sum(L)
#
# print(sum_subset(4, [1 ,2, 3]))
# car `4==sum([1, 3])`.
# * `sum_subset(0, [23, 12])` doit renvoyer `True`.
# car `0==sum([])`
# * `sum_subset(7, [1, 2, 3, 8])` doit renvoyer `False`.
# * `sum_subset(3, [1, 1, 1, 1])` doit donner `True`.
# car `3==sum([1, 1, 1])`.
# * `sum_subset(6, [8, -3, 5, 1)` doit retourner `True`.
# (soit `[5, 1]` soit `[8, -3, 1]`)


ALL_USERS = []


# def register_user(first_name="", last_name="", birth_date=None, **extra_options):
#     ALL_USERS.append(dict(
#         first_name=first_name,
#         last_name=last_name,
#         birth_date=birth_date,
#         **extra_options
#     ))
#
#
# # ----------NE MODIFIEZ PAS LE CODE AU DESSUS DE CETTE LIGNE, IL SERA REINITIALISE LORS DE l'EXECUTION----------
#
# # Veuillez corriger ces appels de fonction ci-dessous :
#
# register_user("John", "Doe", "2001-01-02")
#
# register_user("Julie","Dupont", birth_date="2000-11-10", premium=True)
#
# register_user("1986-06-13", first_name="Julie", last_name="Dupont", premium=False)
#
# # ----------NE MODIFIEZ PAS LE CODE EN DESSOUS DE CETTE LIGNE, IL SERA REINITIALISE LORS DE l'EXECUTION----------


# def vérifier_liste(lst):
#     try:
#         if len(lst) == 2:
#             print(lst)
#         else:
#             lst = []
#             print(lst)
#     except
#
# lst = [1, 1]
#
# vérifier_liste(lst)

def sudoku_line(line):
    new_line = line[:]
    k = 0
    for i in range(1, 10):
        if i not in new_line:
            k = i
    for i in new_line:
        if i == -1:
            new_line[new_line.index(i)] = k
    return new_line

print(sudoku_line([1, 2, 3, 4, 5, -1, 7, 8, 9]))
