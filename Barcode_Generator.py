import PIL
from zipfile import ZipFile
from PIL import Image
import numpy as np
from numpy import asarray
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# import EAN13 from barcode module
from barcode import EAN13


file_name = "MNIST_DS.zip"

with ZipFile(file_name, 'r') as zip:
    zip.extractall()
    print('Done')

# load the image and convert into
List1 = []
for i in range(10):  # External Loop for Folders
    temp = i
    for j in range(10):  # Internal Loop for images
        img = Image.open('MNIST_DS/' + str(i) + '/' + str(j) + '.jpg')
        x = asarray(img)
        # data
        # print(x)
        p1 = np.sum(x, axis=0)  # Sum of each column:
        p2 = np.sum(x, axis=1)  # Sum of each row:
        p3 = x.diagonal()  # Diagonal Sum at 45
        p4 = x.diagonal(1)  # Diagonal Sum at 90
        th_p1 = ""
        th_p2 = ""
        th_p3 = ""
        th_p4 = ""
        for i in p1:  # Converting values to 1 or zero based on threshold values
            if i > np.mean(p1):
                th_p1 += "1"
            else:
                th_p1 += "0"
                #######
        for i in p2:  # Conveting values to 1 or zero based on threshold values
            if i > np.mean(p2):
                th_p2 += "1"
            else:
                th_p2 += "0"
                #######
        for i in p3:  # Conveting values to 1 or zero based on threshold values
            if i > np.mean(p3):
                th_p3 += "1"
            else:
                th_p3 += "0"
                #######
        for i in p4:  # Conveting values to 1 or zero based on threshold values
            if i > np.mean(p4):
                th_p4 += "1"
            else:
                th_p4 += "0"
        Binary_String = th_p4 + th_p4 + th_p4 + th_p4  # Combining Threshold values
        # Binary_String
        Bar_code = EAN13(Binary_String)
        # print(Bar_code)
        List2 = []
        List2.append(temp)  # =  [str(),  ,str(Bar_code) ]
        List2.append(Binary_String)
        List2.append(Bar_code)

        List1.append(List2)  # Creating List of list with Bard Code + Class ID + Binary String
        # print(Bar_code)

# print((List1))
li = []
for c in List1:  # Forming a single list
    a = 0
    for v in c:
        a = a + 1
        # print(v)
        li.append(str(v))
        if a > 2:
            break

len(li)
import joblib

joblib.dump(li, 'List.pkl')  # Saving List for later use

# Our barcode is ready. Let's save it.
# my_code.save("new_code")

# Testing
testURL = 'MNIST_DS/6/0.jpg'
img = Image.open(testURL)
# Need to fix
#display(img)
img.show()
x = asarray(img)
# data
# print(x)
p1 = np.sum(x, axis=0)  # Sum of each column:
p2 = np.sum(x, axis=1)  # Sum of each row:
p3 = x.diagonal()
p4 = x.diagonal(1)
th_p1 = ""
th_p2 = ""
th_p3 = ""
th_p4 = ""
for i in p1:
    if i > np.mean(p1):
        th_p1 += "1"
    else:
        th_p1 += "0"
        #######
for i in p2:
    if i > np.mean(p2):
        th_p2 += "1"
    else:
        th_p2 += "0"
        #######
for i in p3:
    if i > np.mean(p3):
        th_p3 += "1"
    else:
        th_p3 += "0"
        #######
for i in p4:
    if i > np.mean(p4):
        th_p4 += "1"
    else:
        th_p4 += "0"
Binary_String = th_p4 + th_p4 + th_p4 + th_p4
# Binary_String
Bar_code = EAN13(Binary_String)

# Hamming distance
li = joblib.load('List.pkl')


def hammingDist(str1, str2):
    i = 0
    count = 0

    while (i < len(str1)):
        if (str1[i] != str2[i]):
            count += 1
        i += 1
    return count


# print(hammingDist(str1, str2))
min = 100
for bin in range(1, 300, 3):
    # print(li[bin])
    Distance = hammingDist(Binary_String, li[bin])

    if min > Distance:
        min = Distance
        classValue = li[bin - 1]

print(min)
print("The Class Value: ", classValue)


image1 = Image.open(testURL)
image2=Image.open("MNIST_DS/6/2.jpg")
plt.subplot(2,2,2)
plt.title("Image1")
plt.subplot(2,2,2)
plt.title("Image2")
plt.imshow(image1)
plt.imshow(image2)
plt.show()
