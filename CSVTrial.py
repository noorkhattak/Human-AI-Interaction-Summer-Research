#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on July 22, 2022, at 16:45
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

from pylsl import StreamInfo, StreamOutlet#import required classes
info = StreamInfo(name='Triggerstream', type='Markers', channel_count=1, channel_format='int32', source_id='Example') #sets variables for object info 
outlet = StreamOutlet(info) # initialize stream.

from psychopy import core# this returns a time value in seconds, not a clock object:

clock = core.getAbsTime()

import time

from datetime import datetime

ETrial= datetime.fromtimestamp(clock).strftime("%I:%M:%S")
from pylsl import StreamInfo, StreamOutlet#import required classes
info = StreamInfo(name='Triggerstream', type='Markers', channel_count=1, channel_format='int32', source_id='Example') #sets variables for object info 
outlet = StreamOutlet(info) # initialize stream.
from pylsl import StreamInfo, StreamOutlet#import required classes
info = StreamInfo(name='Triggerstream', type='Markers', channel_count=1, channel_format='int32', source_id='Example') #sets variables for object info 
outlet = StreamOutlet(info) # initialize stream.
from pylsl import StreamInfo, StreamOutlet#import required classes
info = StreamInfo(name='Triggerstream', type='Markers', channel_count=1, channel_format='int32', source_id='Example') #sets variables for object info 
outlet = StreamOutlet(info) # initialize stream.
trials = 1
trials2 = 1
trials3 = 1
trials4 = 1
from pylsl import StreamInfo, StreamOutlet#import required classes
info = StreamInfo(name='Triggerstream', type='Markers', channel_count=1, channel_format='int32', source_id='Example') #sets variables for object info 
outlet = StreamOutlet(info) # initialize stream.
from pylsl import StreamInfo, StreamOutlet#import required classes
info = StreamInfo(name='Triggerstream', type='Markers', channel_count=1, channel_format='int32', source_id='Example') #sets variables for object info 
outlet = StreamOutlet(info) # initialize stream.
from pylsl import StreamInfo, StreamOutlet#import required classes
info = StreamInfo(name='Triggerstream', type='Markers', channel_count=1, channel_format='int32', source_id='Example') #sets variables for object info 
outlet = StreamOutlet(info) # initialize stream.
from pylsl import StreamInfo, StreamOutlet#import required classes
info = StreamInfo(name='Triggerstream', type='Markers', channel_count=1, channel_format='int32', source_id='Example') #sets variables for object info 
outlet = StreamOutlet(info) # initialize stream.


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.4'
expName = 'CSVTrial'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\rdill\\Desktop\\PsychoPy Experiment File\\PsychoPy Research\\CSVTrial.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 960], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0.3569, 0.6941, 0.8039], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}
ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='event')

