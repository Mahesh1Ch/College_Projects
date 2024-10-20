##
import numpy as np
import os
import cv2
import scipy.io

from get_density_map_gaussian import get_density_map_gaussian
from get_dot_map import get_dot_map
from tqdm import tqdm

init_maxSize = np.array([1280,1280])
minSize = np.array([576,768])
path = os.getcwd()
output_path = os.getcwd() + '/data/min_' + str(minSize[0]) + 'x' + str(minSize[1]) + '_mod16_2048/'

save_type = np.array([1,0,1,0])

try:
    os.mkdir(output_path)
except Exception as e:
    print(e)

try:
    path_img =output_path + '/img/'
    os.mkdir(path_img)
except Exception as e:
    print(e)

try:
    path_den = output_path + '/den/'
    os.mkdir(path_den)
except Exception as e:
    print(e)

try:
    path_dot = output_path + '/dot/'
    os.mkdir(path_dot)
except Exception as e:
    print(e)

try:
    path_vis = output_path + '/vis/'
    os.mkdir(path_vis)
except Exception as e:
    print(e)


img_list = os.listdir(os.path.join(path, 'images' ))


i_img = 0
for i_img in tqdm(range(len(img_list))):
    img_name = img_list[i_img]
    name_split = img_name.split('.')
    mat_name = name_split[0] +'.mat'
    im = cv2.imread(path + '/images/' + img_name)
    h,w,c = im.shape
    ## resize and save img
    rate = init_maxSize[0] / h
    rate_w = w * rate
    if rate_w > init_maxSize[1]:
        rate = init_maxSize[1] / w
    tmp_h = int(h * rate / 16) * 16
    if tmp_h < minSize[0]:
        rate = minSize[0] / h
    tmp_w = int(w * rate / 16) * 16
    if tmp_w < minSize[1]:
        rate = minSize[1] / w
    tmp_h = int(h * rate / 16) * 16
    tmp_w = int(w * rate / 16) * 16
    rate_h = np.longdouble(tmp_h) / h
    rate_w = np.longdouble(tmp_w) / w
    im = cv2.resize(im, (tmp_h,tmp_w))
    if save_type[0] == 1:
        cv2.imwrite(path_img + img_name, im )
    if not os.path.exists(str(path + '/mats/' + mat_name)) :
        continue
    ## load mat
    annPoints = scipy.io.loadmat(path + '/mats/' + mat_name)['annBoxes']

    if not len(annPoints)==0 :
        annPoints[:,0] = annPoints[:,0] * np.double(rate_w)
        annPoints[:,1] = annPoints[:,1] * np.double(rate_h)
        check_list = np.ones((annPoints.shape[1-1],1))
        for j in np.arange(0,annPoints.shape[1-1]).reshape(-1):
            x = np.ceil(annPoints[j,0])
            y = np.ceil(annPoints[j,1])
            if (x > tmp_w or y > tmp_h or x <= 0 or y <= 0):
                check_list[j] = 0


        annPoints = annPoints[[bool(x[0]) for x in check_list],:]
    ## gen & save labels
    if save_type[1] == 1:
        ## density generation
        im_density = get_density_map_gaussian(im,annPoints,15,4)
        csvwrite(strcat(path_den,name_split[0],'.csv'),im_density)
    if save_type[2] == 1:
        ## dot generation

        im_dots = get_dot_map(im,annPoints)
        im_dots = np.asarray(im_dots, dtype=np.int32)
        cv2.imwrite(path_dot + name_split[0] + '.png', im_dots)
    if save_type[3] == 1:
        ## visualization
        if not len(annPoints)==0 :
            imRGB = insertShape(im,'FilledCircle',np.array([annPoints[:,1],annPoints[:,2],5 * np.ones((annPoints[:,1].shape,annPoints[:,1].shape))]),'Color',np.array(['red']))
        else:
            imRGB = im
        imwrite(imRGB,strcat(path_vis,name_split[0],'.jpg'))
