import cv2 as cv


img=cv.imread(r'data/satranc3x3.jpg')

b,g,r=cv.split(img)

mavi_img=cv.merge((r,g,b))

cv.imshow('Mavi dama',mavi_img)
cv.imwrite(r'data/mavi_dama.jpg', mavi_img)
#Tek kanal olarak  göster
cv.imshow('Satranc 3x3',img)
cv.imshow('Blue Kanali',b)
cv.imshow('Green kanali',g)
cv.imshow('Red Kanali',r)


cv.waitKey(0)
cv.destroyAllWindows()
