import time
import multiprocessing


def factorize(*args):
    res = []
    for i in args:
        res.append(listing(i))


def optimized_factorize(*args):
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as cores:
        result = cores.map(func=listing, iterable=args)
    return result


def listing(num):
    return [i for i in range(1, num + 1) if num % i == 0]


if __name__ == "__main__":
    t1 = time.time()

    #print(factorize(128, 255, 99999, 10651060))

    print(optimized_factorize(128, 255, 99999, 10651060))

    t2 = time.time()

    print(t2 - t1)