import numpy as np
    
def get_dot_map(im = None,points = None): 
    dot_map = np.zeros((im.shape[0],im.shape[1]))
    h,w = dot_map.shape
    if (len(points) == 0):
        return dot_map
    
    points = np.asarray(points, dtype=np.int32)
    for i_dot in range(0, points.shape[0]):
        
        x = points[i_dot,0]
        y = points[i_dot,1]
        if (x >= w or y >= h or x < 0 or y < 0):
            continue

        dot_map[y,x] = dot_map[y,x] + 1



    return dot_map
    
    return dot_map