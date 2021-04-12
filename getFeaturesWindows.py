import numpy as np
import math
import getFeature

L = 42
dataWindow = 23
stride = dataWindow / 2


def getFeaturesWindows(data, out):
    print(len(data))

    lenDat_ = len(data)
    i = 0
    while i < lenDat_:
        indStart_ = i
        indStop_ = i + dataWindow
        if(indStop_  >= lenDat_) :
            indStop_ = lenDat_ - 1
        i += math.floor(dataWindow / 2.0)
        data = getFeature.getFeature(rowData[indStart:indStart + dataWindow, :])  # get corresponding features
        mBad += 1
        print(mBad)
        # print('start', indStart_)
        # print('stop', indStop_)

# def getFeaturesWindows(data,out):
# windows = np.lib.stride_tricks.as_strided(
#    data,
#   shape=(L - dataWindow+1,dataWindow),
#   strides =(stride)
# )
# return windows

# windows2 = np.lib.stride_tricks.sliding_window_view(
#    data,
#    dataWindow,
#    axis =1
# )


#    for i in rowData:
#        indMiddle = int(len(rowData[:, 1]) / 2)
#        indDetecStart = indMiddle - int(dataWindow / 2)  # - 5
#        indDetecStop = indDetecStart + dataWindow
#        print("indMiddle", indMiddle)
#        print("indDetecStart", indDetecStart)
#        print("indDetecStop", indDetecStop)
#        if indDetecStop - indDetecStart == dataWindow:
#                indDetecStart = indmiddle
#               indmiddle = indDetecStop
#               indDetecStop = indmiddle + (dataWindow/2)
#               print("indMiddle", indMiddle)
#              print("indDetecStart", indDetecStart)
#               print("indDetecStop", indDetecStop)

# Window = []  # a python list to hold the windows
# for i in range(0, rowData.shape[0] - int(dataWindow) + int(dataWindow/2)):
#    print('here',i)
#    createWindow = rowData[i:i + dataWindow, :].reshape((-1, 1))  # each individual window
#   Window.append(createWindow)
#  print(Window)
# result = np.hstack(Window)
# return (result)
# print(result)

#   def extract_windows(array, clearing_time_index, max_time, sub_window_size):
#      examples = []
#     start = clearing_time_index + 1 - sub_window_size + 1

#    for i in range(max_time + 1):
#       example = array[start + i:start + sub_window_size + i]
#      examples.append(np.expand_dims(example, 0))

# return np.vstack(examples)
