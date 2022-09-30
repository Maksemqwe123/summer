"""КТО + КОТ = ТОК, старшая буква не равна 0"""
# K = 1
# O = 5
# T = 9
#
# KTO = str(K) + str(T) + str(O)
# KOT = str(K) + str(O) + str(T)
# TOK = str(T) + str(O) + str(K)
#
# if int(KTO) + int(KOT) == int(TOK):
#     print(f'Ребус решён и его ответ {int(TOK)}')
#
# elif int(KTO) + int(KOT) != int(TOK):
#     print(int(KTO) + int(KOT))
#     print(int(TOK))
#     print('нет решений')


# class Rebus:
#     def __init__(self, K: str, O: str, T: str):
#         self.K = K
#         self.O = O
#         self.T = T
#
#     def solution(self, KTO: int, KOT: int, TOK: int):
#         self.KTO = KTO == self.K + self.T + self.O
#         self.KOT = KOT == self.K + self.O + self.T
#         self.TOK = TOK == self.T + self.O + self.K
#
#         if KTO + KOT == TOK:
#             print('ребус решён')
#         elif KTO + KOT != TOK:
#             print(KTO + KOT)
#             print(TOK)
#             print('нет решений')
#
#
# End_Rebus = Rebus('1', '5', '9')
# End_Rebus.solution(195, 159, 951)