# Initialize components for Routine "Intro_Trial_Start"
Intro_Trial_StartClock = core.Clock()
Intro_Slide = visual.TextStim(win=win, name='Intro_Slide',
    text='In the following slide you will be shown a sample of how the experiment will look. You will notice that an image will appear on the left side of the screen and an AI response will appear on the right side of the screen. Please pay close attention to both the image and the AI response. Once you have answered all the administered questions, a continue button will appear which you must click to continue to the next question.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Press_to_Cont = visual.TextStim(win=win, name='Press_to_Cont',
    text='(Please press space bar when ready to continue)',
    font='Open Sans',
    pos=(0, -0.45), height=0.025, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Key_Resp = keyboard.Keyboard()

# Initialize components for Routine "Intro_Trial"
Intro_TrialClock = core.Clock()
Sample_Question = visual.TextStim(win=win, name='Sample_Question',
    text='',
    font='Open Sans',
    pos=(-0.475, 0.48), height=0.0225, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
AI_Response_2 = visual.TextStim(win=win, name='AI_Response_2',
    text='',
    font='Open Sans',
    pos=(-0.45, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Accept_Deny_Button_2 = visual.Slider(win=win, name='Accept_Deny_Button_2',
    startValue=1, size=(0.25, 0.05), pos=(-0.45, -0.1), units=None,
    labels=["Accept","Deny"], ticks=(1,2), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-2, readOnly=False)
ConfidenceText_2 = visual.TextStim(win=win, name='ConfidenceText_2',
    text='Level of confidence in your answer:',
    font='Open Sans',
    pos=(-0.45, -0.25), height=0.02, wrapWidth=None, ori=1.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
ConfidenceSlider_2 = visual.Slider(win=win, name='ConfidenceSlider_2',
    startValue=None, size=(0.4, 0.05), pos=(-0.45, -0.3), units=None,
    labels=["1", "2", "3", "4", "5"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='Black', markerColor='Red', lineColor='Black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=False, ori=0.0, depth=-4, readOnly=False)
Experimental_Images_2 = visual.ImageStim(
    win=win,
    name='Experimental_Images_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.45, 0.25), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
IfDenied_2 = visual.TextStim(win=win, name='IfDenied_2',
    text='How did you decide on your answer?\n\nA.) By myself\nB.) Based on AI Output alone\nC.) A combination of both\n',
    font='Open Sans',
    pos=(0.4, -0.1), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
DenySlider_2 = visual.Slider(win=win, name='DenySlider_2',
    startValue=None, size=(0.2, 0.05), pos=(0.4, -0.2), units=None,
    labels=["A", "B", "C"], ticks=(1, 2, 3), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='white', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-7, readOnly=False)
mouse_4 = event.Mouse(win=win)
x, y = [None, None]
mouse_4.mouseClock = core.Clock()
Click_to_Continue_4 = visual.ImageStim(
    win=win,
    name='Click_to_Continue_4', 
    image='Continue.JPG', mask=None, anchor='center',
    ori=0.0, pos=(0.55, -0.45), size=(0.12, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
AI_Response_Txt_2 = visual.TextStim(win=win, name='AI_Response_Txt_2',
    text='',
    font='Open Sans',
    pos=(0.475, 0.48), height=0.0225, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
Explanation_Image_2 = visual.ImageStim(
    win=win,
    name='Explanation_Image_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.45, 0.225), size=(0.7, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)

# Initialize components for Routine "Trial_Start"
Trial_StartClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='You will now be entering the experiment. Use the information provided on the slides to answer the given questions.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
PresstoCont_4 = visual.TextStim(win=win, name='PresstoCont_4',
    text='(Please press space bar when ready to continue)',
    font='Open Sans',
    pos=(0, -0.45), height=0.025, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
KeyResp_4 = keyboard.Keyboard()

# Initialize components for Routine "Conversational_Based"
Conversational_BasedClock = core.Clock()
Conversational_Intro_Txt = visual.TextStim(win=win, name='Conversational_Intro_Txt',
    text='Please wait for the question to be administered',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Question_Txt = visual.TextStim(win=win, name='Question_Txt',
    text='',
    font='Open Sans',
    pos=(-0.475, 0.48), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
AI_Response = visual.TextStim(win=win, name='AI_Response',
    text='',
    font='Open Sans',
    pos=(-0.45, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Accept_Deny_Button = visual.Slider(win=win, name='Accept_Deny_Button',
    startValue=1, size=(0.25, 0.05), pos=(-0.45, -0.1), units=None,
    labels=["Accept","Deny"], ticks=(1,2), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-3, readOnly=False)
ConfidenceText = visual.TextStim(win=win, name='ConfidenceText',
    text='Level of confidence in your answer:',
    font='Open Sans',
    pos=(-0.45, -0.25), height=0.02, wrapWidth=None, ori=1.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
ConfidenceSlider = visual.Slider(win=win, name='ConfidenceSlider',
    startValue=None, size=(0.4, 0.05), pos=(-0.45, -0.3), units=None,
    labels=["1", "2", "3", "4", "5"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='Black', markerColor='Red', lineColor='Black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=False, ori=0.0, depth=-5, readOnly=False)
Experimental_Images = visual.ImageStim(
    win=win,
    name='Experimental_Images', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.45, 0.25), size=(0.5, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
IfDenied = visual.TextStim(win=win, name='IfDenied',
    text='How did you decide on your answer?\n\nA.) By myself\nB.) Based on AI Output alone\nC.) A combination of both\n',
    font='Open Sans',
    pos=(0.4, -0.1), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
DenySlider = visual.Slider(win=win, name='DenySlider',
    startValue=None, size=(0.2, 0.05), pos=(0.4, -0.2), units=None,
    labels=["A", "B", "C"], ticks=(1, 2, 3), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='white', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-8, readOnly=False)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
Click_to_Continue = visual.ImageStim(
    win=win,
    name='Click_to_Continue', 
    image='Continue.JPG', mask=None, anchor='center',
    ori=0.0, pos=(0.55, -0.45), size=(0.12, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
AI_Response_Txt = visual.TextStim(win=win, name='AI_Response_Txt',
    text='',
    font='Open Sans',
    pos=(0.475, 0.48), height=0.0225, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
Explanation_Image = visual.ImageStim(
    win=win,
    name='Explanation_Image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.45, 0.225), size=(0.7, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)

# Initialize components for Routine "Conversational_Survey_Break"
Conversational_Survey_BreakClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='You will now be going onto the corresponding survey portion of the experiment. Please read and answer all of the questions to the best of your ability',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
PresstoCont = visual.TextStim(win=win, name='PresstoCont',
    text='(Please press space bar when ready to continue)',
    font='Open Sans',
    pos=(0, -0.45), height=0.025, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
KeyResp = keyboard.Keyboard()

# Initialize components for Routine "Survey_Trial"
Survey_TrialClock = core.Clock()
Q1 = visual.TextStim(win=win, name='Q1',
    text='Q1. The system always provides the advice I require to make my decision.',
    font='Open Sans',
    pos=(-0.45, 0.45), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Q1_Slider = visual.Slider(win=win, name='Q1_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,0.4), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-1, readOnly=False)
Q2 = visual.TextStim(win=win, name='Q2',
    text='Q2. The system performs reliably.',
    font='Open Sans',
    pos=(-0.45, 0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Q2_Slider = visual.Slider(win=win, name='Q2_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,0.25), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-3, readOnly=False)
Q3 = visual.TextStim(win=win, name='Q3',
    text='Q3. The system responds the same way under the same \nconditions at different times.',
    font='Open Sans',
    pos=(-0.45, 0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
Q3_Slider = visual.Slider(win=win, name='Q3_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,0.1), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-5, readOnly=False)
Q4 = visual.TextStim(win=win, name='Q4',
    text='Q4. I can rely on the system to function properly.',
    font='Open Sans',
    pos=(-0.45, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
Q4_Slider = visual.Slider(win=win, name='Q4_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,-0.05), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-7, readOnly=False)
Q5 = visual.TextStim(win=win, name='Q5',
    text='Q5. The system analyzes problems consistently.',
    font='Open Sans',
    pos=(-0.45, -0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
Q5_Slider = visual.Slider(win=win, name='Q5_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,-0.2), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-9, readOnly=False)
Q6 = visual.TextStim(win=win, name='Q6',
    text='Q6. The system uses appropriate methods to reach decisions.',
    font='Open Sans',
    pos=(-0.45,-0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
Q6_Slider = visual.Slider(win=win, name='Q6_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,-0.35), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-11, readOnly=False)
Q7 = visual.TextStim(win=win, name='Q7',
    text='Q7. The system has sound knowledge about this type of \nproblem built into it.',
    font='Open Sans',
    pos=(0.45, 0.45), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-12.0);
Q7_Slider = visual.Slider(win=win, name='Q7_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,0.4), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-13, readOnly=False)
Q8 = visual.TextStim(win=win, name='Q8',
    text='Q8. The advice the system produces is as good as that \nwhich a highly competent person could produce.',
    font='Open Sans',
    pos=(0.45, 0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-14.0);
Q8_Slider = visual.Slider(win=win, name='Q8_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,0.25), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-15, readOnly=False)
Q9 = visual.TextStim(win=win, name='Q9',
    text='Q9. I know what will happen the next time I use the \nsystem because I understand how it behaves.',
    font='Open Sans',
    pos=(0.45, 0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-16.0);
Q9_Slider = visual.Slider(win=win, name='Q9_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,0.1), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-17, readOnly=False)
Q10 = visual.TextStim(win=win, name='Q10',
    text='Q10. I understand how the system will assist me with \ndecisions I have to make.',
    font='Open Sans',
    pos=(0.45, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-18.0);
Q10_Slider = visual.Slider(win=win, name='Q10_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,-0.05), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-19, readOnly=False)
Q11 = visual.TextStim(win=win, name='Q11',
    text='Q11. Although I may not know exactly how the system works,\nI know how to use it to make decisions about the problem.\n\n',
    font='Open Sans',
    pos=(0.45, -0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-20.0);
Q11_Slider = visual.Slider(win=win, name='Q11_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,-0.2), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-21, readOnly=False)
Q12 = visual.TextStim(win=win, name='Q12',
    text='Q12. It is easy to follow what the system does.',
    font='Open Sans',
    pos=(0.45,-0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-22.0);
Q12_Slider = visual.Slider(win=win, name='Q12_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,-0.35), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-23, readOnly=False)
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()
Click_to_Continue_2 = visual.ImageStim(
    win=win,
    name='Click_to_Continue_2', 
    image='Continue.JPG', mask=None, anchor='center',
    ori=0.0, pos=(0.55, -0.45), size=(0.12, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-25.0)
Q13 = visual.TextStim(win=win, name='Q13',
    text='Q13. I recognize what I should do to get the advice I\nneed from the system the next time I use it.',
    font='Open Sans',
    pos=(-0.45, 0.45), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-26.0);
Q13_Slider = visual.Slider(win=win, name='Q13_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,0.4), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-27, readOnly=False)
Q14 = visual.TextStim(win=win, name='Q14',
    text='Q14. I believe advice from the system even when I\ndon’t know for certain that it is correct.',
    font='Open Sans',
    pos=(-0.45, 0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-28.0);
Q14_Slider = visual.Slider(win=win, name='Q14_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,0.25), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-29, readOnly=False)
Q15 = visual.TextStim(win=win, name='Q15',
    text='Q15. When I am uncertain about a decision I believe \nthe system rather than myself.',
    font='Open Sans',
    pos=(-0.45, 0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-30.0);
Q15_Slider = visual.Slider(win=win, name='Q15_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,0.1), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-31, readOnly=False)
Q16 = visual.TextStim(win=win, name='Q16',
    text='Q16. If I am not sure about a decision, I have faith that the\nsystem will provide the best solution.',
    font='Open Sans',
    pos=(-0.45, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-32.0);
Q16_Slider = visual.Slider(win=win, name='Q16_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,-0.05), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-33, readOnly=False)
Q17 = visual.TextStim(win=win, name='Q17',
    text='Q17. When the system gives unusual advice I am\nconfident that the advice is correct.',
    font='Open Sans',
    pos=(-0.45, -0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-34.0);
Q17_Slider = visual.Slider(win=win, name='Q17_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,-0.2), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-35, readOnly=False)
Q18 = visual.TextStim(win=win, name='Q18',
    text='Q18. Even if I have no reason to expect the system will be \nable to solve a difficult problem, I still feel certain that it will.',
    font='Open Sans',
    pos=(-0.45,-0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-36.0);
Q18_Slider = visual.Slider(win=win, name='Q18_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,-0.35), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-37, readOnly=False)
Q19 = visual.TextStim(win=win, name='Q19',
    text='Q19. I would feel a sense of loss if the system was \nunavailable and I could no longer use it.',
    font='Open Sans',
    pos=(0.45, 0.45), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-38.0);
Q19_Slider = visual.Slider(win=win, name='Q19_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,0.4), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-39, readOnly=False)
Q20 = visual.TextStim(win=win, name='Q20',
    text='Q20.  I feel a sense of attachment to using the system.',
    font='Open Sans',
    pos=(0.45, 0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-40.0);
Q20_Slider = visual.Slider(win=win, name='Q20_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,0.25), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-41, readOnly=False)
Q21 = visual.TextStim(win=win, name='Q21',
    text='Q21. I find the system suitable to my style of decision making.',
    font='Open Sans',
    pos=(0.45, 0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-42.0);
Q21_Slider = visual.Slider(win=win, name='Q21_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,0.1), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-43, readOnly=False)
Q22 = visual.TextStim(win=win, name='Q22',
    text='Q22.  I like using the system for decision making.',
    font='Open Sans',
    pos=(0.45, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-44.0);
Q22_Slider = visual.Slider(win=win, name='Q22_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,-0.05), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-45, readOnly=False)
Q23 = visual.TextStim(win=win, name='Q23',
    text='Q23. I have a personal preference for making decisions\nwith the system.\n\n',
    font='Open Sans',
    pos=(0.45, -0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-46.0);
Q23_Slider = visual.Slider(win=win, name='Q23_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,-0.2), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-47, readOnly=False)

# Initialize components for Routine "Text_Break"
Text_BreakClock = core.Clock()
Text_Break_Txt = visual.TextStim(win=win, name='Text_Break_Txt',
    text='You will now be going onto the next set of questions in the experiment',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
PresstoCont_3 = visual.TextStim(win=win, name='PresstoCont_3',
    text='(Please press space bar when ready to continue)',
    font='Open Sans',
    pos=(0, -0.45), height=0.025, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
KeyResp_3 = keyboard.Keyboard()

# Initialize components for Routine "Text_Based"
Text_BasedClock = core.Clock()
Text_Intro_Txt = visual.TextStim(win=win, name='Text_Intro_Txt',
    text='Please wait for the question to be administered',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Question_Txt_5 = visual.TextStim(win=win, name='Question_Txt_5',
    text='',
    font='Open Sans',
    pos=(-0.475, 0.48), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
AI_Response_5 = visual.TextStim(win=win, name='AI_Response_5',
    text='',
    font='Open Sans',
    pos=(-0.45, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Accept_Deny_Button_5 = visual.Slider(win=win, name='Accept_Deny_Button_5',
    startValue=1, size=(0.25, 0.05), pos=(-0.45, -0.1), units=None,
    labels=["Accept","Deny"], ticks=(1,2), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-3, readOnly=False)
ConfidenceText_5 = visual.TextStim(win=win, name='ConfidenceText_5',
    text='Level of confidence in your answer:',
    font='Open Sans',
    pos=(-0.45, -0.25), height=0.02, wrapWidth=None, ori=1.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
ConfidenceSlider_5 = visual.Slider(win=win, name='ConfidenceSlider_5',
    startValue=None, size=(0.4, 0.05), pos=(-0.45, -0.3), units=None,
    labels=["1", "2", "3", "4", "5"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='Black', markerColor='Red', lineColor='Black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=False, ori=0.0, depth=-5, readOnly=False)
Experimental_Images_5 = visual.ImageStim(
    win=win,
    name='Experimental_Images_5', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.45, 0.25), size=(0.5, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
IfDenied_5 = visual.TextStim(win=win, name='IfDenied_5',
    text='How did you decide on your answer?\n\nA.) By myself\nB.) Based on AI Output alone\nC.) A combination of both\n',
    font='Open Sans',
    pos=(0.4, -0.1), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
DenySlider_5 = visual.Slider(win=win, name='DenySlider_5',
    startValue=None, size=(0.2, 0.05), pos=(0.4, -0.2), units=None,
    labels=["A", "B", "C"], ticks=(1, 2, 3), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='white', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-8, readOnly=False)
mouse_8 = event.Mouse(win=win)
x, y = [None, None]
mouse_8.mouseClock = core.Clock()
Click_to_Continue_8 = visual.ImageStim(
    win=win,
    name='Click_to_Continue_8', 
    image='Continue.JPG', mask=None, anchor='center',
    ori=0.0, pos=(0.55, -0.45), size=(0.12, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
AI_Response_Txt_5 = visual.TextStim(win=win, name='AI_Response_Txt_5',
    text='',
    font='Open Sans',
    pos=(0.475, 0.48), height=0.0225, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
Explanation_Image_5 = visual.ImageStim(
    win=win,
    name='Explanation_Image_5', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.45, 0.225), size=(0.7, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)

# Initialize components for Routine "Text_Survey_Break"
Text_Survey_BreakClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='You will now be going onto the corresponding survey portion of the experiment. Please read and answer all of the questions to the best of your ability',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
PresstoCont_2 = visual.TextStim(win=win, name='PresstoCont_2',
    text='(Please press space bar when ready to continue)',
    font='Open Sans',
    pos=(0, -0.45), height=0.025, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
KeyResp_2 = keyboard.Keyboard()

# Initialize components for Routine "Survey_Trial"
Survey_TrialClock = core.Clock()
Q1 = visual.TextStim(win=win, name='Q1',
    text='Q1. The system always provides the advice I require to make my decision.',
    font='Open Sans',
    pos=(-0.45, 0.45), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Q1_Slider = visual.Slider(win=win, name='Q1_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,0.4), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-1, readOnly=False)
Q2 = visual.TextStim(win=win, name='Q2',
    text='Q2. The system performs reliably.',
    font='Open Sans',
    pos=(-0.45, 0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Q2_Slider = visual.Slider(win=win, name='Q2_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,0.25), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-3, readOnly=False)
Q3 = visual.TextStim(win=win, name='Q3',
    text='Q3. The system responds the same way under the same \nconditions at different times.',
    font='Open Sans',
    pos=(-0.45, 0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
Q3_Slider = visual.Slider(win=win, name='Q3_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,0.1), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-5, readOnly=False)
Q4 = visual.TextStim(win=win, name='Q4',
    text='Q4. I can rely on the system to function properly.',
    font='Open Sans',
    pos=(-0.45, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
Q4_Slider = visual.Slider(win=win, name='Q4_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,-0.05), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-7, readOnly=False)
Q5 = visual.TextStim(win=win, name='Q5',
    text='Q5. The system analyzes problems consistently.',
    font='Open Sans',
    pos=(-0.45, -0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
Q5_Slider = visual.Slider(win=win, name='Q5_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,-0.2), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-9, readOnly=False)
Q6 = visual.TextStim(win=win, name='Q6',
    text='Q6. The system uses appropriate methods to reach decisions.',
    font='Open Sans',
    pos=(-0.45,-0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
Q6_Slider = visual.Slider(win=win, name='Q6_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,-0.35), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-11, readOnly=False)
Q7 = visual.TextStim(win=win, name='Q7',
    text='Q7. The system has sound knowledge about this type of \nproblem built into it.',
    font='Open Sans',
    pos=(0.45, 0.45), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-12.0);
Q7_Slider = visual.Slider(win=win, name='Q7_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,0.4), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-13, readOnly=False)
Q8 = visual.TextStim(win=win, name='Q8',
    text='Q8. The advice the system produces is as good as that \nwhich a highly competent person could produce.',
    font='Open Sans',
    pos=(0.45, 0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-14.0);
Q8_Slider = visual.Slider(win=win, name='Q8_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,0.25), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-15, readOnly=False)
Q9 = visual.TextStim(win=win, name='Q9',
    text='Q9. I know what will happen the next time I use the \nsystem because I understand how it behaves.',
    font='Open Sans',
    pos=(0.45, 0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-16.0);
Q9_Slider = visual.Slider(win=win, name='Q9_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,0.1), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-17, readOnly=False)
Q10 = visual.TextStim(win=win, name='Q10',
    text='Q10. I understand how the system will assist me with \ndecisions I have to make.',
    font='Open Sans',
    pos=(0.45, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-18.0);
Q10_Slider = visual.Slider(win=win, name='Q10_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,-0.05), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-19, readOnly=False)
Q11 = visual.TextStim(win=win, name='Q11',
    text='Q11. Although I may not know exactly how the system works,\nI know how to use it to make decisions about the problem.\n\n',
    font='Open Sans',
    pos=(0.45, -0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-20.0);
Q11_Slider = visual.Slider(win=win, name='Q11_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,-0.2), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-21, readOnly=False)
Q12 = visual.TextStim(win=win, name='Q12',
    text='Q12. It is easy to follow what the system does.',
    font='Open Sans',
    pos=(0.45,-0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-22.0);
Q12_Slider = visual.Slider(win=win, name='Q12_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,-0.35), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-23, readOnly=False)
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()
Click_to_Continue_2 = visual.ImageStim(
    win=win,
    name='Click_to_Continue_2', 
    image='Continue.JPG', mask=None, anchor='center',
    ori=0.0, pos=(0.55, -0.45), size=(0.12, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-25.0)
Q13 = visual.TextStim(win=win, name='Q13',
    text='Q13. I recognize what I should do to get the advice I\nneed from the system the next time I use it.',
    font='Open Sans',
    pos=(-0.45, 0.45), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-26.0);
Q13_Slider = visual.Slider(win=win, name='Q13_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,0.4), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-27, readOnly=False)
Q14 = visual.TextStim(win=win, name='Q14',
    text='Q14. I believe advice from the system even when I\ndon’t know for certain that it is correct.',
    font='Open Sans',
    pos=(-0.45, 0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-28.0);
Q14_Slider = visual.Slider(win=win, name='Q14_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,0.25), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-29, readOnly=False)
Q15 = visual.TextStim(win=win, name='Q15',
    text='Q15. When I am uncertain about a decision I believe \nthe system rather than myself.',
    font='Open Sans',
    pos=(-0.45, 0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-30.0);
Q15_Slider = visual.Slider(win=win, name='Q15_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,0.1), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-31, readOnly=False)
Q16 = visual.TextStim(win=win, name='Q16',
    text='Q16. If I am not sure about a decision, I have faith that the\nsystem will provide the best solution.',
    font='Open Sans',
    pos=(-0.45, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-32.0);
Q16_Slider = visual.Slider(win=win, name='Q16_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,-0.05), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-33, readOnly=False)
Q17 = visual.TextStim(win=win, name='Q17',
    text='Q17. When the system gives unusual advice I am\nconfident that the advice is correct.',
    font='Open Sans',
    pos=(-0.45, -0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-34.0);
Q17_Slider = visual.Slider(win=win, name='Q17_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,-0.2), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-35, readOnly=False)
Q18 = visual.TextStim(win=win, name='Q18',
    text='Q18. Even if I have no reason to expect the system will be \nable to solve a difficult problem, I still feel certain that it will.',
    font='Open Sans',
    pos=(-0.45,-0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-36.0);
Q18_Slider = visual.Slider(win=win, name='Q18_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,-0.35), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-37, readOnly=False)
Q19 = visual.TextStim(win=win, name='Q19',
    text='Q19. I would feel a sense of loss if the system was \nunavailable and I could no longer use it.',
    font='Open Sans',
    pos=(0.45, 0.45), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-38.0);
Q19_Slider = visual.Slider(win=win, name='Q19_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,0.4), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-39, readOnly=False)
Q20 = visual.TextStim(win=win, name='Q20',
    text='Q20.  I feel a sense of attachment to using the system.',
    font='Open Sans',
    pos=(0.45, 0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-40.0);
Q20_Slider = visual.Slider(win=win, name='Q20_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,0.25), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-41, readOnly=False)
Q21 = visual.TextStim(win=win, name='Q21',
    text='Q21. I find the system suitable to my style of decision making.',
    font='Open Sans',
    pos=(0.45, 0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-42.0);
Q21_Slider = visual.Slider(win=win, name='Q21_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,0.1), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-43, readOnly=False)
Q22 = visual.TextStim(win=win, name='Q22',
    text='Q22.  I like using the system for decision making.',
    font='Open Sans',
    pos=(0.45, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-44.0);
Q22_Slider = visual.Slider(win=win, name='Q22_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,-0.05), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-45, readOnly=False)
Q23 = visual.TextStim(win=win, name='Q23',
    text='Q23. I have a personal preference for making decisions\nwith the system.\n\n',
    font='Open Sans',
    pos=(0.45, -0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-46.0);
Q23_Slider = visual.Slider(win=win, name='Q23_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,-0.2), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-47, readOnly=False)

# Initialize components for Routine "Image_Break"
Image_BreakClock = core.Clock()
Image_Break_Txt = visual.TextStim(win=win, name='Image_Break_Txt',
    text='You will now be going onto the next set of questions in the experiment',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
PresstoCont_5 = visual.TextStim(win=win, name='PresstoCont_5',
    text='(Please press space bar when ready to continue)',
    font='Open Sans',
    pos=(0, -0.45), height=0.025, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
KeyResp_5 = keyboard.Keyboard()

# Initialize components for Routine "Image_Based"
Image_BasedClock = core.Clock()
Image_Intro_Txt = visual.TextStim(win=win, name='Image_Intro_Txt',
    text='Please wait for the question to be administered',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Question_Txt_4 = visual.TextStim(win=win, name='Question_Txt_4',
    text='',
    font='Open Sans',
    pos=(-0.475, 0.48), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
AI_Response_4 = visual.TextStim(win=win, name='AI_Response_4',
    text='',
    font='Open Sans',
    pos=(-0.45, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Accept_Deny_Button_4 = visual.Slider(win=win, name='Accept_Deny_Button_4',
    startValue=1, size=(0.25, 0.05), pos=(-0.45, -0.1), units=None,
    labels=["Accept","Deny"], ticks=(1,2), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-3, readOnly=False)
ConfidenceText_4 = visual.TextStim(win=win, name='ConfidenceText_4',
    text='Level of confidence in your answer:',
    font='Open Sans',
    pos=(-0.45, -0.25), height=0.02, wrapWidth=None, ori=1.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
ConfidenceSlider_4 = visual.Slider(win=win, name='ConfidenceSlider_4',
    startValue=None, size=(0.4, 0.05), pos=(-0.45, -0.3), units=None,
    labels=["1", "2", "3", "4", "5"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='Black', markerColor='Red', lineColor='Black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=False, ori=0.0, depth=-5, readOnly=False)
Experimental_Images_4 = visual.ImageStim(
    win=win,
    name='Experimental_Images_4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.45, 0.25), size=(0.5, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
IfDenied_4 = visual.TextStim(win=win, name='IfDenied_4',
    text='How did you decide on your answer?\n\nA.) By myself\nB.) Based on AI Output alone\nC.) A combination of both\n',
    font='Open Sans',
    pos=(0.4, -0.1), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
DenySlider_4 = visual.Slider(win=win, name='DenySlider_4',
    startValue=None, size=(0.2, 0.05), pos=(0.4, -0.2), units=None,
    labels=["A", "B", "C"], ticks=(1, 2, 3), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='white', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-8, readOnly=False)
mouse_7 = event.Mouse(win=win)
x, y = [None, None]
mouse_7.mouseClock = core.Clock()
Click_to_Continue_7 = visual.ImageStim(
    win=win,
    name='Click_to_Continue_7', 
    image='Continue.JPG', mask=None, anchor='center',
    ori=0.0, pos=(0.55, -0.45), size=(0.12, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
AI_Response_Txt_4 = visual.TextStim(win=win, name='AI_Response_Txt_4',
    text='',
    font='Open Sans',
    pos=(0.475, 0.48), height=0.0225, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
Explanation_Image_4 = visual.ImageStim(
    win=win,
    name='Explanation_Image_4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.45, 0.225), size=(0.7, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)

# Initialize components for Routine "Image_Survey_Break"
Image_Survey_BreakClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='You will now be going onto the corresponding survey portion of the experiment. Please read and answer all of the questions to the best of your ability',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
PresstoCont_7 = visual.TextStim(win=win, name='PresstoCont_7',
    text='(Please press space bar when ready to continue)',
    font='Open Sans',
    pos=(0, -0.45), height=0.025, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
KeyResp_7 = keyboard.Keyboard()

# Initialize components for Routine "Survey_Trial"
Survey_TrialClock = core.Clock()
Q1 = visual.TextStim(win=win, name='Q1',
    text='Q1. The system always provides the advice I require to make my decision.',
    font='Open Sans',
    pos=(-0.45, 0.45), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Q1_Slider = visual.Slider(win=win, name='Q1_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,0.4), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-1, readOnly=False)
Q2 = visual.TextStim(win=win, name='Q2',
    text='Q2. The system performs reliably.',
    font='Open Sans',
    pos=(-0.45, 0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Q2_Slider = visual.Slider(win=win, name='Q2_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,0.25), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-3, readOnly=False)
Q3 = visual.TextStim(win=win, name='Q3',
    text='Q3. The system responds the same way under the same \nconditions at different times.',
    font='Open Sans',
    pos=(-0.45, 0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
Q3_Slider = visual.Slider(win=win, name='Q3_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,0.1), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-5, readOnly=False)
Q4 = visual.TextStim(win=win, name='Q4',
    text='Q4. I can rely on the system to function properly.',
    font='Open Sans',
    pos=(-0.45, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
Q4_Slider = visual.Slider(win=win, name='Q4_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,-0.05), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-7, readOnly=False)
Q5 = visual.TextStim(win=win, name='Q5',
    text='Q5. The system analyzes problems consistently.',
    font='Open Sans',
    pos=(-0.45, -0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
Q5_Slider = visual.Slider(win=win, name='Q5_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,-0.2), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-9, readOnly=False)
Q6 = visual.TextStim(win=win, name='Q6',
    text='Q6. The system uses appropriate methods to reach decisions.',
    font='Open Sans',
    pos=(-0.45,-0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
Q6_Slider = visual.Slider(win=win, name='Q6_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,-0.35), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-11, readOnly=False)
Q7 = visual.TextStim(win=win, name='Q7',
    text='Q7. The system has sound knowledge about this type of \nproblem built into it.',
    font='Open Sans',
    pos=(0.45, 0.45), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-12.0);
Q7_Slider = visual.Slider(win=win, name='Q7_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,0.4), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-13, readOnly=False)
Q8 = visual.TextStim(win=win, name='Q8',
    text='Q8. The advice the system produces is as good as that \nwhich a highly competent person could produce.',
    font='Open Sans',
    pos=(0.45, 0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-14.0);
Q8_Slider = visual.Slider(win=win, name='Q8_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,0.25), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-15, readOnly=False)
Q9 = visual.TextStim(win=win, name='Q9',
    text='Q9. I know what will happen the next time I use the \nsystem because I understand how it behaves.',
    font='Open Sans',
    pos=(0.45, 0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-16.0);
Q9_Slider = visual.Slider(win=win, name='Q9_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,0.1), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-17, readOnly=False)
Q10 = visual.TextStim(win=win, name='Q10',
    text='Q10. I understand how the system will assist me with \ndecisions I have to make.',
    font='Open Sans',
    pos=(0.45, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-18.0);
Q10_Slider = visual.Slider(win=win, name='Q10_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,-0.05), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-19, readOnly=False)
Q11 = visual.TextStim(win=win, name='Q11',
    text='Q11. Although I may not know exactly how the system works,\nI know how to use it to make decisions about the problem.\n\n',
    font='Open Sans',
    pos=(0.45, -0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-20.0);
Q11_Slider = visual.Slider(win=win, name='Q11_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,-0.2), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-21, readOnly=False)
Q12 = visual.TextStim(win=win, name='Q12',
    text='Q12. It is easy to follow what the system does.',
    font='Open Sans',
    pos=(0.45,-0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-22.0);
Q12_Slider = visual.Slider(win=win, name='Q12_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,-0.35), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-23, readOnly=False)
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()
Click_to_Continue_2 = visual.ImageStim(
    win=win,
    name='Click_to_Continue_2', 
    image='Continue.JPG', mask=None, anchor='center',
    ori=0.0, pos=(0.55, -0.45), size=(0.12, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-25.0)
Q13 = visual.TextStim(win=win, name='Q13',
    text='Q13. I recognize what I should do to get the advice I\nneed from the system the next time I use it.',
    font='Open Sans',
    pos=(-0.45, 0.45), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-26.0);
Q13_Slider = visual.Slider(win=win, name='Q13_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,0.4), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-27, readOnly=False)
Q14 = visual.TextStim(win=win, name='Q14',
    text='Q14. I believe advice from the system even when I\ndon’t know for certain that it is correct.',
    font='Open Sans',
    pos=(-0.45, 0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-28.0);
Q14_Slider = visual.Slider(win=win, name='Q14_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,0.25), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-29, readOnly=False)
Q15 = visual.TextStim(win=win, name='Q15',
    text='Q15. When I am uncertain about a decision I believe \nthe system rather than myself.',
    font='Open Sans',
    pos=(-0.45, 0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-30.0);
Q15_Slider = visual.Slider(win=win, name='Q15_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,0.1), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-31, readOnly=False)
Q16 = visual.TextStim(win=win, name='Q16',
    text='Q16. If I am not sure about a decision, I have faith that the\nsystem will provide the best solution.',
    font='Open Sans',
    pos=(-0.45, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-32.0);
Q16_Slider = visual.Slider(win=win, name='Q16_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,-0.05), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-33, readOnly=False)
Q17 = visual.TextStim(win=win, name='Q17',
    text='Q17. When the system gives unusual advice I am\nconfident that the advice is correct.',
    font='Open Sans',
    pos=(-0.45, -0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-34.0);
Q17_Slider = visual.Slider(win=win, name='Q17_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,-0.2), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-35, readOnly=False)
Q18 = visual.TextStim(win=win, name='Q18',
    text='Q18. Even if I have no reason to expect the system will be \nable to solve a difficult problem, I still feel certain that it will.',
    font='Open Sans',
    pos=(-0.45,-0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-36.0);
Q18_Slider = visual.Slider(win=win, name='Q18_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,-0.35), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-37, readOnly=False)
Q19 = visual.TextStim(win=win, name='Q19',
    text='Q19. I would feel a sense of loss if the system was \nunavailable and I could no longer use it.',
    font='Open Sans',
    pos=(0.45, 0.45), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-38.0);
Q19_Slider = visual.Slider(win=win, name='Q19_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,0.4), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-39, readOnly=False)
Q20 = visual.TextStim(win=win, name='Q20',
    text='Q20.  I feel a sense of attachment to using the system.',
    font='Open Sans',
    pos=(0.45, 0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-40.0);
Q20_Slider = visual.Slider(win=win, name='Q20_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,0.25), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-41, readOnly=False)
Q21 = visual.TextStim(win=win, name='Q21',
    text='Q21. I find the system suitable to my style of decision making.',
    font='Open Sans',
    pos=(0.45, 0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-42.0);
Q21_Slider = visual.Slider(win=win, name='Q21_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,0.1), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-43, readOnly=False)
Q22 = visual.TextStim(win=win, name='Q22',
    text='Q22.  I like using the system for decision making.',
    font='Open Sans',
    pos=(0.45, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-44.0);
Q22_Slider = visual.Slider(win=win, name='Q22_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,-0.05), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-45, readOnly=False)
Q23 = visual.TextStim(win=win, name='Q23',
    text='Q23. I have a personal preference for making decisions\nwith the system.\n\n',
    font='Open Sans',
    pos=(0.45, -0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-46.0);
Q23_Slider = visual.Slider(win=win, name='Q23_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,-0.2), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-47, readOnly=False)

# Initialize components for Routine "Feature_Break"
Feature_BreakClock = core.Clock()
Feature_Break_Txt = visual.TextStim(win=win, name='Feature_Break_Txt',
    text='You will now be going onto the next set of questions in the experiment',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
PresstoCont_6 = visual.TextStim(win=win, name='PresstoCont_6',
    text='(Please press space bar when ready to continue)',
    font='Open Sans',
    pos=(0, -0.45), height=0.025, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
KeyResp_6 = keyboard.Keyboard()

# Initialize components for Routine "Feature_Based"
Feature_BasedClock = core.Clock()
Feature_Intro_Txt = visual.TextStim(win=win, name='Feature_Intro_Txt',
    text='Please wait for the question to be administered',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
AI_Response_3 = visual.TextStim(win=win, name='AI_Response_3',
    text='',
    font='Open Sans',
    pos=(-0.45, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Question_Txt_3 = visual.TextStim(win=win, name='Question_Txt_3',
    text='',
    font='Open Sans',
    pos=(-0.475, 0.48), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Accept_Deny_Button_3 = visual.Slider(win=win, name='Accept_Deny_Button_3',
    startValue=1, size=(0.25, 0.05), pos=(-0.45, -0.1), units=None,
    labels=["Accept","Deny"], ticks=(1,2), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-3, readOnly=False)
ConfidenceText_3 = visual.TextStim(win=win, name='ConfidenceText_3',
    text='Level of confidence in your answer:',
    font='Open Sans',
    pos=(-0.45, -0.25), height=0.02, wrapWidth=None, ori=1.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
ConfidenceSlider_3 = visual.Slider(win=win, name='ConfidenceSlider_3',
    startValue=None, size=(0.4, 0.05), pos=(-0.45, -0.3), units=None,
    labels=["1", "2", "3", "4", "5"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='Black', markerColor='Red', lineColor='Black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=False, ori=0.0, depth=-5, readOnly=False)
Experimental_Images_3 = visual.ImageStim(
    win=win,
    name='Experimental_Images_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.45, 0.25), size=(0.5, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
IfDenied_3 = visual.TextStim(win=win, name='IfDenied_3',
    text='How did you decide on your answer?\n\nA.) By myself\nB.) Based on AI Output alone\nC.) A combination of both\n',
    font='Open Sans',
    pos=(0.4, -0.1), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
DenySlider_3 = visual.Slider(win=win, name='DenySlider_3',
    startValue=None, size=(0.2, 0.05), pos=(0.4, -0.2), units=None,
    labels=["A", "B", "C"], ticks=(1, 2, 3), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='white', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-8, readOnly=False)
mouse_6 = event.Mouse(win=win)
x, y = [None, None]
mouse_6.mouseClock = core.Clock()
Click_to_Continue_6 = visual.ImageStim(
    win=win,
    name='Click_to_Continue_6', 
    image='Continue.JPG', mask=None, anchor='center',
    ori=0.0, pos=(0.55, -0.45), size=(0.12, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
AI_Response_Txt_3 = visual.TextStim(win=win, name='AI_Response_Txt_3',
    text='',
    font='Open Sans',
    pos=(0.475, 0.48), height=0.0225, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
Explanation_Image_3 = visual.ImageStim(
    win=win,
    name='Explanation_Image_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.45, 0.225), size=(0.7, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)

# Initialize components for Routine "Feature_Survey_Break"
Feature_Survey_BreakClock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='You will now be going onto the corresponding survey portion of the experiment. Please read and answer all of the questions to the best of your ability',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
PresstoCont_8 = visual.TextStim(win=win, name='PresstoCont_8',
    text='(Please press space bar when ready to continue)',
    font='Open Sans',
    pos=(0, -0.45), height=0.025, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
KeyResp_8 = keyboard.Keyboard()

# Initialize components for Routine "Survey_Trial"
Survey_TrialClock = core.Clock()
Q1 = visual.TextStim(win=win, name='Q1',
    text='Q1. The system always provides the advice I require to make my decision.',
    font='Open Sans',
    pos=(-0.45, 0.45), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Q1_Slider = visual.Slider(win=win, name='Q1_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,0.4), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-1, readOnly=False)
Q2 = visual.TextStim(win=win, name='Q2',
    text='Q2. The system performs reliably.',
    font='Open Sans',
    pos=(-0.45, 0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Q2_Slider = visual.Slider(win=win, name='Q2_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,0.25), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-3, readOnly=False)
Q3 = visual.TextStim(win=win, name='Q3',
    text='Q3. The system responds the same way under the same \nconditions at different times.',
    font='Open Sans',
    pos=(-0.45, 0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
Q3_Slider = visual.Slider(win=win, name='Q3_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,0.1), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-5, readOnly=False)
Q4 = visual.TextStim(win=win, name='Q4',
    text='Q4. I can rely on the system to function properly.',
    font='Open Sans',
    pos=(-0.45, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
Q4_Slider = visual.Slider(win=win, name='Q4_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,-0.05), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-7, readOnly=False)
Q5 = visual.TextStim(win=win, name='Q5',
    text='Q5. The system analyzes problems consistently.',
    font='Open Sans',
    pos=(-0.45, -0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
Q5_Slider = visual.Slider(win=win, name='Q5_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,-0.2), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-9, readOnly=False)
Q6 = visual.TextStim(win=win, name='Q6',
    text='Q6. The system uses appropriate methods to reach decisions.',
    font='Open Sans',
    pos=(-0.45,-0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
Q6_Slider = visual.Slider(win=win, name='Q6_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,-0.35), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-11, readOnly=False)
Q7 = visual.TextStim(win=win, name='Q7',
    text='Q7. The system has sound knowledge about this type of \nproblem built into it.',
    font='Open Sans',
    pos=(0.45, 0.45), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-12.0);
Q7_Slider = visual.Slider(win=win, name='Q7_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,0.4), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-13, readOnly=False)
Q8 = visual.TextStim(win=win, name='Q8',
    text='Q8. The advice the system produces is as good as that \nwhich a highly competent person could produce.',
    font='Open Sans',
    pos=(0.45, 0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-14.0);
Q8_Slider = visual.Slider(win=win, name='Q8_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,0.25), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-15, readOnly=False)
Q9 = visual.TextStim(win=win, name='Q9',
    text='Q9. I know what will happen the next time I use the \nsystem because I understand how it behaves.',
    font='Open Sans',
    pos=(0.45, 0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-16.0);
Q9_Slider = visual.Slider(win=win, name='Q9_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,0.1), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-17, readOnly=False)
Q10 = visual.TextStim(win=win, name='Q10',
    text='Q10. I understand how the system will assist me with \ndecisions I have to make.',
    font='Open Sans',
    pos=(0.45, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-18.0);
Q10_Slider = visual.Slider(win=win, name='Q10_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,-0.05), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-19, readOnly=False)
Q11 = visual.TextStim(win=win, name='Q11',
    text='Q11. Although I may not know exactly how the system works,\nI know how to use it to make decisions about the problem.\n\n',
    font='Open Sans',
    pos=(0.45, -0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-20.0);
Q11_Slider = visual.Slider(win=win, name='Q11_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,-0.2), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-21, readOnly=False)
Q12 = visual.TextStim(win=win, name='Q12',
    text='Q12. It is easy to follow what the system does.',
    font='Open Sans',
    pos=(0.45,-0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-22.0);
Q12_Slider = visual.Slider(win=win, name='Q12_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,-0.35), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-23, readOnly=False)
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()
Click_to_Continue_2 = visual.ImageStim(
    win=win,
    name='Click_to_Continue_2', 
    image='Continue.JPG', mask=None, anchor='center',
    ori=0.0, pos=(0.55, -0.45), size=(0.12, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-25.0)
Q13 = visual.TextStim(win=win, name='Q13',
    text='Q13. I recognize what I should do to get the advice I\nneed from the system the next time I use it.',
    font='Open Sans',
    pos=(-0.45, 0.45), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-26.0);
Q13_Slider = visual.Slider(win=win, name='Q13_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,0.4), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-27, readOnly=False)
Q14 = visual.TextStim(win=win, name='Q14',
    text='Q14. I believe advice from the system even when I\ndon’t know for certain that it is correct.',
    font='Open Sans',
    pos=(-0.45, 0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-28.0);
Q14_Slider = visual.Slider(win=win, name='Q14_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,0.25), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-29, readOnly=False)
Q15 = visual.TextStim(win=win, name='Q15',
    text='Q15. When I am uncertain about a decision I believe \nthe system rather than myself.',
    font='Open Sans',
    pos=(-0.45, 0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-30.0);
Q15_Slider = visual.Slider(win=win, name='Q15_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,0.1), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-31, readOnly=False)
Q16 = visual.TextStim(win=win, name='Q16',
    text='Q16. If I am not sure about a decision, I have faith that the\nsystem will provide the best solution.',
    font='Open Sans',
    pos=(-0.45, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-32.0);
Q16_Slider = visual.Slider(win=win, name='Q16_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,-0.05), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-33, readOnly=False)
Q17 = visual.TextStim(win=win, name='Q17',
    text='Q17. When the system gives unusual advice I am\nconfident that the advice is correct.',
    font='Open Sans',
    pos=(-0.45, -0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-34.0);
Q17_Slider = visual.Slider(win=win, name='Q17_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,-0.2), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-35, readOnly=False)
Q18 = visual.TextStim(win=win, name='Q18',
    text='Q18. Even if I have no reason to expect the system will be \nable to solve a difficult problem, I still feel certain that it will.',
    font='Open Sans',
    pos=(-0.45,-0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-36.0);
Q18_Slider = visual.Slider(win=win, name='Q18_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,-0.35), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-37, readOnly=False)
Q19 = visual.TextStim(win=win, name='Q19',
    text='Q19. I would feel a sense of loss if the system was \nunavailable and I could no longer use it.',
    font='Open Sans',
    pos=(0.45, 0.45), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-38.0);
Q19_Slider = visual.Slider(win=win, name='Q19_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,0.4), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-39, readOnly=False)
Q20 = visual.TextStim(win=win, name='Q20',
    text='Q20.  I feel a sense of attachment to using the system.',
    font='Open Sans',
    pos=(0.45, 0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-40.0);
Q20_Slider = visual.Slider(win=win, name='Q20_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,0.25), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-41, readOnly=False)
Q21 = visual.TextStim(win=win, name='Q21',
    text='Q21. I find the system suitable to my style of decision making.',
    font='Open Sans',
    pos=(0.45, 0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-42.0);
Q21_Slider = visual.Slider(win=win, name='Q21_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,0.1), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-43, readOnly=False)
Q22 = visual.TextStim(win=win, name='Q22',
    text='Q22.  I like using the system for decision making.',
    font='Open Sans',
    pos=(0.45, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-44.0);
Q22_Slider = visual.Slider(win=win, name='Q22_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,-0.05), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-45, readOnly=False)
Q23 = visual.TextStim(win=win, name='Q23',
    text='Q23. I have a personal preference for making decisions\nwith the system.\n\n',
    font='Open Sans',
    pos=(0.45, -0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-46.0);
Q23_Slider = visual.Slider(win=win, name='Q23_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,-0.2), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-47, readOnly=False)

# Initialize components for Routine "Break"
BreakClock = core.Clock()
Break_Txt = visual.TextStim(win=win, name='Break_Txt',
    text='You will now be going onto the next set of questions in the experiment',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Break_PresstoCont = visual.TextStim(win=win, name='Break_PresstoCont',
    text='(Please press space bar when ready to continue)',
    font='Open Sans',
    pos=(0, -0.45), height=0.025, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Break_KeyResp = keyboard.Keyboard()

# Initialize components for Routine "Choice_Trial"
Choice_TrialClock = core.Clock()
Intro_Text = visual.TextStim(win=win, name='Intro_Text',
    text='You will now have the option to pick  from four differnt AI \nresponse types for the last part of the experiment:\n\nPlease choose from the following:',
    font='Open Sans',
    pos=(0, 0.2), height=0.0275, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Stim_slider = visual.Slider(win=win, name='Stim_slider',
    startValue=None, size=(0.6, 0.05), pos=(0,0), units=None,
    labels=["Conversational Based", "Feature Based", "Image Based", "Text Based"], ticks=(1,2,3,4), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.0175,
    flip=False, ori=0.0, depth=-1, readOnly=False)
mouse_5 = event.Mouse(win=win)
x, y = [None, None]
mouse_5.mouseClock = core.Clock()
Click_to_Continue_5 = visual.ImageStim(
    win=win,
    name='Click_to_Continue_5', 
    image='Continue.JPG', mask=None, anchor='center',
    ori=0.0, pos=(0.55, -0.2), size=(0.12, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# Initialize components for Routine "Choice_Break"
Choice_BreakClock = core.Clock()
Choice_Break_Txt = visual.TextStim(win=win, name='Choice_Break_Txt',
    text='You will now be going onto the next set of questions in the experiment',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Choice_Break_PresstoCont = visual.TextStim(win=win, name='Choice_Break_PresstoCont',
    text='(Please press space bar when ready to continue)',
    font='Open Sans',
    pos=(0, -0.45), height=0.025, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Choice_Break_KeyResp = keyboard.Keyboard()

# Initialize components for Routine "Choice_1"
Choice_1Clock = core.Clock()
Choice_1_Intro_Txt = visual.TextStim(win=win, name='Choice_1_Intro_Txt',
    text='Please wait for the question to be administered',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Question_Txt_6 = visual.TextStim(win=win, name='Question_Txt_6',
    text='',
    font='Open Sans',
    pos=(-0.475, 0.48), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
AI_Response_6 = visual.TextStim(win=win, name='AI_Response_6',
    text='',
    font='Open Sans',
    pos=(-0.45, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Accept_Deny_Button_6 = visual.Slider(win=win, name='Accept_Deny_Button_6',
    startValue=1, size=(0.25, 0.05), pos=(-0.45, -0.1), units=None,
    labels=["Accept","Deny"], ticks=(1,2), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-3, readOnly=False)
ConfidenceText_6 = visual.TextStim(win=win, name='ConfidenceText_6',
    text='Level of confidence in your answer:',
    font='Open Sans',
    pos=(-0.45, -0.25), height=0.02, wrapWidth=None, ori=1.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
ConfidenceSlider_6 = visual.Slider(win=win, name='ConfidenceSlider_6',
    startValue=None, size=(0.4, 0.05), pos=(-0.45, -0.3), units=None,
    labels=["1", "2", "3", "4", "5"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='Black', markerColor='Red', lineColor='Black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=False, ori=0.0, depth=-5, readOnly=False)
Experimental_Images_6 = visual.ImageStim(
    win=win,
    name='Experimental_Images_6', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.45, 0.25), size=(0.5, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
IfDenied_6 = visual.TextStim(win=win, name='IfDenied_6',
    text='How did you decide on your answer?\n\nA.) By myself\nB.) Based on AI Output alone\nC.) A combination of both\n',
    font='Open Sans',
    pos=(0.4, -0.1), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
DenySlider_6 = visual.Slider(win=win, name='DenySlider_6',
    startValue=None, size=(0.2, 0.05), pos=(0.4, -0.2), units=None,
    labels=["A", "B", "C"], ticks=(1, 2, 3), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='white', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-8, readOnly=False)
mouse_9 = event.Mouse(win=win)
x, y = [None, None]
mouse_9.mouseClock = core.Clock()
Click_to_Continue_9 = visual.ImageStim(
    win=win,
    name='Click_to_Continue_9', 
    image='Continue.JPG', mask=None, anchor='center',
    ori=0.0, pos=(0.55, -0.45), size=(0.12, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
AI_Response_Txt_6 = visual.TextStim(win=win, name='AI_Response_Txt_6',
    text='',
    font='Open Sans',
    pos=(0.475, 0.48), height=0.0225, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
Explanation_Image_6 = visual.ImageStim(
    win=win,
    name='Explanation_Image_6', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.45, 0.225), size=(0.7, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)

# Initialize components for Routine "Choice_2"
Choice_2Clock = core.Clock()
Choice_2_Intro_Txt = visual.TextStim(win=win, name='Choice_2_Intro_Txt',
    text='Please wait for the question to be administered',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Question_Txt_7 = visual.TextStim(win=win, name='Question_Txt_7',
    text='',
    font='Open Sans',
    pos=(-0.475, 0.48), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
AI_Response_7 = visual.TextStim(win=win, name='AI_Response_7',
    text='',
    font='Open Sans',
    pos=(-0.45, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Accept_Deny_Button_7 = visual.Slider(win=win, name='Accept_Deny_Button_7',
    startValue=1, size=(0.25, 0.05), pos=(-0.45, -0.1), units=None,
    labels=["Accept","Deny"], ticks=(1,2), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-3, readOnly=False)
ConfidenceText_7 = visual.TextStim(win=win, name='ConfidenceText_7',
    text='Level of confidence in your answer:',
    font='Open Sans',
    pos=(-0.45, -0.25), height=0.02, wrapWidth=None, ori=1.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
ConfidenceSlider_7 = visual.Slider(win=win, name='ConfidenceSlider_7',
    startValue=None, size=(0.4, 0.05), pos=(-0.45, -0.3), units=None,
    labels=["1", "2", "3", "4", "5"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='Black', markerColor='Red', lineColor='Black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=False, ori=0.0, depth=-5, readOnly=False)
Experimental_Images_7 = visual.ImageStim(
    win=win,
    name='Experimental_Images_7', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.45, 0.25), size=(0.5, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
IfDenied_7 = visual.TextStim(win=win, name='IfDenied_7',
    text='How did you decide on your answer?\n\nA.) By myself\nB.) Based on AI Output alone\nC.) A combination of both\n',
    font='Open Sans',
    pos=(0.4, -0.1), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
DenySlider_7 = visual.Slider(win=win, name='DenySlider_7',
    startValue=None, size=(0.2, 0.05), pos=(0.4, -0.2), units=None,
    labels=["A", "B", "C"], ticks=(1, 2, 3), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='white', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-8, readOnly=False)
mouse_10 = event.Mouse(win=win)
x, y = [None, None]
mouse_10.mouseClock = core.Clock()
Click_to_Continue_10 = visual.ImageStim(
    win=win,
    name='Click_to_Continue_10', 
    image='Continue.JPG', mask=None, anchor='center',
    ori=0.0, pos=(0.55, -0.45), size=(0.12, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
AI_Response_Txt_7 = visual.TextStim(win=win, name='AI_Response_Txt_7',
    text='',
    font='Open Sans',
    pos=(0.475, 0.48), height=0.0225, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
Explanation_Image_7 = visual.ImageStim(
    win=win,
    name='Explanation_Image_7', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.45, 0.225), size=(0.7, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)

# Initialize components for Routine "Choice_3"
Choice_3Clock = core.Clock()
Choice_3_Intro_Txt = visual.TextStim(win=win, name='Choice_3_Intro_Txt',
    text='Please wait for the question to be administered',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Question_Txt_8 = visual.TextStim(win=win, name='Question_Txt_8',
    text='',
    font='Open Sans',
    pos=(-0.475, 0.48), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
AI_Response_8 = visual.TextStim(win=win, name='AI_Response_8',
    text='',
    font='Open Sans',
    pos=(-0.45, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Accept_Deny_Button_8 = visual.Slider(win=win, name='Accept_Deny_Button_8',
    startValue=1, size=(0.25, 0.05), pos=(-0.45, -0.1), units=None,
    labels=["Accept","Deny"], ticks=(1,2), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-3, readOnly=False)
ConfidenceText_8 = visual.TextStim(win=win, name='ConfidenceText_8',
    text='Level of confidence in your answer:',
    font='Open Sans',
    pos=(-0.45, -0.25), height=0.02, wrapWidth=None, ori=1.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
ConfidenceSlider_8 = visual.Slider(win=win, name='ConfidenceSlider_8',
    startValue=None, size=(0.4, 0.05), pos=(-0.45, -0.3), units=None,
    labels=["1", "2", "3", "4", "5"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='Black', markerColor='Red', lineColor='Black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=False, ori=0.0, depth=-5, readOnly=False)
Experimental_Images_8 = visual.ImageStim(
    win=win,
    name='Experimental_Images_8', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.45, 0.25), size=(0.5, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
IfDenied_8 = visual.TextStim(win=win, name='IfDenied_8',
    text='How did you decide on your answer?\n\nA.) By myself\nB.) Based on AI Output alone\nC.) A combination of both\n',
    font='Open Sans',
    pos=(0.4, -0.1), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
DenySlider_8 = visual.Slider(win=win, name='DenySlider_8',
    startValue=None, size=(0.2, 0.05), pos=(0.4, -0.2), units=None,
    labels=["A", "B", "C"], ticks=(1, 2, 3), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='white', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-8, readOnly=False)
mouse_11 = event.Mouse(win=win)
x, y = [None, None]
mouse_11.mouseClock = core.Clock()
Click_to_Continue_11 = visual.ImageStim(
    win=win,
    name='Click_to_Continue_11', 
    image='Continue.JPG', mask=None, anchor='center',
    ori=0.0, pos=(0.55, -0.45), size=(0.12, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
AI_Response_Txt_8 = visual.TextStim(win=win, name='AI_Response_Txt_8',
    text='',
    font='Open Sans',
    pos=(0.475, 0.48), height=0.0225, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
Explanation_Image_8 = visual.ImageStim(
    win=win,
    name='Explanation_Image_8', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.45, 0.225), size=(0.7, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)

# Initialize components for Routine "Choice_4"
Choice_4Clock = core.Clock()
Choice_4_Intro_Txt = visual.TextStim(win=win, name='Choice_4_Intro_Txt',
    text='Please wait for the question to be administered',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Question_Txt_9 = visual.TextStim(win=win, name='Question_Txt_9',
    text='',
    font='Open Sans',
    pos=(-0.475, 0.48), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
AI_Response_9 = visual.TextStim(win=win, name='AI_Response_9',
    text='',
    font='Open Sans',
    pos=(-0.45, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Accept_Deny_Button_9 = visual.Slider(win=win, name='Accept_Deny_Button_9',
    startValue=1, size=(0.25, 0.05), pos=(-0.45, -0.1), units=None,
    labels=["Accept","Deny"], ticks=(1,2), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-3, readOnly=False)
ConfidenceText_9 = visual.TextStim(win=win, name='ConfidenceText_9',
    text='Level of confidence in your answer:',
    font='Open Sans',
    pos=(-0.45, -0.25), height=0.02, wrapWidth=None, ori=1.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
ConfidenceSlider_9 = visual.Slider(win=win, name='ConfidenceSlider_9',
    startValue=None, size=(0.4, 0.05), pos=(-0.45, -0.3), units=None,
    labels=["1", "2", "3", "4", "5"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='Black', markerColor='Red', lineColor='Black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=False, ori=0.0, depth=-5, readOnly=False)
Experimental_Images_9 = visual.ImageStim(
    win=win,
    name='Experimental_Images_9', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.45, 0.25), size=(0.5, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
IfDenied_9 = visual.TextStim(win=win, name='IfDenied_9',
    text='How did you decide on your answer?\n\nA.) By myself\nB.) Based on AI Output alone\nC.) A combination of both\n',
    font='Open Sans',
    pos=(0.4, -0.1), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
DenySlider_9 = visual.Slider(win=win, name='DenySlider_9',
    startValue=None, size=(0.2, 0.05), pos=(0.4, -0.2), units=None,
    labels=["A", "B", "C"], ticks=(1, 2, 3), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='white', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-8, readOnly=False)
mouse_12 = event.Mouse(win=win)
x, y = [None, None]
mouse_12.mouseClock = core.Clock()
Click_to_Continue_12 = visual.ImageStim(
    win=win,
    name='Click_to_Continue_12', 
    image='Continue.JPG', mask=None, anchor='center',
    ori=0.0, pos=(0.55, -0.45), size=(0.12, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
AI_Response_Txt_9 = visual.TextStim(win=win, name='AI_Response_Txt_9',
    text='',
    font='Open Sans',
    pos=(0.475, 0.48), height=0.0225, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
Explanation_Image_9 = visual.ImageStim(
    win=win,
    name='Explanation_Image_9', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.45, 0.225), size=(0.7, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)

# Initialize components for Routine "Choice_Survey_Break"
Choice_Survey_BreakClock = core.Clock()
text_11 = visual.TextStim(win=win, name='text_11',
    text='You will now be going onto the corresponding survey portion of the experiment. Please read and answer all of the questions to the best of your ability',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
PresstoCont_11 = visual.TextStim(win=win, name='PresstoCont_11',
    text='(Please press space bar when ready to continue)',
    font='Open Sans',
    pos=(0, -0.45), height=0.025, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
KeyResp_11 = keyboard.Keyboard()

# Initialize components for Routine "Survey_Trial"
Survey_TrialClock = core.Clock()
Q1 = visual.TextStim(win=win, name='Q1',
    text='Q1. The system always provides the advice I require to make my decision.',
    font='Open Sans',
    pos=(-0.45, 0.45), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Q1_Slider = visual.Slider(win=win, name='Q1_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,0.4), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-1, readOnly=False)
Q2 = visual.TextStim(win=win, name='Q2',
    text='Q2. The system performs reliably.',
    font='Open Sans',
    pos=(-0.45, 0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Q2_Slider = visual.Slider(win=win, name='Q2_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,0.25), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-3, readOnly=False)
Q3 = visual.TextStim(win=win, name='Q3',
    text='Q3. The system responds the same way under the same \nconditions at different times.',
    font='Open Sans',
    pos=(-0.45, 0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
Q3_Slider = visual.Slider(win=win, name='Q3_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,0.1), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-5, readOnly=False)
Q4 = visual.TextStim(win=win, name='Q4',
    text='Q4. I can rely on the system to function properly.',
    font='Open Sans',
    pos=(-0.45, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
Q4_Slider = visual.Slider(win=win, name='Q4_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,-0.05), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-7, readOnly=False)
Q5 = visual.TextStim(win=win, name='Q5',
    text='Q5. The system analyzes problems consistently.',
    font='Open Sans',
    pos=(-0.45, -0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
Q5_Slider = visual.Slider(win=win, name='Q5_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,-0.2), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-9, readOnly=False)
Q6 = visual.TextStim(win=win, name='Q6',
    text='Q6. The system uses appropriate methods to reach decisions.',
    font='Open Sans',
    pos=(-0.45,-0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
Q6_Slider = visual.Slider(win=win, name='Q6_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,-0.35), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-11, readOnly=False)
Q7 = visual.TextStim(win=win, name='Q7',
    text='Q7. The system has sound knowledge about this type of \nproblem built into it.',
    font='Open Sans',
    pos=(0.45, 0.45), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-12.0);
Q7_Slider = visual.Slider(win=win, name='Q7_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,0.4), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-13, readOnly=False)
Q8 = visual.TextStim(win=win, name='Q8',
    text='Q8. The advice the system produces is as good as that \nwhich a highly competent person could produce.',
    font='Open Sans',
    pos=(0.45, 0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-14.0);
Q8_Slider = visual.Slider(win=win, name='Q8_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,0.25), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-15, readOnly=False)
Q9 = visual.TextStim(win=win, name='Q9',
    text='Q9. I know what will happen the next time I use the \nsystem because I understand how it behaves.',
    font='Open Sans',
    pos=(0.45, 0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-16.0);
Q9_Slider = visual.Slider(win=win, name='Q9_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,0.1), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-17, readOnly=False)
Q10 = visual.TextStim(win=win, name='Q10',
    text='Q10. I understand how the system will assist me with \ndecisions I have to make.',
    font='Open Sans',
    pos=(0.45, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-18.0);
Q10_Slider = visual.Slider(win=win, name='Q10_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,-0.05), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-19, readOnly=False)
Q11 = visual.TextStim(win=win, name='Q11',
    text='Q11. Although I may not know exactly how the system works,\nI know how to use it to make decisions about the problem.\n\n',
    font='Open Sans',
    pos=(0.45, -0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-20.0);
Q11_Slider = visual.Slider(win=win, name='Q11_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,-0.2), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-21, readOnly=False)
Q12 = visual.TextStim(win=win, name='Q12',
    text='Q12. It is easy to follow what the system does.',
    font='Open Sans',
    pos=(0.45,-0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-22.0);
Q12_Slider = visual.Slider(win=win, name='Q12_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,-0.35), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-23, readOnly=False)
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()
Click_to_Continue_2 = visual.ImageStim(
    win=win,
    name='Click_to_Continue_2', 
    image='Continue.JPG', mask=None, anchor='center',
    ori=0.0, pos=(0.55, -0.45), size=(0.12, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-25.0)
Q13 = visual.TextStim(win=win, name='Q13',
    text='Q13. I recognize what I should do to get the advice I\nneed from the system the next time I use it.',
    font='Open Sans',
    pos=(-0.45, 0.45), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-26.0);
Q13_Slider = visual.Slider(win=win, name='Q13_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,0.4), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-27, readOnly=False)
Q14 = visual.TextStim(win=win, name='Q14',
    text='Q14. I believe advice from the system even when I\ndon’t know for certain that it is correct.',
    font='Open Sans',
    pos=(-0.45, 0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-28.0);
Q14_Slider = visual.Slider(win=win, name='Q14_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,0.25), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-29, readOnly=False)
Q15 = visual.TextStim(win=win, name='Q15',
    text='Q15. When I am uncertain about a decision I believe \nthe system rather than myself.',
    font='Open Sans',
    pos=(-0.45, 0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-30.0);
Q15_Slider = visual.Slider(win=win, name='Q15_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,0.1), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-31, readOnly=False)
Q16 = visual.TextStim(win=win, name='Q16',
    text='Q16. If I am not sure about a decision, I have faith that the\nsystem will provide the best solution.',
    font='Open Sans',
    pos=(-0.45, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-32.0);
Q16_Slider = visual.Slider(win=win, name='Q16_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,-0.05), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-33, readOnly=False)
Q17 = visual.TextStim(win=win, name='Q17',
    text='Q17. When the system gives unusual advice I am\nconfident that the advice is correct.',
    font='Open Sans',
    pos=(-0.45, -0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-34.0);
Q17_Slider = visual.Slider(win=win, name='Q17_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,-0.2), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-35, readOnly=False)
Q18 = visual.TextStim(win=win, name='Q18',
    text='Q18. Even if I have no reason to expect the system will be \nable to solve a difficult problem, I still feel certain that it will.',
    font='Open Sans',
    pos=(-0.45,-0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-36.0);
Q18_Slider = visual.Slider(win=win, name='Q18_Slider',
    startValue=None, size=(0.45,0.035), pos=(-0.45,-0.35), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-37, readOnly=False)
Q19 = visual.TextStim(win=win, name='Q19',
    text='Q19. I would feel a sense of loss if the system was \nunavailable and I could no longer use it.',
    font='Open Sans',
    pos=(0.45, 0.45), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-38.0);
Q19_Slider = visual.Slider(win=win, name='Q19_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,0.4), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-39, readOnly=False)
Q20 = visual.TextStim(win=win, name='Q20',
    text='Q20.  I feel a sense of attachment to using the system.',
    font='Open Sans',
    pos=(0.45, 0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-40.0);
Q20_Slider = visual.Slider(win=win, name='Q20_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,0.25), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-41, readOnly=False)
Q21 = visual.TextStim(win=win, name='Q21',
    text='Q21. I find the system suitable to my style of decision making.',
    font='Open Sans',
    pos=(0.45, 0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-42.0);
Q21_Slider = visual.Slider(win=win, name='Q21_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,0.1), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-43, readOnly=False)
Q22 = visual.TextStim(win=win, name='Q22',
    text='Q22.  I like using the system for decision making.',
    font='Open Sans',
    pos=(0.45, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-44.0);
Q22_Slider = visual.Slider(win=win, name='Q22_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,-0.05), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-45, readOnly=False)
Q23 = visual.TextStim(win=win, name='Q23',
    text='Q23. I have a personal preference for making decisions\nwith the system.\n\n',
    font='Open Sans',
    pos=(0.45, -0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-46.0);
Q23_Slider = visual.Slider(win=win, name='Q23_Slider',
    startValue=None, size=(0.45,0.035), pos=(0.45,-0.2), units=None,
    labels=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.015,
    flip=False, ori=0.0, depth=-47, readOnly=False)

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
end_Txt = visual.TextStim(win=win, name='end_Txt',
    text='Thank you for your participation in the experiment!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Intro_Trial_Start"-------
continueRoutine = True
# update component parameters for each repeat
Key_Resp.keys = []
Key_Resp.rt = []
_Key_Resp_allKeys = []
# keep track of which components have finished
Intro_Trial_StartComponents = [Intro_Slide, Press_to_Cont, Key_Resp]
for thisComponent in Intro_Trial_StartComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Intro_Trial_StartClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Intro_Trial_Start"-------
while continueRoutine:
    # get current time
    t = Intro_Trial_StartClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Intro_Trial_StartClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Intro_Slide* updates
    if Intro_Slide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Intro_Slide.frameNStart = frameN  # exact frame index
        Intro_Slide.tStart = t  # local t and not account for scr refresh
        Intro_Slide.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Intro_Slide, 'tStartRefresh')  # time at next scr refresh
        Intro_Slide.setAutoDraw(True)
    
    # *Press_to_Cont* updates
    if Press_to_Cont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Press_to_Cont.frameNStart = frameN  # exact frame index
        Press_to_Cont.tStart = t  # local t and not account for scr refresh
        Press_to_Cont.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Press_to_Cont, 'tStartRefresh')  # time at next scr refresh
        Press_to_Cont.setAutoDraw(True)
    
    # *Key_Resp* updates
    if Key_Resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Key_Resp.frameNStart = frameN  # exact frame index
        Key_Resp.tStart = t  # local t and not account for scr refresh
        Key_Resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Key_Resp, 'tStartRefresh')  # time at next scr refresh
        Key_Resp.status = STARTED
        # keyboard checking is just starting
        Key_Resp.clock.reset()  # now t=0
    if Key_Resp.status == STARTED:
        theseKeys = Key_Resp.getKeys(keyList=['space'], waitRelease=False)
        _Key_Resp_allKeys.extend(theseKeys)
        if len(_Key_Resp_allKeys):
            Key_Resp.keys = _Key_Resp_allKeys[-1].name  # just the last key pressed
            Key_Resp.rt = _Key_Resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Intro_Trial_StartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Intro_Trial_Start"-------
for thisComponent in Intro_Trial_StartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Intro_Trial_Start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Intro_Trial"-------
continueRoutine = True
# update component parameters for each repeat
Sample_Question.setText('Sample Question:')
AI_Response_2.setText('The AI system has determined that the above image is not authentic. \n\nDo you accept or deny this claim?')
Accept_Deny_Button_2.reset()
ConfidenceSlider_2.reset()
Experimental_Images_2.setImage('stim/DogImage.png')
DenySlider_2.reset()
# setup some python lists for storing info about the mouse_4
mouse_4.clicked_name = []
gotValidClick = False  # until a click is received
AI_Response_Txt_2.setText('AI Response:')
# keep track of which components have finished
Intro_TrialComponents = [Sample_Question, AI_Response_2, Accept_Deny_Button_2, ConfidenceText_2, ConfidenceSlider_2, Experimental_Images_2, IfDenied_2, DenySlider_2, mouse_4, Click_to_Continue_4, AI_Response_Txt_2, Explanation_Image_2]
for thisComponent in Intro_TrialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Intro_TrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Intro_Trial"-------
while continueRoutine:
    # get current time
    t = Intro_TrialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Intro_TrialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Sample_Question* updates
    if Sample_Question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Sample_Question.frameNStart = frameN  # exact frame index
        Sample_Question.tStart = t  # local t and not account for scr refresh
        Sample_Question.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Sample_Question, 'tStartRefresh')  # time at next scr refresh
        Sample_Question.setAutoDraw(True)
    
    # *AI_Response_2* updates
    if AI_Response_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        AI_Response_2.frameNStart = frameN  # exact frame index
        AI_Response_2.tStart = t  # local t and not account for scr refresh
        AI_Response_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(AI_Response_2, 'tStartRefresh')  # time at next scr refresh
        AI_Response_2.setAutoDraw(True)
    
    # *Accept_Deny_Button_2* updates
    if Accept_Deny_Button_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Accept_Deny_Button_2.frameNStart = frameN  # exact frame index
        Accept_Deny_Button_2.tStart = t  # local t and not account for scr refresh
        Accept_Deny_Button_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Accept_Deny_Button_2, 'tStartRefresh')  # time at next scr refresh
        Accept_Deny_Button_2.setAutoDraw(True)
    
    # *ConfidenceText_2* updates
    if ConfidenceText_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ConfidenceText_2.frameNStart = frameN  # exact frame index
        ConfidenceText_2.tStart = t  # local t and not account for scr refresh
        ConfidenceText_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ConfidenceText_2, 'tStartRefresh')  # time at next scr refresh
        ConfidenceText_2.setAutoDraw(True)
    
    # *ConfidenceSlider_2* updates
    if ConfidenceSlider_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ConfidenceSlider_2.frameNStart = frameN  # exact frame index
        ConfidenceSlider_2.tStart = t  # local t and not account for scr refresh
        ConfidenceSlider_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ConfidenceSlider_2, 'tStartRefresh')  # time at next scr refresh
        ConfidenceSlider_2.setAutoDraw(True)
    
    # *Experimental_Images_2* updates
    if Experimental_Images_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Experimental_Images_2.frameNStart = frameN  # exact frame index
        Experimental_Images_2.tStart = t  # local t and not account for scr refresh
        Experimental_Images_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Experimental_Images_2, 'tStartRefresh')  # time at next scr refresh
        Experimental_Images_2.setAutoDraw(True)
    
    # *IfDenied_2* updates
    if IfDenied_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IfDenied_2.frameNStart = frameN  # exact frame index
        IfDenied_2.tStart = t  # local t and not account for scr refresh
        IfDenied_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IfDenied_2, 'tStartRefresh')  # time at next scr refresh
        IfDenied_2.setAutoDraw(True)
    
    # *DenySlider_2* updates
    if DenySlider_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        DenySlider_2.frameNStart = frameN  # exact frame index
        DenySlider_2.tStart = t  # local t and not account for scr refresh
        DenySlider_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(DenySlider_2, 'tStartRefresh')  # time at next scr refresh
        DenySlider_2.setAutoDraw(True)
    # *mouse_4* updates
    if mouse_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_4.frameNStart = frameN  # exact frame index
        mouse_4.tStart = t  # local t and not account for scr refresh
        mouse_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_4, 'tStartRefresh')  # time at next scr refresh
        mouse_4.status = STARTED
        mouse_4.mouseClock.reset()
        prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
    if mouse_4.status == STARTED:  # only update if started and not finished!
        buttons = mouse_4.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(Click_to_Continue_4)
                    clickableList = Click_to_Continue_4
                except:
                    clickableList = [Click_to_Continue_4]
                for obj in clickableList:
                    if obj.contains(mouse_4):
                        gotValidClick = True
                        mouse_4.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # *Click_to_Continue_4* updates
    if Click_to_Continue_4.status == NOT_STARTED and Accept_Deny_Button_2.rating and ConfidenceSlider_2.rating and DenySlider_2.rating:
        # keep track of start time/frame for later
        Click_to_Continue_4.frameNStart = frameN  # exact frame index
        Click_to_Continue_4.tStart = t  # local t and not account for scr refresh
        Click_to_Continue_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Click_to_Continue_4, 'tStartRefresh')  # time at next scr refresh
        Click_to_Continue_4.setAutoDraw(True)
    
    # *AI_Response_Txt_2* updates
    if AI_Response_Txt_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        AI_Response_Txt_2.frameNStart = frameN  # exact frame index
        AI_Response_Txt_2.tStart = t  # local t and not account for scr refresh
        AI_Response_Txt_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(AI_Response_Txt_2, 'tStartRefresh')  # time at next scr refresh
        AI_Response_Txt_2.setAutoDraw(True)
    
    # *Explanation_Image_2* updates
    if Explanation_Image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Explanation_Image_2.frameNStart = frameN  # exact frame index
        Explanation_Image_2.tStart = t  # local t and not account for scr refresh
        Explanation_Image_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Explanation_Image_2, 'tStartRefresh')  # time at next scr refresh
        Explanation_Image_2.setAutoDraw(True)
    if Explanation_Image_2.status == STARTED:  # only update if drawing
        Explanation_Image_2.setImage('stim/Intro_Explanation.png', log=False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Intro_TrialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Intro_Trial"-------
for thisComponent in Intro_TrialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "Intro_Trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Trial_Start"-------
continueRoutine = True
# update component parameters for each repeat
KeyResp_4.keys = []
KeyResp_4.rt = []
_KeyResp_4_allKeys = []
# keep track of which components have finished
Trial_StartComponents = [text_3, PresstoCont_4, KeyResp_4]
for thisComponent in Trial_StartComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Trial_StartClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Trial_Start"-------
while continueRoutine:
    # get current time
    t = Trial_StartClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Trial_StartClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *PresstoCont_4* updates
    if PresstoCont_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PresstoCont_4.frameNStart = frameN  # exact frame index
        PresstoCont_4.tStart = t  # local t and not account for scr refresh
        PresstoCont_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PresstoCont_4, 'tStartRefresh')  # time at next scr refresh
        PresstoCont_4.setAutoDraw(True)
    
    # *KeyResp_4* updates
    if KeyResp_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        KeyResp_4.frameNStart = frameN  # exact frame index
        KeyResp_4.tStart = t  # local t and not account for scr refresh
        KeyResp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(KeyResp_4, 'tStartRefresh')  # time at next scr refresh
        KeyResp_4.status = STARTED
        # keyboard checking is just starting
        KeyResp_4.clock.reset()  # now t=0
    if KeyResp_4.status == STARTED:
        theseKeys = KeyResp_4.getKeys(keyList=['space'], waitRelease=False)
        _KeyResp_4_allKeys.extend(theseKeys)
        if len(_KeyResp_4_allKeys):
            KeyResp_4.keys = _KeyResp_4_allKeys[-1].name  # just the last key pressed
            KeyResp_4.rt = _KeyResp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Trial_StartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Trial_Start"-------
for thisComponent in Trial_StartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Trial_Start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Loop_1 = data.TrialHandler(nReps=0.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condtionsFile/conversationalconditionsFile.csv'),
    seed=None, name='Loop_1')
thisExp.addLoop(Loop_1)  # add the loop to the experiment
thisLoop_1 = Loop_1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_1.rgb)
if thisLoop_1 != None:
    for paramName in thisLoop_1:
        exec('{} = thisLoop_1[paramName]'.format(paramName))

for thisLoop_1 in Loop_1:
    currentLoop = Loop_1
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_1.rgb)
    if thisLoop_1 != None:
        for paramName in thisLoop_1:
            exec('{} = thisLoop_1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Conversational_Based"-------
    continueRoutine = True
    # update component parameters for each repeat
    Question_Txt.setText(txtStim)
    AI_Response.setText(AI_Resp)
    Accept_Deny_Button.reset()
    ConfidenceSlider.reset()
    Experimental_Images.setImage(stimFile)
    DenySlider.reset()
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    AI_Response_Txt.setText('AI Response:')
    outlet.push_sample(x=[1])
    
    from psychopy import core# this returns a time value in seconds, not a clock object:
    
    clock = core.getAbsTime()
    
    import time
    
    from datetime import datetime
    
    ETrial= datetime.fromtimestamp(clock).strftime("%I:%M:%S")
    
    Loop_1.addData('trial_start', ETrial)
    # keep track of which components have finished
    Conversational_BasedComponents = [Conversational_Intro_Txt, Question_Txt, AI_Response, Accept_Deny_Button, ConfidenceText, ConfidenceSlider, Experimental_Images, IfDenied, DenySlider, mouse, Click_to_Continue, AI_Response_Txt, Explanation_Image]
    for thisComponent in Conversational_BasedComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Conversational_BasedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Conversational_Based"-------
    while continueRoutine:
        # get current time
        t = Conversational_BasedClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Conversational_BasedClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Conversational_Intro_Txt* updates
        if Conversational_Intro_Txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Conversational_Intro_Txt.frameNStart = frameN  # exact frame index
            Conversational_Intro_Txt.tStart = t  # local t and not account for scr refresh
            Conversational_Intro_Txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Conversational_Intro_Txt, 'tStartRefresh')  # time at next scr refresh
            Conversational_Intro_Txt.setAutoDraw(True)
        if Conversational_Intro_Txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Conversational_Intro_Txt.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                Conversational_Intro_Txt.tStop = t  # not accounting for scr refresh
                Conversational_Intro_Txt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Conversational_Intro_Txt, 'tStopRefresh')  # time at next scr refresh
                Conversational_Intro_Txt.setAutoDraw(False)
        
        # *Question_Txt* updates
        if Question_Txt.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            Question_Txt.frameNStart = frameN  # exact frame index
            Question_Txt.tStart = t  # local t and not account for scr refresh
            Question_Txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Question_Txt, 'tStartRefresh')  # time at next scr refresh
            Question_Txt.setAutoDraw(True)
        
        # *AI_Response* updates
        if AI_Response.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            AI_Response.frameNStart = frameN  # exact frame index
            AI_Response.tStart = t  # local t and not account for scr refresh
            AI_Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AI_Response, 'tStartRefresh')  # time at next scr refresh
            AI_Response.setAutoDraw(True)
        
        # *Accept_Deny_Button* updates
        if Accept_Deny_Button.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            Accept_Deny_Button.frameNStart = frameN  # exact frame index
            Accept_Deny_Button.tStart = t  # local t and not account for scr refresh
            Accept_Deny_Button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Accept_Deny_Button, 'tStartRefresh')  # time at next scr refresh
            Accept_Deny_Button.setAutoDraw(True)
        
        # *ConfidenceText* updates
        if ConfidenceText.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            ConfidenceText.frameNStart = frameN  # exact frame index
            ConfidenceText.tStart = t  # local t and not account for scr refresh
            ConfidenceText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ConfidenceText, 'tStartRefresh')  # time at next scr refresh
            ConfidenceText.setAutoDraw(True)
        
        # *ConfidenceSlider* updates
        if ConfidenceSlider.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            ConfidenceSlider.frameNStart = frameN  # exact frame index
            ConfidenceSlider.tStart = t  # local t and not account for scr refresh
            ConfidenceSlider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ConfidenceSlider, 'tStartRefresh')  # time at next scr refresh
            ConfidenceSlider.setAutoDraw(True)
        
        # *Experimental_Images* updates
        if Experimental_Images.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            Experimental_Images.frameNStart = frameN  # exact frame index
            Experimental_Images.tStart = t  # local t and not account for scr refresh
            Experimental_Images.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Experimental_Images, 'tStartRefresh')  # time at next scr refresh
            Experimental_Images.setAutoDraw(True)
        
        # *IfDenied* updates
        if IfDenied.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            IfDenied.frameNStart = frameN  # exact frame index
            IfDenied.tStart = t  # local t and not account for scr refresh
            IfDenied.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IfDenied, 'tStartRefresh')  # time at next scr refresh
            IfDenied.setAutoDraw(True)
        
        # *DenySlider* updates
        if DenySlider.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            DenySlider.frameNStart = frameN  # exact frame index
            DenySlider.tStart = t  # local t and not account for scr refresh
            DenySlider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DenySlider, 'tStartRefresh')  # time at next scr refresh
            DenySlider.setAutoDraw(True)
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(Click_to_Continue)
                        clickableList = Click_to_Continue
                    except:
                        clickableList = [Click_to_Continue]
                    for obj in clickableList:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # abort routine on response
        
        # *Click_to_Continue* updates
        if Click_to_Continue.status == NOT_STARTED and Accept_Deny_Button.rating and ConfidenceSlider.rating and DenySlider.rating:
            # keep track of start time/frame for later
            Click_to_Continue.frameNStart = frameN  # exact frame index
            Click_to_Continue.tStart = t  # local t and not account for scr refresh
            Click_to_Continue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Click_to_Continue, 'tStartRefresh')  # time at next scr refresh
            Click_to_Continue.setAutoDraw(True)
        
        # *AI_Response_Txt* updates
        if AI_Response_Txt.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            AI_Response_Txt.frameNStart = frameN  # exact frame index
            AI_Response_Txt.tStart = t  # local t and not account for scr refresh
            AI_Response_Txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AI_Response_Txt, 'tStartRefresh')  # time at next scr refresh
            AI_Response_Txt.setAutoDraw(True)
        
        # *Explanation_Image* updates
        if Explanation_Image.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            Explanation_Image.frameNStart = frameN  # exact frame index
            Explanation_Image.tStart = t  # local t and not account for scr refresh
            Explanation_Image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Explanation_Image, 'tStartRefresh')  # time at next scr refresh
            Explanation_Image.setAutoDraw(True)
        if Explanation_Image.status == STARTED:  # only update if drawing
            Explanation_Image.setImage(ExplanationFile, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Conversational_BasedComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Conversational_Based"-------
    for thisComponent in Conversational_BasedComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Loop_1.addData('Conversational_Intro_Txt.started', Conversational_Intro_Txt.tStartRefresh)
    Loop_1.addData('Conversational_Intro_Txt.stopped', Conversational_Intro_Txt.tStopRefresh)
    Loop_1.addData('Accept_Deny_Button.response', Accept_Deny_Button.getRating())
    Loop_1.addData('Accept_Deny_Button.rt', Accept_Deny_Button.getRT())
    Loop_1.addData('Accept_Deny_Button.started', Accept_Deny_Button.tStartRefresh)
    Loop_1.addData('Accept_Deny_Button.stopped', Accept_Deny_Button.tStopRefresh)
    Loop_1.addData('ConfidenceSlider.response', ConfidenceSlider.getRating())
    Loop_1.addData('ConfidenceSlider.rt', ConfidenceSlider.getRT())
    Loop_1.addData('ConfidenceSlider.started', ConfidenceSlider.tStartRefresh)
    Loop_1.addData('ConfidenceSlider.stopped', ConfidenceSlider.tStopRefresh)
    Loop_1.addData('Experimental_Images.started', Experimental_Images.tStartRefresh)
    Loop_1.addData('Experimental_Images.stopped', Experimental_Images.tStopRefresh)
    Loop_1.addData('DenySlider.response', DenySlider.getRating())
    Loop_1.addData('DenySlider.rt', DenySlider.getRT())
    Loop_1.addData('DenySlider.started', DenySlider.tStartRefresh)
    Loop_1.addData('DenySlider.stopped', DenySlider.tStopRefresh)
    # store data for Loop_1 (TrialHandler)
    Loop_1.addData('mouse.x', mouse.x)
    Loop_1.addData('mouse.y', mouse.y)
    Loop_1.addData('mouse.leftButton', mouse.leftButton)
    Loop_1.addData('mouse.midButton', mouse.midButton)
    Loop_1.addData('mouse.rightButton', mouse.rightButton)
    Loop_1.addData('mouse.time', mouse.time)
    Loop_1.addData('mouse.clicked_name', mouse.clicked_name)
    Loop_1.addData('mouse.started', mouse.tStart)
    Loop_1.addData('mouse.stopped', mouse.tStop)
    Loop_1.addData('Click_to_Continue.started', Click_to_Continue.tStartRefresh)
    Loop_1.addData('Click_to_Continue.stopped', Click_to_Continue.tStopRefresh)
    outlet.push_sample(x=[1])
    
    from psychopy import core# this returns a time value in seconds, not a clock object:
    
    clock = core.getAbsTime()
    
    import time
    
    from datetime import datetime
    
    ETrial= datetime.fromtimestamp(clock).strftime("%I:%M:%S")
    
    Loop_1.addData('trial_end', ETrial)
    
    # the Routine "Conversational_Based" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'Loop_1'

# get names of stimulus parameters
if Loop_1.trialList in ([], [None], None):
    params = []
else:
    params = Loop_1.trialList[0].keys()
# save data for this loop
Loop_1.saveAsExcel(filename + '.xlsx', sheetName='Loop_1',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
Loop_1.saveAsText(filename + 'Loop_1.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Conversational_Survey_Break"-------
continueRoutine = True
# update component parameters for each repeat
KeyResp.keys = []
KeyResp.rt = []
_KeyResp_allKeys = []
# keep track of which components have finished
Conversational_Survey_BreakComponents = [text, PresstoCont, KeyResp]
for thisComponent in Conversational_Survey_BreakComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Conversational_Survey_BreakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Conversational_Survey_Break"-------
while continueRoutine:
    # get current time
    t = Conversational_Survey_BreakClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Conversational_Survey_BreakClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *PresstoCont* updates
    if PresstoCont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PresstoCont.frameNStart = frameN  # exact frame index
        PresstoCont.tStart = t  # local t and not account for scr refresh
        PresstoCont.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PresstoCont, 'tStartRefresh')  # time at next scr refresh
        PresstoCont.setAutoDraw(True)
    
    # *KeyResp* updates
    if KeyResp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        KeyResp.frameNStart = frameN  # exact frame index
        KeyResp.tStart = t  # local t and not account for scr refresh
        KeyResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(KeyResp, 'tStartRefresh')  # time at next scr refresh
        KeyResp.status = STARTED
        # keyboard checking is just starting
        KeyResp.clock.reset()  # now t=0
    if KeyResp.status == STARTED:
        theseKeys = KeyResp.getKeys(keyList=['space'], waitRelease=False)
        _KeyResp_allKeys.extend(theseKeys)
        if len(_KeyResp_allKeys):
            KeyResp.keys = _KeyResp_allKeys[-1].name  # just the last key pressed
            KeyResp.rt = _KeyResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Conversational_Survey_BreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Conversational_Survey_Break"-------
for thisComponent in Conversational_Survey_BreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Conversational_Survey_Break" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Survey_Trial"-------
continueRoutine = True
# update component parameters for each repeat
Q1_Slider.reset()
Q2_Slider.reset()
Q3_Slider.reset()
Q4_Slider.reset()
Q5_Slider.reset()
Q6_Slider.reset()
Q7_Slider.reset()
Q8_Slider.reset()
Q9_Slider.reset()
Q10_Slider.reset()
Q11_Slider.reset()
Q12_Slider.reset()
# setup some python lists for storing info about the mouse_2
mouse_2.clicked_name = []
gotValidClick = False  # until a click is received
Q13_Slider.reset()
Q14_Slider.reset()
Q15_Slider.reset()
Q16_Slider.reset()
Q17_Slider.reset()
Q18_Slider.reset()
Q19_Slider.reset()
Q20_Slider.reset()
Q21_Slider.reset()
Q22_Slider.reset()
Q23_Slider.reset()
# keep track of which components have finished
Survey_TrialComponents = [Q1, Q1_Slider, Q2, Q2_Slider, Q3, Q3_Slider, Q4, Q4_Slider, Q5, Q5_Slider, Q6, Q6_Slider, Q7, Q7_Slider, Q8, Q8_Slider, Q9, Q9_Slider, Q10, Q10_Slider, Q11, Q11_Slider, Q12, Q12_Slider, mouse_2, Click_to_Continue_2, Q13, Q13_Slider, Q14, Q14_Slider, Q15, Q15_Slider, Q16, Q16_Slider, Q17, Q17_Slider, Q18, Q18_Slider, Q19, Q19_Slider, Q20, Q20_Slider, Q21, Q21_Slider, Q22, Q22_Slider, Q23, Q23_Slider]
for thisComponent in Survey_TrialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Survey_TrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Survey_Trial"-------
while continueRoutine:
    # get current time
    t = Survey_TrialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Survey_TrialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Q1* updates
    if Q1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q1.frameNStart = frameN  # exact frame index
        Q1.tStart = t  # local t and not account for scr refresh
        Q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q1, 'tStartRefresh')  # time at next scr refresh
        Q1.setAutoDraw(True)
    if Q1.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q1.tStop = t  # not accounting for scr refresh
            Q1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q1, 'tStopRefresh')  # time at next scr refresh
            Q1.setAutoDraw(False)
    
    # *Q1_Slider* updates
    if Q1_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q1_Slider.frameNStart = frameN  # exact frame index
        Q1_Slider.tStart = t  # local t and not account for scr refresh
        Q1_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q1_Slider, 'tStartRefresh')  # time at next scr refresh
        Q1_Slider.setAutoDraw(True)
    if Q1_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q1_Slider.tStop = t  # not accounting for scr refresh
            Q1_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q1_Slider, 'tStopRefresh')  # time at next scr refresh
            Q1_Slider.setAutoDraw(False)
    
    # *Q2* updates
    if Q2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q2.frameNStart = frameN  # exact frame index
        Q2.tStart = t  # local t and not account for scr refresh
        Q2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q2, 'tStartRefresh')  # time at next scr refresh
        Q2.setAutoDraw(True)
    if Q2.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q2.tStop = t  # not accounting for scr refresh
            Q2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q2, 'tStopRefresh')  # time at next scr refresh
            Q2.setAutoDraw(False)
    
    # *Q2_Slider* updates
    if Q2_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q2_Slider.frameNStart = frameN  # exact frame index
        Q2_Slider.tStart = t  # local t and not account for scr refresh
        Q2_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q2_Slider, 'tStartRefresh')  # time at next scr refresh
        Q2_Slider.setAutoDraw(True)
    if Q2_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q2_Slider.tStop = t  # not accounting for scr refresh
            Q2_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q2_Slider, 'tStopRefresh')  # time at next scr refresh
            Q2_Slider.setAutoDraw(False)
    
    # *Q3* updates
    if Q3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q3.frameNStart = frameN  # exact frame index
        Q3.tStart = t  # local t and not account for scr refresh
        Q3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q3, 'tStartRefresh')  # time at next scr refresh
        Q3.setAutoDraw(True)
    if Q3.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q3.tStop = t  # not accounting for scr refresh
            Q3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q3, 'tStopRefresh')  # time at next scr refresh
            Q3.setAutoDraw(False)
    
    # *Q3_Slider* updates
    if Q3_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q3_Slider.frameNStart = frameN  # exact frame index
        Q3_Slider.tStart = t  # local t and not account for scr refresh
        Q3_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q3_Slider, 'tStartRefresh')  # time at next scr refresh
        Q3_Slider.setAutoDraw(True)
    if Q3_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q3_Slider.tStop = t  # not accounting for scr refresh
            Q3_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q3_Slider, 'tStopRefresh')  # time at next scr refresh
            Q3_Slider.setAutoDraw(False)
    
    # *Q4* updates
    if Q4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q4.frameNStart = frameN  # exact frame index
        Q4.tStart = t  # local t and not account for scr refresh
        Q4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q4, 'tStartRefresh')  # time at next scr refresh
        Q4.setAutoDraw(True)
    if Q4.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q4.tStop = t  # not accounting for scr refresh
            Q4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q4, 'tStopRefresh')  # time at next scr refresh
            Q4.setAutoDraw(False)
    
    # *Q4_Slider* updates
    if Q4_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q4_Slider.frameNStart = frameN  # exact frame index
        Q4_Slider.tStart = t  # local t and not account for scr refresh
        Q4_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q4_Slider, 'tStartRefresh')  # time at next scr refresh
        Q4_Slider.setAutoDraw(True)
    if Q4_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q4_Slider.tStop = t  # not accounting for scr refresh
            Q4_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q4_Slider, 'tStopRefresh')  # time at next scr refresh
            Q4_Slider.setAutoDraw(False)
    
    # *Q5* updates
    if Q5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q5.frameNStart = frameN  # exact frame index
        Q5.tStart = t  # local t and not account for scr refresh
        Q5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q5, 'tStartRefresh')  # time at next scr refresh
        Q5.setAutoDraw(True)
    if Q5.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q5.tStop = t  # not accounting for scr refresh
            Q5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q5, 'tStopRefresh')  # time at next scr refresh
            Q5.setAutoDraw(False)
    
    # *Q5_Slider* updates
    if Q5_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q5_Slider.frameNStart = frameN  # exact frame index
        Q5_Slider.tStart = t  # local t and not account for scr refresh
        Q5_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q5_Slider, 'tStartRefresh')  # time at next scr refresh
        Q5_Slider.setAutoDraw(True)
    if Q5_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q5_Slider.tStop = t  # not accounting for scr refresh
            Q5_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q5_Slider, 'tStopRefresh')  # time at next scr refresh
            Q5_Slider.setAutoDraw(False)
    
    # *Q6* updates
    if Q6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q6.frameNStart = frameN  # exact frame index
        Q6.tStart = t  # local t and not account for scr refresh
        Q6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q6, 'tStartRefresh')  # time at next scr refresh
        Q6.setAutoDraw(True)
    if Q6.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q6.tStop = t  # not accounting for scr refresh
            Q6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q6, 'tStopRefresh')  # time at next scr refresh
            Q6.setAutoDraw(False)
    
    # *Q6_Slider* updates
    if Q6_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q6_Slider.frameNStart = frameN  # exact frame index
        Q6_Slider.tStart = t  # local t and not account for scr refresh
        Q6_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q6_Slider, 'tStartRefresh')  # time at next scr refresh
        Q6_Slider.setAutoDraw(True)
    if Q6_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q6_Slider.tStop = t  # not accounting for scr refresh
            Q6_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q6_Slider, 'tStopRefresh')  # time at next scr refresh
            Q6_Slider.setAutoDraw(False)
    
    # *Q7* updates
    if Q7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q7.frameNStart = frameN  # exact frame index
        Q7.tStart = t  # local t and not account for scr refresh
        Q7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q7, 'tStartRefresh')  # time at next scr refresh
        Q7.setAutoDraw(True)
    if Q7.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q7.tStop = t  # not accounting for scr refresh
            Q7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q7, 'tStopRefresh')  # time at next scr refresh
            Q7.setAutoDraw(False)
    
    # *Q7_Slider* updates
    if Q7_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q7_Slider.frameNStart = frameN  # exact frame index
        Q7_Slider.tStart = t  # local t and not account for scr refresh
        Q7_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q7_Slider, 'tStartRefresh')  # time at next scr refresh
        Q7_Slider.setAutoDraw(True)
    if Q7_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q7_Slider.tStop = t  # not accounting for scr refresh
            Q7_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q7_Slider, 'tStopRefresh')  # time at next scr refresh
            Q7_Slider.setAutoDraw(False)
    
    # *Q8* updates
    if Q8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q8.frameNStart = frameN  # exact frame index
        Q8.tStart = t  # local t and not account for scr refresh
        Q8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q8, 'tStartRefresh')  # time at next scr refresh
        Q8.setAutoDraw(True)
    if Q8.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q8.tStop = t  # not accounting for scr refresh
            Q8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q8, 'tStopRefresh')  # time at next scr refresh
            Q8.setAutoDraw(False)
    
    # *Q8_Slider* updates
    if Q8_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q8_Slider.frameNStart = frameN  # exact frame index
        Q8_Slider.tStart = t  # local t and not account for scr refresh
        Q8_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q8_Slider, 'tStartRefresh')  # time at next scr refresh
        Q8_Slider.setAutoDraw(True)
    if Q8_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q8_Slider.tStop = t  # not accounting for scr refresh
            Q8_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q8_Slider, 'tStopRefresh')  # time at next scr refresh
            Q8_Slider.setAutoDraw(False)
    
    # *Q9* updates
    if Q9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q9.frameNStart = frameN  # exact frame index
        Q9.tStart = t  # local t and not account for scr refresh
        Q9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q9, 'tStartRefresh')  # time at next scr refresh
        Q9.setAutoDraw(True)
    if Q9.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q9.tStop = t  # not accounting for scr refresh
            Q9.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q9, 'tStopRefresh')  # time at next scr refresh
            Q9.setAutoDraw(False)
    
    # *Q9_Slider* updates
    if Q9_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q9_Slider.frameNStart = frameN  # exact frame index
        Q9_Slider.tStart = t  # local t and not account for scr refresh
        Q9_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q9_Slider, 'tStartRefresh')  # time at next scr refresh
        Q9_Slider.setAutoDraw(True)
    if Q9_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q9_Slider.tStop = t  # not accounting for scr refresh
            Q9_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q9_Slider, 'tStopRefresh')  # time at next scr refresh
            Q9_Slider.setAutoDraw(False)
    
    # *Q10* updates
    if Q10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q10.frameNStart = frameN  # exact frame index
        Q10.tStart = t  # local t and not account for scr refresh
        Q10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q10, 'tStartRefresh')  # time at next scr refresh
        Q10.setAutoDraw(True)
    if Q10.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q10.tStop = t  # not accounting for scr refresh
            Q10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q10, 'tStopRefresh')  # time at next scr refresh
            Q10.setAutoDraw(False)
    
    # *Q10_Slider* updates
    if Q10_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q10_Slider.frameNStart = frameN  # exact frame index
        Q10_Slider.tStart = t  # local t and not account for scr refresh
        Q10_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q10_Slider, 'tStartRefresh')  # time at next scr refresh
        Q10_Slider.setAutoDraw(True)
    if Q10_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q10_Slider.tStop = t  # not accounting for scr refresh
            Q10_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q10_Slider, 'tStopRefresh')  # time at next scr refresh
            Q10_Slider.setAutoDraw(False)
    
    # *Q11* updates
    if Q11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q11.frameNStart = frameN  # exact frame index
        Q11.tStart = t  # local t and not account for scr refresh
        Q11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q11, 'tStartRefresh')  # time at next scr refresh
        Q11.setAutoDraw(True)
    if Q11.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q11.tStop = t  # not accounting for scr refresh
            Q11.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q11, 'tStopRefresh')  # time at next scr refresh
            Q11.setAutoDraw(False)
    
    # *Q11_Slider* updates
    if Q11_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q11_Slider.frameNStart = frameN  # exact frame index
        Q11_Slider.tStart = t  # local t and not account for scr refresh
        Q11_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q11_Slider, 'tStartRefresh')  # time at next scr refresh
        Q11_Slider.setAutoDraw(True)
    if Q11_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q11_Slider.tStop = t  # not accounting for scr refresh
            Q11_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q11_Slider, 'tStopRefresh')  # time at next scr refresh
            Q11_Slider.setAutoDraw(False)
    
    # *Q12* updates
    if Q12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q12.frameNStart = frameN  # exact frame index
        Q12.tStart = t  # local t and not account for scr refresh
        Q12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q12, 'tStartRefresh')  # time at next scr refresh
        Q12.setAutoDraw(True)
    if Q12.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q12.tStop = t  # not accounting for scr refresh
            Q12.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q12, 'tStopRefresh')  # time at next scr refresh
            Q12.setAutoDraw(False)
    
    # *Q12_Slider* updates
    if Q12_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q12_Slider.frameNStart = frameN  # exact frame index
        Q12_Slider.tStart = t  # local t and not account for scr refresh
        Q12_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q12_Slider, 'tStartRefresh')  # time at next scr refresh
        Q12_Slider.setAutoDraw(True)
    if Q12_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q12_Slider.tStop = t  # not accounting for scr refresh
            Q12_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q12_Slider, 'tStopRefresh')  # time at next scr refresh
            Q12_Slider.setAutoDraw(False)
    # *mouse_2* updates
    if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_2.frameNStart = frameN  # exact frame index
        mouse_2.tStart = t  # local t and not account for scr refresh
        mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
        mouse_2.status = STARTED
        mouse_2.mouseClock.reset()
        prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
    if mouse_2.status == STARTED:  # only update if started and not finished!
        buttons = mouse_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(Click_to_Continue_2)
                    clickableList = Click_to_Continue_2
                except:
                    clickableList = [Click_to_Continue_2]
                for obj in clickableList:
                    if obj.contains(mouse_2):
                        gotValidClick = True
                        mouse_2.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # *Click_to_Continue_2* updates
    if Click_to_Continue_2.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating and Q13_Slider.rating and Q14_Slider.rating and Q15_Slider.rating and Q16_Slider.rating and Q17_Slider.rating and Q18_Slider.rating and Q19_Slider.rating and Q20_Slider.rating and Q21_Slider.rating and Q22_Slider.rating and Q23_Slider.rating:
        # keep track of start time/frame for later
        Click_to_Continue_2.frameNStart = frameN  # exact frame index
        Click_to_Continue_2.tStart = t  # local t and not account for scr refresh
        Click_to_Continue_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Click_to_Continue_2, 'tStartRefresh')  # time at next scr refresh
        Click_to_Continue_2.setAutoDraw(True)
    
    # *Q13* updates
    if Q13.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q13.frameNStart = frameN  # exact frame index
        Q13.tStart = t  # local t and not account for scr refresh
        Q13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q13, 'tStartRefresh')  # time at next scr refresh
        Q13.setAutoDraw(True)
    
    # *Q13_Slider* updates
    if Q13_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q13_Slider.frameNStart = frameN  # exact frame index
        Q13_Slider.tStart = t  # local t and not account for scr refresh
        Q13_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q13_Slider, 'tStartRefresh')  # time at next scr refresh
        Q13_Slider.setAutoDraw(True)
    
    # *Q14* updates
    if Q14.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q14.frameNStart = frameN  # exact frame index
        Q14.tStart = t  # local t and not account for scr refresh
        Q14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q14, 'tStartRefresh')  # time at next scr refresh
        Q14.setAutoDraw(True)
    
    # *Q14_Slider* updates
    if Q14_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q14_Slider.frameNStart = frameN  # exact frame index
        Q14_Slider.tStart = t  # local t and not account for scr refresh
        Q14_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q14_Slider, 'tStartRefresh')  # time at next scr refresh
        Q14_Slider.setAutoDraw(True)
    
    # *Q15* updates
    if Q15.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q15.frameNStart = frameN  # exact frame index
        Q15.tStart = t  # local t and not account for scr refresh
        Q15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q15, 'tStartRefresh')  # time at next scr refresh
        Q15.setAutoDraw(True)
    
    # *Q15_Slider* updates
    if Q15_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q15_Slider.frameNStart = frameN  # exact frame index
        Q15_Slider.tStart = t  # local t and not account for scr refresh
        Q15_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q15_Slider, 'tStartRefresh')  # time at next scr refresh
        Q15_Slider.setAutoDraw(True)
    
    # *Q16* updates
    if Q16.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q16.frameNStart = frameN  # exact frame index
        Q16.tStart = t  # local t and not account for scr refresh
        Q16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q16, 'tStartRefresh')  # time at next scr refresh
        Q16.setAutoDraw(True)
    
    # *Q16_Slider* updates
    if Q16_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q16_Slider.frameNStart = frameN  # exact frame index
        Q16_Slider.tStart = t  # local t and not account for scr refresh
        Q16_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q16_Slider, 'tStartRefresh')  # time at next scr refresh
        Q16_Slider.setAutoDraw(True)
    
    # *Q17* updates
    if Q17.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q17.frameNStart = frameN  # exact frame index
        Q17.tStart = t  # local t and not account for scr refresh
        Q17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q17, 'tStartRefresh')  # time at next scr refresh
        Q17.setAutoDraw(True)
    
    # *Q17_Slider* updates
    if Q17_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q17_Slider.frameNStart = frameN  # exact frame index
        Q17_Slider.tStart = t  # local t and not account for scr refresh
        Q17_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q17_Slider, 'tStartRefresh')  # time at next scr refresh
        Q17_Slider.setAutoDraw(True)
    
    # *Q18* updates
    if Q18.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q18.frameNStart = frameN  # exact frame index
        Q18.tStart = t  # local t and not account for scr refresh
        Q18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q18, 'tStartRefresh')  # time at next scr refresh
        Q18.setAutoDraw(True)
    
    # *Q18_Slider* updates
    if Q18_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q18_Slider.frameNStart = frameN  # exact frame index
        Q18_Slider.tStart = t  # local t and not account for scr refresh
        Q18_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q18_Slider, 'tStartRefresh')  # time at next scr refresh
        Q18_Slider.setAutoDraw(True)
    
    # *Q19* updates
    if Q19.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q19.frameNStart = frameN  # exact frame index
        Q19.tStart = t  # local t and not account for scr refresh
        Q19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q19, 'tStartRefresh')  # time at next scr refresh
        Q19.setAutoDraw(True)
    
    # *Q19_Slider* updates
    if Q19_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q19_Slider.frameNStart = frameN  # exact frame index
        Q19_Slider.tStart = t  # local t and not account for scr refresh
        Q19_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q19_Slider, 'tStartRefresh')  # time at next scr refresh
        Q19_Slider.setAutoDraw(True)
    
    # *Q20* updates
    if Q20.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q20.frameNStart = frameN  # exact frame index
        Q20.tStart = t  # local t and not account for scr refresh
        Q20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q20, 'tStartRefresh')  # time at next scr refresh
        Q20.setAutoDraw(True)
    
    # *Q20_Slider* updates
    if Q20_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q20_Slider.frameNStart = frameN  # exact frame index
        Q20_Slider.tStart = t  # local t and not account for scr refresh
        Q20_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q20_Slider, 'tStartRefresh')  # time at next scr refresh
        Q20_Slider.setAutoDraw(True)
    
    # *Q21* updates
    if Q21.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q21.frameNStart = frameN  # exact frame index
        Q21.tStart = t  # local t and not account for scr refresh
        Q21.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q21, 'tStartRefresh')  # time at next scr refresh
        Q21.setAutoDraw(True)
    
    # *Q21_Slider* updates
    if Q21_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q21_Slider.frameNStart = frameN  # exact frame index
        Q21_Slider.tStart = t  # local t and not account for scr refresh
        Q21_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q21_Slider, 'tStartRefresh')  # time at next scr refresh
        Q21_Slider.setAutoDraw(True)
    
    # *Q22* updates
    if Q22.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q22.frameNStart = frameN  # exact frame index
        Q22.tStart = t  # local t and not account for scr refresh
        Q22.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q22, 'tStartRefresh')  # time at next scr refresh
        Q22.setAutoDraw(True)
    
    # *Q22_Slider* updates
    if Q22_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q22_Slider.frameNStart = frameN  # exact frame index
        Q22_Slider.tStart = t  # local t and not account for scr refresh
        Q22_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q22_Slider, 'tStartRefresh')  # time at next scr refresh
        Q22_Slider.setAutoDraw(True)
    
    # *Q23* updates
    if Q23.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q23.frameNStart = frameN  # exact frame index
        Q23.tStart = t  # local t and not account for scr refresh
        Q23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q23, 'tStartRefresh')  # time at next scr refresh
        Q23.setAutoDraw(True)
    
    # *Q23_Slider* updates
    if Q23_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q23_Slider.frameNStart = frameN  # exact frame index
        Q23_Slider.tStart = t  # local t and not account for scr refresh
        Q23_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q23_Slider, 'tStartRefresh')  # time at next scr refresh
        Q23_Slider.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Survey_TrialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Survey_Trial"-------
for thisComponent in Survey_TrialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Q1_Slider.response', Q1_Slider.getRating())
thisExp.addData('Q2_Slider.response', Q2_Slider.getRating())
thisExp.addData('Q3_Slider.response', Q3_Slider.getRating())
thisExp.addData('Q4_Slider.response', Q4_Slider.getRating())
thisExp.addData('Q5_Slider.response', Q5_Slider.getRating())
thisExp.addData('Q6_Slider.response', Q6_Slider.getRating())
thisExp.addData('Q7_Slider.response', Q7_Slider.getRating())
thisExp.addData('Q8_Slider.response', Q8_Slider.getRating())
thisExp.addData('Q9_Slider.response', Q9_Slider.getRating())
thisExp.addData('Q10_Slider.response', Q10_Slider.getRating())
thisExp.addData('Q11_Slider.response', Q11_Slider.getRating())
thisExp.addData('Q12_Slider.response', Q12_Slider.getRating())
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
thisExp.addData('Q13_Slider.response', Q13_Slider.getRating())
thisExp.addData('Q14_Slider.response', Q14_Slider.getRating())
thisExp.addData('Q15_Slider.response', Q15_Slider.getRating())
thisExp.addData('Q16_Slider.response', Q16_Slider.getRating())
thisExp.addData('Q17_Slider.response', Q17_Slider.getRating())
thisExp.addData('Q18_Slider.response', Q18_Slider.getRating())
thisExp.addData('Q19_Slider.response', Q19_Slider.getRating())
thisExp.addData('Q20_Slider.response', Q20_Slider.getRating())
thisExp.addData('Q21_Slider.response', Q21_Slider.getRating())
thisExp.addData('Q22_Slider.response', Q22_Slider.getRating())
thisExp.addData('Q23_Slider.response', Q23_Slider.getRating())
# the Routine "Survey_Trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Text_Break"-------
continueRoutine = True
# update component parameters for each repeat
KeyResp_3.keys = []
KeyResp_3.rt = []
_KeyResp_3_allKeys = []
# keep track of which components have finished
Text_BreakComponents = [Text_Break_Txt, PresstoCont_3, KeyResp_3]
for thisComponent in Text_BreakComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Text_BreakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Text_Break"-------
while continueRoutine:
    # get current time
    t = Text_BreakClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Text_BreakClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Text_Break_Txt* updates
    if Text_Break_Txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Text_Break_Txt.frameNStart = frameN  # exact frame index
        Text_Break_Txt.tStart = t  # local t and not account for scr refresh
        Text_Break_Txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Text_Break_Txt, 'tStartRefresh')  # time at next scr refresh
        Text_Break_Txt.setAutoDraw(True)
    
    # *PresstoCont_3* updates
    if PresstoCont_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PresstoCont_3.frameNStart = frameN  # exact frame index
        PresstoCont_3.tStart = t  # local t and not account for scr refresh
        PresstoCont_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PresstoCont_3, 'tStartRefresh')  # time at next scr refresh
        PresstoCont_3.setAutoDraw(True)
    
    # *KeyResp_3* updates
    if KeyResp_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        KeyResp_3.frameNStart = frameN  # exact frame index
        KeyResp_3.tStart = t  # local t and not account for scr refresh
        KeyResp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(KeyResp_3, 'tStartRefresh')  # time at next scr refresh
        KeyResp_3.status = STARTED
        # keyboard checking is just starting
        KeyResp_3.clock.reset()  # now t=0
    if KeyResp_3.status == STARTED:
        theseKeys = KeyResp_3.getKeys(keyList=['space'], waitRelease=False)
        _KeyResp_3_allKeys.extend(theseKeys)
        if len(_KeyResp_3_allKeys):
            KeyResp_3.keys = _KeyResp_3_allKeys[-1].name  # just the last key pressed
            KeyResp_3.rt = _KeyResp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Text_BreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Text_Break"-------
for thisComponent in Text_BreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Text_Break" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Loop_2 = data.TrialHandler(nReps=0.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condtionsFile/textbasedconditionsFile.csv'),
    seed=None, name='Loop_2')
thisExp.addLoop(Loop_2)  # add the loop to the experiment
thisLoop_2 = Loop_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_2.rgb)
if thisLoop_2 != None:
    for paramName in thisLoop_2:
        exec('{} = thisLoop_2[paramName]'.format(paramName))

for thisLoop_2 in Loop_2:
    currentLoop = Loop_2
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_2.rgb)
    if thisLoop_2 != None:
        for paramName in thisLoop_2:
            exec('{} = thisLoop_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Text_Based"-------
    continueRoutine = True
    # update component parameters for each repeat
    Question_Txt_5.setText(txtStim)
    AI_Response_5.setText(AI_Resp)
    Accept_Deny_Button_5.reset()
    ConfidenceSlider_5.reset()
    Experimental_Images_5.setImage(stimFile)
    DenySlider_5.reset()
    # setup some python lists for storing info about the mouse_8
    mouse_8.x = []
    mouse_8.y = []
    mouse_8.leftButton = []
    mouse_8.midButton = []
    mouse_8.rightButton = []
    mouse_8.time = []
    mouse_8.clicked_name = []
    gotValidClick = False  # until a click is received
    AI_Response_Txt_5.setText('AI Response:')
    outlet.push_sample(x=[2])
    
    from psychopy import core# this returns a time value in seconds, not a clock object:
    
    clock = core.getAbsTime()
    
    import time
    
    from datetime import datetime
    
    ETrial= datetime.fromtimestamp(clock).strftime("%A, %B %d, %Y %I:%M:%S")
    
    Loop_2.addData('trial_start', ETrial)
    # keep track of which components have finished
    Text_BasedComponents = [Text_Intro_Txt, Question_Txt_5, AI_Response_5, Accept_Deny_Button_5, ConfidenceText_5, ConfidenceSlider_5, Experimental_Images_5, IfDenied_5, DenySlider_5, mouse_8, Click_to_Continue_8, AI_Response_Txt_5, Explanation_Image_5]
    for thisComponent in Text_BasedComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Text_BasedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Text_Based"-------
    while continueRoutine:
        # get current time
        t = Text_BasedClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Text_BasedClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Text_Intro_Txt* updates
        if Text_Intro_Txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Text_Intro_Txt.frameNStart = frameN  # exact frame index
            Text_Intro_Txt.tStart = t  # local t and not account for scr refresh
            Text_Intro_Txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Text_Intro_Txt, 'tStartRefresh')  # time at next scr refresh
            Text_Intro_Txt.setAutoDraw(True)
        if Text_Intro_Txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Text_Intro_Txt.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                Text_Intro_Txt.tStop = t  # not accounting for scr refresh
                Text_Intro_Txt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Text_Intro_Txt, 'tStopRefresh')  # time at next scr refresh
                Text_Intro_Txt.setAutoDraw(False)
        
        # *Question_Txt_5* updates
        if Question_Txt_5.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            Question_Txt_5.frameNStart = frameN  # exact frame index
            Question_Txt_5.tStart = t  # local t and not account for scr refresh
            Question_Txt_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Question_Txt_5, 'tStartRefresh')  # time at next scr refresh
            Question_Txt_5.setAutoDraw(True)
        
        # *AI_Response_5* updates
        if AI_Response_5.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            AI_Response_5.frameNStart = frameN  # exact frame index
            AI_Response_5.tStart = t  # local t and not account for scr refresh
            AI_Response_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AI_Response_5, 'tStartRefresh')  # time at next scr refresh
            AI_Response_5.setAutoDraw(True)
        
        # *Accept_Deny_Button_5* updates
        if Accept_Deny_Button_5.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            Accept_Deny_Button_5.frameNStart = frameN  # exact frame index
            Accept_Deny_Button_5.tStart = t  # local t and not account for scr refresh
            Accept_Deny_Button_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Accept_Deny_Button_5, 'tStartRefresh')  # time at next scr refresh
            Accept_Deny_Button_5.setAutoDraw(True)
        
        # *ConfidenceText_5* updates
        if ConfidenceText_5.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            ConfidenceText_5.frameNStart = frameN  # exact frame index
            ConfidenceText_5.tStart = t  # local t and not account for scr refresh
            ConfidenceText_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ConfidenceText_5, 'tStartRefresh')  # time at next scr refresh
            ConfidenceText_5.setAutoDraw(True)
        
        # *ConfidenceSlider_5* updates
        if ConfidenceSlider_5.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            ConfidenceSlider_5.frameNStart = frameN  # exact frame index
            ConfidenceSlider_5.tStart = t  # local t and not account for scr refresh
            ConfidenceSlider_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ConfidenceSlider_5, 'tStartRefresh')  # time at next scr refresh
            ConfidenceSlider_5.setAutoDraw(True)
        
        # *Experimental_Images_5* updates
        if Experimental_Images_5.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            Experimental_Images_5.frameNStart = frameN  # exact frame index
            Experimental_Images_5.tStart = t  # local t and not account for scr refresh
            Experimental_Images_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Experimental_Images_5, 'tStartRefresh')  # time at next scr refresh
            Experimental_Images_5.setAutoDraw(True)
        
        # *IfDenied_5* updates
        if IfDenied_5.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            IfDenied_5.frameNStart = frameN  # exact frame index
            IfDenied_5.tStart = t  # local t and not account for scr refresh
            IfDenied_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IfDenied_5, 'tStartRefresh')  # time at next scr refresh
            IfDenied_5.setAutoDraw(True)
        
        # *DenySlider_5* updates
        if DenySlider_5.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            DenySlider_5.frameNStart = frameN  # exact frame index
            DenySlider_5.tStart = t  # local t and not account for scr refresh
            DenySlider_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DenySlider_5, 'tStartRefresh')  # time at next scr refresh
            DenySlider_5.setAutoDraw(True)
        # *mouse_8* updates
        if mouse_8.status == NOT_STARTED and t >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_8.frameNStart = frameN  # exact frame index
            mouse_8.tStart = t  # local t and not account for scr refresh
            mouse_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_8, 'tStartRefresh')  # time at next scr refresh
            mouse_8.status = STARTED
            mouse_8.mouseClock.reset()
            prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
        if mouse_8.status == STARTED:  # only update if started and not finished!
            buttons = mouse_8.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(Click_to_Continue_8)
                        clickableList = Click_to_Continue_8
                    except:
                        clickableList = [Click_to_Continue_8]
                    for obj in clickableList:
                        if obj.contains(mouse_8):
                            gotValidClick = True
                            mouse_8.clicked_name.append(obj.name)
                    x, y = mouse_8.getPos()
                    mouse_8.x.append(x)
                    mouse_8.y.append(y)
                    buttons = mouse_8.getPressed()
                    mouse_8.leftButton.append(buttons[0])
                    mouse_8.midButton.append(buttons[1])
                    mouse_8.rightButton.append(buttons[2])
                    mouse_8.time.append(mouse_8.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # abort routine on response
        
        # *Click_to_Continue_8* updates
        if Click_to_Continue_8.status == NOT_STARTED and Accept_Deny_Button_5.rating and ConfidenceSlider_5.rating and DenySlider_5.rating:
            # keep track of start time/frame for later
            Click_to_Continue_8.frameNStart = frameN  # exact frame index
            Click_to_Continue_8.tStart = t  # local t and not account for scr refresh
            Click_to_Continue_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Click_to_Continue_8, 'tStartRefresh')  # time at next scr refresh
            Click_to_Continue_8.setAutoDraw(True)
        
        # *AI_Response_Txt_5* updates
        if AI_Response_Txt_5.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            AI_Response_Txt_5.frameNStart = frameN  # exact frame index
            AI_Response_Txt_5.tStart = t  # local t and not account for scr refresh
            AI_Response_Txt_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AI_Response_Txt_5, 'tStartRefresh')  # time at next scr refresh
            AI_Response_Txt_5.setAutoDraw(True)
        
        # *Explanation_Image_5* updates
        if Explanation_Image_5.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            Explanation_Image_5.frameNStart = frameN  # exact frame index
            Explanation_Image_5.tStart = t  # local t and not account for scr refresh
            Explanation_Image_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Explanation_Image_5, 'tStartRefresh')  # time at next scr refresh
            Explanation_Image_5.setAutoDraw(True)
        if Explanation_Image_5.status == STARTED:  # only update if drawing
            Explanation_Image_5.setImage(ExplanationFile, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Text_BasedComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Text_Based"-------
    for thisComponent in Text_BasedComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Loop_2.addData('Text_Intro_Txt.started', Text_Intro_Txt.tStartRefresh)
    Loop_2.addData('Text_Intro_Txt.stopped', Text_Intro_Txt.tStopRefresh)
    Loop_2.addData('Question_Txt_5.started', Question_Txt_5.tStartRefresh)
    Loop_2.addData('Question_Txt_5.stopped', Question_Txt_5.tStopRefresh)
    Loop_2.addData('Accept_Deny_Button_5.response', Accept_Deny_Button_5.getRating())
    Loop_2.addData('Accept_Deny_Button_5.rt', Accept_Deny_Button_5.getRT())
    Loop_2.addData('Accept_Deny_Button_5.started', Accept_Deny_Button_5.tStartRefresh)
    Loop_2.addData('Accept_Deny_Button_5.stopped', Accept_Deny_Button_5.tStopRefresh)
    Loop_2.addData('ConfidenceSlider_5.response', ConfidenceSlider_5.getRating())
    Loop_2.addData('ConfidenceSlider_5.rt', ConfidenceSlider_5.getRT())
    Loop_2.addData('ConfidenceSlider_5.started', ConfidenceSlider_5.tStartRefresh)
    Loop_2.addData('ConfidenceSlider_5.stopped', ConfidenceSlider_5.tStopRefresh)
    Loop_2.addData('DenySlider_5.response', DenySlider_5.getRating())
    Loop_2.addData('DenySlider_5.rt', DenySlider_5.getRT())
    Loop_2.addData('DenySlider_5.started', DenySlider_5.tStartRefresh)
    Loop_2.addData('DenySlider_5.stopped', DenySlider_5.tStopRefresh)
    # store data for Loop_2 (TrialHandler)
    Loop_2.addData('mouse_8.x', mouse_8.x)
    Loop_2.addData('mouse_8.y', mouse_8.y)
    Loop_2.addData('mouse_8.leftButton', mouse_8.leftButton)
    Loop_2.addData('mouse_8.midButton', mouse_8.midButton)
    Loop_2.addData('mouse_8.rightButton', mouse_8.rightButton)
    Loop_2.addData('mouse_8.time', mouse_8.time)
    Loop_2.addData('mouse_8.clicked_name', mouse_8.clicked_name)
    Loop_2.addData('mouse_8.started', mouse_8.tStart)
    Loop_2.addData('mouse_8.stopped', mouse_8.tStop)
    Loop_2.addData('Click_to_Continue_8.started', Click_to_Continue_8.tStartRefresh)
    Loop_2.addData('Click_to_Continue_8.stopped', Click_to_Continue_8.tStopRefresh)
    outlet.push_sample(x=[2])
    
    from psychopy import core# this returns a time value in seconds, not a clock object:
    
    clock = core.getAbsTime()
    
    import time
    
    from datetime import datetime
    
    ETrial= datetime.fromtimestamp(clock).strftime("%A, %B %d, %Y %I:%M:%S")
    
    Loop_2.addData('trial_end', ETrial)
    # the Routine "Text_Based" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'Loop_2'

# get names of stimulus parameters
if Loop_2.trialList in ([], [None], None):
    params = []
else:
    params = Loop_2.trialList[0].keys()
# save data for this loop
Loop_2.saveAsExcel(filename + '.xlsx', sheetName='Loop_2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
Loop_2.saveAsText(filename + 'Loop_2.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Text_Survey_Break"-------
continueRoutine = True
# update component parameters for each repeat
KeyResp_2.keys = []
KeyResp_2.rt = []
_KeyResp_2_allKeys = []
# keep track of which components have finished
Text_Survey_BreakComponents = [text_4, PresstoCont_2, KeyResp_2]
for thisComponent in Text_Survey_BreakComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Text_Survey_BreakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Text_Survey_Break"-------
while continueRoutine:
    # get current time
    t = Text_Survey_BreakClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Text_Survey_BreakClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # *PresstoCont_2* updates
    if PresstoCont_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PresstoCont_2.frameNStart = frameN  # exact frame index
        PresstoCont_2.tStart = t  # local t and not account for scr refresh
        PresstoCont_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PresstoCont_2, 'tStartRefresh')  # time at next scr refresh
        PresstoCont_2.setAutoDraw(True)
    
    # *KeyResp_2* updates
    if KeyResp_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        KeyResp_2.frameNStart = frameN  # exact frame index
        KeyResp_2.tStart = t  # local t and not account for scr refresh
        KeyResp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(KeyResp_2, 'tStartRefresh')  # time at next scr refresh
        KeyResp_2.status = STARTED
        # keyboard checking is just starting
        KeyResp_2.clock.reset()  # now t=0
    if KeyResp_2.status == STARTED:
        theseKeys = KeyResp_2.getKeys(keyList=['space'], waitRelease=False)
        _KeyResp_2_allKeys.extend(theseKeys)
        if len(_KeyResp_2_allKeys):
            KeyResp_2.keys = _KeyResp_2_allKeys[-1].name  # just the last key pressed
            KeyResp_2.rt = _KeyResp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Text_Survey_BreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Text_Survey_Break"-------
for thisComponent in Text_Survey_BreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Text_Survey_Break" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Survey_Trial"-------
continueRoutine = True
# update component parameters for each repeat
Q1_Slider.reset()
Q2_Slider.reset()
Q3_Slider.reset()
Q4_Slider.reset()
Q5_Slider.reset()
Q6_Slider.reset()
Q7_Slider.reset()
Q8_Slider.reset()
Q9_Slider.reset()
Q10_Slider.reset()
Q11_Slider.reset()
Q12_Slider.reset()
# setup some python lists for storing info about the mouse_2
mouse_2.clicked_name = []
gotValidClick = False  # until a click is received
Q13_Slider.reset()
Q14_Slider.reset()
Q15_Slider.reset()
Q16_Slider.reset()
Q17_Slider.reset()
Q18_Slider.reset()
Q19_Slider.reset()
Q20_Slider.reset()
Q21_Slider.reset()
Q22_Slider.reset()
Q23_Slider.reset()
# keep track of which components have finished
Survey_TrialComponents = [Q1, Q1_Slider, Q2, Q2_Slider, Q3, Q3_Slider, Q4, Q4_Slider, Q5, Q5_Slider, Q6, Q6_Slider, Q7, Q7_Slider, Q8, Q8_Slider, Q9, Q9_Slider, Q10, Q10_Slider, Q11, Q11_Slider, Q12, Q12_Slider, mouse_2, Click_to_Continue_2, Q13, Q13_Slider, Q14, Q14_Slider, Q15, Q15_Slider, Q16, Q16_Slider, Q17, Q17_Slider, Q18, Q18_Slider, Q19, Q19_Slider, Q20, Q20_Slider, Q21, Q21_Slider, Q22, Q22_Slider, Q23, Q23_Slider]
for thisComponent in Survey_TrialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Survey_TrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Survey_Trial"-------
while continueRoutine:
    # get current time
    t = Survey_TrialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Survey_TrialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Q1* updates
    if Q1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q1.frameNStart = frameN  # exact frame index
        Q1.tStart = t  # local t and not account for scr refresh
        Q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q1, 'tStartRefresh')  # time at next scr refresh
        Q1.setAutoDraw(True)
    if Q1.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q1.tStop = t  # not accounting for scr refresh
            Q1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q1, 'tStopRefresh')  # time at next scr refresh
            Q1.setAutoDraw(False)
    
    # *Q1_Slider* updates
    if Q1_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q1_Slider.frameNStart = frameN  # exact frame index
        Q1_Slider.tStart = t  # local t and not account for scr refresh
        Q1_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q1_Slider, 'tStartRefresh')  # time at next scr refresh
        Q1_Slider.setAutoDraw(True)
    if Q1_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q1_Slider.tStop = t  # not accounting for scr refresh
            Q1_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q1_Slider, 'tStopRefresh')  # time at next scr refresh
            Q1_Slider.setAutoDraw(False)
    
    # *Q2* updates
    if Q2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q2.frameNStart = frameN  # exact frame index
        Q2.tStart = t  # local t and not account for scr refresh
        Q2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q2, 'tStartRefresh')  # time at next scr refresh
        Q2.setAutoDraw(True)
    if Q2.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q2.tStop = t  # not accounting for scr refresh
            Q2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q2, 'tStopRefresh')  # time at next scr refresh
            Q2.setAutoDraw(False)
    
    # *Q2_Slider* updates
    if Q2_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q2_Slider.frameNStart = frameN  # exact frame index
        Q2_Slider.tStart = t  # local t and not account for scr refresh
        Q2_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q2_Slider, 'tStartRefresh')  # time at next scr refresh
        Q2_Slider.setAutoDraw(True)
    if Q2_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q2_Slider.tStop = t  # not accounting for scr refresh
            Q2_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q2_Slider, 'tStopRefresh')  # time at next scr refresh
            Q2_Slider.setAutoDraw(False)
    
    # *Q3* updates
    if Q3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q3.frameNStart = frameN  # exact frame index
        Q3.tStart = t  # local t and not account for scr refresh
        Q3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q3, 'tStartRefresh')  # time at next scr refresh
        Q3.setAutoDraw(True)
    if Q3.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q3.tStop = t  # not accounting for scr refresh
            Q3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q3, 'tStopRefresh')  # time at next scr refresh
            Q3.setAutoDraw(False)
    
    # *Q3_Slider* updates
    if Q3_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q3_Slider.frameNStart = frameN  # exact frame index
        Q3_Slider.tStart = t  # local t and not account for scr refresh
        Q3_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q3_Slider, 'tStartRefresh')  # time at next scr refresh
        Q3_Slider.setAutoDraw(True)
    if Q3_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q3_Slider.tStop = t  # not accounting for scr refresh
            Q3_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q3_Slider, 'tStopRefresh')  # time at next scr refresh
            Q3_Slider.setAutoDraw(False)
    
    # *Q4* updates
    if Q4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q4.frameNStart = frameN  # exact frame index
        Q4.tStart = t  # local t and not account for scr refresh
        Q4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q4, 'tStartRefresh')  # time at next scr refresh
        Q4.setAutoDraw(True)
    if Q4.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q4.tStop = t  # not accounting for scr refresh
            Q4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q4, 'tStopRefresh')  # time at next scr refresh
            Q4.setAutoDraw(False)
    
    # *Q4_Slider* updates
    if Q4_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q4_Slider.frameNStart = frameN  # exact frame index
        Q4_Slider.tStart = t  # local t and not account for scr refresh
        Q4_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q4_Slider, 'tStartRefresh')  # time at next scr refresh
        Q4_Slider.setAutoDraw(True)
    if Q4_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q4_Slider.tStop = t  # not accounting for scr refresh
            Q4_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q4_Slider, 'tStopRefresh')  # time at next scr refresh
            Q4_Slider.setAutoDraw(False)
    
    # *Q5* updates
    if Q5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q5.frameNStart = frameN  # exact frame index
        Q5.tStart = t  # local t and not account for scr refresh
        Q5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q5, 'tStartRefresh')  # time at next scr refresh
        Q5.setAutoDraw(True)
    if Q5.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q5.tStop = t  # not accounting for scr refresh
            Q5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q5, 'tStopRefresh')  # time at next scr refresh
            Q5.setAutoDraw(False)
    
    # *Q5_Slider* updates
    if Q5_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q5_Slider.frameNStart = frameN  # exact frame index
        Q5_Slider.tStart = t  # local t and not account for scr refresh
        Q5_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q5_Slider, 'tStartRefresh')  # time at next scr refresh
        Q5_Slider.setAutoDraw(True)
    if Q5_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q5_Slider.tStop = t  # not accounting for scr refresh
            Q5_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q5_Slider, 'tStopRefresh')  # time at next scr refresh
            Q5_Slider.setAutoDraw(False)
    
    # *Q6* updates
    if Q6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q6.frameNStart = frameN  # exact frame index
        Q6.tStart = t  # local t and not account for scr refresh
        Q6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q6, 'tStartRefresh')  # time at next scr refresh
        Q6.setAutoDraw(True)
    if Q6.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q6.tStop = t  # not accounting for scr refresh
            Q6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q6, 'tStopRefresh')  # time at next scr refresh
            Q6.setAutoDraw(False)
    
    # *Q6_Slider* updates
    if Q6_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q6_Slider.frameNStart = frameN  # exact frame index
        Q6_Slider.tStart = t  # local t and not account for scr refresh
        Q6_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q6_Slider, 'tStartRefresh')  # time at next scr refresh
        Q6_Slider.setAutoDraw(True)
    if Q6_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q6_Slider.tStop = t  # not accounting for scr refresh
            Q6_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q6_Slider, 'tStopRefresh')  # time at next scr refresh
            Q6_Slider.setAutoDraw(False)
    
    # *Q7* updates
    if Q7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q7.frameNStart = frameN  # exact frame index
        Q7.tStart = t  # local t and not account for scr refresh
        Q7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q7, 'tStartRefresh')  # time at next scr refresh
        Q7.setAutoDraw(True)
    if Q7.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q7.tStop = t  # not accounting for scr refresh
            Q7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q7, 'tStopRefresh')  # time at next scr refresh
            Q7.setAutoDraw(False)
    
    # *Q7_Slider* updates
    if Q7_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q7_Slider.frameNStart = frameN  # exact frame index
        Q7_Slider.tStart = t  # local t and not account for scr refresh
        Q7_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q7_Slider, 'tStartRefresh')  # time at next scr refresh
        Q7_Slider.setAutoDraw(True)
    if Q7_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q7_Slider.tStop = t  # not accounting for scr refresh
            Q7_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q7_Slider, 'tStopRefresh')  # time at next scr refresh
            Q7_Slider.setAutoDraw(False)
    
    # *Q8* updates
    if Q8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q8.frameNStart = frameN  # exact frame index
        Q8.tStart = t  # local t and not account for scr refresh
        Q8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q8, 'tStartRefresh')  # time at next scr refresh
        Q8.setAutoDraw(True)
    if Q8.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q8.tStop = t  # not accounting for scr refresh
            Q8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q8, 'tStopRefresh')  # time at next scr refresh
            Q8.setAutoDraw(False)
    
    # *Q8_Slider* updates
    if Q8_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q8_Slider.frameNStart = frameN  # exact frame index
        Q8_Slider.tStart = t  # local t and not account for scr refresh
        Q8_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q8_Slider, 'tStartRefresh')  # time at next scr refresh
        Q8_Slider.setAutoDraw(True)
    if Q8_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q8_Slider.tStop = t  # not accounting for scr refresh
            Q8_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q8_Slider, 'tStopRefresh')  # time at next scr refresh
            Q8_Slider.setAutoDraw(False)
    
    # *Q9* updates
    if Q9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q9.frameNStart = frameN  # exact frame index
        Q9.tStart = t  # local t and not account for scr refresh
        Q9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q9, 'tStartRefresh')  # time at next scr refresh
        Q9.setAutoDraw(True)
    if Q9.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q9.tStop = t  # not accounting for scr refresh
            Q9.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q9, 'tStopRefresh')  # time at next scr refresh
            Q9.setAutoDraw(False)
    
    # *Q9_Slider* updates
    if Q9_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q9_Slider.frameNStart = frameN  # exact frame index
        Q9_Slider.tStart = t  # local t and not account for scr refresh
        Q9_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q9_Slider, 'tStartRefresh')  # time at next scr refresh
        Q9_Slider.setAutoDraw(True)
    if Q9_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q9_Slider.tStop = t  # not accounting for scr refresh
            Q9_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q9_Slider, 'tStopRefresh')  # time at next scr refresh
            Q9_Slider.setAutoDraw(False)
    
    # *Q10* updates
    if Q10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q10.frameNStart = frameN  # exact frame index
        Q10.tStart = t  # local t and not account for scr refresh
        Q10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q10, 'tStartRefresh')  # time at next scr refresh
        Q10.setAutoDraw(True)
    if Q10.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q10.tStop = t  # not accounting for scr refresh
            Q10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q10, 'tStopRefresh')  # time at next scr refresh
            Q10.setAutoDraw(False)
    
    # *Q10_Slider* updates
    if Q10_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q10_Slider.frameNStart = frameN  # exact frame index
        Q10_Slider.tStart = t  # local t and not account for scr refresh
        Q10_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q10_Slider, 'tStartRefresh')  # time at next scr refresh
        Q10_Slider.setAutoDraw(True)
    if Q10_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q10_Slider.tStop = t  # not accounting for scr refresh
            Q10_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q10_Slider, 'tStopRefresh')  # time at next scr refresh
            Q10_Slider.setAutoDraw(False)
    
    # *Q11* updates
    if Q11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q11.frameNStart = frameN  # exact frame index
        Q11.tStart = t  # local t and not account for scr refresh
        Q11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q11, 'tStartRefresh')  # time at next scr refresh
        Q11.setAutoDraw(True)
    if Q11.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q11.tStop = t  # not accounting for scr refresh
            Q11.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q11, 'tStopRefresh')  # time at next scr refresh
            Q11.setAutoDraw(False)
    
    # *Q11_Slider* updates
    if Q11_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q11_Slider.frameNStart = frameN  # exact frame index
        Q11_Slider.tStart = t  # local t and not account for scr refresh
        Q11_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q11_Slider, 'tStartRefresh')  # time at next scr refresh
        Q11_Slider.setAutoDraw(True)
    if Q11_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q11_Slider.tStop = t  # not accounting for scr refresh
            Q11_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q11_Slider, 'tStopRefresh')  # time at next scr refresh
            Q11_Slider.setAutoDraw(False)
    
    # *Q12* updates
    if Q12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q12.frameNStart = frameN  # exact frame index
        Q12.tStart = t  # local t and not account for scr refresh
        Q12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q12, 'tStartRefresh')  # time at next scr refresh
        Q12.setAutoDraw(True)
    if Q12.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q12.tStop = t  # not accounting for scr refresh
            Q12.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q12, 'tStopRefresh')  # time at next scr refresh
            Q12.setAutoDraw(False)
    
    # *Q12_Slider* updates
    if Q12_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q12_Slider.frameNStart = frameN  # exact frame index
        Q12_Slider.tStart = t  # local t and not account for scr refresh
        Q12_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q12_Slider, 'tStartRefresh')  # time at next scr refresh
        Q12_Slider.setAutoDraw(True)
    if Q12_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q12_Slider.tStop = t  # not accounting for scr refresh
            Q12_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q12_Slider, 'tStopRefresh')  # time at next scr refresh
            Q12_Slider.setAutoDraw(False)
    # *mouse_2* updates
    if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_2.frameNStart = frameN  # exact frame index
        mouse_2.tStart = t  # local t and not account for scr refresh
        mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
        mouse_2.status = STARTED
        mouse_2.mouseClock.reset()
        prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
    if mouse_2.status == STARTED:  # only update if started and not finished!
        buttons = mouse_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(Click_to_Continue_2)
                    clickableList = Click_to_Continue_2
                except:
                    clickableList = [Click_to_Continue_2]
                for obj in clickableList:
                    if obj.contains(mouse_2):
                        gotValidClick = True
                        mouse_2.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # *Click_to_Continue_2* updates
    if Click_to_Continue_2.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating and Q13_Slider.rating and Q14_Slider.rating and Q15_Slider.rating and Q16_Slider.rating and Q17_Slider.rating and Q18_Slider.rating and Q19_Slider.rating and Q20_Slider.rating and Q21_Slider.rating and Q22_Slider.rating and Q23_Slider.rating:
        # keep track of start time/frame for later
        Click_to_Continue_2.frameNStart = frameN  # exact frame index
        Click_to_Continue_2.tStart = t  # local t and not account for scr refresh
        Click_to_Continue_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Click_to_Continue_2, 'tStartRefresh')  # time at next scr refresh
        Click_to_Continue_2.setAutoDraw(True)
    
    # *Q13* updates
    if Q13.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q13.frameNStart = frameN  # exact frame index
        Q13.tStart = t  # local t and not account for scr refresh
        Q13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q13, 'tStartRefresh')  # time at next scr refresh
        Q13.setAutoDraw(True)
    
    # *Q13_Slider* updates
    if Q13_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q13_Slider.frameNStart = frameN  # exact frame index
        Q13_Slider.tStart = t  # local t and not account for scr refresh
        Q13_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q13_Slider, 'tStartRefresh')  # time at next scr refresh
        Q13_Slider.setAutoDraw(True)
    
    # *Q14* updates
    if Q14.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q14.frameNStart = frameN  # exact frame index
        Q14.tStart = t  # local t and not account for scr refresh
        Q14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q14, 'tStartRefresh')  # time at next scr refresh
        Q14.setAutoDraw(True)
    
    # *Q14_Slider* updates
    if Q14_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q14_Slider.frameNStart = frameN  # exact frame index
        Q14_Slider.tStart = t  # local t and not account for scr refresh
        Q14_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q14_Slider, 'tStartRefresh')  # time at next scr refresh
        Q14_Slider.setAutoDraw(True)
    
    # *Q15* updates
    if Q15.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q15.frameNStart = frameN  # exact frame index
        Q15.tStart = t  # local t and not account for scr refresh
        Q15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q15, 'tStartRefresh')  # time at next scr refresh
        Q15.setAutoDraw(True)
    
    # *Q15_Slider* updates
    if Q15_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q15_Slider.frameNStart = frameN  # exact frame index
        Q15_Slider.tStart = t  # local t and not account for scr refresh
        Q15_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q15_Slider, 'tStartRefresh')  # time at next scr refresh
        Q15_Slider.setAutoDraw(True)
    
    # *Q16* updates
    if Q16.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q16.frameNStart = frameN  # exact frame index
        Q16.tStart = t  # local t and not account for scr refresh
        Q16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q16, 'tStartRefresh')  # time at next scr refresh
        Q16.setAutoDraw(True)
    
    # *Q16_Slider* updates
    if Q16_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q16_Slider.frameNStart = frameN  # exact frame index
        Q16_Slider.tStart = t  # local t and not account for scr refresh
        Q16_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q16_Slider, 'tStartRefresh')  # time at next scr refresh
        Q16_Slider.setAutoDraw(True)
    
    # *Q17* updates
    if Q17.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q17.frameNStart = frameN  # exact frame index
        Q17.tStart = t  # local t and not account for scr refresh
        Q17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q17, 'tStartRefresh')  # time at next scr refresh
        Q17.setAutoDraw(True)
    
    # *Q17_Slider* updates
    if Q17_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q17_Slider.frameNStart = frameN  # exact frame index
        Q17_Slider.tStart = t  # local t and not account for scr refresh
        Q17_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q17_Slider, 'tStartRefresh')  # time at next scr refresh
        Q17_Slider.setAutoDraw(True)
    
    # *Q18* updates
    if Q18.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q18.frameNStart = frameN  # exact frame index
        Q18.tStart = t  # local t and not account for scr refresh
        Q18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q18, 'tStartRefresh')  # time at next scr refresh
        Q18.setAutoDraw(True)
    
    # *Q18_Slider* updates
    if Q18_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q18_Slider.frameNStart = frameN  # exact frame index
        Q18_Slider.tStart = t  # local t and not account for scr refresh
        Q18_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q18_Slider, 'tStartRefresh')  # time at next scr refresh
        Q18_Slider.setAutoDraw(True)
    
    # *Q19* updates
    if Q19.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q19.frameNStart = frameN  # exact frame index
        Q19.tStart = t  # local t and not account for scr refresh
        Q19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q19, 'tStartRefresh')  # time at next scr refresh
        Q19.setAutoDraw(True)
    
    # *Q19_Slider* updates
    if Q19_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q19_Slider.frameNStart = frameN  # exact frame index
        Q19_Slider.tStart = t  # local t and not account for scr refresh
        Q19_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q19_Slider, 'tStartRefresh')  # time at next scr refresh
        Q19_Slider.setAutoDraw(True)
    
    # *Q20* updates
    if Q20.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q20.frameNStart = frameN  # exact frame index
        Q20.tStart = t  # local t and not account for scr refresh
        Q20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q20, 'tStartRefresh')  # time at next scr refresh
        Q20.setAutoDraw(True)
    
    # *Q20_Slider* updates
    if Q20_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q20_Slider.frameNStart = frameN  # exact frame index
        Q20_Slider.tStart = t  # local t and not account for scr refresh
        Q20_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q20_Slider, 'tStartRefresh')  # time at next scr refresh
        Q20_Slider.setAutoDraw(True)
    
    # *Q21* updates
    if Q21.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q21.frameNStart = frameN  # exact frame index
        Q21.tStart = t  # local t and not account for scr refresh
        Q21.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q21, 'tStartRefresh')  # time at next scr refresh
        Q21.setAutoDraw(True)
    
    # *Q21_Slider* updates
    if Q21_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q21_Slider.frameNStart = frameN  # exact frame index
        Q21_Slider.tStart = t  # local t and not account for scr refresh
        Q21_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q21_Slider, 'tStartRefresh')  # time at next scr refresh
        Q21_Slider.setAutoDraw(True)
    
    # *Q22* updates
    if Q22.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q22.frameNStart = frameN  # exact frame index
        Q22.tStart = t  # local t and not account for scr refresh
        Q22.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q22, 'tStartRefresh')  # time at next scr refresh
        Q22.setAutoDraw(True)
    
    # *Q22_Slider* updates
    if Q22_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q22_Slider.frameNStart = frameN  # exact frame index
        Q22_Slider.tStart = t  # local t and not account for scr refresh
        Q22_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q22_Slider, 'tStartRefresh')  # time at next scr refresh
        Q22_Slider.setAutoDraw(True)
    
    # *Q23* updates
    if Q23.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q23.frameNStart = frameN  # exact frame index
        Q23.tStart = t  # local t and not account for scr refresh
        Q23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q23, 'tStartRefresh')  # time at next scr refresh
        Q23.setAutoDraw(True)
    
    # *Q23_Slider* updates
    if Q23_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q23_Slider.frameNStart = frameN  # exact frame index
        Q23_Slider.tStart = t  # local t and not account for scr refresh
        Q23_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q23_Slider, 'tStartRefresh')  # time at next scr refresh
        Q23_Slider.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Survey_TrialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Survey_Trial"-------
for thisComponent in Survey_TrialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Q1_Slider.response', Q1_Slider.getRating())
thisExp.addData('Q2_Slider.response', Q2_Slider.getRating())
thisExp.addData('Q3_Slider.response', Q3_Slider.getRating())
thisExp.addData('Q4_Slider.response', Q4_Slider.getRating())
thisExp.addData('Q5_Slider.response', Q5_Slider.getRating())
thisExp.addData('Q6_Slider.response', Q6_Slider.getRating())
thisExp.addData('Q7_Slider.response', Q7_Slider.getRating())
thisExp.addData('Q8_Slider.response', Q8_Slider.getRating())
thisExp.addData('Q9_Slider.response', Q9_Slider.getRating())
thisExp.addData('Q10_Slider.response', Q10_Slider.getRating())
thisExp.addData('Q11_Slider.response', Q11_Slider.getRating())
thisExp.addData('Q12_Slider.response', Q12_Slider.getRating())
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
thisExp.addData('Q13_Slider.response', Q13_Slider.getRating())
thisExp.addData('Q14_Slider.response', Q14_Slider.getRating())
thisExp.addData('Q15_Slider.response', Q15_Slider.getRating())
thisExp.addData('Q16_Slider.response', Q16_Slider.getRating())
thisExp.addData('Q17_Slider.response', Q17_Slider.getRating())
thisExp.addData('Q18_Slider.response', Q18_Slider.getRating())
thisExp.addData('Q19_Slider.response', Q19_Slider.getRating())
thisExp.addData('Q20_Slider.response', Q20_Slider.getRating())
thisExp.addData('Q21_Slider.response', Q21_Slider.getRating())
thisExp.addData('Q22_Slider.response', Q22_Slider.getRating())
thisExp.addData('Q23_Slider.response', Q23_Slider.getRating())
# the Routine "Survey_Trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Image_Break"-------
continueRoutine = True
# update component parameters for each repeat
KeyResp_5.keys = []
KeyResp_5.rt = []
_KeyResp_5_allKeys = []
# keep track of which components have finished
Image_BreakComponents = [Image_Break_Txt, PresstoCont_5, KeyResp_5]
for thisComponent in Image_BreakComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Image_BreakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Image_Break"-------
while continueRoutine:
    # get current time
    t = Image_BreakClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Image_BreakClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Image_Break_Txt* updates
    if Image_Break_Txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Image_Break_Txt.frameNStart = frameN  # exact frame index
        Image_Break_Txt.tStart = t  # local t and not account for scr refresh
        Image_Break_Txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image_Break_Txt, 'tStartRefresh')  # time at next scr refresh
        Image_Break_Txt.setAutoDraw(True)
    
    # *PresstoCont_5* updates
    if PresstoCont_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PresstoCont_5.frameNStart = frameN  # exact frame index
        PresstoCont_5.tStart = t  # local t and not account for scr refresh
        PresstoCont_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PresstoCont_5, 'tStartRefresh')  # time at next scr refresh
        PresstoCont_5.setAutoDraw(True)
    
    # *KeyResp_5* updates
    if KeyResp_5.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        KeyResp_5.frameNStart = frameN  # exact frame index
        KeyResp_5.tStart = t  # local t and not account for scr refresh
        KeyResp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(KeyResp_5, 'tStartRefresh')  # time at next scr refresh
        KeyResp_5.status = STARTED
        # keyboard checking is just starting
        KeyResp_5.clock.reset()  # now t=0
    if KeyResp_5.status == STARTED:
        theseKeys = KeyResp_5.getKeys(keyList=['space'], waitRelease=False)
        _KeyResp_5_allKeys.extend(theseKeys)
        if len(_KeyResp_5_allKeys):
            KeyResp_5.keys = _KeyResp_5_allKeys[-1].name  # just the last key pressed
            KeyResp_5.rt = _KeyResp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Image_BreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Image_Break"-------
for thisComponent in Image_BreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Image_Break" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Loop_3 = data.TrialHandler(nReps=0.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condtionsFile/imagebasedconditionsFile.csv'),
    seed=None, name='Loop_3')
thisExp.addLoop(Loop_3)  # add the loop to the experiment
thisLoop_3 = Loop_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_3.rgb)
if thisLoop_3 != None:
    for paramName in thisLoop_3:
        exec('{} = thisLoop_3[paramName]'.format(paramName))

for thisLoop_3 in Loop_3:
    currentLoop = Loop_3
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_3.rgb)
    if thisLoop_3 != None:
        for paramName in thisLoop_3:
            exec('{} = thisLoop_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Image_Based"-------
    continueRoutine = True
    # update component parameters for each repeat
    Question_Txt_4.setText(txtStim)
    AI_Response_4.setText(AI_Resp)
    Accept_Deny_Button_4.reset()
    ConfidenceSlider_4.reset()
    Experimental_Images_4.setImage(stimFile)
    DenySlider_4.reset()
    # setup some python lists for storing info about the mouse_7
    mouse_7.x = []
    mouse_7.y = []
    mouse_7.leftButton = []
    mouse_7.midButton = []
    mouse_7.rightButton = []
    mouse_7.time = []
    mouse_7.clicked_name = []
    gotValidClick = False  # until a click is received
    AI_Response_Txt_4.setText('AI Response:')
    outlet.push_sample(x=[3])
    
    from psychopy import core# this returns a time value in seconds, not a clock object:
    
    clock = core.getAbsTime()
    
    import time
    
    from datetime import datetime
    
    ETrial= datetime.fromtimestamp(clock).strftime("%A, %B %d, %Y %I:%M:%S")
    
    Loop_3.addData('trial_start', ETrial)
    # keep track of which components have finished
    Image_BasedComponents = [Image_Intro_Txt, Question_Txt_4, AI_Response_4, Accept_Deny_Button_4, ConfidenceText_4, ConfidenceSlider_4, Experimental_Images_4, IfDenied_4, DenySlider_4, mouse_7, Click_to_Continue_7, AI_Response_Txt_4, Explanation_Image_4]
    for thisComponent in Image_BasedComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Image_BasedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Image_Based"-------
    while continueRoutine:
        # get current time
        t = Image_BasedClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Image_BasedClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Image_Intro_Txt* updates
        if Image_Intro_Txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Image_Intro_Txt.frameNStart = frameN  # exact frame index
            Image_Intro_Txt.tStart = t  # local t and not account for scr refresh
            Image_Intro_Txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Image_Intro_Txt, 'tStartRefresh')  # time at next scr refresh
            Image_Intro_Txt.setAutoDraw(True)
        if Image_Intro_Txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Image_Intro_Txt.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                Image_Intro_Txt.tStop = t  # not accounting for scr refresh
                Image_Intro_Txt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Image_Intro_Txt, 'tStopRefresh')  # time at next scr refresh
                Image_Intro_Txt.setAutoDraw(False)
        
        # *Question_Txt_4* updates
        if Question_Txt_4.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            Question_Txt_4.frameNStart = frameN  # exact frame index
            Question_Txt_4.tStart = t  # local t and not account for scr refresh
            Question_Txt_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Question_Txt_4, 'tStartRefresh')  # time at next scr refresh
            Question_Txt_4.setAutoDraw(True)
        
        # *AI_Response_4* updates
        if AI_Response_4.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            AI_Response_4.frameNStart = frameN  # exact frame index
            AI_Response_4.tStart = t  # local t and not account for scr refresh
            AI_Response_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AI_Response_4, 'tStartRefresh')  # time at next scr refresh
            AI_Response_4.setAutoDraw(True)
        
        # *Accept_Deny_Button_4* updates
        if Accept_Deny_Button_4.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            Accept_Deny_Button_4.frameNStart = frameN  # exact frame index
            Accept_Deny_Button_4.tStart = t  # local t and not account for scr refresh
            Accept_Deny_Button_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Accept_Deny_Button_4, 'tStartRefresh')  # time at next scr refresh
            Accept_Deny_Button_4.setAutoDraw(True)
        
        # *ConfidenceText_4* updates
        if ConfidenceText_4.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            ConfidenceText_4.frameNStart = frameN  # exact frame index
            ConfidenceText_4.tStart = t  # local t and not account for scr refresh
            ConfidenceText_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ConfidenceText_4, 'tStartRefresh')  # time at next scr refresh
            ConfidenceText_4.setAutoDraw(True)
        
        # *ConfidenceSlider_4* updates
        if ConfidenceSlider_4.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            ConfidenceSlider_4.frameNStart = frameN  # exact frame index
            ConfidenceSlider_4.tStart = t  # local t and not account for scr refresh
            ConfidenceSlider_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ConfidenceSlider_4, 'tStartRefresh')  # time at next scr refresh
            ConfidenceSlider_4.setAutoDraw(True)
        
        # *Experimental_Images_4* updates
        if Experimental_Images_4.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            Experimental_Images_4.frameNStart = frameN  # exact frame index
            Experimental_Images_4.tStart = t  # local t and not account for scr refresh
            Experimental_Images_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Experimental_Images_4, 'tStartRefresh')  # time at next scr refresh
            Experimental_Images_4.setAutoDraw(True)
        
        # *IfDenied_4* updates
        if IfDenied_4.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            IfDenied_4.frameNStart = frameN  # exact frame index
            IfDenied_4.tStart = t  # local t and not account for scr refresh
            IfDenied_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IfDenied_4, 'tStartRefresh')  # time at next scr refresh
            IfDenied_4.setAutoDraw(True)
        
        # *DenySlider_4* updates
        if DenySlider_4.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            DenySlider_4.frameNStart = frameN  # exact frame index
            DenySlider_4.tStart = t  # local t and not account for scr refresh
            DenySlider_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DenySlider_4, 'tStartRefresh')  # time at next scr refresh
            DenySlider_4.setAutoDraw(True)
        # *mouse_7* updates
        if mouse_7.status == NOT_STARTED and t >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_7.frameNStart = frameN  # exact frame index
            mouse_7.tStart = t  # local t and not account for scr refresh
            mouse_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_7, 'tStartRefresh')  # time at next scr refresh
            mouse_7.status = STARTED
            mouse_7.mouseClock.reset()
            prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
        if mouse_7.status == STARTED:  # only update if started and not finished!
            buttons = mouse_7.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(Click_to_Continue_7)
                        clickableList = Click_to_Continue_7
                    except:
                        clickableList = [Click_to_Continue_7]
                    for obj in clickableList:
                        if obj.contains(mouse_7):
                            gotValidClick = True
                            mouse_7.clicked_name.append(obj.name)
                    x, y = mouse_7.getPos()
                    mouse_7.x.append(x)
                    mouse_7.y.append(y)
                    buttons = mouse_7.getPressed()
                    mouse_7.leftButton.append(buttons[0])
                    mouse_7.midButton.append(buttons[1])
                    mouse_7.rightButton.append(buttons[2])
                    mouse_7.time.append(mouse_7.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # abort routine on response
        
        # *Click_to_Continue_7* updates
        if Click_to_Continue_7.status == NOT_STARTED and Accept_Deny_Button_4.rating and ConfidenceSlider_4.rating and DenySlider_4.rating:
            # keep track of start time/frame for later
            Click_to_Continue_7.frameNStart = frameN  # exact frame index
            Click_to_Continue_7.tStart = t  # local t and not account for scr refresh
            Click_to_Continue_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Click_to_Continue_7, 'tStartRefresh')  # time at next scr refresh
            Click_to_Continue_7.setAutoDraw(True)
        
        # *AI_Response_Txt_4* updates
        if AI_Response_Txt_4.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            AI_Response_Txt_4.frameNStart = frameN  # exact frame index
            AI_Response_Txt_4.tStart = t  # local t and not account for scr refresh
            AI_Response_Txt_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AI_Response_Txt_4, 'tStartRefresh')  # time at next scr refresh
            AI_Response_Txt_4.setAutoDraw(True)
        
        # *Explanation_Image_4* updates
        if Explanation_Image_4.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            Explanation_Image_4.frameNStart = frameN  # exact frame index
            Explanation_Image_4.tStart = t  # local t and not account for scr refresh
            Explanation_Image_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Explanation_Image_4, 'tStartRefresh')  # time at next scr refresh
            Explanation_Image_4.setAutoDraw(True)
        if Explanation_Image_4.status == STARTED:  # only update if drawing
            Explanation_Image_4.setImage(ExplanationFile, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Image_BasedComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Image_Based"-------
    for thisComponent in Image_BasedComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Loop_3.addData('Image_Intro_Txt.started', Image_Intro_Txt.tStartRefresh)
    Loop_3.addData('Image_Intro_Txt.stopped', Image_Intro_Txt.tStopRefresh)
    Loop_3.addData('Question_Txt_4.started', Question_Txt_4.tStartRefresh)
    Loop_3.addData('Question_Txt_4.stopped', Question_Txt_4.tStopRefresh)
    Loop_3.addData('Accept_Deny_Button_4.response', Accept_Deny_Button_4.getRating())
    Loop_3.addData('Accept_Deny_Button_4.rt', Accept_Deny_Button_4.getRT())
    Loop_3.addData('Accept_Deny_Button_4.started', Accept_Deny_Button_4.tStartRefresh)
    Loop_3.addData('Accept_Deny_Button_4.stopped', Accept_Deny_Button_4.tStopRefresh)
    Loop_3.addData('ConfidenceSlider_4.response', ConfidenceSlider_4.getRating())
    Loop_3.addData('ConfidenceSlider_4.rt', ConfidenceSlider_4.getRT())
    Loop_3.addData('ConfidenceSlider_4.started', ConfidenceSlider_4.tStartRefresh)
    Loop_3.addData('ConfidenceSlider_4.stopped', ConfidenceSlider_4.tStopRefresh)
    Loop_3.addData('Experimental_Images_4.started', Experimental_Images_4.tStartRefresh)
    Loop_3.addData('Experimental_Images_4.stopped', Experimental_Images_4.tStopRefresh)
    Loop_3.addData('DenySlider_4.response', DenySlider_4.getRating())
    Loop_3.addData('DenySlider_4.rt', DenySlider_4.getRT())
    Loop_3.addData('DenySlider_4.started', DenySlider_4.tStartRefresh)
    Loop_3.addData('DenySlider_4.stopped', DenySlider_4.tStopRefresh)
    # store data for Loop_3 (TrialHandler)
    Loop_3.addData('mouse_7.x', mouse_7.x)
    Loop_3.addData('mouse_7.y', mouse_7.y)
    Loop_3.addData('mouse_7.leftButton', mouse_7.leftButton)
    Loop_3.addData('mouse_7.midButton', mouse_7.midButton)
    Loop_3.addData('mouse_7.rightButton', mouse_7.rightButton)
    Loop_3.addData('mouse_7.time', mouse_7.time)
    Loop_3.addData('mouse_7.clicked_name', mouse_7.clicked_name)
    Loop_3.addData('mouse_7.started', mouse_7.tStart)
    Loop_3.addData('mouse_7.stopped', mouse_7.tStop)
    Loop_3.addData('Click_to_Continue_7.started', Click_to_Continue_7.tStartRefresh)
    Loop_3.addData('Click_to_Continue_7.stopped', Click_to_Continue_7.tStopRefresh)
    outlet.push_sample(x=[3])
    
    from psychopy import core# this returns a time value in seconds, not a clock object:
    
    clock = core.getAbsTime()
    
    import time
    
    from datetime import datetime
    
    ETrial= datetime.fromtimestamp(clock).strftime("%A, %B %d, %Y %I:%M:%S")
    
    Loop_3.addData('trial_end', ETrial)
    # the Routine "Image_Based" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'Loop_3'

# get names of stimulus parameters
if Loop_3.trialList in ([], [None], None):
    params = []
else:
    params = Loop_3.trialList[0].keys()
# save data for this loop
Loop_3.saveAsExcel(filename + '.xlsx', sheetName='Loop_3',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
Loop_3.saveAsText(filename + 'Loop_3.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Image_Survey_Break"-------
continueRoutine = True
# update component parameters for each repeat
KeyResp_7.keys = []
KeyResp_7.rt = []
_KeyResp_7_allKeys = []
# keep track of which components have finished
Image_Survey_BreakComponents = [text_7, PresstoCont_7, KeyResp_7]
for thisComponent in Image_Survey_BreakComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Image_Survey_BreakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Image_Survey_Break"-------
while continueRoutine:
    # get current time
    t = Image_Survey_BreakClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Image_Survey_BreakClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    
    # *PresstoCont_7* updates
    if PresstoCont_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PresstoCont_7.frameNStart = frameN  # exact frame index
        PresstoCont_7.tStart = t  # local t and not account for scr refresh
        PresstoCont_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PresstoCont_7, 'tStartRefresh')  # time at next scr refresh
        PresstoCont_7.setAutoDraw(True)
    
    # *KeyResp_7* updates
    if KeyResp_7.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        KeyResp_7.frameNStart = frameN  # exact frame index
        KeyResp_7.tStart = t  # local t and not account for scr refresh
        KeyResp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(KeyResp_7, 'tStartRefresh')  # time at next scr refresh
        KeyResp_7.status = STARTED
        # keyboard checking is just starting
        KeyResp_7.clock.reset()  # now t=0
    if KeyResp_7.status == STARTED:
        theseKeys = KeyResp_7.getKeys(keyList=['space'], waitRelease=False)
        _KeyResp_7_allKeys.extend(theseKeys)
        if len(_KeyResp_7_allKeys):
            KeyResp_7.keys = _KeyResp_7_allKeys[-1].name  # just the last key pressed
            KeyResp_7.rt = _KeyResp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Image_Survey_BreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Image_Survey_Break"-------
for thisComponent in Image_Survey_BreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('PresstoCont_7.started', PresstoCont_7.tStartRefresh)
thisExp.addData('PresstoCont_7.stopped', PresstoCont_7.tStopRefresh)
# the Routine "Image_Survey_Break" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Survey_Trial"-------
continueRoutine = True
# update component parameters for each repeat
Q1_Slider.reset()
Q2_Slider.reset()
Q3_Slider.reset()
Q4_Slider.reset()
Q5_Slider.reset()
Q6_Slider.reset()
Q7_Slider.reset()
Q8_Slider.reset()
Q9_Slider.reset()
Q10_Slider.reset()
Q11_Slider.reset()
Q12_Slider.reset()
# setup some python lists for storing info about the mouse_2
mouse_2.clicked_name = []
gotValidClick = False  # until a click is received
Q13_Slider.reset()
Q14_Slider.reset()
Q15_Slider.reset()
Q16_Slider.reset()
Q17_Slider.reset()
Q18_Slider.reset()
Q19_Slider.reset()
Q20_Slider.reset()
Q21_Slider.reset()
Q22_Slider.reset()
Q23_Slider.reset()
# keep track of which components have finished
Survey_TrialComponents = [Q1, Q1_Slider, Q2, Q2_Slider, Q3, Q3_Slider, Q4, Q4_Slider, Q5, Q5_Slider, Q6, Q6_Slider, Q7, Q7_Slider, Q8, Q8_Slider, Q9, Q9_Slider, Q10, Q10_Slider, Q11, Q11_Slider, Q12, Q12_Slider, mouse_2, Click_to_Continue_2, Q13, Q13_Slider, Q14, Q14_Slider, Q15, Q15_Slider, Q16, Q16_Slider, Q17, Q17_Slider, Q18, Q18_Slider, Q19, Q19_Slider, Q20, Q20_Slider, Q21, Q21_Slider, Q22, Q22_Slider, Q23, Q23_Slider]
for thisComponent in Survey_TrialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Survey_TrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Survey_Trial"-------
while continueRoutine:
    # get current time
    t = Survey_TrialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Survey_TrialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Q1* updates
    if Q1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q1.frameNStart = frameN  # exact frame index
        Q1.tStart = t  # local t and not account for scr refresh
        Q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q1, 'tStartRefresh')  # time at next scr refresh
        Q1.setAutoDraw(True)
    if Q1.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q1.tStop = t  # not accounting for scr refresh
            Q1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q1, 'tStopRefresh')  # time at next scr refresh
            Q1.setAutoDraw(False)
    
    # *Q1_Slider* updates
    if Q1_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q1_Slider.frameNStart = frameN  # exact frame index
        Q1_Slider.tStart = t  # local t and not account for scr refresh
        Q1_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q1_Slider, 'tStartRefresh')  # time at next scr refresh
        Q1_Slider.setAutoDraw(True)
    if Q1_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q1_Slider.tStop = t  # not accounting for scr refresh
            Q1_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q1_Slider, 'tStopRefresh')  # time at next scr refresh
            Q1_Slider.setAutoDraw(False)
    
    # *Q2* updates
    if Q2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q2.frameNStart = frameN  # exact frame index
        Q2.tStart = t  # local t and not account for scr refresh
        Q2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q2, 'tStartRefresh')  # time at next scr refresh
        Q2.setAutoDraw(True)
    if Q2.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q2.tStop = t  # not accounting for scr refresh
            Q2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q2, 'tStopRefresh')  # time at next scr refresh
            Q2.setAutoDraw(False)
    
    # *Q2_Slider* updates
    if Q2_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q2_Slider.frameNStart = frameN  # exact frame index
        Q2_Slider.tStart = t  # local t and not account for scr refresh
        Q2_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q2_Slider, 'tStartRefresh')  # time at next scr refresh
        Q2_Slider.setAutoDraw(True)
    if Q2_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q2_Slider.tStop = t  # not accounting for scr refresh
            Q2_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q2_Slider, 'tStopRefresh')  # time at next scr refresh
            Q2_Slider.setAutoDraw(False)
    
    # *Q3* updates
    if Q3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q3.frameNStart = frameN  # exact frame index
        Q3.tStart = t  # local t and not account for scr refresh
        Q3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q3, 'tStartRefresh')  # time at next scr refresh
        Q3.setAutoDraw(True)
    if Q3.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q3.tStop = t  # not accounting for scr refresh
            Q3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q3, 'tStopRefresh')  # time at next scr refresh
            Q3.setAutoDraw(False)
    
    # *Q3_Slider* updates
    if Q3_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q3_Slider.frameNStart = frameN  # exact frame index
        Q3_Slider.tStart = t  # local t and not account for scr refresh
        Q3_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q3_Slider, 'tStartRefresh')  # time at next scr refresh
        Q3_Slider.setAutoDraw(True)
    if Q3_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q3_Slider.tStop = t  # not accounting for scr refresh
            Q3_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q3_Slider, 'tStopRefresh')  # time at next scr refresh
            Q3_Slider.setAutoDraw(False)
    
    # *Q4* updates
    if Q4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q4.frameNStart = frameN  # exact frame index
        Q4.tStart = t  # local t and not account for scr refresh
        Q4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q4, 'tStartRefresh')  # time at next scr refresh
        Q4.setAutoDraw(True)
    if Q4.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q4.tStop = t  # not accounting for scr refresh
            Q4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q4, 'tStopRefresh')  # time at next scr refresh
            Q4.setAutoDraw(False)
    
    # *Q4_Slider* updates
    if Q4_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q4_Slider.frameNStart = frameN  # exact frame index
        Q4_Slider.tStart = t  # local t and not account for scr refresh
        Q4_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q4_Slider, 'tStartRefresh')  # time at next scr refresh
        Q4_Slider.setAutoDraw(True)
    if Q4_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q4_Slider.tStop = t  # not accounting for scr refresh
            Q4_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q4_Slider, 'tStopRefresh')  # time at next scr refresh
            Q4_Slider.setAutoDraw(False)
    
    # *Q5* updates
    if Q5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q5.frameNStart = frameN  # exact frame index
        Q5.tStart = t  # local t and not account for scr refresh
        Q5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q5, 'tStartRefresh')  # time at next scr refresh
        Q5.setAutoDraw(True)
    if Q5.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q5.tStop = t  # not accounting for scr refresh
            Q5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q5, 'tStopRefresh')  # time at next scr refresh
            Q5.setAutoDraw(False)
    
    # *Q5_Slider* updates
    if Q5_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q5_Slider.frameNStart = frameN  # exact frame index
        Q5_Slider.tStart = t  # local t and not account for scr refresh
        Q5_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q5_Slider, 'tStartRefresh')  # time at next scr refresh
        Q5_Slider.setAutoDraw(True)
    if Q5_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q5_Slider.tStop = t  # not accounting for scr refresh
            Q5_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q5_Slider, 'tStopRefresh')  # time at next scr refresh
            Q5_Slider.setAutoDraw(False)
    
    # *Q6* updates
    if Q6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q6.frameNStart = frameN  # exact frame index
        Q6.tStart = t  # local t and not account for scr refresh
        Q6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q6, 'tStartRefresh')  # time at next scr refresh
        Q6.setAutoDraw(True)
    if Q6.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q6.tStop = t  # not accounting for scr refresh
            Q6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q6, 'tStopRefresh')  # time at next scr refresh
            Q6.setAutoDraw(False)
    
    # *Q6_Slider* updates
    if Q6_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q6_Slider.frameNStart = frameN  # exact frame index
        Q6_Slider.tStart = t  # local t and not account for scr refresh
        Q6_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q6_Slider, 'tStartRefresh')  # time at next scr refresh
        Q6_Slider.setAutoDraw(True)
    if Q6_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q6_Slider.tStop = t  # not accounting for scr refresh
            Q6_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q6_Slider, 'tStopRefresh')  # time at next scr refresh
            Q6_Slider.setAutoDraw(False)
    
    # *Q7* updates
    if Q7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q7.frameNStart = frameN  # exact frame index
        Q7.tStart = t  # local t and not account for scr refresh
        Q7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q7, 'tStartRefresh')  # time at next scr refresh
        Q7.setAutoDraw(True)
    if Q7.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q7.tStop = t  # not accounting for scr refresh
            Q7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q7, 'tStopRefresh')  # time at next scr refresh
            Q7.setAutoDraw(False)
    
    # *Q7_Slider* updates
    if Q7_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q7_Slider.frameNStart = frameN  # exact frame index
        Q7_Slider.tStart = t  # local t and not account for scr refresh
        Q7_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q7_Slider, 'tStartRefresh')  # time at next scr refresh
        Q7_Slider.setAutoDraw(True)
    if Q7_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q7_Slider.tStop = t  # not accounting for scr refresh
            Q7_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q7_Slider, 'tStopRefresh')  # time at next scr refresh
            Q7_Slider.setAutoDraw(False)
    
    # *Q8* updates
    if Q8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q8.frameNStart = frameN  # exact frame index
        Q8.tStart = t  # local t and not account for scr refresh
        Q8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q8, 'tStartRefresh')  # time at next scr refresh
        Q8.setAutoDraw(True)
    if Q8.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q8.tStop = t  # not accounting for scr refresh
            Q8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q8, 'tStopRefresh')  # time at next scr refresh
            Q8.setAutoDraw(False)
    
    # *Q8_Slider* updates
    if Q8_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q8_Slider.frameNStart = frameN  # exact frame index
        Q8_Slider.tStart = t  # local t and not account for scr refresh
        Q8_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q8_Slider, 'tStartRefresh')  # time at next scr refresh
        Q8_Slider.setAutoDraw(True)
    if Q8_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q8_Slider.tStop = t  # not accounting for scr refresh
            Q8_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q8_Slider, 'tStopRefresh')  # time at next scr refresh
            Q8_Slider.setAutoDraw(False)
    
    # *Q9* updates
    if Q9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q9.frameNStart = frameN  # exact frame index
        Q9.tStart = t  # local t and not account for scr refresh
        Q9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q9, 'tStartRefresh')  # time at next scr refresh
        Q9.setAutoDraw(True)
    if Q9.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q9.tStop = t  # not accounting for scr refresh
            Q9.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q9, 'tStopRefresh')  # time at next scr refresh
            Q9.setAutoDraw(False)
    
    # *Q9_Slider* updates
    if Q9_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q9_Slider.frameNStart = frameN  # exact frame index
        Q9_Slider.tStart = t  # local t and not account for scr refresh
        Q9_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q9_Slider, 'tStartRefresh')  # time at next scr refresh
        Q9_Slider.setAutoDraw(True)
    if Q9_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q9_Slider.tStop = t  # not accounting for scr refresh
            Q9_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q9_Slider, 'tStopRefresh')  # time at next scr refresh
            Q9_Slider.setAutoDraw(False)
    
    # *Q10* updates
    if Q10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q10.frameNStart = frameN  # exact frame index
        Q10.tStart = t  # local t and not account for scr refresh
        Q10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q10, 'tStartRefresh')  # time at next scr refresh
        Q10.setAutoDraw(True)
    if Q10.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q10.tStop = t  # not accounting for scr refresh
            Q10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q10, 'tStopRefresh')  # time at next scr refresh
            Q10.setAutoDraw(False)
    
    # *Q10_Slider* updates
    if Q10_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q10_Slider.frameNStart = frameN  # exact frame index
        Q10_Slider.tStart = t  # local t and not account for scr refresh
        Q10_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q10_Slider, 'tStartRefresh')  # time at next scr refresh
        Q10_Slider.setAutoDraw(True)
    if Q10_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q10_Slider.tStop = t  # not accounting for scr refresh
            Q10_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q10_Slider, 'tStopRefresh')  # time at next scr refresh
            Q10_Slider.setAutoDraw(False)
    
    # *Q11* updates
    if Q11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q11.frameNStart = frameN  # exact frame index
        Q11.tStart = t  # local t and not account for scr refresh
        Q11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q11, 'tStartRefresh')  # time at next scr refresh
        Q11.setAutoDraw(True)
    if Q11.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q11.tStop = t  # not accounting for scr refresh
            Q11.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q11, 'tStopRefresh')  # time at next scr refresh
            Q11.setAutoDraw(False)
    
    # *Q11_Slider* updates
    if Q11_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q11_Slider.frameNStart = frameN  # exact frame index
        Q11_Slider.tStart = t  # local t and not account for scr refresh
        Q11_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q11_Slider, 'tStartRefresh')  # time at next scr refresh
        Q11_Slider.setAutoDraw(True)
    if Q11_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q11_Slider.tStop = t  # not accounting for scr refresh
            Q11_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q11_Slider, 'tStopRefresh')  # time at next scr refresh
            Q11_Slider.setAutoDraw(False)
    
    # *Q12* updates
    if Q12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q12.frameNStart = frameN  # exact frame index
        Q12.tStart = t  # local t and not account for scr refresh
        Q12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q12, 'tStartRefresh')  # time at next scr refresh
        Q12.setAutoDraw(True)
    if Q12.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q12.tStop = t  # not accounting for scr refresh
            Q12.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q12, 'tStopRefresh')  # time at next scr refresh
            Q12.setAutoDraw(False)
    
    # *Q12_Slider* updates
    if Q12_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q12_Slider.frameNStart = frameN  # exact frame index
        Q12_Slider.tStart = t  # local t and not account for scr refresh
        Q12_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q12_Slider, 'tStartRefresh')  # time at next scr refresh
        Q12_Slider.setAutoDraw(True)
    if Q12_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q12_Slider.tStop = t  # not accounting for scr refresh
            Q12_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q12_Slider, 'tStopRefresh')  # time at next scr refresh
            Q12_Slider.setAutoDraw(False)
    # *mouse_2* updates
    if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_2.frameNStart = frameN  # exact frame index
        mouse_2.tStart = t  # local t and not account for scr refresh
        mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
        mouse_2.status = STARTED
        mouse_2.mouseClock.reset()
        prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
    if mouse_2.status == STARTED:  # only update if started and not finished!
        buttons = mouse_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(Click_to_Continue_2)
                    clickableList = Click_to_Continue_2
                except:
                    clickableList = [Click_to_Continue_2]
                for obj in clickableList:
                    if obj.contains(mouse_2):
                        gotValidClick = True
                        mouse_2.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # *Click_to_Continue_2* updates
    if Click_to_Continue_2.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating and Q13_Slider.rating and Q14_Slider.rating and Q15_Slider.rating and Q16_Slider.rating and Q17_Slider.rating and Q18_Slider.rating and Q19_Slider.rating and Q20_Slider.rating and Q21_Slider.rating and Q22_Slider.rating and Q23_Slider.rating:
        # keep track of start time/frame for later
        Click_to_Continue_2.frameNStart = frameN  # exact frame index
        Click_to_Continue_2.tStart = t  # local t and not account for scr refresh
        Click_to_Continue_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Click_to_Continue_2, 'tStartRefresh')  # time at next scr refresh
        Click_to_Continue_2.setAutoDraw(True)
    
    # *Q13* updates
    if Q13.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q13.frameNStart = frameN  # exact frame index
        Q13.tStart = t  # local t and not account for scr refresh
        Q13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q13, 'tStartRefresh')  # time at next scr refresh
        Q13.setAutoDraw(True)
    
    # *Q13_Slider* updates
    if Q13_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q13_Slider.frameNStart = frameN  # exact frame index
        Q13_Slider.tStart = t  # local t and not account for scr refresh
        Q13_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q13_Slider, 'tStartRefresh')  # time at next scr refresh
        Q13_Slider.setAutoDraw(True)
    
    # *Q14* updates
    if Q14.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q14.frameNStart = frameN  # exact frame index
        Q14.tStart = t  # local t and not account for scr refresh
        Q14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q14, 'tStartRefresh')  # time at next scr refresh
        Q14.setAutoDraw(True)
    
    # *Q14_Slider* updates
    if Q14_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q14_Slider.frameNStart = frameN  # exact frame index
        Q14_Slider.tStart = t  # local t and not account for scr refresh
        Q14_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q14_Slider, 'tStartRefresh')  # time at next scr refresh
        Q14_Slider.setAutoDraw(True)
    
    # *Q15* updates
    if Q15.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q15.frameNStart = frameN  # exact frame index
        Q15.tStart = t  # local t and not account for scr refresh
        Q15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q15, 'tStartRefresh')  # time at next scr refresh
        Q15.setAutoDraw(True)
    
    # *Q15_Slider* updates
    if Q15_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q15_Slider.frameNStart = frameN  # exact frame index
        Q15_Slider.tStart = t  # local t and not account for scr refresh
        Q15_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q15_Slider, 'tStartRefresh')  # time at next scr refresh
        Q15_Slider.setAutoDraw(True)
    
    # *Q16* updates
    if Q16.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q16.frameNStart = frameN  # exact frame index
        Q16.tStart = t  # local t and not account for scr refresh
        Q16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q16, 'tStartRefresh')  # time at next scr refresh
        Q16.setAutoDraw(True)
    
    # *Q16_Slider* updates
    if Q16_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q16_Slider.frameNStart = frameN  # exact frame index
        Q16_Slider.tStart = t  # local t and not account for scr refresh
        Q16_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q16_Slider, 'tStartRefresh')  # time at next scr refresh
        Q16_Slider.setAutoDraw(True)
    
    # *Q17* updates
    if Q17.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q17.frameNStart = frameN  # exact frame index
        Q17.tStart = t  # local t and not account for scr refresh
        Q17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q17, 'tStartRefresh')  # time at next scr refresh
        Q17.setAutoDraw(True)
    
    # *Q17_Slider* updates
    if Q17_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q17_Slider.frameNStart = frameN  # exact frame index
        Q17_Slider.tStart = t  # local t and not account for scr refresh
        Q17_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q17_Slider, 'tStartRefresh')  # time at next scr refresh
        Q17_Slider.setAutoDraw(True)
    
    # *Q18* updates
    if Q18.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q18.frameNStart = frameN  # exact frame index
        Q18.tStart = t  # local t and not account for scr refresh
        Q18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q18, 'tStartRefresh')  # time at next scr refresh
        Q18.setAutoDraw(True)
    
    # *Q18_Slider* updates
    if Q18_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q18_Slider.frameNStart = frameN  # exact frame index
        Q18_Slider.tStart = t  # local t and not account for scr refresh
        Q18_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q18_Slider, 'tStartRefresh')  # time at next scr refresh
        Q18_Slider.setAutoDraw(True)
    
    # *Q19* updates
    if Q19.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q19.frameNStart = frameN  # exact frame index
        Q19.tStart = t  # local t and not account for scr refresh
        Q19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q19, 'tStartRefresh')  # time at next scr refresh
        Q19.setAutoDraw(True)
    
    # *Q19_Slider* updates
    if Q19_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q19_Slider.frameNStart = frameN  # exact frame index
        Q19_Slider.tStart = t  # local t and not account for scr refresh
        Q19_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q19_Slider, 'tStartRefresh')  # time at next scr refresh
        Q19_Slider.setAutoDraw(True)
    
    # *Q20* updates
    if Q20.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q20.frameNStart = frameN  # exact frame index
        Q20.tStart = t  # local t and not account for scr refresh
        Q20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q20, 'tStartRefresh')  # time at next scr refresh
        Q20.setAutoDraw(True)
    
    # *Q20_Slider* updates
    if Q20_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q20_Slider.frameNStart = frameN  # exact frame index
        Q20_Slider.tStart = t  # local t and not account for scr refresh
        Q20_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q20_Slider, 'tStartRefresh')  # time at next scr refresh
        Q20_Slider.setAutoDraw(True)
    
    # *Q21* updates
    if Q21.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q21.frameNStart = frameN  # exact frame index
        Q21.tStart = t  # local t and not account for scr refresh
        Q21.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q21, 'tStartRefresh')  # time at next scr refresh
        Q21.setAutoDraw(True)
    
    # *Q21_Slider* updates
    if Q21_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q21_Slider.frameNStart = frameN  # exact frame index
        Q21_Slider.tStart = t  # local t and not account for scr refresh
        Q21_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q21_Slider, 'tStartRefresh')  # time at next scr refresh
        Q21_Slider.setAutoDraw(True)
    
    # *Q22* updates
    if Q22.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q22.frameNStart = frameN  # exact frame index
        Q22.tStart = t  # local t and not account for scr refresh
        Q22.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q22, 'tStartRefresh')  # time at next scr refresh
        Q22.setAutoDraw(True)
    
    # *Q22_Slider* updates
    if Q22_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q22_Slider.frameNStart = frameN  # exact frame index
        Q22_Slider.tStart = t  # local t and not account for scr refresh
        Q22_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q22_Slider, 'tStartRefresh')  # time at next scr refresh
        Q22_Slider.setAutoDraw(True)
    
    # *Q23* updates
    if Q23.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q23.frameNStart = frameN  # exact frame index
        Q23.tStart = t  # local t and not account for scr refresh
        Q23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q23, 'tStartRefresh')  # time at next scr refresh
        Q23.setAutoDraw(True)
    
    # *Q23_Slider* updates
    if Q23_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q23_Slider.frameNStart = frameN  # exact frame index
        Q23_Slider.tStart = t  # local t and not account for scr refresh
        Q23_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q23_Slider, 'tStartRefresh')  # time at next scr refresh
        Q23_Slider.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Survey_TrialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Survey_Trial"-------
for thisComponent in Survey_TrialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Q1_Slider.response', Q1_Slider.getRating())
thisExp.addData('Q2_Slider.response', Q2_Slider.getRating())
thisExp.addData('Q3_Slider.response', Q3_Slider.getRating())
thisExp.addData('Q4_Slider.response', Q4_Slider.getRating())
thisExp.addData('Q5_Slider.response', Q5_Slider.getRating())
thisExp.addData('Q6_Slider.response', Q6_Slider.getRating())
thisExp.addData('Q7_Slider.response', Q7_Slider.getRating())
thisExp.addData('Q8_Slider.response', Q8_Slider.getRating())
thisExp.addData('Q9_Slider.response', Q9_Slider.getRating())
thisExp.addData('Q10_Slider.response', Q10_Slider.getRating())
thisExp.addData('Q11_Slider.response', Q11_Slider.getRating())
thisExp.addData('Q12_Slider.response', Q12_Slider.getRating())
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
thisExp.addData('Q13_Slider.response', Q13_Slider.getRating())
thisExp.addData('Q14_Slider.response', Q14_Slider.getRating())
thisExp.addData('Q15_Slider.response', Q15_Slider.getRating())
thisExp.addData('Q16_Slider.response', Q16_Slider.getRating())
thisExp.addData('Q17_Slider.response', Q17_Slider.getRating())
thisExp.addData('Q18_Slider.response', Q18_Slider.getRating())
thisExp.addData('Q19_Slider.response', Q19_Slider.getRating())
thisExp.addData('Q20_Slider.response', Q20_Slider.getRating())
thisExp.addData('Q21_Slider.response', Q21_Slider.getRating())
thisExp.addData('Q22_Slider.response', Q22_Slider.getRating())
thisExp.addData('Q23_Slider.response', Q23_Slider.getRating())
# the Routine "Survey_Trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Feature_Break"-------
continueRoutine = True
# update component parameters for each repeat
KeyResp_6.keys = []
KeyResp_6.rt = []
_KeyResp_6_allKeys = []
# keep track of which components have finished
Feature_BreakComponents = [Feature_Break_Txt, PresstoCont_6, KeyResp_6]
for thisComponent in Feature_BreakComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Feature_BreakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Feature_Break"-------
while continueRoutine:
    # get current time
    t = Feature_BreakClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Feature_BreakClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Feature_Break_Txt* updates
    if Feature_Break_Txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Feature_Break_Txt.frameNStart = frameN  # exact frame index
        Feature_Break_Txt.tStart = t  # local t and not account for scr refresh
        Feature_Break_Txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Feature_Break_Txt, 'tStartRefresh')  # time at next scr refresh
        Feature_Break_Txt.setAutoDraw(True)
    
    # *PresstoCont_6* updates
    if PresstoCont_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PresstoCont_6.frameNStart = frameN  # exact frame index
        PresstoCont_6.tStart = t  # local t and not account for scr refresh
        PresstoCont_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PresstoCont_6, 'tStartRefresh')  # time at next scr refresh
        PresstoCont_6.setAutoDraw(True)
    
    # *KeyResp_6* updates
    if KeyResp_6.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        KeyResp_6.frameNStart = frameN  # exact frame index
        KeyResp_6.tStart = t  # local t and not account for scr refresh
        KeyResp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(KeyResp_6, 'tStartRefresh')  # time at next scr refresh
        KeyResp_6.status = STARTED
        # keyboard checking is just starting
        KeyResp_6.clock.reset()  # now t=0
    if KeyResp_6.status == STARTED:
        theseKeys = KeyResp_6.getKeys(keyList=['space'], waitRelease=False)
        _KeyResp_6_allKeys.extend(theseKeys)
        if len(_KeyResp_6_allKeys):
            KeyResp_6.keys = _KeyResp_6_allKeys[-1].name  # just the last key pressed
            KeyResp_6.rt = _KeyResp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Feature_BreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Feature_Break"-------
for thisComponent in Feature_BreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Feature_Break" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Loop_4 = data.TrialHandler(nReps=0.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condtionsFile/featurebasedconditionsFile.csv'),
    seed=None, name='Loop_4')
thisExp.addLoop(Loop_4)  # add the loop to the experiment
thisLoop_4 = Loop_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_4.rgb)
if thisLoop_4 != None:
    for paramName in thisLoop_4:
        exec('{} = thisLoop_4[paramName]'.format(paramName))

for thisLoop_4 in Loop_4:
    currentLoop = Loop_4
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_4.rgb)
    if thisLoop_4 != None:
        for paramName in thisLoop_4:
            exec('{} = thisLoop_4[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Feature_Based"-------
    continueRoutine = True
    # update component parameters for each repeat
    AI_Response_3.setText(AI_Resp)
    Question_Txt_3.setText(txtStim)
    Accept_Deny_Button_3.reset()
    ConfidenceSlider_3.reset()
    Experimental_Images_3.setImage(stimFile)
    DenySlider_3.reset()
    # setup some python lists for storing info about the mouse_6
    mouse_6.x = []
    mouse_6.y = []
    mouse_6.leftButton = []
    mouse_6.midButton = []
    mouse_6.rightButton = []
    mouse_6.time = []
    mouse_6.clicked_name = []
    gotValidClick = False  # until a click is received
    AI_Response_Txt_3.setText('AI Response:')
    outlet.push_sample(x=[4])
    
    from psychopy import core# this returns a time value in seconds, not a clock object:
    
    clock = core.getAbsTime()
    
    import time
    
    from datetime import datetime
    
    ETrial= datetime.fromtimestamp(clock).strftime("%A, %B %d, %Y %I:%M:%S")
    
    Loop_4.addData('trial_start', ETrial)
    # keep track of which components have finished
    Feature_BasedComponents = [Feature_Intro_Txt, AI_Response_3, Question_Txt_3, Accept_Deny_Button_3, ConfidenceText_3, ConfidenceSlider_3, Experimental_Images_3, IfDenied_3, DenySlider_3, mouse_6, Click_to_Continue_6, AI_Response_Txt_3, Explanation_Image_3]
    for thisComponent in Feature_BasedComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Feature_BasedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Feature_Based"-------
    while continueRoutine:
        # get current time
        t = Feature_BasedClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Feature_BasedClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Feature_Intro_Txt* updates
        if Feature_Intro_Txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Feature_Intro_Txt.frameNStart = frameN  # exact frame index
            Feature_Intro_Txt.tStart = t  # local t and not account for scr refresh
            Feature_Intro_Txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Feature_Intro_Txt, 'tStartRefresh')  # time at next scr refresh
            Feature_Intro_Txt.setAutoDraw(True)
        if Feature_Intro_Txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Feature_Intro_Txt.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                Feature_Intro_Txt.tStop = t  # not accounting for scr refresh
                Feature_Intro_Txt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Feature_Intro_Txt, 'tStopRefresh')  # time at next scr refresh
                Feature_Intro_Txt.setAutoDraw(False)
        
        # *AI_Response_3* updates
        if AI_Response_3.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            AI_Response_3.frameNStart = frameN  # exact frame index
            AI_Response_3.tStart = t  # local t and not account for scr refresh
            AI_Response_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AI_Response_3, 'tStartRefresh')  # time at next scr refresh
            AI_Response_3.setAutoDraw(True)
        
        # *Question_Txt_3* updates
        if Question_Txt_3.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            Question_Txt_3.frameNStart = frameN  # exact frame index
            Question_Txt_3.tStart = t  # local t and not account for scr refresh
            Question_Txt_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Question_Txt_3, 'tStartRefresh')  # time at next scr refresh
            Question_Txt_3.setAutoDraw(True)
        
        # *Accept_Deny_Button_3* updates
        if Accept_Deny_Button_3.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            Accept_Deny_Button_3.frameNStart = frameN  # exact frame index
            Accept_Deny_Button_3.tStart = t  # local t and not account for scr refresh
            Accept_Deny_Button_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Accept_Deny_Button_3, 'tStartRefresh')  # time at next scr refresh
            Accept_Deny_Button_3.setAutoDraw(True)
        
        # *ConfidenceText_3* updates
        if ConfidenceText_3.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            ConfidenceText_3.frameNStart = frameN  # exact frame index
            ConfidenceText_3.tStart = t  # local t and not account for scr refresh
            ConfidenceText_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ConfidenceText_3, 'tStartRefresh')  # time at next scr refresh
            ConfidenceText_3.setAutoDraw(True)
        
        # *ConfidenceSlider_3* updates
        if ConfidenceSlider_3.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            ConfidenceSlider_3.frameNStart = frameN  # exact frame index
            ConfidenceSlider_3.tStart = t  # local t and not account for scr refresh
            ConfidenceSlider_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ConfidenceSlider_3, 'tStartRefresh')  # time at next scr refresh
            ConfidenceSlider_3.setAutoDraw(True)
        
        # *Experimental_Images_3* updates
        if Experimental_Images_3.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            Experimental_Images_3.frameNStart = frameN  # exact frame index
            Experimental_Images_3.tStart = t  # local t and not account for scr refresh
            Experimental_Images_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Experimental_Images_3, 'tStartRefresh')  # time at next scr refresh
            Experimental_Images_3.setAutoDraw(True)
        
        # *IfDenied_3* updates
        if IfDenied_3.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            IfDenied_3.frameNStart = frameN  # exact frame index
            IfDenied_3.tStart = t  # local t and not account for scr refresh
            IfDenied_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IfDenied_3, 'tStartRefresh')  # time at next scr refresh
            IfDenied_3.setAutoDraw(True)
        
        # *DenySlider_3* updates
        if DenySlider_3.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            DenySlider_3.frameNStart = frameN  # exact frame index
            DenySlider_3.tStart = t  # local t and not account for scr refresh
            DenySlider_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DenySlider_3, 'tStartRefresh')  # time at next scr refresh
            DenySlider_3.setAutoDraw(True)
        # *mouse_6* updates
        if mouse_6.status == NOT_STARTED and t >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_6.frameNStart = frameN  # exact frame index
            mouse_6.tStart = t  # local t and not account for scr refresh
            mouse_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_6, 'tStartRefresh')  # time at next scr refresh
            mouse_6.status = STARTED
            mouse_6.mouseClock.reset()
            prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
        if mouse_6.status == STARTED:  # only update if started and not finished!
            buttons = mouse_6.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(Click_to_Continue_6)
                        clickableList = Click_to_Continue_6
                    except:
                        clickableList = [Click_to_Continue_6]
                    for obj in clickableList:
                        if obj.contains(mouse_6):
                            gotValidClick = True
                            mouse_6.clicked_name.append(obj.name)
                    x, y = mouse_6.getPos()
                    mouse_6.x.append(x)
                    mouse_6.y.append(y)
                    buttons = mouse_6.getPressed()
                    mouse_6.leftButton.append(buttons[0])
                    mouse_6.midButton.append(buttons[1])
                    mouse_6.rightButton.append(buttons[2])
                    mouse_6.time.append(mouse_6.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # abort routine on response
        
        # *Click_to_Continue_6* updates
        if Click_to_Continue_6.status == NOT_STARTED and Accept_Deny_Button_3.rating and ConfidenceSlider_3.rating and DenySlider_3.rating:
            # keep track of start time/frame for later
            Click_to_Continue_6.frameNStart = frameN  # exact frame index
            Click_to_Continue_6.tStart = t  # local t and not account for scr refresh
            Click_to_Continue_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Click_to_Continue_6, 'tStartRefresh')  # time at next scr refresh
            Click_to_Continue_6.setAutoDraw(True)
        
        # *AI_Response_Txt_3* updates
        if AI_Response_Txt_3.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            AI_Response_Txt_3.frameNStart = frameN  # exact frame index
            AI_Response_Txt_3.tStart = t  # local t and not account for scr refresh
            AI_Response_Txt_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AI_Response_Txt_3, 'tStartRefresh')  # time at next scr refresh
            AI_Response_Txt_3.setAutoDraw(True)
        
        # *Explanation_Image_3* updates
        if Explanation_Image_3.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            Explanation_Image_3.frameNStart = frameN  # exact frame index
            Explanation_Image_3.tStart = t  # local t and not account for scr refresh
            Explanation_Image_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Explanation_Image_3, 'tStartRefresh')  # time at next scr refresh
            Explanation_Image_3.setAutoDraw(True)
        if Explanation_Image_3.status == STARTED:  # only update if drawing
            Explanation_Image_3.setImage(ExplanationFile, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Feature_BasedComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feature_Based"-------
    for thisComponent in Feature_BasedComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Loop_4.addData('Feature_Intro_Txt.started', Feature_Intro_Txt.tStartRefresh)
    Loop_4.addData('Feature_Intro_Txt.stopped', Feature_Intro_Txt.tStopRefresh)
    Loop_4.addData('Question_Txt_3.started', Question_Txt_3.tStartRefresh)
    Loop_4.addData('Question_Txt_3.stopped', Question_Txt_3.tStopRefresh)
    Loop_4.addData('Accept_Deny_Button_3.response', Accept_Deny_Button_3.getRating())
    Loop_4.addData('Accept_Deny_Button_3.rt', Accept_Deny_Button_3.getRT())
    Loop_4.addData('Accept_Deny_Button_3.started', Accept_Deny_Button_3.tStartRefresh)
    Loop_4.addData('Accept_Deny_Button_3.stopped', Accept_Deny_Button_3.tStopRefresh)
    Loop_4.addData('ConfidenceSlider_3.response', ConfidenceSlider_3.getRating())
    Loop_4.addData('ConfidenceSlider_3.rt', ConfidenceSlider_3.getRT())
    Loop_4.addData('ConfidenceSlider_3.started', ConfidenceSlider_3.tStartRefresh)
    Loop_4.addData('ConfidenceSlider_3.stopped', ConfidenceSlider_3.tStopRefresh)
    Loop_4.addData('Experimental_Images_3.started', Experimental_Images_3.tStartRefresh)
    Loop_4.addData('Experimental_Images_3.stopped', Experimental_Images_3.tStopRefresh)
    Loop_4.addData('DenySlider_3.response', DenySlider_3.getRating())
    Loop_4.addData('DenySlider_3.rt', DenySlider_3.getRT())
    Loop_4.addData('DenySlider_3.started', DenySlider_3.tStartRefresh)
    Loop_4.addData('DenySlider_3.stopped', DenySlider_3.tStopRefresh)
    # store data for Loop_4 (TrialHandler)
    Loop_4.addData('mouse_6.x', mouse_6.x)
    Loop_4.addData('mouse_6.y', mouse_6.y)
    Loop_4.addData('mouse_6.leftButton', mouse_6.leftButton)
    Loop_4.addData('mouse_6.midButton', mouse_6.midButton)
    Loop_4.addData('mouse_6.rightButton', mouse_6.rightButton)
    Loop_4.addData('mouse_6.time', mouse_6.time)
    Loop_4.addData('mouse_6.clicked_name', mouse_6.clicked_name)
    Loop_4.addData('mouse_6.started', mouse_6.tStart)
    Loop_4.addData('mouse_6.stopped', mouse_6.tStop)
    Loop_4.addData('Click_to_Continue_6.started', Click_to_Continue_6.tStartRefresh)
    Loop_4.addData('Click_to_Continue_6.stopped', Click_to_Continue_6.tStopRefresh)
    outlet.push_sample(x=[4])
    
    from psychopy import core# this returns a time value in seconds, not a clock object:
    
    clock = core.getAbsTime()
    
    import time
    
    from datetime import datetime
    
    ETrial= datetime.fromtimestamp(clock).strftime("%A, %B %d, %Y %I:%M:%S")
    
    Loop_4.addData('trial_end', ETrial)
    # the Routine "Feature_Based" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'Loop_4'

# get names of stimulus parameters
if Loop_4.trialList in ([], [None], None):
    params = []
else:
    params = Loop_4.trialList[0].keys()
# save data for this loop
Loop_4.saveAsExcel(filename + '.xlsx', sheetName='Loop_4',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
Loop_4.saveAsText(filename + 'Loop_4.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Feature_Survey_Break"-------
continueRoutine = True
# update component parameters for each repeat
KeyResp_8.keys = []
KeyResp_8.rt = []
_KeyResp_8_allKeys = []
# keep track of which components have finished
Feature_Survey_BreakComponents = [text_8, PresstoCont_8, KeyResp_8]
for thisComponent in Feature_Survey_BreakComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Feature_Survey_BreakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Feature_Survey_Break"-------
while continueRoutine:
    # get current time
    t = Feature_Survey_BreakClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Feature_Survey_BreakClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_8* updates
    if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_8.frameNStart = frameN  # exact frame index
        text_8.tStart = t  # local t and not account for scr refresh
        text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        text_8.setAutoDraw(True)
    
    # *PresstoCont_8* updates
    if PresstoCont_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PresstoCont_8.frameNStart = frameN  # exact frame index
        PresstoCont_8.tStart = t  # local t and not account for scr refresh
        PresstoCont_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PresstoCont_8, 'tStartRefresh')  # time at next scr refresh
        PresstoCont_8.setAutoDraw(True)
    
    # *KeyResp_8* updates
    if KeyResp_8.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        KeyResp_8.frameNStart = frameN  # exact frame index
        KeyResp_8.tStart = t  # local t and not account for scr refresh
        KeyResp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(KeyResp_8, 'tStartRefresh')  # time at next scr refresh
        KeyResp_8.status = STARTED
        # keyboard checking is just starting
        KeyResp_8.clock.reset()  # now t=0
    if KeyResp_8.status == STARTED:
        theseKeys = KeyResp_8.getKeys(keyList=['space'], waitRelease=False)
        _KeyResp_8_allKeys.extend(theseKeys)
        if len(_KeyResp_8_allKeys):
            KeyResp_8.keys = _KeyResp_8_allKeys[-1].name  # just the last key pressed
            KeyResp_8.rt = _KeyResp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Feature_Survey_BreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Feature_Survey_Break"-------
for thisComponent in Feature_Survey_BreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('PresstoCont_8.started', PresstoCont_8.tStartRefresh)
thisExp.addData('PresstoCont_8.stopped', PresstoCont_8.tStopRefresh)
# the Routine "Feature_Survey_Break" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Survey_Trial"-------
continueRoutine = True
# update component parameters for each repeat
Q1_Slider.reset()
Q2_Slider.reset()
Q3_Slider.reset()
Q4_Slider.reset()
Q5_Slider.reset()
Q6_Slider.reset()
Q7_Slider.reset()
Q8_Slider.reset()
Q9_Slider.reset()
Q10_Slider.reset()
Q11_Slider.reset()
Q12_Slider.reset()
# setup some python lists for storing info about the mouse_2
mouse_2.clicked_name = []
gotValidClick = False  # until a click is received
Q13_Slider.reset()
Q14_Slider.reset()
Q15_Slider.reset()
Q16_Slider.reset()
Q17_Slider.reset()
Q18_Slider.reset()
Q19_Slider.reset()
Q20_Slider.reset()
Q21_Slider.reset()
Q22_Slider.reset()
Q23_Slider.reset()
# keep track of which components have finished
Survey_TrialComponents = [Q1, Q1_Slider, Q2, Q2_Slider, Q3, Q3_Slider, Q4, Q4_Slider, Q5, Q5_Slider, Q6, Q6_Slider, Q7, Q7_Slider, Q8, Q8_Slider, Q9, Q9_Slider, Q10, Q10_Slider, Q11, Q11_Slider, Q12, Q12_Slider, mouse_2, Click_to_Continue_2, Q13, Q13_Slider, Q14, Q14_Slider, Q15, Q15_Slider, Q16, Q16_Slider, Q17, Q17_Slider, Q18, Q18_Slider, Q19, Q19_Slider, Q20, Q20_Slider, Q21, Q21_Slider, Q22, Q22_Slider, Q23, Q23_Slider]
for thisComponent in Survey_TrialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Survey_TrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Survey_Trial"-------
while continueRoutine:
    # get current time
    t = Survey_TrialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Survey_TrialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Q1* updates
    if Q1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q1.frameNStart = frameN  # exact frame index
        Q1.tStart = t  # local t and not account for scr refresh
        Q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q1, 'tStartRefresh')  # time at next scr refresh
        Q1.setAutoDraw(True)
    if Q1.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q1.tStop = t  # not accounting for scr refresh
            Q1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q1, 'tStopRefresh')  # time at next scr refresh
            Q1.setAutoDraw(False)
    
    # *Q1_Slider* updates
    if Q1_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q1_Slider.frameNStart = frameN  # exact frame index
        Q1_Slider.tStart = t  # local t and not account for scr refresh
        Q1_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q1_Slider, 'tStartRefresh')  # time at next scr refresh
        Q1_Slider.setAutoDraw(True)
    if Q1_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q1_Slider.tStop = t  # not accounting for scr refresh
            Q1_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q1_Slider, 'tStopRefresh')  # time at next scr refresh
            Q1_Slider.setAutoDraw(False)
    
    # *Q2* updates
    if Q2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q2.frameNStart = frameN  # exact frame index
        Q2.tStart = t  # local t and not account for scr refresh
        Q2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q2, 'tStartRefresh')  # time at next scr refresh
        Q2.setAutoDraw(True)
    if Q2.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q2.tStop = t  # not accounting for scr refresh
            Q2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q2, 'tStopRefresh')  # time at next scr refresh
            Q2.setAutoDraw(False)
    
    # *Q2_Slider* updates
    if Q2_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q2_Slider.frameNStart = frameN  # exact frame index
        Q2_Slider.tStart = t  # local t and not account for scr refresh
        Q2_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q2_Slider, 'tStartRefresh')  # time at next scr refresh
        Q2_Slider.setAutoDraw(True)
    if Q2_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q2_Slider.tStop = t  # not accounting for scr refresh
            Q2_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q2_Slider, 'tStopRefresh')  # time at next scr refresh
            Q2_Slider.setAutoDraw(False)
    
    # *Q3* updates
    if Q3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q3.frameNStart = frameN  # exact frame index
        Q3.tStart = t  # local t and not account for scr refresh
        Q3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q3, 'tStartRefresh')  # time at next scr refresh
        Q3.setAutoDraw(True)
    if Q3.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q3.tStop = t  # not accounting for scr refresh
            Q3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q3, 'tStopRefresh')  # time at next scr refresh
            Q3.setAutoDraw(False)
    
    # *Q3_Slider* updates
    if Q3_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q3_Slider.frameNStart = frameN  # exact frame index
        Q3_Slider.tStart = t  # local t and not account for scr refresh
        Q3_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q3_Slider, 'tStartRefresh')  # time at next scr refresh
        Q3_Slider.setAutoDraw(True)
    if Q3_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q3_Slider.tStop = t  # not accounting for scr refresh
            Q3_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q3_Slider, 'tStopRefresh')  # time at next scr refresh
            Q3_Slider.setAutoDraw(False)
    
    # *Q4* updates
    if Q4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q4.frameNStart = frameN  # exact frame index
        Q4.tStart = t  # local t and not account for scr refresh
        Q4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q4, 'tStartRefresh')  # time at next scr refresh
        Q4.setAutoDraw(True)
    if Q4.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q4.tStop = t  # not accounting for scr refresh
            Q4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q4, 'tStopRefresh')  # time at next scr refresh
            Q4.setAutoDraw(False)
    
    # *Q4_Slider* updates
    if Q4_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q4_Slider.frameNStart = frameN  # exact frame index
        Q4_Slider.tStart = t  # local t and not account for scr refresh
        Q4_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q4_Slider, 'tStartRefresh')  # time at next scr refresh
        Q4_Slider.setAutoDraw(True)
    if Q4_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q4_Slider.tStop = t  # not accounting for scr refresh
            Q4_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q4_Slider, 'tStopRefresh')  # time at next scr refresh
            Q4_Slider.setAutoDraw(False)
    
    # *Q5* updates
    if Q5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q5.frameNStart = frameN  # exact frame index
        Q5.tStart = t  # local t and not account for scr refresh
        Q5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q5, 'tStartRefresh')  # time at next scr refresh
        Q5.setAutoDraw(True)
    if Q5.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q5.tStop = t  # not accounting for scr refresh
            Q5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q5, 'tStopRefresh')  # time at next scr refresh
            Q5.setAutoDraw(False)
    
    # *Q5_Slider* updates
    if Q5_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q5_Slider.frameNStart = frameN  # exact frame index
        Q5_Slider.tStart = t  # local t and not account for scr refresh
        Q5_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q5_Slider, 'tStartRefresh')  # time at next scr refresh
        Q5_Slider.setAutoDraw(True)
    if Q5_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q5_Slider.tStop = t  # not accounting for scr refresh
            Q5_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q5_Slider, 'tStopRefresh')  # time at next scr refresh
            Q5_Slider.setAutoDraw(False)
    
    # *Q6* updates
    if Q6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q6.frameNStart = frameN  # exact frame index
        Q6.tStart = t  # local t and not account for scr refresh
        Q6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q6, 'tStartRefresh')  # time at next scr refresh
        Q6.setAutoDraw(True)
    if Q6.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q6.tStop = t  # not accounting for scr refresh
            Q6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q6, 'tStopRefresh')  # time at next scr refresh
            Q6.setAutoDraw(False)
    
    # *Q6_Slider* updates
    if Q6_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q6_Slider.frameNStart = frameN  # exact frame index
        Q6_Slider.tStart = t  # local t and not account for scr refresh
        Q6_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q6_Slider, 'tStartRefresh')  # time at next scr refresh
        Q6_Slider.setAutoDraw(True)
    if Q6_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q6_Slider.tStop = t  # not accounting for scr refresh
            Q6_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q6_Slider, 'tStopRefresh')  # time at next scr refresh
            Q6_Slider.setAutoDraw(False)
    
    # *Q7* updates
    if Q7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q7.frameNStart = frameN  # exact frame index
        Q7.tStart = t  # local t and not account for scr refresh
        Q7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q7, 'tStartRefresh')  # time at next scr refresh
        Q7.setAutoDraw(True)
    if Q7.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q7.tStop = t  # not accounting for scr refresh
            Q7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q7, 'tStopRefresh')  # time at next scr refresh
            Q7.setAutoDraw(False)
    
    # *Q7_Slider* updates
    if Q7_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q7_Slider.frameNStart = frameN  # exact frame index
        Q7_Slider.tStart = t  # local t and not account for scr refresh
        Q7_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q7_Slider, 'tStartRefresh')  # time at next scr refresh
        Q7_Slider.setAutoDraw(True)
    if Q7_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q7_Slider.tStop = t  # not accounting for scr refresh
            Q7_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q7_Slider, 'tStopRefresh')  # time at next scr refresh
            Q7_Slider.setAutoDraw(False)
    
    # *Q8* updates
    if Q8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q8.frameNStart = frameN  # exact frame index
        Q8.tStart = t  # local t and not account for scr refresh
        Q8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q8, 'tStartRefresh')  # time at next scr refresh
        Q8.setAutoDraw(True)
    if Q8.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q8.tStop = t  # not accounting for scr refresh
            Q8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q8, 'tStopRefresh')  # time at next scr refresh
            Q8.setAutoDraw(False)
    
    # *Q8_Slider* updates
    if Q8_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q8_Slider.frameNStart = frameN  # exact frame index
        Q8_Slider.tStart = t  # local t and not account for scr refresh
        Q8_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q8_Slider, 'tStartRefresh')  # time at next scr refresh
        Q8_Slider.setAutoDraw(True)
    if Q8_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q8_Slider.tStop = t  # not accounting for scr refresh
            Q8_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q8_Slider, 'tStopRefresh')  # time at next scr refresh
            Q8_Slider.setAutoDraw(False)
    
    # *Q9* updates
    if Q9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q9.frameNStart = frameN  # exact frame index
        Q9.tStart = t  # local t and not account for scr refresh
        Q9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q9, 'tStartRefresh')  # time at next scr refresh
        Q9.setAutoDraw(True)
    if Q9.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q9.tStop = t  # not accounting for scr refresh
            Q9.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q9, 'tStopRefresh')  # time at next scr refresh
            Q9.setAutoDraw(False)
    
    # *Q9_Slider* updates
    if Q9_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q9_Slider.frameNStart = frameN  # exact frame index
        Q9_Slider.tStart = t  # local t and not account for scr refresh
        Q9_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q9_Slider, 'tStartRefresh')  # time at next scr refresh
        Q9_Slider.setAutoDraw(True)
    if Q9_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q9_Slider.tStop = t  # not accounting for scr refresh
            Q9_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q9_Slider, 'tStopRefresh')  # time at next scr refresh
            Q9_Slider.setAutoDraw(False)
    
    # *Q10* updates
    if Q10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q10.frameNStart = frameN  # exact frame index
        Q10.tStart = t  # local t and not account for scr refresh
        Q10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q10, 'tStartRefresh')  # time at next scr refresh
        Q10.setAutoDraw(True)
    if Q10.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q10.tStop = t  # not accounting for scr refresh
            Q10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q10, 'tStopRefresh')  # time at next scr refresh
            Q10.setAutoDraw(False)
    
    # *Q10_Slider* updates
    if Q10_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q10_Slider.frameNStart = frameN  # exact frame index
        Q10_Slider.tStart = t  # local t and not account for scr refresh
        Q10_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q10_Slider, 'tStartRefresh')  # time at next scr refresh
        Q10_Slider.setAutoDraw(True)
    if Q10_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q10_Slider.tStop = t  # not accounting for scr refresh
            Q10_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q10_Slider, 'tStopRefresh')  # time at next scr refresh
            Q10_Slider.setAutoDraw(False)
    
    # *Q11* updates
    if Q11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q11.frameNStart = frameN  # exact frame index
        Q11.tStart = t  # local t and not account for scr refresh
        Q11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q11, 'tStartRefresh')  # time at next scr refresh
        Q11.setAutoDraw(True)
    if Q11.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q11.tStop = t  # not accounting for scr refresh
            Q11.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q11, 'tStopRefresh')  # time at next scr refresh
            Q11.setAutoDraw(False)
    
    # *Q11_Slider* updates
    if Q11_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q11_Slider.frameNStart = frameN  # exact frame index
        Q11_Slider.tStart = t  # local t and not account for scr refresh
        Q11_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q11_Slider, 'tStartRefresh')  # time at next scr refresh
        Q11_Slider.setAutoDraw(True)
    if Q11_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q11_Slider.tStop = t  # not accounting for scr refresh
            Q11_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q11_Slider, 'tStopRefresh')  # time at next scr refresh
            Q11_Slider.setAutoDraw(False)
    
    # *Q12* updates
    if Q12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q12.frameNStart = frameN  # exact frame index
        Q12.tStart = t  # local t and not account for scr refresh
        Q12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q12, 'tStartRefresh')  # time at next scr refresh
        Q12.setAutoDraw(True)
    if Q12.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q12.tStop = t  # not accounting for scr refresh
            Q12.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q12, 'tStopRefresh')  # time at next scr refresh
            Q12.setAutoDraw(False)
    
    # *Q12_Slider* updates
    if Q12_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q12_Slider.frameNStart = frameN  # exact frame index
        Q12_Slider.tStart = t  # local t and not account for scr refresh
        Q12_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q12_Slider, 'tStartRefresh')  # time at next scr refresh
        Q12_Slider.setAutoDraw(True)
    if Q12_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q12_Slider.tStop = t  # not accounting for scr refresh
            Q12_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q12_Slider, 'tStopRefresh')  # time at next scr refresh
            Q12_Slider.setAutoDraw(False)
    # *mouse_2* updates
    if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_2.frameNStart = frameN  # exact frame index
        mouse_2.tStart = t  # local t and not account for scr refresh
        mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
        mouse_2.status = STARTED
        mouse_2.mouseClock.reset()
        prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
    if mouse_2.status == STARTED:  # only update if started and not finished!
        buttons = mouse_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(Click_to_Continue_2)
                    clickableList = Click_to_Continue_2
                except:
                    clickableList = [Click_to_Continue_2]
                for obj in clickableList:
                    if obj.contains(mouse_2):
                        gotValidClick = True
                        mouse_2.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # *Click_to_Continue_2* updates
    if Click_to_Continue_2.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating and Q13_Slider.rating and Q14_Slider.rating and Q15_Slider.rating and Q16_Slider.rating and Q17_Slider.rating and Q18_Slider.rating and Q19_Slider.rating and Q20_Slider.rating and Q21_Slider.rating and Q22_Slider.rating and Q23_Slider.rating:
        # keep track of start time/frame for later
        Click_to_Continue_2.frameNStart = frameN  # exact frame index
        Click_to_Continue_2.tStart = t  # local t and not account for scr refresh
        Click_to_Continue_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Click_to_Continue_2, 'tStartRefresh')  # time at next scr refresh
        Click_to_Continue_2.setAutoDraw(True)
    
    # *Q13* updates
    if Q13.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q13.frameNStart = frameN  # exact frame index
        Q13.tStart = t  # local t and not account for scr refresh
        Q13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q13, 'tStartRefresh')  # time at next scr refresh
        Q13.setAutoDraw(True)
    
    # *Q13_Slider* updates
    if Q13_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q13_Slider.frameNStart = frameN  # exact frame index
        Q13_Slider.tStart = t  # local t and not account for scr refresh
        Q13_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q13_Slider, 'tStartRefresh')  # time at next scr refresh
        Q13_Slider.setAutoDraw(True)
    
    # *Q14* updates
    if Q14.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q14.frameNStart = frameN  # exact frame index
        Q14.tStart = t  # local t and not account for scr refresh
        Q14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q14, 'tStartRefresh')  # time at next scr refresh
        Q14.setAutoDraw(True)
    
    # *Q14_Slider* updates
    if Q14_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q14_Slider.frameNStart = frameN  # exact frame index
        Q14_Slider.tStart = t  # local t and not account for scr refresh
        Q14_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q14_Slider, 'tStartRefresh')  # time at next scr refresh
        Q14_Slider.setAutoDraw(True)
    
    # *Q15* updates
    if Q15.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q15.frameNStart = frameN  # exact frame index
        Q15.tStart = t  # local t and not account for scr refresh
        Q15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q15, 'tStartRefresh')  # time at next scr refresh
        Q15.setAutoDraw(True)
    
    # *Q15_Slider* updates
    if Q15_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q15_Slider.frameNStart = frameN  # exact frame index
        Q15_Slider.tStart = t  # local t and not account for scr refresh
        Q15_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q15_Slider, 'tStartRefresh')  # time at next scr refresh
        Q15_Slider.setAutoDraw(True)
    
    # *Q16* updates
    if Q16.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q16.frameNStart = frameN  # exact frame index
        Q16.tStart = t  # local t and not account for scr refresh
        Q16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q16, 'tStartRefresh')  # time at next scr refresh
        Q16.setAutoDraw(True)
    
    # *Q16_Slider* updates
    if Q16_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q16_Slider.frameNStart = frameN  # exact frame index
        Q16_Slider.tStart = t  # local t and not account for scr refresh
        Q16_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q16_Slider, 'tStartRefresh')  # time at next scr refresh
        Q16_Slider.setAutoDraw(True)
    
    # *Q17* updates
    if Q17.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q17.frameNStart = frameN  # exact frame index
        Q17.tStart = t  # local t and not account for scr refresh
        Q17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q17, 'tStartRefresh')  # time at next scr refresh
        Q17.setAutoDraw(True)
    
    # *Q17_Slider* updates
    if Q17_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q17_Slider.frameNStart = frameN  # exact frame index
        Q17_Slider.tStart = t  # local t and not account for scr refresh
        Q17_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q17_Slider, 'tStartRefresh')  # time at next scr refresh
        Q17_Slider.setAutoDraw(True)
    
    # *Q18* updates
    if Q18.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q18.frameNStart = frameN  # exact frame index
        Q18.tStart = t  # local t and not account for scr refresh
        Q18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q18, 'tStartRefresh')  # time at next scr refresh
        Q18.setAutoDraw(True)
    
    # *Q18_Slider* updates
    if Q18_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q18_Slider.frameNStart = frameN  # exact frame index
        Q18_Slider.tStart = t  # local t and not account for scr refresh
        Q18_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q18_Slider, 'tStartRefresh')  # time at next scr refresh
        Q18_Slider.setAutoDraw(True)
    
    # *Q19* updates
    if Q19.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q19.frameNStart = frameN  # exact frame index
        Q19.tStart = t  # local t and not account for scr refresh
        Q19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q19, 'tStartRefresh')  # time at next scr refresh
        Q19.setAutoDraw(True)
    
    # *Q19_Slider* updates
    if Q19_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q19_Slider.frameNStart = frameN  # exact frame index
        Q19_Slider.tStart = t  # local t and not account for scr refresh
        Q19_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q19_Slider, 'tStartRefresh')  # time at next scr refresh
        Q19_Slider.setAutoDraw(True)
    
    # *Q20* updates
    if Q20.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q20.frameNStart = frameN  # exact frame index
        Q20.tStart = t  # local t and not account for scr refresh
        Q20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q20, 'tStartRefresh')  # time at next scr refresh
        Q20.setAutoDraw(True)
    
    # *Q20_Slider* updates
    if Q20_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q20_Slider.frameNStart = frameN  # exact frame index
        Q20_Slider.tStart = t  # local t and not account for scr refresh
        Q20_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q20_Slider, 'tStartRefresh')  # time at next scr refresh
        Q20_Slider.setAutoDraw(True)
    
    # *Q21* updates
    if Q21.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q21.frameNStart = frameN  # exact frame index
        Q21.tStart = t  # local t and not account for scr refresh
        Q21.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q21, 'tStartRefresh')  # time at next scr refresh
        Q21.setAutoDraw(True)
    
    # *Q21_Slider* updates
    if Q21_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q21_Slider.frameNStart = frameN  # exact frame index
        Q21_Slider.tStart = t  # local t and not account for scr refresh
        Q21_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q21_Slider, 'tStartRefresh')  # time at next scr refresh
        Q21_Slider.setAutoDraw(True)
    
    # *Q22* updates
    if Q22.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q22.frameNStart = frameN  # exact frame index
        Q22.tStart = t  # local t and not account for scr refresh
        Q22.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q22, 'tStartRefresh')  # time at next scr refresh
        Q22.setAutoDraw(True)
    
    # *Q22_Slider* updates
    if Q22_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q22_Slider.frameNStart = frameN  # exact frame index
        Q22_Slider.tStart = t  # local t and not account for scr refresh
        Q22_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q22_Slider, 'tStartRefresh')  # time at next scr refresh
        Q22_Slider.setAutoDraw(True)
    
    # *Q23* updates
    if Q23.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q23.frameNStart = frameN  # exact frame index
        Q23.tStart = t  # local t and not account for scr refresh
        Q23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q23, 'tStartRefresh')  # time at next scr refresh
        Q23.setAutoDraw(True)
    
    # *Q23_Slider* updates
    if Q23_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q23_Slider.frameNStart = frameN  # exact frame index
        Q23_Slider.tStart = t  # local t and not account for scr refresh
        Q23_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q23_Slider, 'tStartRefresh')  # time at next scr refresh
        Q23_Slider.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Survey_TrialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Survey_Trial"-------
for thisComponent in Survey_TrialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Q1_Slider.response', Q1_Slider.getRating())
thisExp.addData('Q2_Slider.response', Q2_Slider.getRating())
thisExp.addData('Q3_Slider.response', Q3_Slider.getRating())
thisExp.addData('Q4_Slider.response', Q4_Slider.getRating())
thisExp.addData('Q5_Slider.response', Q5_Slider.getRating())
thisExp.addData('Q6_Slider.response', Q6_Slider.getRating())
thisExp.addData('Q7_Slider.response', Q7_Slider.getRating())
thisExp.addData('Q8_Slider.response', Q8_Slider.getRating())
thisExp.addData('Q9_Slider.response', Q9_Slider.getRating())
thisExp.addData('Q10_Slider.response', Q10_Slider.getRating())
thisExp.addData('Q11_Slider.response', Q11_Slider.getRating())
thisExp.addData('Q12_Slider.response', Q12_Slider.getRating())
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
thisExp.addData('Q13_Slider.response', Q13_Slider.getRating())
thisExp.addData('Q14_Slider.response', Q14_Slider.getRating())
thisExp.addData('Q15_Slider.response', Q15_Slider.getRating())
thisExp.addData('Q16_Slider.response', Q16_Slider.getRating())
thisExp.addData('Q17_Slider.response', Q17_Slider.getRating())
thisExp.addData('Q18_Slider.response', Q18_Slider.getRating())
thisExp.addData('Q19_Slider.response', Q19_Slider.getRating())
thisExp.addData('Q20_Slider.response', Q20_Slider.getRating())
thisExp.addData('Q21_Slider.response', Q21_Slider.getRating())
thisExp.addData('Q22_Slider.response', Q22_Slider.getRating())
thisExp.addData('Q23_Slider.response', Q23_Slider.getRating())
# the Routine "Survey_Trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Break"-------
continueRoutine = True
# update component parameters for each repeat
Break_KeyResp.keys = []
Break_KeyResp.rt = []
_Break_KeyResp_allKeys = []
# keep track of which components have finished
BreakComponents = [Break_Txt, Break_PresstoCont, Break_KeyResp]
for thisComponent in BreakComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BreakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Break"-------
while continueRoutine:
    # get current time
    t = BreakClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BreakClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Break_Txt* updates
    if Break_Txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Break_Txt.frameNStart = frameN  # exact frame index
        Break_Txt.tStart = t  # local t and not account for scr refresh
        Break_Txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Break_Txt, 'tStartRefresh')  # time at next scr refresh
        Break_Txt.setAutoDraw(True)
    
    # *Break_PresstoCont* updates
    if Break_PresstoCont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Break_PresstoCont.frameNStart = frameN  # exact frame index
        Break_PresstoCont.tStart = t  # local t and not account for scr refresh
        Break_PresstoCont.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Break_PresstoCont, 'tStartRefresh')  # time at next scr refresh
        Break_PresstoCont.setAutoDraw(True)
    
    # *Break_KeyResp* updates
    if Break_KeyResp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Break_KeyResp.frameNStart = frameN  # exact frame index
        Break_KeyResp.tStart = t  # local t and not account for scr refresh
        Break_KeyResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Break_KeyResp, 'tStartRefresh')  # time at next scr refresh
        Break_KeyResp.status = STARTED
        # keyboard checking is just starting
        Break_KeyResp.clock.reset()  # now t=0
    if Break_KeyResp.status == STARTED:
        theseKeys = Break_KeyResp.getKeys(keyList=['space'], waitRelease=False)
        _Break_KeyResp_allKeys.extend(theseKeys)
        if len(_Break_KeyResp_allKeys):
            Break_KeyResp.keys = _Break_KeyResp_allKeys[-1].name  # just the last key pressed
            Break_KeyResp.rt = _Break_KeyResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Break"-------
for thisComponent in BreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Break" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Choice_Trial"-------
continueRoutine = True
# update component parameters for each repeat
Stim_slider.reset()
# setup some python lists for storing info about the mouse_5
mouse_5.x = []
mouse_5.y = []
mouse_5.leftButton = []
mouse_5.midButton = []
mouse_5.rightButton = []
mouse_5.time = []
mouse_5.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
Choice_TrialComponents = [Intro_Text, Stim_slider, mouse_5, Click_to_Continue_5]
for thisComponent in Choice_TrialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Choice_TrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Choice_Trial"-------
while continueRoutine:
    # get current time
    t = Choice_TrialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Choice_TrialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Intro_Text* updates
    if Intro_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Intro_Text.frameNStart = frameN  # exact frame index
        Intro_Text.tStart = t  # local t and not account for scr refresh
        Intro_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Intro_Text, 'tStartRefresh')  # time at next scr refresh
        Intro_Text.setAutoDraw(True)
    
    # *Stim_slider* updates
    if Stim_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Stim_slider.frameNStart = frameN  # exact frame index
        Stim_slider.tStart = t  # local t and not account for scr refresh
        Stim_slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Stim_slider, 'tStartRefresh')  # time at next scr refresh
        Stim_slider.setAutoDraw(True)
    # *mouse_5* updates
    if mouse_5.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_5.frameNStart = frameN  # exact frame index
        mouse_5.tStart = t  # local t and not account for scr refresh
        mouse_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_5, 'tStartRefresh')  # time at next scr refresh
        mouse_5.status = STARTED
        mouse_5.mouseClock.reset()
        prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
    if mouse_5.status == STARTED:  # only update if started and not finished!
        buttons = mouse_5.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(Click_to_Continue_5)
                    clickableList = Click_to_Continue_5
                except:
                    clickableList = [Click_to_Continue_5]
                for obj in clickableList:
                    if obj.contains(mouse_5):
                        gotValidClick = True
                        mouse_5.clicked_name.append(obj.name)
                x, y = mouse_5.getPos()
                mouse_5.x.append(x)
                mouse_5.y.append(y)
                buttons = mouse_5.getPressed()
                mouse_5.leftButton.append(buttons[0])
                mouse_5.midButton.append(buttons[1])
                mouse_5.rightButton.append(buttons[2])
                mouse_5.time.append(mouse_5.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # *Click_to_Continue_5* updates
    if Click_to_Continue_5.status == NOT_STARTED and Stim_slider.rating:
        # keep track of start time/frame for later
        Click_to_Continue_5.frameNStart = frameN  # exact frame index
        Click_to_Continue_5.tStart = t  # local t and not account for scr refresh
        Click_to_Continue_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Click_to_Continue_5, 'tStartRefresh')  # time at next scr refresh
        Click_to_Continue_5.setAutoDraw(True)
    Click_to_Continue_5.autoDraw = True
    Click_to_Continue_5.pos = [-1000,0]
    if Stim_slider.rating == 1:
        Click_to_Continue_5.pos = [0.55,-0.45]
    if Stim_slider.rating == 2:
        Click_to_Continue_5.pos = [0.55,-0.45]
    if Stim_slider.rating == 3:
        Click_to_Continue_5.pos = [0.55,-0.45]
    elif Stim_slider.rating == 4:
        Click_to_Continue_5.pos = [0.55,-0.45]
    
    if mouse_5.isPressedIn(Click_to_Continue_5):
        if Stim_slider.rating == 1:
            trials = 1
            trials2 = 0
            trials3 = 0
            trials4 = 0
        elif Stim_slider.rating == 2:
            trials = 0
            trials2 =1
            trials3 = 0
            trials4 = 0
        elif Stim_slider.rating == 3:
            trials = 0
            trials2 = 0
            trials3 = 1
            trials4 = 0
        elif Stim_slider.rating == 4:
            trials = 0
            trials2 = 0
            trials3 = 0
            trials4 = 1
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Choice_TrialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Choice_Trial"-------
for thisComponent in Choice_TrialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Intro_Text.started', Intro_Text.tStartRefresh)
thisExp.addData('Intro_Text.stopped', Intro_Text.tStopRefresh)
thisExp.addData('Stim_slider.response', Stim_slider.getRating())
thisExp.addData('Stim_slider.rt', Stim_slider.getRT())
thisExp.addData('Stim_slider.started', Stim_slider.tStartRefresh)
thisExp.addData('Stim_slider.stopped', Stim_slider.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_5.x', mouse_5.x)
thisExp.addData('mouse_5.y', mouse_5.y)
thisExp.addData('mouse_5.leftButton', mouse_5.leftButton)
thisExp.addData('mouse_5.midButton', mouse_5.midButton)
thisExp.addData('mouse_5.rightButton', mouse_5.rightButton)
thisExp.addData('mouse_5.time', mouse_5.time)
thisExp.addData('mouse_5.clicked_name', mouse_5.clicked_name)
thisExp.addData('mouse_5.started', mouse_5.tStart)
thisExp.addData('mouse_5.stopped', mouse_5.tStop)
thisExp.nextEntry()
thisExp.addData('Click_to_Continue_5.started', Click_to_Continue_5.tStartRefresh)
thisExp.addData('Click_to_Continue_5.stopped', Click_to_Continue_5.tStopRefresh)
# the Routine "Choice_Trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Choice_Break"-------
continueRoutine = True
# update component parameters for each repeat
Choice_Break_KeyResp.keys = []
Choice_Break_KeyResp.rt = []
_Choice_Break_KeyResp_allKeys = []
# keep track of which components have finished
Choice_BreakComponents = [Choice_Break_Txt, Choice_Break_PresstoCont, Choice_Break_KeyResp]
for thisComponent in Choice_BreakComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Choice_BreakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Choice_Break"-------
while continueRoutine:
    # get current time
    t = Choice_BreakClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Choice_BreakClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Choice_Break_Txt* updates
    if Choice_Break_Txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Choice_Break_Txt.frameNStart = frameN  # exact frame index
        Choice_Break_Txt.tStart = t  # local t and not account for scr refresh
        Choice_Break_Txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Choice_Break_Txt, 'tStartRefresh')  # time at next scr refresh
        Choice_Break_Txt.setAutoDraw(True)
    
    # *Choice_Break_PresstoCont* updates
    if Choice_Break_PresstoCont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Choice_Break_PresstoCont.frameNStart = frameN  # exact frame index
        Choice_Break_PresstoCont.tStart = t  # local t and not account for scr refresh
        Choice_Break_PresstoCont.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Choice_Break_PresstoCont, 'tStartRefresh')  # time at next scr refresh
        Choice_Break_PresstoCont.setAutoDraw(True)
    
    # *Choice_Break_KeyResp* updates
    if Choice_Break_KeyResp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Choice_Break_KeyResp.frameNStart = frameN  # exact frame index
        Choice_Break_KeyResp.tStart = t  # local t and not account for scr refresh
        Choice_Break_KeyResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Choice_Break_KeyResp, 'tStartRefresh')  # time at next scr refresh
        Choice_Break_KeyResp.status = STARTED
        # keyboard checking is just starting
        Choice_Break_KeyResp.clock.reset()  # now t=0
    if Choice_Break_KeyResp.status == STARTED:
        theseKeys = Choice_Break_KeyResp.getKeys(keyList=['space'], waitRelease=False)
        _Choice_Break_KeyResp_allKeys.extend(theseKeys)
        if len(_Choice_Break_KeyResp_allKeys):
            Choice_Break_KeyResp.keys = _Choice_Break_KeyResp_allKeys[-1].name  # just the last key pressed
            Choice_Break_KeyResp.rt = _Choice_Break_KeyResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Choice_BreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Choice_Break"-------
for thisComponent in Choice_BreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Choice_Break" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=trials, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('final block/conditions/conversational_conditionsFile.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Choice_1"-------
    continueRoutine = True
    # update component parameters for each repeat
    Question_Txt_6.setText(txtStim)
    AI_Response_6.setText(AI_Resp)
    Accept_Deny_Button_6.reset()
    ConfidenceSlider_6.reset()
    Experimental_Images_6.setImage(stimFile)
    DenySlider_6.reset()
    # setup some python lists for storing info about the mouse_9
    mouse_9.x = []
    mouse_9.y = []
    mouse_9.leftButton = []
    mouse_9.midButton = []
    mouse_9.rightButton = []
    mouse_9.time = []
    mouse_9.clicked_name = []
    gotValidClick = False  # until a click is received
    AI_Response_Txt_6.setText('AI Response:')
    outlet.push_sample(x=[5])
    
    from psychopy import core# this returns a time value in seconds, not a clock object:
    
    clock = core.getAbsTime()
    
    import time
    
    from datetime import datetime
    
    ETrial= datetime.fromtimestamp(clock).strftime("%A, %B %d, %Y %I:%M:%S")
    
    trials.addData('trial_start', ETrial)
    # keep track of which components have finished
    Choice_1Components = [Choice_1_Intro_Txt, Question_Txt_6, AI_Response_6, Accept_Deny_Button_6, ConfidenceText_6, ConfidenceSlider_6, Experimental_Images_6, IfDenied_6, DenySlider_6, mouse_9, Click_to_Continue_9, AI_Response_Txt_6, Explanation_Image_6]
    for thisComponent in Choice_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Choice_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Choice_1"-------
    while continueRoutine:
        # get current time
        t = Choice_1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Choice_1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Choice_1_Intro_Txt* updates
        if Choice_1_Intro_Txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Choice_1_Intro_Txt.frameNStart = frameN  # exact frame index
            Choice_1_Intro_Txt.tStart = t  # local t and not account for scr refresh
            Choice_1_Intro_Txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice_1_Intro_Txt, 'tStartRefresh')  # time at next scr refresh
            Choice_1_Intro_Txt.setAutoDraw(True)
        if Choice_1_Intro_Txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Choice_1_Intro_Txt.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                Choice_1_Intro_Txt.tStop = t  # not accounting for scr refresh
                Choice_1_Intro_Txt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Choice_1_Intro_Txt, 'tStopRefresh')  # time at next scr refresh
                Choice_1_Intro_Txt.setAutoDraw(False)
        
        # *Question_Txt_6* updates
        if Question_Txt_6.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            Question_Txt_6.frameNStart = frameN  # exact frame index
            Question_Txt_6.tStart = t  # local t and not account for scr refresh
            Question_Txt_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Question_Txt_6, 'tStartRefresh')  # time at next scr refresh
            Question_Txt_6.setAutoDraw(True)
        
        # *AI_Response_6* updates
        if AI_Response_6.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            AI_Response_6.frameNStart = frameN  # exact frame index
            AI_Response_6.tStart = t  # local t and not account for scr refresh
            AI_Response_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AI_Response_6, 'tStartRefresh')  # time at next scr refresh
            AI_Response_6.setAutoDraw(True)
        
        # *Accept_Deny_Button_6* updates
        if Accept_Deny_Button_6.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            Accept_Deny_Button_6.frameNStart = frameN  # exact frame index
            Accept_Deny_Button_6.tStart = t  # local t and not account for scr refresh
            Accept_Deny_Button_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Accept_Deny_Button_6, 'tStartRefresh')  # time at next scr refresh
            Accept_Deny_Button_6.setAutoDraw(True)
        
        # *ConfidenceText_6* updates
        if ConfidenceText_6.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            ConfidenceText_6.frameNStart = frameN  # exact frame index
            ConfidenceText_6.tStart = t  # local t and not account for scr refresh
            ConfidenceText_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ConfidenceText_6, 'tStartRefresh')  # time at next scr refresh
            ConfidenceText_6.setAutoDraw(True)
        
        # *ConfidenceSlider_6* updates
        if ConfidenceSlider_6.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            ConfidenceSlider_6.frameNStart = frameN  # exact frame index
            ConfidenceSlider_6.tStart = t  # local t and not account for scr refresh
            ConfidenceSlider_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ConfidenceSlider_6, 'tStartRefresh')  # time at next scr refresh
            ConfidenceSlider_6.setAutoDraw(True)
        
        # *Experimental_Images_6* updates
        if Experimental_Images_6.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            Experimental_Images_6.frameNStart = frameN  # exact frame index
            Experimental_Images_6.tStart = t  # local t and not account for scr refresh
            Experimental_Images_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Experimental_Images_6, 'tStartRefresh')  # time at next scr refresh
            Experimental_Images_6.setAutoDraw(True)
        
        # *IfDenied_6* updates
        if IfDenied_6.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            IfDenied_6.frameNStart = frameN  # exact frame index
            IfDenied_6.tStart = t  # local t and not account for scr refresh
            IfDenied_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IfDenied_6, 'tStartRefresh')  # time at next scr refresh
            IfDenied_6.setAutoDraw(True)
        
        # *DenySlider_6* updates
        if DenySlider_6.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            DenySlider_6.frameNStart = frameN  # exact frame index
            DenySlider_6.tStart = t  # local t and not account for scr refresh
            DenySlider_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DenySlider_6, 'tStartRefresh')  # time at next scr refresh
            DenySlider_6.setAutoDraw(True)
        # *mouse_9* updates
        if mouse_9.status == NOT_STARTED and t >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_9.frameNStart = frameN  # exact frame index
            mouse_9.tStart = t  # local t and not account for scr refresh
            mouse_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_9, 'tStartRefresh')  # time at next scr refresh
            mouse_9.status = STARTED
            mouse_9.mouseClock.reset()
            prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
        if mouse_9.status == STARTED:  # only update if started and not finished!
            buttons = mouse_9.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(Click_to_Continue_9)
                        clickableList = Click_to_Continue_9
                    except:
                        clickableList = [Click_to_Continue_9]
                    for obj in clickableList:
                        if obj.contains(mouse_9):
                            gotValidClick = True
                            mouse_9.clicked_name.append(obj.name)
                    x, y = mouse_9.getPos()
                    mouse_9.x.append(x)
                    mouse_9.y.append(y)
                    buttons = mouse_9.getPressed()
                    mouse_9.leftButton.append(buttons[0])
                    mouse_9.midButton.append(buttons[1])
                    mouse_9.rightButton.append(buttons[2])
                    mouse_9.time.append(mouse_9.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # abort routine on response
        
        # *Click_to_Continue_9* updates
        if Click_to_Continue_9.status == NOT_STARTED and Accept_Deny_Button_6.rating and ConfidenceSlider_6.rating and DenySlider_6.rating:
            # keep track of start time/frame for later
            Click_to_Continue_9.frameNStart = frameN  # exact frame index
            Click_to_Continue_9.tStart = t  # local t and not account for scr refresh
            Click_to_Continue_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Click_to_Continue_9, 'tStartRefresh')  # time at next scr refresh
            Click_to_Continue_9.setAutoDraw(True)
        
        # *AI_Response_Txt_6* updates
        if AI_Response_Txt_6.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            AI_Response_Txt_6.frameNStart = frameN  # exact frame index
            AI_Response_Txt_6.tStart = t  # local t and not account for scr refresh
            AI_Response_Txt_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AI_Response_Txt_6, 'tStartRefresh')  # time at next scr refresh
            AI_Response_Txt_6.setAutoDraw(True)
        
        # *Explanation_Image_6* updates
        if Explanation_Image_6.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            Explanation_Image_6.frameNStart = frameN  # exact frame index
            Explanation_Image_6.tStart = t  # local t and not account for scr refresh
            Explanation_Image_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Explanation_Image_6, 'tStartRefresh')  # time at next scr refresh
            Explanation_Image_6.setAutoDraw(True)
        if Explanation_Image_6.status == STARTED:  # only update if drawing
            Explanation_Image_6.setImage(ExplanationFile, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Choice_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Choice_1"-------
    for thisComponent in Choice_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Choice_1_Intro_Txt.started', Choice_1_Intro_Txt.tStartRefresh)
    trials.addData('Choice_1_Intro_Txt.stopped', Choice_1_Intro_Txt.tStopRefresh)
    trials.addData('Accept_Deny_Button_6.response', Accept_Deny_Button_6.getRating())
    trials.addData('Accept_Deny_Button_6.rt', Accept_Deny_Button_6.getRT())
    trials.addData('Accept_Deny_Button_6.started', Accept_Deny_Button_6.tStartRefresh)
    trials.addData('Accept_Deny_Button_6.stopped', Accept_Deny_Button_6.tStopRefresh)
    trials.addData('ConfidenceSlider_6.response', ConfidenceSlider_6.getRating())
    trials.addData('ConfidenceSlider_6.rt', ConfidenceSlider_6.getRT())
    trials.addData('ConfidenceSlider_6.started', ConfidenceSlider_6.tStartRefresh)
    trials.addData('ConfidenceSlider_6.stopped', ConfidenceSlider_6.tStopRefresh)
    trials.addData('Experimental_Images_6.started', Experimental_Images_6.tStartRefresh)
    trials.addData('Experimental_Images_6.stopped', Experimental_Images_6.tStopRefresh)
    trials.addData('DenySlider_6.response', DenySlider_6.getRating())
    trials.addData('DenySlider_6.rt', DenySlider_6.getRT())
    trials.addData('DenySlider_6.started', DenySlider_6.tStartRefresh)
    trials.addData('DenySlider_6.stopped', DenySlider_6.tStopRefresh)
    # store data for trials (TrialHandler)
    trials.addData('mouse_9.x', mouse_9.x)
    trials.addData('mouse_9.y', mouse_9.y)
    trials.addData('mouse_9.leftButton', mouse_9.leftButton)
    trials.addData('mouse_9.midButton', mouse_9.midButton)
    trials.addData('mouse_9.rightButton', mouse_9.rightButton)
    trials.addData('mouse_9.time', mouse_9.time)
    trials.addData('mouse_9.clicked_name', mouse_9.clicked_name)
    trials.addData('mouse_9.started', mouse_9.tStart)
    trials.addData('mouse_9.stopped', mouse_9.tStop)
    trials.addData('Click_to_Continue_9.started', Click_to_Continue_9.tStartRefresh)
    trials.addData('Click_to_Continue_9.stopped', Click_to_Continue_9.tStopRefresh)
    outlet.push_sample(x=[5])
    
    from psychopy import core# this returns a time value in seconds, not a clock object:
    
    clock = core.getAbsTime()
    
    import time
    
    from datetime import datetime
    
    ETrial= datetime.fromtimestamp(clock).strftime("%A, %B %d, %Y %I:%M:%S")
    
    trials.addData('trial_end', ETrial)
    # the Routine "Choice_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed trials repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials.saveAsText(filename + 'trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=trials2, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('final block/conditions/feature_based_conditionsFile.csv'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Choice_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    Question_Txt_7.setText(txtStim)
    AI_Response_7.setText(AI_Resp)
    Accept_Deny_Button_7.reset()
    ConfidenceSlider_7.reset()
    Experimental_Images_7.setImage(stimFile)
    DenySlider_7.reset()
    # setup some python lists for storing info about the mouse_10
    mouse_10.x = []
    mouse_10.y = []
    mouse_10.leftButton = []
    mouse_10.midButton = []
    mouse_10.rightButton = []
    mouse_10.time = []
    mouse_10.clicked_name = []
    gotValidClick = False  # until a click is received
    AI_Response_Txt_7.setText('AI Response:')
    outlet.push_sample(x=[6])
    
    from psychopy import core# this returns a time value in seconds, not a clock object:
    
    clock = core.getAbsTime()
    
    import time
    
    from datetime import datetime
    
    ETrial= datetime.fromtimestamp(clock).strftime("%A, %B %d, %Y %I:%M:%S")
    
    trials_2.addData('trial_start', ETrial)
    # keep track of which components have finished
    Choice_2Components = [Choice_2_Intro_Txt, Question_Txt_7, AI_Response_7, Accept_Deny_Button_7, ConfidenceText_7, ConfidenceSlider_7, Experimental_Images_7, IfDenied_7, DenySlider_7, mouse_10, Click_to_Continue_10, AI_Response_Txt_7, Explanation_Image_7]
    for thisComponent in Choice_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Choice_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Choice_2"-------
    while continueRoutine:
        # get current time
        t = Choice_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Choice_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Choice_2_Intro_Txt* updates
        if Choice_2_Intro_Txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Choice_2_Intro_Txt.frameNStart = frameN  # exact frame index
            Choice_2_Intro_Txt.tStart = t  # local t and not account for scr refresh
            Choice_2_Intro_Txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice_2_Intro_Txt, 'tStartRefresh')  # time at next scr refresh
            Choice_2_Intro_Txt.setAutoDraw(True)
        if Choice_2_Intro_Txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Choice_2_Intro_Txt.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                Choice_2_Intro_Txt.tStop = t  # not accounting for scr refresh
                Choice_2_Intro_Txt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Choice_2_Intro_Txt, 'tStopRefresh')  # time at next scr refresh
                Choice_2_Intro_Txt.setAutoDraw(False)
        
        # *Question_Txt_7* updates
        if Question_Txt_7.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            Question_Txt_7.frameNStart = frameN  # exact frame index
            Question_Txt_7.tStart = t  # local t and not account for scr refresh
            Question_Txt_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Question_Txt_7, 'tStartRefresh')  # time at next scr refresh
            Question_Txt_7.setAutoDraw(True)
        
        # *AI_Response_7* updates
        if AI_Response_7.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            AI_Response_7.frameNStart = frameN  # exact frame index
            AI_Response_7.tStart = t  # local t and not account for scr refresh
            AI_Response_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AI_Response_7, 'tStartRefresh')  # time at next scr refresh
            AI_Response_7.setAutoDraw(True)
        
        # *Accept_Deny_Button_7* updates
        if Accept_Deny_Button_7.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            Accept_Deny_Button_7.frameNStart = frameN  # exact frame index
            Accept_Deny_Button_7.tStart = t  # local t and not account for scr refresh
            Accept_Deny_Button_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Accept_Deny_Button_7, 'tStartRefresh')  # time at next scr refresh
            Accept_Deny_Button_7.setAutoDraw(True)
        
        # *ConfidenceText_7* updates
        if ConfidenceText_7.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            ConfidenceText_7.frameNStart = frameN  # exact frame index
            ConfidenceText_7.tStart = t  # local t and not account for scr refresh
            ConfidenceText_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ConfidenceText_7, 'tStartRefresh')  # time at next scr refresh
            ConfidenceText_7.setAutoDraw(True)
        
        # *ConfidenceSlider_7* updates
        if ConfidenceSlider_7.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            ConfidenceSlider_7.frameNStart = frameN  # exact frame index
            ConfidenceSlider_7.tStart = t  # local t and not account for scr refresh
            ConfidenceSlider_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ConfidenceSlider_7, 'tStartRefresh')  # time at next scr refresh
            ConfidenceSlider_7.setAutoDraw(True)
        
        # *Experimental_Images_7* updates
        if Experimental_Images_7.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            Experimental_Images_7.frameNStart = frameN  # exact frame index
            Experimental_Images_7.tStart = t  # local t and not account for scr refresh
            Experimental_Images_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Experimental_Images_7, 'tStartRefresh')  # time at next scr refresh
            Experimental_Images_7.setAutoDraw(True)
        
        # *IfDenied_7* updates
        if IfDenied_7.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            IfDenied_7.frameNStart = frameN  # exact frame index
            IfDenied_7.tStart = t  # local t and not account for scr refresh
            IfDenied_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IfDenied_7, 'tStartRefresh')  # time at next scr refresh
            IfDenied_7.setAutoDraw(True)
        
        # *DenySlider_7* updates
        if DenySlider_7.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            DenySlider_7.frameNStart = frameN  # exact frame index
            DenySlider_7.tStart = t  # local t and not account for scr refresh
            DenySlider_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DenySlider_7, 'tStartRefresh')  # time at next scr refresh
            DenySlider_7.setAutoDraw(True)
        # *mouse_10* updates
        if mouse_10.status == NOT_STARTED and t >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_10.frameNStart = frameN  # exact frame index
            mouse_10.tStart = t  # local t and not account for scr refresh
            mouse_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_10, 'tStartRefresh')  # time at next scr refresh
            mouse_10.status = STARTED
            mouse_10.mouseClock.reset()
            prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
        if mouse_10.status == STARTED:  # only update if started and not finished!
            buttons = mouse_10.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(Click_to_Continue_10)
                        clickableList = Click_to_Continue_10
                    except:
                        clickableList = [Click_to_Continue_10]
                    for obj in clickableList:
                        if obj.contains(mouse_10):
                            gotValidClick = True
                            mouse_10.clicked_name.append(obj.name)
                    x, y = mouse_10.getPos()
                    mouse_10.x.append(x)
                    mouse_10.y.append(y)
                    buttons = mouse_10.getPressed()
                    mouse_10.leftButton.append(buttons[0])
                    mouse_10.midButton.append(buttons[1])
                    mouse_10.rightButton.append(buttons[2])
                    mouse_10.time.append(mouse_10.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # abort routine on response
        
        # *Click_to_Continue_10* updates
        if Click_to_Continue_10.status == NOT_STARTED and Accept_Deny_Button_7.rating and ConfidenceSlider_7.rating and DenySlider_7.rating:
            # keep track of start time/frame for later
            Click_to_Continue_10.frameNStart = frameN  # exact frame index
            Click_to_Continue_10.tStart = t  # local t and not account for scr refresh
            Click_to_Continue_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Click_to_Continue_10, 'tStartRefresh')  # time at next scr refresh
            Click_to_Continue_10.setAutoDraw(True)
        
        # *AI_Response_Txt_7* updates
        if AI_Response_Txt_7.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            AI_Response_Txt_7.frameNStart = frameN  # exact frame index
            AI_Response_Txt_7.tStart = t  # local t and not account for scr refresh
            AI_Response_Txt_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AI_Response_Txt_7, 'tStartRefresh')  # time at next scr refresh
            AI_Response_Txt_7.setAutoDraw(True)
        
        # *Explanation_Image_7* updates
        if Explanation_Image_7.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            Explanation_Image_7.frameNStart = frameN  # exact frame index
            Explanation_Image_7.tStart = t  # local t and not account for scr refresh
            Explanation_Image_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Explanation_Image_7, 'tStartRefresh')  # time at next scr refresh
            Explanation_Image_7.setAutoDraw(True)
        if Explanation_Image_7.status == STARTED:  # only update if drawing
            Explanation_Image_7.setImage(ExplanationFile, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Choice_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Choice_2"-------
    for thisComponent in Choice_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('Choice_2_Intro_Txt.started', Choice_2_Intro_Txt.tStartRefresh)
    trials_2.addData('Choice_2_Intro_Txt.stopped', Choice_2_Intro_Txt.tStopRefresh)
    trials_2.addData('Question_Txt_7.started', Question_Txt_7.tStartRefresh)
    trials_2.addData('Question_Txt_7.stopped', Question_Txt_7.tStopRefresh)
    trials_2.addData('Accept_Deny_Button_7.response', Accept_Deny_Button_7.getRating())
    trials_2.addData('Accept_Deny_Button_7.rt', Accept_Deny_Button_7.getRT())
    trials_2.addData('Accept_Deny_Button_7.started', Accept_Deny_Button_7.tStartRefresh)
    trials_2.addData('Accept_Deny_Button_7.stopped', Accept_Deny_Button_7.tStopRefresh)
    trials_2.addData('ConfidenceSlider_7.response', ConfidenceSlider_7.getRating())
    trials_2.addData('ConfidenceSlider_7.rt', ConfidenceSlider_7.getRT())
    trials_2.addData('ConfidenceSlider_7.started', ConfidenceSlider_7.tStartRefresh)
    trials_2.addData('ConfidenceSlider_7.stopped', ConfidenceSlider_7.tStopRefresh)
    trials_2.addData('Experimental_Images_7.started', Experimental_Images_7.tStartRefresh)
    trials_2.addData('Experimental_Images_7.stopped', Experimental_Images_7.tStopRefresh)
    trials_2.addData('DenySlider_7.response', DenySlider_7.getRating())
    trials_2.addData('DenySlider_7.rt', DenySlider_7.getRT())
    trials_2.addData('DenySlider_7.started', DenySlider_7.tStartRefresh)
    trials_2.addData('DenySlider_7.stopped', DenySlider_7.tStopRefresh)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('mouse_10.x', mouse_10.x)
    trials_2.addData('mouse_10.y', mouse_10.y)
    trials_2.addData('mouse_10.leftButton', mouse_10.leftButton)
    trials_2.addData('mouse_10.midButton', mouse_10.midButton)
    trials_2.addData('mouse_10.rightButton', mouse_10.rightButton)
    trials_2.addData('mouse_10.time', mouse_10.time)
    trials_2.addData('mouse_10.clicked_name', mouse_10.clicked_name)
    trials_2.addData('mouse_10.started', mouse_10.tStart)
    trials_2.addData('mouse_10.stopped', mouse_10.tStop)
    trials_2.addData('Click_to_Continue_10.started', Click_to_Continue_10.tStartRefresh)
    trials_2.addData('Click_to_Continue_10.stopped', Click_to_Continue_10.tStopRefresh)
    outlet.push_sample(x=[6])
    
    from psychopy import core# this returns a time value in seconds, not a clock object:
    
    clock = core.getAbsTime()
    
    import time
    
    from datetime import datetime
    
    ETrial= datetime.fromtimestamp(clock).strftime("%A, %B %d, %Y %I:%M:%S")
    
    trials_2.addData('trial_end', ETrial)
    # the Routine "Choice_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed trials2 repeats of 'trials_2'

# get names of stimulus parameters
if trials_2.trialList in ([], [None], None):
    params = []
else:
    params = trials_2.trialList[0].keys()
# save data for this loop
trials_2.saveAsExcel(filename + '.xlsx', sheetName='trials_2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials_2.saveAsText(filename + 'trials_2.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=trials3, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('final block/conditions/image_based_conditionsFile.csv'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Choice_3"-------
    continueRoutine = True
    # update component parameters for each repeat
    Question_Txt_8.setText(txtStim)
    AI_Response_8.setText(AI_Resp)
    Accept_Deny_Button_8.reset()
    ConfidenceSlider_8.reset()
    Experimental_Images_8.setImage(stimFile)
    DenySlider_8.reset()
    # setup some python lists for storing info about the mouse_11
    mouse_11.x = []
    mouse_11.y = []
    mouse_11.leftButton = []
    mouse_11.midButton = []
    mouse_11.rightButton = []
    mouse_11.time = []
    mouse_11.clicked_name = []
    gotValidClick = False  # until a click is received
    AI_Response_Txt_8.setText('AI Response:')
    outlet.push_sample(x=[7])
    
    from psychopy import core# this returns a time value in seconds, not a clock object:
    
    clock = core.getAbsTime()
    
    import time
    
    from datetime import datetime
    
    ETrial= datetime.fromtimestamp(clock).strftime("%A, %B %d, %Y %I:%M:%S")
    
    trials_3.addData('trial_start', ETrial)
    # keep track of which components have finished
    Choice_3Components = [Choice_3_Intro_Txt, Question_Txt_8, AI_Response_8, Accept_Deny_Button_8, ConfidenceText_8, ConfidenceSlider_8, Experimental_Images_8, IfDenied_8, DenySlider_8, mouse_11, Click_to_Continue_11, AI_Response_Txt_8, Explanation_Image_8]
    for thisComponent in Choice_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Choice_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Choice_3"-------
    while continueRoutine:
        # get current time
        t = Choice_3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Choice_3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Choice_3_Intro_Txt* updates
        if Choice_3_Intro_Txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Choice_3_Intro_Txt.frameNStart = frameN  # exact frame index
            Choice_3_Intro_Txt.tStart = t  # local t and not account for scr refresh
            Choice_3_Intro_Txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice_3_Intro_Txt, 'tStartRefresh')  # time at next scr refresh
            Choice_3_Intro_Txt.setAutoDraw(True)
        if Choice_3_Intro_Txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Choice_3_Intro_Txt.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                Choice_3_Intro_Txt.tStop = t  # not accounting for scr refresh
                Choice_3_Intro_Txt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Choice_3_Intro_Txt, 'tStopRefresh')  # time at next scr refresh
                Choice_3_Intro_Txt.setAutoDraw(False)
        
        # *Question_Txt_8* updates
        if Question_Txt_8.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            Question_Txt_8.frameNStart = frameN  # exact frame index
            Question_Txt_8.tStart = t  # local t and not account for scr refresh
            Question_Txt_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Question_Txt_8, 'tStartRefresh')  # time at next scr refresh
            Question_Txt_8.setAutoDraw(True)
        
        # *AI_Response_8* updates
        if AI_Response_8.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            AI_Response_8.frameNStart = frameN  # exact frame index
            AI_Response_8.tStart = t  # local t and not account for scr refresh
            AI_Response_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AI_Response_8, 'tStartRefresh')  # time at next scr refresh
            AI_Response_8.setAutoDraw(True)
        
        # *Accept_Deny_Button_8* updates
        if Accept_Deny_Button_8.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            Accept_Deny_Button_8.frameNStart = frameN  # exact frame index
            Accept_Deny_Button_8.tStart = t  # local t and not account for scr refresh
            Accept_Deny_Button_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Accept_Deny_Button_8, 'tStartRefresh')  # time at next scr refresh
            Accept_Deny_Button_8.setAutoDraw(True)
        
        # *ConfidenceText_8* updates
        if ConfidenceText_8.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            ConfidenceText_8.frameNStart = frameN  # exact frame index
            ConfidenceText_8.tStart = t  # local t and not account for scr refresh
            ConfidenceText_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ConfidenceText_8, 'tStartRefresh')  # time at next scr refresh
            ConfidenceText_8.setAutoDraw(True)
        
        # *ConfidenceSlider_8* updates
        if ConfidenceSlider_8.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            ConfidenceSlider_8.frameNStart = frameN  # exact frame index
            ConfidenceSlider_8.tStart = t  # local t and not account for scr refresh
            ConfidenceSlider_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ConfidenceSlider_8, 'tStartRefresh')  # time at next scr refresh
            ConfidenceSlider_8.setAutoDraw(True)
        
        # *Experimental_Images_8* updates
        if Experimental_Images_8.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            Experimental_Images_8.frameNStart = frameN  # exact frame index
            Experimental_Images_8.tStart = t  # local t and not account for scr refresh
            Experimental_Images_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Experimental_Images_8, 'tStartRefresh')  # time at next scr refresh
            Experimental_Images_8.setAutoDraw(True)
        
        # *IfDenied_8* updates
        if IfDenied_8.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            IfDenied_8.frameNStart = frameN  # exact frame index
            IfDenied_8.tStart = t  # local t and not account for scr refresh
            IfDenied_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IfDenied_8, 'tStartRefresh')  # time at next scr refresh
            IfDenied_8.setAutoDraw(True)
        
        # *DenySlider_8* updates
        if DenySlider_8.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            DenySlider_8.frameNStart = frameN  # exact frame index
            DenySlider_8.tStart = t  # local t and not account for scr refresh
            DenySlider_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DenySlider_8, 'tStartRefresh')  # time at next scr refresh
            DenySlider_8.setAutoDraw(True)
        # *mouse_11* updates
        if mouse_11.status == NOT_STARTED and t >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_11.frameNStart = frameN  # exact frame index
            mouse_11.tStart = t  # local t and not account for scr refresh
            mouse_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_11, 'tStartRefresh')  # time at next scr refresh
            mouse_11.status = STARTED
            mouse_11.mouseClock.reset()
            prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
        if mouse_11.status == STARTED:  # only update if started and not finished!
            buttons = mouse_11.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(Click_to_Continue_11)
                        clickableList = Click_to_Continue_11
                    except:
                        clickableList = [Click_to_Continue_11]
                    for obj in clickableList:
                        if obj.contains(mouse_11):
                            gotValidClick = True
                            mouse_11.clicked_name.append(obj.name)
                    x, y = mouse_11.getPos()
                    mouse_11.x.append(x)
                    mouse_11.y.append(y)
                    buttons = mouse_11.getPressed()
                    mouse_11.leftButton.append(buttons[0])
                    mouse_11.midButton.append(buttons[1])
                    mouse_11.rightButton.append(buttons[2])
                    mouse_11.time.append(mouse_11.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # abort routine on response
        
        # *Click_to_Continue_11* updates
        if Click_to_Continue_11.status == NOT_STARTED and Accept_Deny_Button_8.rating and ConfidenceSlider_8.rating and DenySlider_8.rating:
            # keep track of start time/frame for later
            Click_to_Continue_11.frameNStart = frameN  # exact frame index
            Click_to_Continue_11.tStart = t  # local t and not account for scr refresh
            Click_to_Continue_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Click_to_Continue_11, 'tStartRefresh')  # time at next scr refresh
            Click_to_Continue_11.setAutoDraw(True)
        
        # *AI_Response_Txt_8* updates
        if AI_Response_Txt_8.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            AI_Response_Txt_8.frameNStart = frameN  # exact frame index
            AI_Response_Txt_8.tStart = t  # local t and not account for scr refresh
            AI_Response_Txt_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AI_Response_Txt_8, 'tStartRefresh')  # time at next scr refresh
            AI_Response_Txt_8.setAutoDraw(True)
        
        # *Explanation_Image_8* updates
        if Explanation_Image_8.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            Explanation_Image_8.frameNStart = frameN  # exact frame index
            Explanation_Image_8.tStart = t  # local t and not account for scr refresh
            Explanation_Image_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Explanation_Image_8, 'tStartRefresh')  # time at next scr refresh
            Explanation_Image_8.setAutoDraw(True)
        if Explanation_Image_8.status == STARTED:  # only update if drawing
            Explanation_Image_8.setImage(ExplanationFile, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Choice_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Choice_3"-------
    for thisComponent in Choice_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('Choice_3_Intro_Txt.started', Choice_3_Intro_Txt.tStartRefresh)
    trials_3.addData('Choice_3_Intro_Txt.stopped', Choice_3_Intro_Txt.tStopRefresh)
    trials_3.addData('Question_Txt_8.started', Question_Txt_8.tStartRefresh)
    trials_3.addData('Question_Txt_8.stopped', Question_Txt_8.tStopRefresh)
    trials_3.addData('Accept_Deny_Button_8.response', Accept_Deny_Button_8.getRating())
    trials_3.addData('Accept_Deny_Button_8.rt', Accept_Deny_Button_8.getRT())
    trials_3.addData('Accept_Deny_Button_8.started', Accept_Deny_Button_8.tStartRefresh)
    trials_3.addData('Accept_Deny_Button_8.stopped', Accept_Deny_Button_8.tStopRefresh)
    trials_3.addData('ConfidenceSlider_8.response', ConfidenceSlider_8.getRating())
    trials_3.addData('ConfidenceSlider_8.rt', ConfidenceSlider_8.getRT())
    trials_3.addData('ConfidenceSlider_8.started', ConfidenceSlider_8.tStartRefresh)
    trials_3.addData('ConfidenceSlider_8.stopped', ConfidenceSlider_8.tStopRefresh)
    trials_3.addData('Experimental_Images_8.started', Experimental_Images_8.tStartRefresh)
    trials_3.addData('Experimental_Images_8.stopped', Experimental_Images_8.tStopRefresh)
    trials_3.addData('DenySlider_8.response', DenySlider_8.getRating())
    trials_3.addData('DenySlider_8.rt', DenySlider_8.getRT())
    trials_3.addData('DenySlider_8.started', DenySlider_8.tStartRefresh)
    trials_3.addData('DenySlider_8.stopped', DenySlider_8.tStopRefresh)
    # store data for trials_3 (TrialHandler)
    trials_3.addData('mouse_11.x', mouse_11.x)
    trials_3.addData('mouse_11.y', mouse_11.y)
    trials_3.addData('mouse_11.leftButton', mouse_11.leftButton)
    trials_3.addData('mouse_11.midButton', mouse_11.midButton)
    trials_3.addData('mouse_11.rightButton', mouse_11.rightButton)
    trials_3.addData('mouse_11.time', mouse_11.time)
    trials_3.addData('mouse_11.clicked_name', mouse_11.clicked_name)
    trials_3.addData('mouse_11.started', mouse_11.tStart)
    trials_3.addData('mouse_11.stopped', mouse_11.tStop)
    trials_3.addData('Click_to_Continue_11.started', Click_to_Continue_11.tStartRefresh)
    trials_3.addData('Click_to_Continue_11.stopped', Click_to_Continue_11.tStopRefresh)
    outlet.push_sample(x=[7])
    
    from psychopy import core# this returns a time value in seconds, not a clock object:
    
    clock = core.getAbsTime()
    
    import time
    
    from datetime import datetime
    
    ETrial= datetime.fromtimestamp(clock).strftime("%A, %B %d, %Y %I:%M:%S")
    
    trials_3.addData('trial_end', ETrial)
    # the Routine "Choice_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed trials3 repeats of 'trials_3'


# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=trials4, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('final block/conditions/text_based_conditionsFile.csv'),
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4:
        exec('{} = thisTrial_4[paramName]'.format(paramName))

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Choice_4"-------
    continueRoutine = True
    # update component parameters for each repeat
    Question_Txt_9.setText(txtStim)
    AI_Response_9.setText(AI_Resp)
    Accept_Deny_Button_9.reset()
    ConfidenceSlider_9.reset()
    Experimental_Images_9.setImage(stimFile)
    DenySlider_9.reset()
    # setup some python lists for storing info about the mouse_12
    mouse_12.x = []
    mouse_12.y = []
    mouse_12.leftButton = []
    mouse_12.midButton = []
    mouse_12.rightButton = []
    mouse_12.time = []
    mouse_12.clicked_name = []
    gotValidClick = False  # until a click is received
    AI_Response_Txt_9.setText('AI Response:')
    outlet.push_sample(x=[8])
    
    from psychopy import core# this returns a time value in seconds, not a clock object:
    
    clock = core.getAbsTime()
    
    import time
    
    from datetime import datetime
    
    ETrial= datetime.fromtimestamp(clock).strftime("%A, %B %d, %Y %I:%M:%S")
    
    trials_4.addData('trial_start', ETrial)
    # keep track of which components have finished
    Choice_4Components = [Choice_4_Intro_Txt, Question_Txt_9, AI_Response_9, Accept_Deny_Button_9, ConfidenceText_9, ConfidenceSlider_9, Experimental_Images_9, IfDenied_9, DenySlider_9, mouse_12, Click_to_Continue_12, AI_Response_Txt_9, Explanation_Image_9]
    for thisComponent in Choice_4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Choice_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Choice_4"-------
    while continueRoutine:
        # get current time
        t = Choice_4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Choice_4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Choice_4_Intro_Txt* updates
        if Choice_4_Intro_Txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Choice_4_Intro_Txt.frameNStart = frameN  # exact frame index
            Choice_4_Intro_Txt.tStart = t  # local t and not account for scr refresh
            Choice_4_Intro_Txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice_4_Intro_Txt, 'tStartRefresh')  # time at next scr refresh
            Choice_4_Intro_Txt.setAutoDraw(True)
        if Choice_4_Intro_Txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Choice_4_Intro_Txt.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                Choice_4_Intro_Txt.tStop = t  # not accounting for scr refresh
                Choice_4_Intro_Txt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Choice_4_Intro_Txt, 'tStopRefresh')  # time at next scr refresh
                Choice_4_Intro_Txt.setAutoDraw(False)
        
        # *Question_Txt_9* updates
        if Question_Txt_9.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            Question_Txt_9.frameNStart = frameN  # exact frame index
            Question_Txt_9.tStart = t  # local t and not account for scr refresh
            Question_Txt_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Question_Txt_9, 'tStartRefresh')  # time at next scr refresh
            Question_Txt_9.setAutoDraw(True)
        
        # *AI_Response_9* updates
        if AI_Response_9.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            AI_Response_9.frameNStart = frameN  # exact frame index
            AI_Response_9.tStart = t  # local t and not account for scr refresh
            AI_Response_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AI_Response_9, 'tStartRefresh')  # time at next scr refresh
            AI_Response_9.setAutoDraw(True)
        
        # *Accept_Deny_Button_9* updates
        if Accept_Deny_Button_9.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            Accept_Deny_Button_9.frameNStart = frameN  # exact frame index
            Accept_Deny_Button_9.tStart = t  # local t and not account for scr refresh
            Accept_Deny_Button_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Accept_Deny_Button_9, 'tStartRefresh')  # time at next scr refresh
            Accept_Deny_Button_9.setAutoDraw(True)
        
        # *ConfidenceText_9* updates
        if ConfidenceText_9.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            ConfidenceText_9.frameNStart = frameN  # exact frame index
            ConfidenceText_9.tStart = t  # local t and not account for scr refresh
            ConfidenceText_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ConfidenceText_9, 'tStartRefresh')  # time at next scr refresh
            ConfidenceText_9.setAutoDraw(True)
        
        # *ConfidenceSlider_9* updates
        if ConfidenceSlider_9.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            ConfidenceSlider_9.frameNStart = frameN  # exact frame index
            ConfidenceSlider_9.tStart = t  # local t and not account for scr refresh
            ConfidenceSlider_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ConfidenceSlider_9, 'tStartRefresh')  # time at next scr refresh
            ConfidenceSlider_9.setAutoDraw(True)
        
        # *Experimental_Images_9* updates
        if Experimental_Images_9.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            Experimental_Images_9.frameNStart = frameN  # exact frame index
            Experimental_Images_9.tStart = t  # local t and not account for scr refresh
            Experimental_Images_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Experimental_Images_9, 'tStartRefresh')  # time at next scr refresh
            Experimental_Images_9.setAutoDraw(True)
        
        # *IfDenied_9* updates
        if IfDenied_9.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            IfDenied_9.frameNStart = frameN  # exact frame index
            IfDenied_9.tStart = t  # local t and not account for scr refresh
            IfDenied_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IfDenied_9, 'tStartRefresh')  # time at next scr refresh
            IfDenied_9.setAutoDraw(True)
        
        # *DenySlider_9* updates
        if DenySlider_9.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            DenySlider_9.frameNStart = frameN  # exact frame index
            DenySlider_9.tStart = t  # local t and not account for scr refresh
            DenySlider_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DenySlider_9, 'tStartRefresh')  # time at next scr refresh
            DenySlider_9.setAutoDraw(True)
        # *mouse_12* updates
        if mouse_12.status == NOT_STARTED and t >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_12.frameNStart = frameN  # exact frame index
            mouse_12.tStart = t  # local t and not account for scr refresh
            mouse_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_12, 'tStartRefresh')  # time at next scr refresh
            mouse_12.status = STARTED
            mouse_12.mouseClock.reset()
            prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
        if mouse_12.status == STARTED:  # only update if started and not finished!
            buttons = mouse_12.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(Click_to_Continue_12)
                        clickableList = Click_to_Continue_12
                    except:
                        clickableList = [Click_to_Continue_12]
                    for obj in clickableList:
                        if obj.contains(mouse_12):
                            gotValidClick = True
                            mouse_12.clicked_name.append(obj.name)
                    x, y = mouse_12.getPos()
                    mouse_12.x.append(x)
                    mouse_12.y.append(y)
                    buttons = mouse_12.getPressed()
                    mouse_12.leftButton.append(buttons[0])
                    mouse_12.midButton.append(buttons[1])
                    mouse_12.rightButton.append(buttons[2])
                    mouse_12.time.append(mouse_12.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # abort routine on response
        
        # *Click_to_Continue_12* updates
        if Click_to_Continue_12.status == NOT_STARTED and Accept_Deny_Button_9.rating and ConfidenceSlider_9.rating and DenySlider_9.rating:
            # keep track of start time/frame for later
            Click_to_Continue_12.frameNStart = frameN  # exact frame index
            Click_to_Continue_12.tStart = t  # local t and not account for scr refresh
            Click_to_Continue_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Click_to_Continue_12, 'tStartRefresh')  # time at next scr refresh
            Click_to_Continue_12.setAutoDraw(True)
        
        # *AI_Response_Txt_9* updates
        if AI_Response_Txt_9.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            AI_Response_Txt_9.frameNStart = frameN  # exact frame index
            AI_Response_Txt_9.tStart = t  # local t and not account for scr refresh
            AI_Response_Txt_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AI_Response_Txt_9, 'tStartRefresh')  # time at next scr refresh
            AI_Response_Txt_9.setAutoDraw(True)
        
        # *Explanation_Image_9* updates
        if Explanation_Image_9.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            Explanation_Image_9.frameNStart = frameN  # exact frame index
            Explanation_Image_9.tStart = t  # local t and not account for scr refresh
            Explanation_Image_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Explanation_Image_9, 'tStartRefresh')  # time at next scr refresh
            Explanation_Image_9.setAutoDraw(True)
        if Explanation_Image_9.status == STARTED:  # only update if drawing
            Explanation_Image_9.setImage(ExplanationFile, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Choice_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Choice_4"-------
    for thisComponent in Choice_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_4.addData('Choice_4_Intro_Txt.started', Choice_4_Intro_Txt.tStartRefresh)
    trials_4.addData('Choice_4_Intro_Txt.stopped', Choice_4_Intro_Txt.tStopRefresh)
    trials_4.addData('Question_Txt_9.started', Question_Txt_9.tStartRefresh)
    trials_4.addData('Question_Txt_9.stopped', Question_Txt_9.tStopRefresh)
    trials_4.addData('Accept_Deny_Button_9.response', Accept_Deny_Button_9.getRating())
    trials_4.addData('Accept_Deny_Button_9.rt', Accept_Deny_Button_9.getRT())
    trials_4.addData('Accept_Deny_Button_9.started', Accept_Deny_Button_9.tStartRefresh)
    trials_4.addData('Accept_Deny_Button_9.stopped', Accept_Deny_Button_9.tStopRefresh)
    trials_4.addData('ConfidenceSlider_9.response', ConfidenceSlider_9.getRating())
    trials_4.addData('ConfidenceSlider_9.rt', ConfidenceSlider_9.getRT())
    trials_4.addData('ConfidenceSlider_9.started', ConfidenceSlider_9.tStartRefresh)
    trials_4.addData('ConfidenceSlider_9.stopped', ConfidenceSlider_9.tStopRefresh)
    trials_4.addData('Experimental_Images_9.started', Experimental_Images_9.tStartRefresh)
    trials_4.addData('Experimental_Images_9.stopped', Experimental_Images_9.tStopRefresh)
    trials_4.addData('DenySlider_9.response', DenySlider_9.getRating())
    trials_4.addData('DenySlider_9.rt', DenySlider_9.getRT())
    trials_4.addData('DenySlider_9.started', DenySlider_9.tStartRefresh)
    trials_4.addData('DenySlider_9.stopped', DenySlider_9.tStopRefresh)
    # store data for trials_4 (TrialHandler)
    trials_4.addData('mouse_12.x', mouse_12.x)
    trials_4.addData('mouse_12.y', mouse_12.y)
    trials_4.addData('mouse_12.leftButton', mouse_12.leftButton)
    trials_4.addData('mouse_12.midButton', mouse_12.midButton)
    trials_4.addData('mouse_12.rightButton', mouse_12.rightButton)
    trials_4.addData('mouse_12.time', mouse_12.time)
    trials_4.addData('mouse_12.clicked_name', mouse_12.clicked_name)
    trials_4.addData('mouse_12.started', mouse_12.tStart)
    trials_4.addData('mouse_12.stopped', mouse_12.tStop)
    trials_4.addData('Click_to_Continue_12.started', Click_to_Continue_12.tStartRefresh)
    trials_4.addData('Click_to_Continue_12.stopped', Click_to_Continue_12.tStopRefresh)
    outlet.push_sample(x=[8])
    
    from psychopy import core# this returns a time value in seconds, not a clock object:
    
    clock = core.getAbsTime()
    
    import time
    
    from datetime import datetime
    
    ETrial= datetime.fromtimestamp(clock).strftime("%A, %B %d, %Y %I:%M:%S")
    
    trials_4.addData('trial_end', ETrial)
    # the Routine "Choice_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed trials4 repeats of 'trials_4'

# get names of stimulus parameters
if trials_4.trialList in ([], [None], None):
    params = []
else:
    params = trials_4.trialList[0].keys()
# save data for this loop
trials_4.saveAsExcel(filename + '.xlsx', sheetName='trials_4',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials_4.saveAsText(filename + 'trials_4.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Choice_Survey_Break"-------
continueRoutine = True
# update component parameters for each repeat
KeyResp_11.keys = []
KeyResp_11.rt = []
_KeyResp_11_allKeys = []
# keep track of which components have finished
Choice_Survey_BreakComponents = [text_11, PresstoCont_11, KeyResp_11]
for thisComponent in Choice_Survey_BreakComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Choice_Survey_BreakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Choice_Survey_Break"-------
while continueRoutine:
    # get current time
    t = Choice_Survey_BreakClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Choice_Survey_BreakClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_11* updates
    if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_11.frameNStart = frameN  # exact frame index
        text_11.tStart = t  # local t and not account for scr refresh
        text_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
        text_11.setAutoDraw(True)
    
    # *PresstoCont_11* updates
    if PresstoCont_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PresstoCont_11.frameNStart = frameN  # exact frame index
        PresstoCont_11.tStart = t  # local t and not account for scr refresh
        PresstoCont_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PresstoCont_11, 'tStartRefresh')  # time at next scr refresh
        PresstoCont_11.setAutoDraw(True)
    
    # *KeyResp_11* updates
    if KeyResp_11.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        KeyResp_11.frameNStart = frameN  # exact frame index
        KeyResp_11.tStart = t  # local t and not account for scr refresh
        KeyResp_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(KeyResp_11, 'tStartRefresh')  # time at next scr refresh
        KeyResp_11.status = STARTED
        # keyboard checking is just starting
        KeyResp_11.clock.reset()  # now t=0
    if KeyResp_11.status == STARTED:
        theseKeys = KeyResp_11.getKeys(keyList=['space'], waitRelease=False)
        _KeyResp_11_allKeys.extend(theseKeys)
        if len(_KeyResp_11_allKeys):
            KeyResp_11.keys = _KeyResp_11_allKeys[-1].name  # just the last key pressed
            KeyResp_11.rt = _KeyResp_11_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Choice_Survey_BreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Choice_Survey_Break"-------
for thisComponent in Choice_Survey_BreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Choice_Survey_Break" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Survey_Trial"-------
continueRoutine = True
# update component parameters for each repeat
Q1_Slider.reset()
Q2_Slider.reset()
Q3_Slider.reset()
Q4_Slider.reset()
Q5_Slider.reset()
Q6_Slider.reset()
Q7_Slider.reset()
Q8_Slider.reset()
Q9_Slider.reset()
Q10_Slider.reset()
Q11_Slider.reset()
Q12_Slider.reset()
# setup some python lists for storing info about the mouse_2
mouse_2.clicked_name = []
gotValidClick = False  # until a click is received
Q13_Slider.reset()
Q14_Slider.reset()
Q15_Slider.reset()
Q16_Slider.reset()
Q17_Slider.reset()
Q18_Slider.reset()
Q19_Slider.reset()
Q20_Slider.reset()
Q21_Slider.reset()
Q22_Slider.reset()
Q23_Slider.reset()
# keep track of which components have finished
Survey_TrialComponents = [Q1, Q1_Slider, Q2, Q2_Slider, Q3, Q3_Slider, Q4, Q4_Slider, Q5, Q5_Slider, Q6, Q6_Slider, Q7, Q7_Slider, Q8, Q8_Slider, Q9, Q9_Slider, Q10, Q10_Slider, Q11, Q11_Slider, Q12, Q12_Slider, mouse_2, Click_to_Continue_2, Q13, Q13_Slider, Q14, Q14_Slider, Q15, Q15_Slider, Q16, Q16_Slider, Q17, Q17_Slider, Q18, Q18_Slider, Q19, Q19_Slider, Q20, Q20_Slider, Q21, Q21_Slider, Q22, Q22_Slider, Q23, Q23_Slider]
for thisComponent in Survey_TrialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Survey_TrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Survey_Trial"-------
while continueRoutine:
    # get current time
    t = Survey_TrialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Survey_TrialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Q1* updates
    if Q1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q1.frameNStart = frameN  # exact frame index
        Q1.tStart = t  # local t and not account for scr refresh
        Q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q1, 'tStartRefresh')  # time at next scr refresh
        Q1.setAutoDraw(True)
    if Q1.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q1.tStop = t  # not accounting for scr refresh
            Q1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q1, 'tStopRefresh')  # time at next scr refresh
            Q1.setAutoDraw(False)
    
    # *Q1_Slider* updates
    if Q1_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q1_Slider.frameNStart = frameN  # exact frame index
        Q1_Slider.tStart = t  # local t and not account for scr refresh
        Q1_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q1_Slider, 'tStartRefresh')  # time at next scr refresh
        Q1_Slider.setAutoDraw(True)
    if Q1_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q1_Slider.tStop = t  # not accounting for scr refresh
            Q1_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q1_Slider, 'tStopRefresh')  # time at next scr refresh
            Q1_Slider.setAutoDraw(False)
    
    # *Q2* updates
    if Q2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q2.frameNStart = frameN  # exact frame index
        Q2.tStart = t  # local t and not account for scr refresh
        Q2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q2, 'tStartRefresh')  # time at next scr refresh
        Q2.setAutoDraw(True)
    if Q2.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q2.tStop = t  # not accounting for scr refresh
            Q2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q2, 'tStopRefresh')  # time at next scr refresh
            Q2.setAutoDraw(False)
    
    # *Q2_Slider* updates
    if Q2_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q2_Slider.frameNStart = frameN  # exact frame index
        Q2_Slider.tStart = t  # local t and not account for scr refresh
        Q2_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q2_Slider, 'tStartRefresh')  # time at next scr refresh
        Q2_Slider.setAutoDraw(True)
    if Q2_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q2_Slider.tStop = t  # not accounting for scr refresh
            Q2_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q2_Slider, 'tStopRefresh')  # time at next scr refresh
            Q2_Slider.setAutoDraw(False)
    
    # *Q3* updates
    if Q3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q3.frameNStart = frameN  # exact frame index
        Q3.tStart = t  # local t and not account for scr refresh
        Q3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q3, 'tStartRefresh')  # time at next scr refresh
        Q3.setAutoDraw(True)
    if Q3.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q3.tStop = t  # not accounting for scr refresh
            Q3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q3, 'tStopRefresh')  # time at next scr refresh
            Q3.setAutoDraw(False)
    
    # *Q3_Slider* updates
    if Q3_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q3_Slider.frameNStart = frameN  # exact frame index
        Q3_Slider.tStart = t  # local t and not account for scr refresh
        Q3_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q3_Slider, 'tStartRefresh')  # time at next scr refresh
        Q3_Slider.setAutoDraw(True)
    if Q3_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q3_Slider.tStop = t  # not accounting for scr refresh
            Q3_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q3_Slider, 'tStopRefresh')  # time at next scr refresh
            Q3_Slider.setAutoDraw(False)
    
    # *Q4* updates
    if Q4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q4.frameNStart = frameN  # exact frame index
        Q4.tStart = t  # local t and not account for scr refresh
        Q4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q4, 'tStartRefresh')  # time at next scr refresh
        Q4.setAutoDraw(True)
    if Q4.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q4.tStop = t  # not accounting for scr refresh
            Q4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q4, 'tStopRefresh')  # time at next scr refresh
            Q4.setAutoDraw(False)
    
    # *Q4_Slider* updates
    if Q4_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q4_Slider.frameNStart = frameN  # exact frame index
        Q4_Slider.tStart = t  # local t and not account for scr refresh
        Q4_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q4_Slider, 'tStartRefresh')  # time at next scr refresh
        Q4_Slider.setAutoDraw(True)
    if Q4_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q4_Slider.tStop = t  # not accounting for scr refresh
            Q4_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q4_Slider, 'tStopRefresh')  # time at next scr refresh
            Q4_Slider.setAutoDraw(False)
    
    # *Q5* updates
    if Q5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q5.frameNStart = frameN  # exact frame index
        Q5.tStart = t  # local t and not account for scr refresh
        Q5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q5, 'tStartRefresh')  # time at next scr refresh
        Q5.setAutoDraw(True)
    if Q5.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q5.tStop = t  # not accounting for scr refresh
            Q5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q5, 'tStopRefresh')  # time at next scr refresh
            Q5.setAutoDraw(False)
    
    # *Q5_Slider* updates
    if Q5_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q5_Slider.frameNStart = frameN  # exact frame index
        Q5_Slider.tStart = t  # local t and not account for scr refresh
        Q5_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q5_Slider, 'tStartRefresh')  # time at next scr refresh
        Q5_Slider.setAutoDraw(True)
    if Q5_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q5_Slider.tStop = t  # not accounting for scr refresh
            Q5_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q5_Slider, 'tStopRefresh')  # time at next scr refresh
            Q5_Slider.setAutoDraw(False)
    
    # *Q6* updates
    if Q6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q6.frameNStart = frameN  # exact frame index
        Q6.tStart = t  # local t and not account for scr refresh
        Q6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q6, 'tStartRefresh')  # time at next scr refresh
        Q6.setAutoDraw(True)
    if Q6.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q6.tStop = t  # not accounting for scr refresh
            Q6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q6, 'tStopRefresh')  # time at next scr refresh
            Q6.setAutoDraw(False)
    
    # *Q6_Slider* updates
    if Q6_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q6_Slider.frameNStart = frameN  # exact frame index
        Q6_Slider.tStart = t  # local t and not account for scr refresh
        Q6_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q6_Slider, 'tStartRefresh')  # time at next scr refresh
        Q6_Slider.setAutoDraw(True)
    if Q6_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q6_Slider.tStop = t  # not accounting for scr refresh
            Q6_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q6_Slider, 'tStopRefresh')  # time at next scr refresh
            Q6_Slider.setAutoDraw(False)
    
    # *Q7* updates
    if Q7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q7.frameNStart = frameN  # exact frame index
        Q7.tStart = t  # local t and not account for scr refresh
        Q7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q7, 'tStartRefresh')  # time at next scr refresh
        Q7.setAutoDraw(True)
    if Q7.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q7.tStop = t  # not accounting for scr refresh
            Q7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q7, 'tStopRefresh')  # time at next scr refresh
            Q7.setAutoDraw(False)
    
    # *Q7_Slider* updates
    if Q7_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q7_Slider.frameNStart = frameN  # exact frame index
        Q7_Slider.tStart = t  # local t and not account for scr refresh
        Q7_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q7_Slider, 'tStartRefresh')  # time at next scr refresh
        Q7_Slider.setAutoDraw(True)
    if Q7_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q7_Slider.tStop = t  # not accounting for scr refresh
            Q7_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q7_Slider, 'tStopRefresh')  # time at next scr refresh
            Q7_Slider.setAutoDraw(False)
    
    # *Q8* updates
    if Q8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q8.frameNStart = frameN  # exact frame index
        Q8.tStart = t  # local t and not account for scr refresh
        Q8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q8, 'tStartRefresh')  # time at next scr refresh
        Q8.setAutoDraw(True)
    if Q8.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q8.tStop = t  # not accounting for scr refresh
            Q8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q8, 'tStopRefresh')  # time at next scr refresh
            Q8.setAutoDraw(False)
    
    # *Q8_Slider* updates
    if Q8_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q8_Slider.frameNStart = frameN  # exact frame index
        Q8_Slider.tStart = t  # local t and not account for scr refresh
        Q8_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q8_Slider, 'tStartRefresh')  # time at next scr refresh
        Q8_Slider.setAutoDraw(True)
    if Q8_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q8_Slider.tStop = t  # not accounting for scr refresh
            Q8_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q8_Slider, 'tStopRefresh')  # time at next scr refresh
            Q8_Slider.setAutoDraw(False)
    
    # *Q9* updates
    if Q9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q9.frameNStart = frameN  # exact frame index
        Q9.tStart = t  # local t and not account for scr refresh
        Q9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q9, 'tStartRefresh')  # time at next scr refresh
        Q9.setAutoDraw(True)
    if Q9.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q9.tStop = t  # not accounting for scr refresh
            Q9.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q9, 'tStopRefresh')  # time at next scr refresh
            Q9.setAutoDraw(False)
    
    # *Q9_Slider* updates
    if Q9_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q9_Slider.frameNStart = frameN  # exact frame index
        Q9_Slider.tStart = t  # local t and not account for scr refresh
        Q9_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q9_Slider, 'tStartRefresh')  # time at next scr refresh
        Q9_Slider.setAutoDraw(True)
    if Q9_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q9_Slider.tStop = t  # not accounting for scr refresh
            Q9_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q9_Slider, 'tStopRefresh')  # time at next scr refresh
            Q9_Slider.setAutoDraw(False)
    
    # *Q10* updates
    if Q10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q10.frameNStart = frameN  # exact frame index
        Q10.tStart = t  # local t and not account for scr refresh
        Q10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q10, 'tStartRefresh')  # time at next scr refresh
        Q10.setAutoDraw(True)
    if Q10.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q10.tStop = t  # not accounting for scr refresh
            Q10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q10, 'tStopRefresh')  # time at next scr refresh
            Q10.setAutoDraw(False)
    
    # *Q10_Slider* updates
    if Q10_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q10_Slider.frameNStart = frameN  # exact frame index
        Q10_Slider.tStart = t  # local t and not account for scr refresh
        Q10_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q10_Slider, 'tStartRefresh')  # time at next scr refresh
        Q10_Slider.setAutoDraw(True)
    if Q10_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q10_Slider.tStop = t  # not accounting for scr refresh
            Q10_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q10_Slider, 'tStopRefresh')  # time at next scr refresh
            Q10_Slider.setAutoDraw(False)
    
    # *Q11* updates
    if Q11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q11.frameNStart = frameN  # exact frame index
        Q11.tStart = t  # local t and not account for scr refresh
        Q11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q11, 'tStartRefresh')  # time at next scr refresh
        Q11.setAutoDraw(True)
    if Q11.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q11.tStop = t  # not accounting for scr refresh
            Q11.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q11, 'tStopRefresh')  # time at next scr refresh
            Q11.setAutoDraw(False)
    
    # *Q11_Slider* updates
    if Q11_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q11_Slider.frameNStart = frameN  # exact frame index
        Q11_Slider.tStart = t  # local t and not account for scr refresh
        Q11_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q11_Slider, 'tStartRefresh')  # time at next scr refresh
        Q11_Slider.setAutoDraw(True)
    if Q11_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q11_Slider.tStop = t  # not accounting for scr refresh
            Q11_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q11_Slider, 'tStopRefresh')  # time at next scr refresh
            Q11_Slider.setAutoDraw(False)
    
    # *Q12* updates
    if Q12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q12.frameNStart = frameN  # exact frame index
        Q12.tStart = t  # local t and not account for scr refresh
        Q12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q12, 'tStartRefresh')  # time at next scr refresh
        Q12.setAutoDraw(True)
    if Q12.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q12.tStop = t  # not accounting for scr refresh
            Q12.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q12, 'tStopRefresh')  # time at next scr refresh
            Q12.setAutoDraw(False)
    
    # *Q12_Slider* updates
    if Q12_Slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q12_Slider.frameNStart = frameN  # exact frame index
        Q12_Slider.tStart = t  # local t and not account for scr refresh
        Q12_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q12_Slider, 'tStartRefresh')  # time at next scr refresh
        Q12_Slider.setAutoDraw(True)
    if Q12_Slider.status == STARTED:
        if bool(Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating):
            # keep track of stop time/frame for later
            Q12_Slider.tStop = t  # not accounting for scr refresh
            Q12_Slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Q12_Slider, 'tStopRefresh')  # time at next scr refresh
            Q12_Slider.setAutoDraw(False)
    # *mouse_2* updates
    if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_2.frameNStart = frameN  # exact frame index
        mouse_2.tStart = t  # local t and not account for scr refresh
        mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
        mouse_2.status = STARTED
        mouse_2.mouseClock.reset()
        prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
    if mouse_2.status == STARTED:  # only update if started and not finished!
        buttons = mouse_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(Click_to_Continue_2)
                    clickableList = Click_to_Continue_2
                except:
                    clickableList = [Click_to_Continue_2]
                for obj in clickableList:
                    if obj.contains(mouse_2):
                        gotValidClick = True
                        mouse_2.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # *Click_to_Continue_2* updates
    if Click_to_Continue_2.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating and Q13_Slider.rating and Q14_Slider.rating and Q15_Slider.rating and Q16_Slider.rating and Q17_Slider.rating and Q18_Slider.rating and Q19_Slider.rating and Q20_Slider.rating and Q21_Slider.rating and Q22_Slider.rating and Q23_Slider.rating:
        # keep track of start time/frame for later
        Click_to_Continue_2.frameNStart = frameN  # exact frame index
        Click_to_Continue_2.tStart = t  # local t and not account for scr refresh
        Click_to_Continue_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Click_to_Continue_2, 'tStartRefresh')  # time at next scr refresh
        Click_to_Continue_2.setAutoDraw(True)
    
    # *Q13* updates
    if Q13.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q13.frameNStart = frameN  # exact frame index
        Q13.tStart = t  # local t and not account for scr refresh
        Q13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q13, 'tStartRefresh')  # time at next scr refresh
        Q13.setAutoDraw(True)
    
    # *Q13_Slider* updates
    if Q13_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q13_Slider.frameNStart = frameN  # exact frame index
        Q13_Slider.tStart = t  # local t and not account for scr refresh
        Q13_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q13_Slider, 'tStartRefresh')  # time at next scr refresh
        Q13_Slider.setAutoDraw(True)
    
    # *Q14* updates
    if Q14.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q14.frameNStart = frameN  # exact frame index
        Q14.tStart = t  # local t and not account for scr refresh
        Q14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q14, 'tStartRefresh')  # time at next scr refresh
        Q14.setAutoDraw(True)
    
    # *Q14_Slider* updates
    if Q14_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q14_Slider.frameNStart = frameN  # exact frame index
        Q14_Slider.tStart = t  # local t and not account for scr refresh
        Q14_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q14_Slider, 'tStartRefresh')  # time at next scr refresh
        Q14_Slider.setAutoDraw(True)
    
    # *Q15* updates
    if Q15.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q15.frameNStart = frameN  # exact frame index
        Q15.tStart = t  # local t and not account for scr refresh
        Q15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q15, 'tStartRefresh')  # time at next scr refresh
        Q15.setAutoDraw(True)
    
    # *Q15_Slider* updates
    if Q15_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q15_Slider.frameNStart = frameN  # exact frame index
        Q15_Slider.tStart = t  # local t and not account for scr refresh
        Q15_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q15_Slider, 'tStartRefresh')  # time at next scr refresh
        Q15_Slider.setAutoDraw(True)
    
    # *Q16* updates
    if Q16.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q16.frameNStart = frameN  # exact frame index
        Q16.tStart = t  # local t and not account for scr refresh
        Q16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q16, 'tStartRefresh')  # time at next scr refresh
        Q16.setAutoDraw(True)
    
    # *Q16_Slider* updates
    if Q16_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q16_Slider.frameNStart = frameN  # exact frame index
        Q16_Slider.tStart = t  # local t and not account for scr refresh
        Q16_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q16_Slider, 'tStartRefresh')  # time at next scr refresh
        Q16_Slider.setAutoDraw(True)
    
    # *Q17* updates
    if Q17.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q17.frameNStart = frameN  # exact frame index
        Q17.tStart = t  # local t and not account for scr refresh
        Q17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q17, 'tStartRefresh')  # time at next scr refresh
        Q17.setAutoDraw(True)
    
    # *Q17_Slider* updates
    if Q17_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q17_Slider.frameNStart = frameN  # exact frame index
        Q17_Slider.tStart = t  # local t and not account for scr refresh
        Q17_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q17_Slider, 'tStartRefresh')  # time at next scr refresh
        Q17_Slider.setAutoDraw(True)
    
    # *Q18* updates
    if Q18.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q18.frameNStart = frameN  # exact frame index
        Q18.tStart = t  # local t and not account for scr refresh
        Q18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q18, 'tStartRefresh')  # time at next scr refresh
        Q18.setAutoDraw(True)
    
    # *Q18_Slider* updates
    if Q18_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q18_Slider.frameNStart = frameN  # exact frame index
        Q18_Slider.tStart = t  # local t and not account for scr refresh
        Q18_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q18_Slider, 'tStartRefresh')  # time at next scr refresh
        Q18_Slider.setAutoDraw(True)
    
    # *Q19* updates
    if Q19.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q19.frameNStart = frameN  # exact frame index
        Q19.tStart = t  # local t and not account for scr refresh
        Q19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q19, 'tStartRefresh')  # time at next scr refresh
        Q19.setAutoDraw(True)
    
    # *Q19_Slider* updates
    if Q19_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q19_Slider.frameNStart = frameN  # exact frame index
        Q19_Slider.tStart = t  # local t and not account for scr refresh
        Q19_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q19_Slider, 'tStartRefresh')  # time at next scr refresh
        Q19_Slider.setAutoDraw(True)
    
    # *Q20* updates
    if Q20.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q20.frameNStart = frameN  # exact frame index
        Q20.tStart = t  # local t and not account for scr refresh
        Q20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q20, 'tStartRefresh')  # time at next scr refresh
        Q20.setAutoDraw(True)
    
    # *Q20_Slider* updates
    if Q20_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q20_Slider.frameNStart = frameN  # exact frame index
        Q20_Slider.tStart = t  # local t and not account for scr refresh
        Q20_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q20_Slider, 'tStartRefresh')  # time at next scr refresh
        Q20_Slider.setAutoDraw(True)
    
    # *Q21* updates
    if Q21.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q21.frameNStart = frameN  # exact frame index
        Q21.tStart = t  # local t and not account for scr refresh
        Q21.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q21, 'tStartRefresh')  # time at next scr refresh
        Q21.setAutoDraw(True)
    
    # *Q21_Slider* updates
    if Q21_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q21_Slider.frameNStart = frameN  # exact frame index
        Q21_Slider.tStart = t  # local t and not account for scr refresh
        Q21_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q21_Slider, 'tStartRefresh')  # time at next scr refresh
        Q21_Slider.setAutoDraw(True)
    
    # *Q22* updates
    if Q22.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q22.frameNStart = frameN  # exact frame index
        Q22.tStart = t  # local t and not account for scr refresh
        Q22.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q22, 'tStartRefresh')  # time at next scr refresh
        Q22.setAutoDraw(True)
    
    # *Q22_Slider* updates
    if Q22_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q22_Slider.frameNStart = frameN  # exact frame index
        Q22_Slider.tStart = t  # local t and not account for scr refresh
        Q22_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q22_Slider, 'tStartRefresh')  # time at next scr refresh
        Q22_Slider.setAutoDraw(True)
    
    # *Q23* updates
    if Q23.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q23.frameNStart = frameN  # exact frame index
        Q23.tStart = t  # local t and not account for scr refresh
        Q23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q23, 'tStartRefresh')  # time at next scr refresh
        Q23.setAutoDraw(True)
    
    # *Q23_Slider* updates
    if Q23_Slider.status == NOT_STARTED and Q1_Slider.rating and Q2_Slider.rating and Q3_Slider.rating and Q4_Slider.rating and Q5_Slider.rating and Q6_Slider.rating and Q7_Slider.rating and Q8_Slider.rating and Q9_Slider.rating and Q10_Slider.rating and Q11_Slider.rating and Q12_Slider.rating:
        # keep track of start time/frame for later
        Q23_Slider.frameNStart = frameN  # exact frame index
        Q23_Slider.tStart = t  # local t and not account for scr refresh
        Q23_Slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q23_Slider, 'tStartRefresh')  # time at next scr refresh
        Q23_Slider.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Survey_TrialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Survey_Trial"-------
