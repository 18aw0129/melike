import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import base64
import cv2
import numpy as np
import os, time, random, string, pathlib

cred = credentials.Certificate('./app/data/key/melike-key.json')

firebase_admin.initialize_app(cred, {
  # 'databaseURL': Your URL,
})

log_ref = db.reference('/log')
url_ref = db.reference('/url')

base_path = './app/data'
img_path = base_path + '/img/'
dist_path = base_path + '/dist/'
if not os.path.isdir(dist_path) or not os.path.isdir(img_path) :
  os.makedirs(dist_path, exist_ok=True)
  os.makedirs(img_path, exist_ok=True)

if log_ref.get():
  num = len(log_ref.get())
else:
  num = 0

start = 0
# 赤色の検出
def detect_red_color(hsv,img):
  # 赤色のHSVの値域1
  hsv_min = np.array([0,90,150])
  hsv_max = np.array([6,255,255])
  mask1 = cv2.inRange(hsv, hsv_min, hsv_max)

  # 赤色のHSVの値域2
  hsv_min = np.array([172,90,150])
  hsv_max = np.array([179,255,255])
  mask2 = cv2.inRange(hsv, hsv_min, hsv_max)

  # 赤色領域のマスク（255：赤色、0：赤色以外）    
  mask = mask1 + mask2

  # マスキング処理
  masked_img = cv2.bitwise_and(img, img, mask=mask)

  return mask, masked_img

# オレンジ色の検出
def detect_orange_color(hsv,img):
  hsv_min = np.array([7,90,150])
  hsv_max = np.array([23, 255, 255])
  
  mask = cv2.inRange(hsv, hsv_min, hsv_max)

  masked_img = cv2.bitwise_and(img, img, mask=mask)

  return mask, masked_img

# 茶色の検出*
def detect_brown_color(hsv,img):
  hsv_min = np.array([0,64,80])
  hsv_max = np.array([23, 90, 150])
  
  mask = cv2.inRange(hsv, hsv_min, hsv_max)

  masked_img = cv2.bitwise_and(img, img, mask=mask)

  return mask, masked_img

# 黄色の検出
def detect_yellow_color(hsv,img):
  hsv_min = np.array([25,90,80])
  hsv_max = np.array([30, 255, 255])
  
  mask = cv2.inRange(hsv, hsv_min, hsv_max)

  masked_img = cv2.bitwise_and(img, img, mask=mask)

  return mask, masked_img

# 黄緑色の検出
def detect_yellowgreen_color(hsv,img):
  hsv_min = np.array([33,90,0])
  hsv_max = np.array([46, 255, 255])

  mask = cv2.inRange(hsv, hsv_min, hsv_max)

  masked_img = cv2.bitwise_and(img, img, mask=mask)

  return mask, masked_img

# 緑色の検出
def detect_green_color(hsv,img):
  hsv_min = np.array([47, 90, 0])
  hsv_max = np.array([82, 255, 255])
  
  mask = cv2.inRange(hsv, hsv_min, hsv_max)

  masked_img = cv2.bitwise_and(img, img, mask=mask)

  return mask, masked_img

# 水色の検出
def detect_lightblue_color(hsv,img):
  hsv_min = np.array([83,90,0])
  hsv_max = np.array([96, 255, 255])
  
  mask = cv2.inRange(hsv, hsv_min, hsv_max)

  masked_img = cv2.bitwise_and(img, img, mask=mask)

  return mask, masked_img

# 青色の検出
def detect_blue_color(hsv,img):
  hsv_min = np.array([97,90,0])
  hsv_max = np.array([115, 255, 255])
  
  mask = cv2.inRange(hsv, hsv_min, hsv_max)

  masked_img = cv2.bitwise_and(img, img, mask=mask)

  return mask, masked_img

# 紫色の検出
def detect_violet_color(hsv,img):
  hsv_min = np.array([125,90,0])
  hsv_max = np.array([150, 255, 255])
  
  mask = cv2.inRange(hsv, hsv_min, hsv_max)

  masked_img = cv2.bitwise_and(img, img, mask=mask)

  return mask, masked_img

# ピンク紫色の検出
def detect_pinkvio_color(hsv,img):
  hsv_min = np.array([155,90,0])
  hsv_max = np.array([164, 255, 255])
  
  mask = cv2.inRange(hsv, hsv_min, hsv_max)

  masked_img = cv2.bitwise_and(img, img, mask=mask)

  return mask, masked_img

