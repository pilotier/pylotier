import pylotier as plt
import pylotier.read as read
from pylotier.image import ImageMaker

imgs = read.dir("/Users/ibrahim/Projects/tools/data/OFTEST", "GAP_Cine_Left.FinalImageM_BAOpticalFlow_Dynamic.*.exr")

viewer = ImageMaker(video=False, save=False)
for file in imgs:
    flow = read.flow(file)
    img = read.flow_to_color(flow)
    viewer.show(img, duration=30, mode=plt.HORIZONTAL)