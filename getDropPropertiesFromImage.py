import pyDSA_core as dsa
import matplotlib.pyplot as plt
import os
import imageio
# Import an image
import numpy as np
import cv2
from PIL import Image
def GetParametersFromImage(resolution):
    print("---------------------------------------------------------------------------------------------")
    print(resolution)
    # resolution = resolution*10
    print(resolution)
    # src = Image.open("static/uploads/droplet.jpg")
    src = cv2.imread("static/uploads/droplet.jpg")
    img = cv2.rotate(src, cv2.ROTATE_180)
    # img = src.rotate(180)
    # img.save("static/uploads/rotated_droplet.jpg")
    cv2.imwrite("static/uploads/rotated_droplet.jpg",img)
    print("----------------------------------------------------------------------------------------------")
    im = dsa.import_from_image('static/uploads/rotated_droplet.jpg', dx=1/resolution, dy=1/resolution, unit_x='mm', unit_y='mm')
    # Display it
    # plt.figure()
    # im.display()
    # plt.show()
    im.set_baseline(pt1=[2, 2.4/resolution], pt2=[4.5, 2.4/resolution])
    edge = im.edge_detection()
    
    edge_cont = im.edge_detection()
    
    edge_cont = im.edge_detection_contour(level=.15)
    # plt.figure()
    # im.display()
    # edge_cont.display()
    # plt.show()
    sfit = edge_cont.fit_spline()
    # plt.figure()
    # im.display()
    # plt.show()
    sfit.compute_contact_angle()
    print('Contact angles: {}'.format(sfit.thetas))
    c_angles = [sfit.thetas[0], 180-sfit.thetas[1]]
    radius = sfit.get_base_diameter()

    # plt.figure()
    # im.display()
    # sfit.display()
    # plt.show()

    print("\n=== Drop base diameter: ===")
    print(radius)

    height = sfit.get_drop_height()
    print("\n=== Drop height: ===")
    print(height)

    volume = sfit.get_drop_volume()
    print("\n=== Drop Volume: ===")
    print(volume)

    result = {"contactAngle": c_angles, "radius": (radius)/2,
              "height": height, "volume": volume}

    
    os.remove("static/uploads/rotated_droplet.info")
    image = imageio.imread('droplet.jpg')
    # plt.figure()
    # plt.imshow(image)
    # plt.colorbar()
    # plt.show()
    thres1 = image.min()
    thres2 = image.max()
    edges = cv2.Canny(image, thres1, thres2)
    # plt.figure()
    # plt.imshow(edges)
    ys, xs = np.where(edges)
    # print(ys,xs)
    y_max = np.max(ys)
    y_min = np.min(ys)
    height = y_max-y_min
    print("-------------------------------")
    print(height/resolution-0.2)
        

    return result

# GetParametersFromImage(120)