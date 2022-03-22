import cv2 as cv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("logo", type=str, help="the logo path")
parser.add_argument("image", type=str, help="the image path")
parser.add_argument("target", type=str, help="the crop image path")
args = parser.parse_args()

img_rgb, template_rgb = cv.imread(args.image), cv.imread(args.logo)
img_gray, template_gray = cv.cvtColor(img_rgb, 6), cv.cvtColor(template_rgb, 6)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(cv.matchTemplate(img_gray, template_gray, 0))
w, h = img_gray.shape[::-1]
cv.imwrite(args.target, img_rgb[0:max_loc[1], 0:w])
