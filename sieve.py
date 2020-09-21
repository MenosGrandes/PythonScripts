import logging
import math
import time

def timing(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        value = function(*args, **kwargs)
        end_time = time.time()
        logging.info(f"{function.__name__} took {end_time-start_time} ")
        return value
    return wrapper

@timing
def sieve_5(end):
    container = [False] * end
    for x in range(2, math.ceil(math.sqrt(end))):
        for y in range(x*2, end, x):
            container[y] = True
    return [i for i, x in enumerate(container) if x is False]


@timing
def sieve_4(end):
    y_to_remove = list(set(y for x in range(2, math.ceil(end/2 + 1))
                           for y in range(x+x, end, x)))  # indeksy do usuniecia
    return [n for n in range(end) if n not in y_to_remove]


@timing
def sieve_3(end):
    container = [x for x in range(end)]
    for x in range(2, math.ceil(end/2 + 1)):
        for y in range(x+x, end, x):
            if y in container:
                container.remove(y)
    return container


@timing
def sieve_2(end):
    container = [x for x in range(0, end)]
    for x in range(2, end):
        current_sieve = x
        while current_sieve+x < end:
            current_sieve += x
            if current_sieve in container:
                container.remove(current_sieve)
    return container


@timing
def sieve_1(end):
    container = [x for x in range(end)]
    for x in range(2, end):
        current_sieve = x
        while True:
            current_sieve += x
            if current_sieve > end:
                break
            if current_sieve in container:
                container.remove(current_sieve)
    return container


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    a = []
    a.extend([sieve_1, sieve_2, sieve_3, sieve_4, sieve_5])
    for x in range(100, 10000, 1000):
        logging.info(f"for {x}")
        res = [t(x) for t in a]
        if all(x == res[0] for x in res) is True:
            print("same")
        else:
            print("Differ")
            break
