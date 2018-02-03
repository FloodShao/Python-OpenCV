import cv2

def get_image(cap):
    retval, im = cap.read()
    return im

if __name__ == "__main__":

    cap = cv2.VideoCapture(0)
    num = 0

    while(1):

        im = get_image(cap)

        cv2.imshow("show", im)
        cv2.imwrite("../data/capture_images_" + str(num) + ".jpg", im)

        num += 1
        cv2.waitKey(30)

