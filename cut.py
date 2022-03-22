import cv2 as cv
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-l", "--logo", type=str, required=True,
                help="path to logo image")
ap.add_argument("-i", "--image", type=str, required=True,
                help="path to input image where we'll apply template matching")
ap.add_argument("-t", "--target", type=str, required=True,
                help="path to logo image")
args = vars(ap.parse_args())

print("[INFO] loading images...")
img_rgb, template_rgb = cv.imread(args["image"]), cv.imread(args["logo"])
img_gray, template_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY), cv.cvtColor(template_rgb, cv.COLOR_BGR2GRAY)

print("[INFO] performing template matching...")
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(cv.matchTemplate(img_gray, template_gray, cv.TM_SQDIFF))
cv.imwrite(args["target"], img_rgb[0:max_loc[1], 0:img_gray.shape[::-1][0]])
