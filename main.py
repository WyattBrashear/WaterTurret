# Water Turret, Uses AI for targeting and whatnot
from ultralytics import YOLO
import cv2
import argparse
import json
import time
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
            sectors.append([[sector_tmpvar[0]+sector_width, sector_tmpvar[1]],[sector_tmpvar[0], sector_tmpvar[1]+sector_height]])
    return sectors


global sectors_calculated
sectors_calculated = calculate_sectors(1920, 1080)

def check_pos(x,y):
    for sector in sectors_calculated:
        if x >= sector[0][0] and x <= sector[1][0] and y >= sector[0][1] and y <= sector[1][1]:
            return sectors_calculated.index(sector)
    return None

cap = cv2.VideoCapture(0)
async def run_prediction(model, video_source):
    global cap
    frame, ret = cap.read()
    #look i know this is inneficent but ITS FINE!!!
    model_loaded = YOLO(model)
    model_loaded.predict()
#Main Loop
print("A.P.W.D.S. initialization complete. Starting main...")

async def main_loop():
    exited = False
    while not exited:
        #Run prediction