# ピンク色の検出
def detect_pink_color(hsv,img):
  hsv_min = np.array([165,90,0])
  hsv_max = np.array([170, 255, 255])
  
  mask = cv2.inRange(hsv, hsv_min, hsv_max)

  masked_img = cv2.bitwise_and(img, img, mask=mask)

  return mask, masked_img


def main():
  cv2.namedWindow("MeLike", cv2.WINDOW_NORMAL)
  cv2.resizeWindow("MeLike", 640, 480)
  video = cv2.VideoCapture(0)
  
  while (video.isOpened()):
    ret, frame = video.read()
    cv2.imshow('MeLike', frame)
    if not ret:
        break

    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
      now = time.time()
      global start
      if (int(now - start) > 5):
        print('start')
        start = now
        img = scale_to_height(frame, 90)
        color_check(img)
      else:
        print('wait please')
    if key == ord('q'):
      break
  cv2.waitKey(0)
  cv2.destroyAllWindows()

def scale_to_height(img, height):
  scale = height / img.shape[0]
  return cv2.resize(img, dsize=None, fx=scale, fy=scale)
  
def rname(n):
  return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

def regidb(img):
  with open(img, 'rb') as f:
    data = f.read()
  b64 = base64.encodebytes(data)
  return str(b64.decode('utf8'))

def numcheck():
  global num
  num += 1
  return str(num)

