import cv2
import numpy as np
import math

fisheye_image = cv2.imread('image/fe1.jpg')

height, width = fisheye_image.shape[:2]
transform_map_x = np.zeros((height, width), dtype=np.float32)
transform_map_y = np.zeros((height, width), dtype=np.float32)

Cx = width // 2
Cy = height // 2
F = width / math.pi

for v in range(height):
    for u in range(width):
        
        xt = u
        yt = v - Cy
        r = width / math.pi
        alpha = (width - xt) / r
        xp = r * math.cos(alpha)
        yp = yt
        zp = r * math.fabs(math.sin(alpha))
        rp = math.sqrt(xp ** 2 + yp ** 2)
        theta = math.atan2(rp, zp)
        x1 = F * theta * xp / rp
        y1 = F * theta * yp / rp
        transform_map_x[v, u] = x1 + Cx
        transform_map_y[v, u] = y1 + Cy

corrected_image = cv2.remap(fisheye_image, transform_map_x, transform_map_y, cv2.INTER_CUBIC)

cv2.imshow('Fisheye Image', fisheye_image)
cv2.imshow('Corrected Image',corrected_image)
cv2.imwrite('output_hemi_cylinder.jpg', corrected_image)
cv2.waitKey(0)