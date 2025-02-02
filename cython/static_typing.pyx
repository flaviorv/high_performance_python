#cython: boundscheck=False

def calculate_z(maxiter, zs, cs):
    output = [0] * len(zs)

    cdef unsigned int i, n
    cdef double complex z, c

    for i in range(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]
        while n < maxiter and (z.real * z.real + z.imag * z.imag) < 4:
            z = z * z + c
            n += 1
        output[i] = n

    return output