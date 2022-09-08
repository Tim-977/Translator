# from time import sleep
# import os
# 
# # line_1 = "You have woken up in a mysterious maze"
# # line_2 = "The building has 5 levels"
# # line_3 = "Scans show that the floors increase in size as you go down"
# # 
# # for x in line_1:
# #     print(x, end='')
# #     sleep(0.05)
# print('test test test')
# sleep(2)
# os.system(‘CLS’)
# input("CLEARED")

from os import system, name
from time import sleep
def clear():
   if name == 'nt':
      _ = system('cls')
print("Hi")
sleep(5)
clear()
print('CLEARED')
sleep(3)

