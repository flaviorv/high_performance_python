import julia_set

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("julia_set.calc_pure_python(desired_width = 1000, max_iterations = 300)", setup="from __main__ import julia_set", number=3))


#to use in terminal
# -n is the number of loops and the -r is the repetitions

python3 -m timeit -n 5 -r 1 -s "import julia_set" "julia_set.calc_pure_python(desired_width=1000, max_iterations=300)"