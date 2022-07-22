import os
os.chdir('.')
print(os.getcwd())
import tobii_research as tr
import time
import datetime
import csv
import pandas as pd
import turtle
import wx

f = open('mycsv.csv', 'w+', newline='')
writer = csv.writer(f)
writer.writerow(['Left Eye (x)','Left Eye (y)','Right Eye (x)','Right Eye (y)','Current Time'])

found_eyetrackers = tr.find_all_eyetrackers()
my_eyetracker = found_eyetrackers[0]
print("Address: " + my_eyetracker.address)
print("Model: " + my_eyetracker.model)
print("Name: " + my_eyetracker.device_name)
print("Serial number: " + my_eyetracker.serial_number)

def execute(my_eyetracker):
    if my_eyetracker is None:
        return
    # <BeginExample>
    
    calibration = tr.ScreenBasedCalibration(my_eyetracker)
   
    # Enter calibration mode.
    calibration.enter_calibration_mode()
    print("Entered calibration mode for eye tracker with serial number {0}.".format(my_eyetracker.serial_number))
   
    # Define the points on screen we should calibrate at.
    # The coordinates are normalized, i.e. (0.0, 0.0) is the upper left corner and (1.0, 1.0) is the lower right corner.
    points_to_calibrate = [(0.5, 0.5), (0.1, 0.1), (0.1, 0.9), (0.9, 0.1), (0.9, 0.9)]

    screen = turtle.Screen()
    screenTk = screen.getcanvas().winfo_toplevel()
    screenTk.attributes("-fullscreen", True)

    app = wx.App(False)
    width , height = wx.GetDisplaySize()
    print(width, height)

    turtle.home()
    turtle.up()
    turtle.shape("circle")

    for point in points_to_calibrate:
        print("Show a point on screen at {0}.".format(point))

        if point == (0.5,0.5) :
            turtle.setpos(0,0)

        elif point == (0.1,0.1) :
            turtle.setpos((width/(-2))+20,(height/2)-20)

        elif point == (0.1,0.9) :
            turtle.setpos((width/(-2))+20,(height/(-2))+20)

        elif point == (0.9,0.1) :
            turtle.setpos((width/2)-20,(height/2)-20)

        elif point == (0.9,0.9) :
            turtle.setpos((width/2)-20,(height/(-2))+20)

        # Wait a little for user to focus.
        time.sleep(0.7)

        print("Collecting data at {0}.".format(point))
        if calibration.collect_data(point[0], point[1]) != tr.CALIBRATION_STATUS_SUCCESS:
            # Try again if it didn't go well the first time.
            # Not all eye tracker models will fail at this point, but instead fail on ComputeAndApply.
            calibration.collect_data(point[0], point[1])
    
    print("Computing and applying calibration.")
    calibration_result = calibration.compute_and_apply()
    print("Compute and apply returned {0} and collected at {1} points.".
        format(calibration_result.status, len(calibration_result.calibration_points)))
    
    # Analyze the data and maybe remove points that weren't good.
    recalibrate_point = (0.1, 0.1)
    print("Removing calibration point at {0}.".format(recalibrate_point))
    calibration.discard_data(recalibrate_point[0], recalibrate_point[1])
   
    # Redo collection at the discarded point
    print("Show a point on screen at {0}.".format(recalibrate_point))
    calibration.collect_data(recalibrate_point[0], recalibrate_point[1])
   
    # Compute and apply again.
    print("Computing and applying calibration.")
    calibration_result = calibration.compute_and_apply()
    print("Compute and apply returned {0} and collected at {1} points.".
        format(calibration_result.status, len(calibration_result.calibration_points)))
    
    # See that you're happy with the result.
    
     # The calibration is done. Leave calibration mode.
    calibration.leave_calibration_mode()
   
    print("Left calibration mode.")

    turtle.bye()

def gaze_data_callback(gaze_data):
    #Print gaze points of left and right eye
    print("Left eye: ({gaze_left_eye}) \t Right eye: ({gaze_right_eye})".format(
        gaze_left_eye=gaze_data['left_gaze_point_on_display_area'],
        gaze_right_eye=gaze_data['right_gaze_point_on_display_area']))

    ct = datetime.datetime.now()
    print("current time:-", ct)
    data_left = gaze_data['left_gaze_point_on_display_area']
    data_right = gaze_data['right_gaze_point_on_display_area']

    data_left = str(data_left).strip("(")
    data_left = str(data_left).strip(")")
    data_right = str(data_right).strip("(")
    data_right = str(data_right).strip(")")

    writer.writerow([ data_left.split(',')[0],data_left.split(',')[1],data_right.split(',')[0], data_right.split(',')[1],str(ct)])

my_eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)

while(1):
    {}

writer.close()