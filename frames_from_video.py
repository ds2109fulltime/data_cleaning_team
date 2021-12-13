import cv2 as cv
import os

def frames_from_video(pathIn, pathOut, ms_extract = 1000):
    '''
    This function extracts frames from videos in an explicit path, modifies the resolution of the frames and, finally, 
    it saves them in another path.
    Parameters:
    - pathIn: Path where videos are.
    - pathOut: Path where frames will be saved.
    - ms_extract: miliseconds between frames.
    '''

    filenames = os.listdir(pathIn)
    count = 0
    for filename in filenames:
        vidcap = cv.VideoCapture(pathIn + '\\' + filename)
        print(pathIn + '\\' + filename)
        counter = 0
        while True:
            vidcap.set(cv.CAP_PROP_POS_MSEC,(counter*ms_extract))
            success,image = vidcap.read()
            if success:
                print ('Read a new frame: ', success, count)
                imagesmall = cv.resize(image, (int(image.shape[1]*0.5), int(image.shape[0]*0.5)))                                         
                cv.imwrite( pathOut + "\\frame_{}.jpg".format(count), imagesmall)
                count = count + 1
                counter = counter + 1
            else:
                print('***********************')
                print('All frames catched.')
                print('***********************')
                break

    return 'All videos have been catched'