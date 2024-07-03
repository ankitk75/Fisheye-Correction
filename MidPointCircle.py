import cv2
import numpy as np
import sys
from tqdm import tqdm

g_cClicks = 0
aPoints = []

SECONDS = 1000

def CallBackFunc(event, x, y, flags, param):
    global g_cClicks, aPoints
    if event == cv2.EVENT_LBUTTONDOWN:
        aPoints.append((x, y))
        g_cClicks += 1
        print(f"Point No. {g_cClicks} - position ({x}, {y})")

def PointMean(points):
    mean_x = sum(p[0] for p in points) / len(points)
    mean_y = sum(p[1] for p in points) / len(points)
    return mean_x, mean_y

def main():
    input_frame = cv2.imread('/Users/pranayjaju/Desktop/Coding/Python/FishEye/Photos/fisheye0.jpg')
    nHeight, nWidth = input_frame.shape[:2]
    
    if nHeight > 600:
        input_frame = cv2.resize(input_frame, (int(nWidth * 600 / nHeight), 600))
        nHeight, nWidth = input_frame.shape[:2]
    
    if input_frame is None:
        print("Error in loading input file")
        sys.exit(-1)

    temp_frame = input_frame.copy()
    cv2.imshow("Input Frame", temp_frame)

    cv2.setMouseCallback("Input Frame", CallBackFunc)

    print("\nPlease mark 12 points on the boundary of the circle\n\n")
    while len(aPoints) < 12:
        cv2.waitKey(250)
        for point in aPoints:
            cv2.drawMarker(temp_frame, point, (0, 0, 255), markerType=cv2.MARKER_CROSS, markerSize=10, thickness=2)
        cv2.imshow("Input Frame", temp_frame)

    mean_x, mean_y = PointMean(aPoints)
    
    A = np.array([[x, y, 1] for x, y in aPoints])
    B = np.array([-((x**2 + y**2)) for x, y in aPoints])

    C = np.linalg.lstsq(A, B, rcond=None)[0]

    A, B, C = C
    Cx = -A/2
    Cy = -B/2
    R = np.sqrt(Cx**2 + Cy**2 - C)

    print(f"Center = ({Cx}, {Cy}), Radius = {R}")
    
    # cv2.imwrite("people_οutput_crosses.jpg", temp_frame)
    cv2.circle(temp_frame, (int(Cx), int(Cy)), int(R), (0, 255, 0), 4)
    cv2.imshow("Input Frame", temp_frame)
    # cv2.imwrite("people_output_intermediate.jpg", temp_frame)
    cv2.waitKey(2 * SECONDS)

    print("Awaiting this to finish")
    
    transform_map_x = np.zeros((nHeight, nWidth), dtype=np.float32)
    transform_map_y = np.zeros((nHeight, nWidth), dtype=np.float32)    

    p_bar = tqdm(total=nWidth * nHeight)
    for u in range(nWidth):
        for v in range(nHeight):
            
            p_bar.update(1)
            
            xt = float(u - Cx)
            yt = float(v - Cy)
            if xt != 0:
                AO1 = (xt * xt + R * R) / (2.0 * xt)
                AB = np.sqrt(xt * xt + R * R)
                AP = yt
                PE = R - yt

                a = AP / PE
                b = 2.0 * np.arcsin(AB / (2.0 * AO1))

                alpha = a * b / (a + 1.0)
                x1 = xt - AO1 + AO1 * np.cos(alpha)
                y1 = AO1 * np.sin(alpha)
            else:
                x1 = xt
                y1 = yt
            
            transform_map_x[v, u] = x1 + Cx
            transform_map_y[v, u] = y1 + Cy
            
    p_bar.close()

    output_frame = cv2.remap(input_frame, transform_map_x, transform_map_y, cv2.INTER_CUBIC)

    # cv2.imwrite("people_output.jpg", output_frame)
    cv2.imshow("Output Frame", output_frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
