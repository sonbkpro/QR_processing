"""
Author: PHAN HONG SON
Univ: SungKuynKwan University
"""
import cv2

def readQR(file):
    """
    :param file: image get from frame
    :return: value of QR  code
    """
    try:
        print('Call readQR function')
        # img = cv2.imread(file)
        detect = cv2.QRCodeDetector()
        value, points, straight_qrcode = detect.detectAndDecode(file)
        print('This is QR value: ', value)
        return value
    except:
        print('Cannot read QR code')
        return
def main():
    print('========> Starting Read <==========')
    # define a video capture object
    vid = cv2.VideoCapture(-1)
    while(True):
        # # Flag is value to determine the previous state(0 : True, 1, 2, 3, 4: False)
        # flag = True
        # file = open('result.txt', 'r')
        # list = file.read()
        # list = list.split('\n')
        # file.close()
        # if list[-1] == 0 or len(list) == 1:
        #     flag = False
        # else:
        #     flag = True
        # # print('===========> This is list[-1]: ', list[-1])
        # # print('This is flag value: ', flag)
        # # print('This is list: ', list)
        # Capture video frame by frame
        ret, frame = vid.read()
        # Read QR information
        value = readQR(frame)
        if value == 'Product 1' or value == 'Product 2' or value == 'Product 3' or value == 'Product 4':
            print('Pass here with product: ', value)
            value = value.split(' ')
            f = open("result.txt", "w")
            f.write(value[1])
            f.close()
            print('This is  value:[1] ', value[1])
        # else:
        #     if flag == True:
        #         f = open("result.txt", "a")
        #         f.write('\n' + str(0))
        #         f.close()
        cv2.imshow('frame', frame)
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    vid.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
