import time
from without_cython import calculate_z_serial_purepython
import static_typing, with_numpy, dynamic_typing
import numpy as np

def calculate_cython_time(desired_width, max_iterations):
    x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
    c_real, c_imag = -0.62772, -.42193

    x_step = (x2 - x1) / desired_width
    y_step = (y1 - y2) / desired_width

    x = []
    y = []
    
    ycoord = y2
    while ycoord > y1:
        y.append(ycoord)
        ycoord += y_step
    
    xcoord = x1
    while xcoord < x2:
        x.append(xcoord)
        xcoord += x_step

    zs = []
    cs = []
    
    for ycoord in y:
        for xcoord in x:
            zs.append(complex(xcoord, ycoord))
            cs.append(complex(c_real, c_imag))

    start_time = time.time()
    output = calculate_z_serial_purepython(max_iterations, zs, cs)
    end_time = time.time()
    secs = end_time - start_time
    print("Without cython took", secs, "seconds")

    start_time = time.time()
    output = dynamic_typing.calculate_z(max_iterations, zs, cs)
    end_time = time.time()
    secs = end_time - start_time
    print("Dynamic typing took", secs, "seconds")

    start_time = time.time()
    output = static_typing.calculate_z(max_iterations, zs, cs)
    end_time = time.time()
    secs = end_time - start_time
    print("Static typing took", secs, "seconds")

    start_time = time.time()
    _zs = np.array(zs)
    _cs = np.array(cs)
    output = with_numpy.calculate_z(max_iterations, _zs, _cs)
    end_time = time.time()
    secs = end_time - start_time
    print("Static typing took", secs, "seconds")

    assert sum(output) == 33219980

if __name__ == "__main__":
    calculate_cython_time(desired_width=1000, max_iterations=300)