from collections import Counter

time = []


def periods(tupla):
    
    if type(tupla[0]) != 'int' or type(tupla[1]) != 'int':
        return None
    for i in range(tupla[0], tupla[1] + 1):
        time.append(i)


def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    for i in permanence_period:
        if periods(i) == None:
            return None
        periods(i)

    most_common = Counter(time).most_common(1)
    print('AQUIII', most_common)

    return most_common

# study_schedule([(1,2),(3,8),(1,3),(2,2)],0)