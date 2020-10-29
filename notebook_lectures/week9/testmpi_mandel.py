
# file: mandelbrot-mpi.py
import numpy as np
from mpi4py import MPI
from matplotlib import pyplot as plt
from matplotlib import colors

def mandelbrot(c, maxit):
    z = c
    for n in range(maxit):
        if abs(z) > 2:
            return n
        z = z*z + c
    return 0


xmin,xmax = -2.0, 1.0
ymin,ymax = -1.0, 1.0
width,height = 320,200

maxit = 127

comm = MPI.COMM_WORLD
comm_size = comm.Get_size()
comm_rank = comm.Get_rank()

ncols = width // comm_size + (width % comm_size > comm_rank)
col_start = comm.scan(ncols) - ncols

xlin = np.linspace(xmin, xmax, width)
ylin = np.linspace(ymin, ymax, height)

C_local = np.empty((ncols,height), np.int64)

for w in range(ncols):
    for h in range(height):
        C_local[w, h] = mandelbrot(xlin[w+col_start] + 1j*ylin[h], maxit)

# Gather Results here
comm_gather_num = comm.gather(ncols, root=0)
C = None
if comm_rank == 0:
    C = np.empty((width,height), np.int64)
else:
    C = None
rowtype = MPI.INT64_T.Create_contiguous(height)
rowtype.Commit()

comm.Gatherv(sendbuf=[C_local, MPI.INT64_T],
        recvbuf=[C, (comm_gather_num, None), rowtype],
        root=0)
rowtype.Free()

if comm_rank == 0:
    fig, ax = plt.subplots(figsize=(7,7), dpi=72)
    plt.xticks([])
    plt.yticks([])
    #plt.title("[{xmin}, {ymin}] to [{xmax}, {ymax}]".format(**locals()))
    norm = colors.PowerNorm(0.3)
    ax.imshow(C,origin='lower', cmap='magma', norm=norm)
    #plt.imshow(C, aspect='equal')
    #plt.cm.spectral()
    plt.savefig("MandelParal.png")
    plt.show()
