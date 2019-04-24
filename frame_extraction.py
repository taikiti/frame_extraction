#coding:utf-8

import numpy as np
import cv2

for g in range(0,2240):#ファイルの数だけ回す→len(os.listdir(srcDir))みたいにしても良い
    #img+数列でファイル名の変換を行うと良い
    src_img = cv2.imread("../image_yamami/img"+str(g)+".jpg",0)
    #二値化
    _,bin_img = cv2.threshold(src_img,150,255,cv2.THRESH_BINARY)
    #枠線抽出
    image, contours,hierarchy = cv2.findContours(bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    count = 0
    for i in range(0, len(contours)):
        if len(contours[i]) > 0:
            #閾値で枠線の大きさを調整
            if 50000<cv2.contourArea(contours[i]) < 65000:
                rect = contours[i]
                x, y, w, h = cv2.boundingRect(rect)
                count=count+1
    #1つだけ枠線を切り取れた場合
    if count == 1:
        print(g)
        print("x1:{}x2:{}y1:{}y2:{}".format(x,x+w,y,y+h))
        #枠線が消えるように少し小さく切り取る
        dst = src_img[y+5:y+h-5,x+5:x+w-90]
        #書き出し
        cv2.imwrite('./tmp/frame'+str(g)+'.jpg',dst)
    else:
        print("error?")
#cv2.imshow("Result",res_img)
cv2.imshow("Result2",src_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
