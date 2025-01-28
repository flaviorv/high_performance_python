@profile
def calc_pure_python(desired_width, max_iterations):
    x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
    
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
  
    output = calculate_z_serial_purepython(max_iterations, x, y)
    assert sum(output) == 33219980


@profile
def calculate_z_serial_purepython(maxiter, x, y):
    c_real, c_imag = -0.62772, -.42193
    output = []
    for ycoord in y:
        for xcoord in x:
            z = complex(xcoord, ycoord)
            c = complex(c_real, c_imag)
            n = 0
            while n < maxiter and abs(z) < 2:
                z = z * z + c
                n += 1
            output.append(n)
    return output


if __name__ == "__main__":
 
    calc_pure_python(desired_width=1000, max_iterations=300)