for thisComponent in Survey_TrialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Q1_Slider.response', Q1_Slider.getRating())
thisExp.addData('Q2_Slider.response', Q2_Slider.getRating())
thisExp.addData('Q3_Slider.response', Q3_Slider.getRating())
thisExp.addData('Q4_Slider.response', Q4_Slider.getRating())
thisExp.addData('Q5_Slider.response', Q5_Slider.getRating())
thisExp.addData('Q6_Slider.response', Q6_Slider.getRating())
thisExp.addData('Q7_Slider.response', Q7_Slider.getRating())
thisExp.addData('Q8_Slider.response', Q8_Slider.getRating())
thisExp.addData('Q9_Slider.response', Q9_Slider.getRating())
thisExp.addData('Q10_Slider.response', Q10_Slider.getRating())
thisExp.addData('Q11_Slider.response', Q11_Slider.getRating())
thisExp.addData('Q12_Slider.response', Q12_Slider.getRating())
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
thisExp.addData('Q13_Slider.response', Q13_Slider.getRating())
thisExp.addData('Q14_Slider.response', Q14_Slider.getRating())
thisExp.addData('Q15_Slider.response', Q15_Slider.getRating())
thisExp.addData('Q16_Slider.response', Q16_Slider.getRating())
thisExp.addData('Q17_Slider.response', Q17_Slider.getRating())
thisExp.addData('Q18_Slider.response', Q18_Slider.getRating())
thisExp.addData('Q19_Slider.response', Q19_Slider.getRating())
thisExp.addData('Q20_Slider.response', Q20_Slider.getRating())
thisExp.addData('Q21_Slider.response', Q21_Slider.getRating())
thisExp.addData('Q22_Slider.response', Q22_Slider.getRating())
thisExp.addData('Q23_Slider.response', Q23_Slider.getRating())
# the Routine "Survey_Trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "thanks"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [end_Txt]
for thisComponent in thanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
thanksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=thanksClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_Txt* updates
    if end_Txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_Txt.frameNStart = frameN  # exact frame index
        end_Txt.tStart = t  # local t and not account for scr refresh
        end_Txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_Txt, 'tStartRefresh')  # time at next scr refresh
        end_Txt.setAutoDraw(True)
    if end_Txt.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_Txt.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            end_Txt.tStop = t  # not accounting for scr refresh
            end_Txt.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_Txt, 'tStopRefresh')  # time at next scr refresh
            end_Txt.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('end_Txt.started', end_Txt.tStartRefresh)
thisExp.addData('end_Txt.stopped', end_Txt.tStopRefresh)
outlet.push_sample(x=[0])
outlet.push_sample(x=[0])
outlet.push_sample(x=[0])
outlet.push_sample(x=[0])

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
