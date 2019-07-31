import cv2
import matplotlib.pyplot as plt

img = cv2.imread('beauty.png')
size = img.shape
if size[0] > size[1]:
    colum = int((size[0] - size[1]) / 2)
    if colum < (size[0] - size[1]) / 2:
        img1 = cv2.copyMakeBorder(img, 0, 0, colum, colum + 1, cv2.BORDER_ISOLATED)
        img2 = cv2.resize(img1, (512, 512), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite('input.png', img2)
    else:
        img1 = cv2.copyMakeBorder(img, 0, 0, colum, colum, cv2.BORDER_ISOLATED)
        img2 = cv2.resize(img1, (512, 512), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite('input.png', img2)
else:
    row = int((size[1] - size[0]) / 2)
    if row < (size[1] - size[0]) / 2:
        img1 = cv2.copyMakeBorder(img, 0, 0, row, row + 1, cv2.BORDER_ISOLATED)
        img2 = cv2.resize(img1, (512, 512), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite('input.png', img2)
    else:
        img1 = cv2.copyMakeBorder(img, 0, 0, row, row, cv2.BORDER_ISOLATED)
        img2 = cv2.resize(img1, (512, 512), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite('input.png', img2)
# if max<=512:
#     row = int((512-size[0])/2)
#     colum = int((512-size[0])/2)
#     img1 = cv2.copyMakeBorder(img, row, row, colum, colum, cv2.BORDER_REPLICATE)
#     img2 = cv2.resize(img1, (512, 512), interpolation=cv2.INTER_CUBIC)
#     cv2.imwrite('input.png', img2)
# elif max<=1024:
#     row = int((1024 - size[0]) / 2)
#     colum = int((1024 - size[1]) / 2)
#     img1 = cv2.copyMakeBorder(img, row, row, colum, colum, cv2.BORDER_ISOLATED)
#     img2 = cv2.resize(img1, (512, 512), interpolation=cv2.INTER_CUBIC)
#     cv2.imwrite('input.png', img2)
# elif max<=1536:
#     row = int((1536 - size[0]) / 2)
#     colum = int((1536 - size[1]) / 2)
#     img1 = cv2.copyMakeBorder(img, row, row, colum, colum, cv2.BORDER_ISOLATED)
#     img2 = cv2.resize(img1, (512, 512), interpolation=cv2.INTER_CUBIC)
#     cv2.imwrite('input.png', img2)
# else:
#     row = int((2048 - size[0]) / 2)
#     colum = int((2048 - size[1]) / 2)
#     img1 = cv2.copyMakeBorder(img, row, row, colum, colum, cv2.BORDER_ISOLATED)
#     img2 = cv2.resize(img1, (512, 512), interpolation=cv2.INTER_CUBIC)
#     cv2.imwrite('input.png', img2)

img3 = cv2.imread('input.png')
print(img3.shape)
cv2.imshow('input', img3)
cv2.waitKey()
cv2.destroyAllWindows()
