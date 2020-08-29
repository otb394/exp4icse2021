from multiprocessing import Pool
from release_runner import run

if __name__ == '__main__':
    with Pool(4) as p:
        p.map(run, range(5))
