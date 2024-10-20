import numpy as np
    
def fspecial(size, sigma):
     m,n = size
     h, k = m//2, n//2
     x, y = np.mgrid[-h:h, -k:k]


def get_density_map_gaussian(im = None,points = None,k_size = None,sigma = None): 
    im_density = np.zeros((im.shape[1-1],im.shape[2-1]))
    h,w = im_density.shape
    if (len(points) == 0):
        return im_density
    
    #     GJY
# if(length(points(:,1))==1)
#     x1 = max(1,min(w,round(points(1,1))));
#     y1 = max(1,min(h,round(points(1,2))));
    
    #     im_density(y1,x1) = 255;
#     return;
# end
    for j in np.arange(1,points.shape[1-1]+1).reshape(-1):
        f_sz = k_size
        #     sigma = 4.0;
        H = fspecial(np.array([f_sz,f_sz]),sigma)
        x = np.amin(w,np.amax(1,np.abs(int(int(np.floor(points[j,1]))))))
        y = np.amin(h,np.amax(1,np.abs(int(int(np.floor(points[j,2]))))))
        if (x > w or y > h):
            continue
        x1 = x - int32(int(np.floor(f_sz / 2)))
        y1 = y - int32(int(np.floor(f_sz / 2)))
        x2 = x + int32(int(np.floor(f_sz / 2)))
        y2 = y + int32(int(np.floor(f_sz / 2)))
        dfx1 = 0
        dfy1 = 0
        dfx2 = 0
        dfy2 = 0
        change_H = False
        if (x1 < 1):
            dfx1 = np.abs(x1) + 1
            x1 = 1
            change_H = True
        if (y1 < 1):
            dfy1 = np.abs(y1) + 1
            y1 = 1
            change_H = True
        if (x2 > w):
            dfx2 = x2 - w
            x2 = w
            change_H = True
        if (y2 > h):
            dfy2 = y2 - h
            y2 = h
            change_H = True
        x1h = 1 + dfx1
        y1h = 1 + dfy1
        x2h = f_sz - dfx2
        y2h = f_sz - dfy2
        if (change_H == True):
            H = fspecial(np.array([double(y2h - y1h + 1),double(x2h - x1h + 1)]),sigma)
            xxx = 1
        im_density[np.arange[y1,y2+1],np.arange[x1,x2+1]] = im_density(np.arange(y1,y2+1),np.arange(x1,x2+1)) + H
    
    return im_density
    
    return im_density