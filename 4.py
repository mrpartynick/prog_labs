from math import sqrt

carlos_dep_prob = float(input("Введите вероятность того, что Карлоса депортируют через 9 дней "))
rodr_dep_prob = float(input("Введите вероятность того, что Родригеса депортируют через 9 дней "))
sant_dep_prob = float(input("Введите вероятность того, что Сантьяго депортируют через 9 дней "))

carlos_prob_for_all_time = (1-carlos_dep_prob)**(1/9)
rodr_prob_for_all_time = (1-rodr_dep_prob)**(1/9)
sant_prob_for_all_time = (1-sant_dep_prob)**(1/9)

result = (carlos_prob_for_all_time**309) * (1 - rodr_prob_for_all_time**309) * (1 - sant_prob_for_all_time**309)

print(result)