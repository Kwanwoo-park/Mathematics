import random
'''
총합이 20이 될 때까지 주사위 굴리기
'''

target_score = 20


def roll():
    return random.randint(1, 6)


score = 0
num_rolls = 0

while score < target_score:
    die_roll = roll()
    num_rolls += 1
    print('Rolled: {0}'.format(die_roll))
    score += die_roll

print('Score of {0} reached in {1} rolls'.format(score, num_rolls))