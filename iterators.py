import random
N = 10
[random.randint(1, 100) for i in range(N)]  # generate new list
(random.randint(1, 100) for i in range(N))  # create generator
{i: random.randint(1, 100) for i in range(N)} # create dict


def generator(N):
    for i in range(N):
        yield random.randint(1, 100)