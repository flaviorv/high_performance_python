import time
from functools import wraps
import pstats

p = pstats.Stats("profile.stats")
p.sort_stats("cumulative")
p.print_stats()

def timefn(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print(f"@timefn: {fn.__name__} took {t2 - t1} seconds")
        return result
    return measure_time


# area of complex space to investigate
x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -.42193

def calc_pure_python(desired_width, max_iterations):
    """Create a list of complex coordinates (zs) and complex parameters (cs),
    build Julia set"""
    
    x_step = (x2 - x1) / desired_width
    print(f"x2 {x2} - x1 {x1} / {desired_width}  = {x_step}")
    y_step = (y1 - y2) / desired_width
    print(f"y1 {y1} - y2 {y2} / {desired_width}  = {y_step}")
    x = []
    y = []
    ycoord = y2
    # print(f"ycoord = {ycoord}")
    while ycoord > y1:
        # print(f"ycoord {ycoord} is greater than y1 {y1}")
        y.append(ycoord)
        # print(f"ycoord = ycoord {ycoord} + y_step {y_step}")
        ycoord += y_step
        # print(f"ycoord = {ycoord}")
    xcoord = x1
    # print(f"xcoord = {xcoord}")
    while xcoord < x2:
        # print(f"xcoord is lower than x2 {x2}")
        x.append(xcoord)
        # print(f"xcoord = xcoord {xcoord} + x_step {x_step}")
        xcoord += x_step
        # print(f"xcoord = {xcoord}")
    # build a list of coordinates and the initial condition for each cell.
    # Note that our initial condition is a constant and could easily be removed,
    # we use it to simulate a real-world scenario with several inputs to our
    # function
    zs = []
    cs = []
    for ycoord in y:
        for xcoord in x:
            zs.append(complex(xcoord, ycoord))
            cs.append(complex(c_real, c_imag))

    # print("Length of x:", len(x))
    # print("Total elements:", len(zs))
    start_time = time.time()
    output = calculate_z_serial_purepython(max_iterations, zs, cs)
    end_time = time.time()
    secs = end_time - start_time
    print(calculate_z_serial_purepython.__name__ + " took", secs, "seconds")

    # This sum is expected for a 1000^2 grid with 300 iterations
    # It ensures that our code evolves exactly as we'd intended
    assert sum(output) == 33219980

@timefn
def calculate_z_serial_purepython(maxiter, zs, cs):
    """Calculate output list using Julia update rule"""
    output = [0] * len(zs)
    for i in range(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]
        
        while abs(z) < 2 and n < maxiter:
            # print(f"z = {z} c = {c} z*z+c = {z*z+c}")
            z = z * z + c
            # print(z)
            
            n += 1
            # print(f"Position: {i} Iteration: {n} Magnitude: {abs(z)}")

        output[i] = n
    return output

if __name__ == "__main__":
    # Calculate the Julia set using a pure Python solution with
    # reasonable defaults for a laptop
    calc_pure_python(desired_width=1000, max_iterations=300)