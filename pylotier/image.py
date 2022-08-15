import cv2
import numpy as np
import os

import pylotier as plt

class ImageMaker:
    def __init__(self, name="out", path="outputs", save=False, video=False):
        self.name = name
        self.title = "Image"
        self.duration = 30

        self.save = save
        self.counter = 0

        self.path = path
        if not os.path.isdir(self.path):
            os.mkdir(self.path)
            os.mkdir(os.path.join(self.path, 'saved'))
        
        self.video = video
        if video:
            self.fourcc = cv2.VideoWriter_fourcc(*'X264')
            self.videowritter = None
            self.framerate = 15
            

    def combine(self, *args, mode=plt.NONE):
        if len(args) == 1:
            return args[0]
        elif mode is plt.NONE:
            for i, img in enumerate(args):
                # cv2.imshow(self.title + str(i), img)
                pass
        elif mode is plt.HORIZONTAL:
            return np.hstack(args)
        elif mode is plt.VERTICAL:
            return np.vstack(args)


    def show(self, *args, mode=plt.NONE, duration=-1):
        img = self.combine(*args, mode=mode)

        cv2.imshow(self.title, img)
        cv2.waitKey(duration if duration >= 0 else self.duration )
        if self.video:
            if self.videowritter is None:
                size = img.shape
                self.size = (size[1], size[0])
                self.videowritter = cv2.VideoWriter(os.path.join(self.path, self.name+'.mp4'),self.fourcc, self.framerate, self.size)
            self.videowritter.write(img)
        if self.save:
            cv2.imwrite(os.path.join(self.path, 'saved', self.name+f'_{self.counter:05}.png'), img)
        
        self.counter += 1
    

    def save(self, *args, mode=plt.NONE):
        img = self.combine(*args, mode=mode)
        cv2.imwrite(os.path.join(self.path, 'saved', self.name+f'_{self.counter:05}.png'), img)
        self.counter += 1


    def write(self, *args, mode=plt.NONE):
        img = self.combine(*args, mode=mode)
        if self.videowritter is None:
            size = img.shape
            self.size = (size[1], size[0])
            self.videowritter = cv2.VideoWriter(os.path.join(self.path, self.name+'.mp4'),self.fourcc, self.framerate, self.size)
        self.videowritter.write(img)
        
        self.counter += 1


    def __del__(self):
        if self.video and self.videowritter is not None:
            self.videowritter.release()
        cv2.destroyAllWindows()