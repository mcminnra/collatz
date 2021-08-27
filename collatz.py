#!/usr/bin/env python3

import argparse
from timeit import default_timer as timer


def collatz(n):

    intial_num = n
    series = [n]
    iter = 1

    while(n>1):
        if n % 2 == 0:
            n = int(n/2)
            series.append(n)
            iter += 1
        elif n % 2 == 1:
            n = int(3*n+1)
            series.append(n)
            iter += 1
        else:
            print('Error')
    
    return intial_num, series, iter
    

if __name__ == '__main__':
    # Arg Parsers
    parser = argparse.ArgumentParser(description='Test the Collatz Conjecture')
    parser.add_argument(
        'num',
        nargs='?',
        metavar='n',
        type=int,
        help='Test Collatz on single integer.'
    )
    parser.add_argument(
        '-r',
        '--range',
        nargs=2,
        metavar=('start_num', 'end_num'),
        type=int,
        help='Test Collatz on a range of integers.',
    )
    args = parser.parse_args()

    if args.range:
        start_num = args.range[0]
        end_num = args.range[1]

        total_time = 0
        most_iter = 0
        most_iter_num = 0
        
        for num in range(start_num, end_num+1):
            start_time = timer()
            initial_num, series, iter = collatz(num)
            end_time = timer()
            time_elapsed = end_time-start_time

            total_time += time_elapsed
            if iter > most_iter:
                most_iter = iter
                most_iter_num = initial_num

            print(f'{initial_num} => {iter} iterations [{time_elapsed}]')

        # Run stats
        print(f'Total Time: {total_time}')
        print(f'Num. with Most Iterations: {most_iter_num} ({most_iter})')

    elif args.num:
        num = args.num

        start_time = timer()
        initial_num, series, iter = collatz(num)
        end_time = timer()
        time_elapsed = end_time-start_time

        print(f'{initial_num} => {iter} iterations [{time_elapsed}]')

    else:
        print('Provide an int or use --range to test a range of ints.')