def percheck(item):
  li = []
  if item:
    s = sum(item)
    for i in item:
      li.append(i * 100 // s)
    return li
  else:
    return li

def adjust(img, alpha=1.0, beta=0.0):
  # 積和演算を行う。
  dst = alpha * img + beta
  # [0, 255] でクリップし、uint8 型にする。
  return np.clip(dst, 0, 255).astype(np.uint8)

def color_check(img):
  i = rname(10)
  cv2.imwrite('{}{}.jpg'.format(img_path, i), img)
  dist = '{}{}.jpg'.format(img_path, i)
  url = regidb(dist)
  dst = adjust(img, alpha=1.5, beta=30.0)
  # HSV色空間に変換
  hsv = cv2.cvtColor(dst, cv2.COLOR_BGR2HSV)
  # 色検出
  red_mask, red_masked_img = detect_red_color(hsv,img)
  orange_mask, orange_masked_img = detect_orange_color(hsv,img)
  brown_mask, brown_masked_img = detect_brown_color(hsv,img)
  yellow_mask, yellow_masked_img = detect_yellow_color(hsv,img)
  green_mask, green_masked_img = detect_green_color(hsv,img)
  yellowgreen_mask, yellowgreen_masked_img = detect_yellowgreen_color(hsv, img)
  blue_mask, blue_masked_img = detect_blue_color(hsv,img)
  lightblue_mask, lightblue_masked_img = detect_lightblue_color(hsv,img)
  violet_mask, violet_masked_img = detect_violet_color(hsv,img)
  pinkvio_mask, pinkvio_masked_img = detect_pinkvio_color(hsv,img)
  pink_mask, pink_masked_img = detect_pink_color(hsv, img)

  # 認識済みレゴの数
  color_list = []
  color_area = []


  while len(color_list) < 15:
 
    if len(color_list) > 14:
      break
    if not "red" in color_list:
      if red_mask.any():
        count = cv2.countNonZero(red_mask)
        if count > 300:
          color_list.append("red")
          color_area.append(count)
          continue
    if not "orange" in color_list:
      if orange_mask.any():
        count = cv2.countNonZero(orange_mask)
        if count > 300:
          color_list.append("orange")
          color_area.append(count)
          continue
    if not "brown" in color_list:
      if brown_mask.any():
        count = cv2.countNonZero(brown_mask)
        if count > 300:
          color_list.append("brown")
          color_area.append(count)
          continue
    if not "yellow" in color_list:
      if yellow_mask.any():
        count = cv2.countNonZero(yellow_mask)
        if count > 300:
          color_list.append("yellow")
          color_area.append(count)
          continue
    if not "green" in color_list:
      if green_mask.any():
        count = cv2.countNonZero(green_mask)
        if count > 300:
          color_list.append("green")
          color_area.append(count)
          continue
    if not "yellowgreen" in color_list:
      if yellowgreen_mask.any():
        count = cv2.countNonZero(yellowgreen_mask)
        if count > 300:
          color_list.append("yellowgreen")
          color_area.append(count)
          continue
    if not "blue" in color_list:
      if blue_mask.any():
        count = cv2.countNonZero(blue_mask)
        if count > 300:
          color_list.append("blue")
          color_area.append(count)
          continue
    if not "lightblue" in color_list:
      if lightblue_mask.any():
        count = cv2.countNonZero(lightblue_mask)
        if count > 300:
          color_list.append("lightblue")
          color_area.append(count)
          continue
    if not "violet" in color_list:
      if violet_mask.any():
        count = cv2.countNonZero(violet_mask)
        if count > 300:
          color_list.append("violet")
          color_area.append(count)
          continue
    if not "pinkvio" in color_list:
      if pinkvio_mask.any():
        count = cv2.countNonZero(pinkvio_mask)
        if count > 300:
          color_list.append("pinkvio")
          color_area.append(count)
          continue
    if not "pink" in color_list:
      if pink_mask.any():
        count = cv2.countNonZero(pink_mask)
        if count > 300:
          color_list.append("pink")
          color_area.append(count)
          continue
    if len(color_list) == 0:
      color_list.append("black")
      color_area.append(100)
    break
  else:
    print('error')

  color_per = percheck(color_area)
  print(color_list)

  if 'yellow' in color_list:
    if color_per[color_list.index('yellow')] > 25:
      dst = adjust(img, alpha=1, beta=50.0)
      # HSV色空間に変換
      hsv = cv2.cvtColor(dst, cv2.COLOR_BGR2HSV)
      # 色検出
      red_mask, red_masked_img = detect_red_color(hsv,img)
      orange_mask, orange_masked_img = detect_orange_color(hsv,img)
      brown_mask, brown_masked_img = detect_brown_color(hsv,img)
      yellow_mask, yellow_masked_img = detect_yellow_color(hsv,img)
      green_mask, green_masked_img = detect_green_color(hsv,img)
      yellowgreen_mask, yellowgreen_masked_img = detect_yellowgreen_color(hsv, img)
      blue_mask, blue_masked_img = detect_blue_color(hsv,img)
      lightblue_mask, lightblue_masked_img = detect_lightblue_color(hsv,img)
      violet_mask, violet_masked_img = detect_violet_color(hsv,img)
      pinkvio_mask, pinkvio_masked_img = detect_pinkvio_color(hsv,img)
      pink_mask, pink_masked_img = detect_pink_color(hsv, img)
      black_mask, black_masked_img = detect_black_color(hsv, img)
      color_list = []
      color_area = []
      while len(color_list) < 15:
    
        if len(color_list) > 14:
          break
        if not "red" in color_list:
          if red_mask.any():
            count = cv2.countNonZero(red_mask)
            if count > 300:
              color_list.append("red")
              color_area.append(count)
              continue
        if not "orange" in color_list:
          if orange_mask.any():
            count = cv2.countNonZero(orange_mask)
            if count > 300:
              color_list.append("orange")
              color_area.append(count)
              continue
        if not "brown" in color_list:
          if brown_mask.any():
            count = cv2.countNonZero(brown_mask)
            if count > 3000:
              color_list.append("brown")
              color_area.append(count)
              continue
        if not "yellow" in color_list:
          if yellow_mask.any():
            count = cv2.countNonZero(yellow_mask)
            if count > 300:
              color_list.append("yellow")
              color_area.append(count)
              continue
        if not "green" in color_list:
          if green_mask.any():
            count = cv2.countNonZero(green_mask)
            if count > 300:
              color_list.append("green")
              color_area.append(count)
              continue
        if not "yellowgreen" in color_list:
          if yellowgreen_mask.any():
            count = cv2.countNonZero(yellowgreen_mask)
            if count > 300:
              color_list.append("yellowgreen")
              color_area.append(count)
              continue
        if not "blue" in color_list:
          if blue_mask.any():
            count = cv2.countNonZero(blue_mask)
            if count > 300:
              color_list.append("blue")
              color_area.append(count)
              continue
        if not "lightblue" in color_list:
          if lightblue_mask.any():
            count = cv2.countNonZero(lightblue_mask)
            if count > 300:
              color_list.append("lightblue")
              color_area.append(count)
              continue
        if not "violet" in color_list:
          if violet_mask.any():
            count = cv2.countNonZero(violet_mask)
            if count > 300:
              color_list.append("violet")
              color_area.append(count)
              continue
        if not "pinkvio" in color_list:
          if pinkvio_mask.any():
            count = cv2.countNonZero(pinkvio_mask)
            if count > 300:
              color_list.append("pinkvio")
              color_area.append(count)
              continue
        if not "pink" in color_list:
          if pink_mask.any():
            count = cv2.countNonZero(pink_mask)
            if count > 300:
              color_list.append("pink")
              color_area.append(count)
              continue
        if len(color_list) == 0:
          color_list.append("black")
          color_area.append(100)
        break

      color_per = percheck(color_area)
      print('黄色補正',color_list)
  if 'blue' in color_list:
    if color_per[color_list.index('blue')] > 25:
      dst = adjust(img, alpha=1, beta=50.0)
      # HSV色空間に変換
      hsv = cv2.cvtColor(dst, cv2.COLOR_BGR2HSV)
      # 色検出
      red_mask, red_masked_img = detect_red_color(hsv,img)
      orange_mask, orange_masked_img = detect_orange_color(hsv,img)
      brown_mask, brown_masked_img = detect_brown_color(hsv,img)
      yellow_mask, yellow_masked_img = detect_yellow_color(hsv,img)
      green_mask, green_masked_img = detect_green_color(hsv,img)
      yellowgreen_mask, yellowgreen_masked_img = detect_yellowgreen_color(hsv, img)
      blue_mask, blue_masked_img = detect_blue_color(hsv,img)
      lightblue_mask, lightblue_masked_img = detect_lightblue_color(hsv,img)
      violet_mask, violet_masked_img = detect_violet_color(hsv,img)
      pinkvio_mask, pinkvio_masked_img = detect_pinkvio_color(hsv,img)
      pink_mask, pink_masked_img = detect_pink_color(hsv, img)
      black_mask, black_masked_img = detect_black_color(hsv, img)
      color_list = []
      color_area = []
      while len(color_list) < 15:
    
        if len(color_list) > 14:
          break
        if not "red" in color_list:
          if red_mask.any():
            count = cv2.countNonZero(red_mask)
            if count > 300:
              color_list.append("red")
              color_area.append(count)
              continue
        if not "orange" in color_list:
          if orange_mask.any():
            count = cv2.countNonZero(orange_mask)
            if count > 300:
              color_list.append("orange")
              color_area.append(count)
              continue
        if not "brown" in color_list:
          if brown_mask.any():
            count = cv2.countNonZero(brown_mask)
            if count > 3000:
              color_list.append("brown")
              color_area.append(count)
              continue
        if not "yellow" in color_list:
          if yellow_mask.any():
            count = cv2.countNonZero(yellow_mask)
            if count > 300:
              color_list.append("yellow")
              color_area.append(count)
              continue
        if not "green" in color_list:
          if green_mask.any():
            count = cv2.countNonZero(green_mask)
            if count > 300:
              color_list.append("green")
              color_area.append(count)
              continue
        if not "yellowgreen" in color_list:
          if yellowgreen_mask.any():
            count = cv2.countNonZero(yellowgreen_mask)
            if count > 300:
              color_list.append("yellowgreen")
              color_area.append(count)
              continue
        if not "blue" in color_list:
          if blue_mask.any():
            count = cv2.countNonZero(blue_mask)
            if count > 300:
              color_list.append("blue")
              color_area.append(count)
              continue
        if not "lightblue" in color_list:
          if lightblue_mask.any():
            count = cv2.countNonZero(lightblue_mask)
            if count > 300:
              color_list.append("lightblue")
              color_area.append(count)
              continue
        if not "violet" in color_list:
          if violet_mask.any():
            count = cv2.countNonZero(violet_mask)
            if count > 300:
              color_list.append("violet")
              color_area.append(count)
              continue
        if not "pinkvio" in color_list:
          if pinkvio_mask.any():
            count = cv2.countNonZero(pinkvio_mask)
            if count > 300:
              color_list.append("pinkvio")
              color_area.append(count)
              continue
        if not "pink" in color_list:
          if pink_mask.any():
            count = cv2.countNonZero(pink_mask)
            if count > 300:
              color_list.append("pink")
              color_area.append(count)
              continue
        if len(color_list) == 0:
          color_list.append("black")
          color_area.append(100)
        break

      color_per = percheck(color_area)

  number = numcheck()
  if (len(color_list) > 10):
    color_list = ["rainbow"]
    color_per = ["100"]
  if color_list:
    log_ref.child(number).set({
        'id': int(number),
        'list': color_list,
        'area': color_per
    })
    url_ref.child(number).set({
        'id': int(number),
        'url': url,
    })


if __name__ == "__main__":
  main()

