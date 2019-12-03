import numpy as np
import emailto

def risingegde(m1,m2):
    m = np.bitwise_xor(m1,m2)
    x = 0
    y = 0
    for row in m:
        for col in row:
            if col == 1:
                if (m1[x][y]) == 0 & (m2 [x][y] == 1):
                    emailto.emailto(x,y)
            y += 1    
        x += 1
        y = 0       