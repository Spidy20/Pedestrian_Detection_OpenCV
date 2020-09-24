import cv2
from Human_Detection import Detector

cap = cv2.VideoCapture('./testing/t3.mp4')
# size = (800, int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# # size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# print(size)
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 'x264' doesn't work
# out = cv2.VideoWriter('./testing/res_t2.mp4',fourcc, 20.0,(980,498))  # 'False' for 1-ch instead of 3-ch for color

while True:
    ret, frame = cap.read()
    # frame = cv2.resize(frame,(980,498))
    # frame = imutils.resize(frame, width=800)
    frame = Detector(frame)
    # out.write(frame)
    # cv2.resizeWindow('Car Detection System', 600, 600)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()