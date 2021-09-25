import random


t = [
"""
 * 
""", """
 *
   * 
""", """
 *
  *
   * 
""", """
 * *
 * *
""", """
* *
 *
* *
""", """
 * * *
 * * * 
 """
]
s = 'На кубике выпало:'


def toss_coin():
    toss = random.sample(range(0, 2), k=1)[0]
    if toss == 0:
        print('На монетке выпала: решка')
    else:
        print('На монетке выпал: орел')


def toss_cube():
    toss = random.sample(range(0, 6), k=1)[0]
    print('На кубике выпало:', t[toss])


toss_coin()

toss_cube()
