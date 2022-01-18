import multiprocessing
import os

def to_be_run():
    for i in range(100):
        print(i*i*i)


if __name__ == '__main__':
    processes = []
    num_processes = os.cpu_count()
    print(f'number of cores = {num_processes}')

# create processes
    for i in range(num_processes):
        p = multiprocessing.Process(target=to_be_run())
        processes.append(p)

# start
    for p in processes:
        p.start()

# block the main thread until all processes are done
    for p in processes:
        p.join()

    print('done')


