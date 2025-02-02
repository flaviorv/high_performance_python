import julia_set

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("julia_set.calc_pure_python(desired_width = 1000, max_iterations = 300)", setup="from __main__ import julia_set", number=3))


#uses in terminal

#with timeit
#-n is the number of loops and the -r is the repetitions
#python3 -m timeit -v -n 5 -r 1 -s "import julia_set" "julia_set.calc_pure_python(desired_width=1000, max_iterations=300)"

#with os
#obs: diff between user and sys (or only real) might tell about system is busy with other things
#/usr/bin/time --verbose python3 julia_set.py

#with cProfile
#-s cumulative is a sort by cumulative time
#python -m cProfile -s cumulative julia1_set.py

#with pstats module
#import, use the options and print in the source code
#python3 -m cProfile -o profile.stats julia_set.py

#with snakeviz to generate a chart
#python3 -m cProfile -o chart julia_set.py
#snakeviz chart