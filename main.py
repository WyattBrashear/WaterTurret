# Water Turret, Uses AI for targeting and whatnot
from ultralytics import YOLO
import cv2
import argparse
# Calculate the 9 sectors
# Ok so basic explanation of how this thing works, it splits the screen into 9 sectors and adjusts its targeting until
# the target's center is in the center of the screen

def calculate_sectors(camera_x, camera_y):
    sector_width = camera_x // 3
    sector_height = camera_y // 3
    sectors = []
    for y in range(3):
        for x in range(3):
            #Each sector should be a pair 2 cordinates
            sector_tmpvar = [sector_width*x, sector_height*y]
            sectors.append([[],[]])