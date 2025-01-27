
x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -.42193

def calc_pure_python(desired_width, max_iterations):
    
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


   
    output = calculate_z_serial_purepython(max_iterations, zs, cs)
    assert sum(output) == 33219980

@profile
def calculate_z_serial_purepython(maxiter, zs, cs):

    output = [0] * len(zs)
    for i in range(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]
        
        while abs(z) < 2 and n < maxiter:
            z = z * z + c
            n += 1

        output[i] = n
    return output

if __name__ == "__main__":
 
    calc_pure_python(desired_width=1000, max_iterations=300)

    #kernprof -l -v julia_lineprofiler.py