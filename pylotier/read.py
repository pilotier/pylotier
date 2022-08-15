import cv2
import os
from glob import glob

import pylotier.types.opticalflow as ofl

def read_exr(file):
    return cv2.imread(file,  cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)


def flow(file):
    if file.endswith('.exr'):
        os.environ["OPENCV_IO_ENABLE_OPENEXR"]="1"
        img = read_exr(file)
    else:
        img = cv2.imread(file)
    
    flow = img[:,:,1:]
    flow[:,:,1] *= -1 # flip y

    return flow


def flow_to_color(flow):
    return ofl.flow_to_image(flow)


def depth(file):
    depth = cv2.imread(file, cv2.IMREAD_ANYDEPTH)
    return depth


def image(file):
    img = cv2.imread(file)
    return img


def dir(folder, pattern="*"):
    imgs = sorted(glob(os.path.join(folder, pattern)))
    return imgs