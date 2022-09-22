#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on September 22, 2022, at 10:44
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, parallel
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code_17
import serial
import time
import threading

Connected = True
PulseWidth = 0.01

def ReadThread(port):
    while Connected:
        if port.inWaiting() > 0:
            print ("0x%X"%ord(port.read(1)))

# Open the Windows device manager, search for the "TriggerBox VirtualSerial Port (COM6)"
# in "Ports /COM & LPT)" and enter the COM port number in the constructor.
#port = serial.Serial('COM3')

# Start the read thread
#thread = threading.Thread(target=ReadThread, args=(port,))
#thread.start()

# Set the port to an initial state
#port.write([0x00])
#time.sleep(PulseWidth)

def send_the_code(code):
    print(code)



# Run 'Before Experiment' code from code_22
send_the_code(1)

# Run 'Before Experiment' code from code_23
send_the_code(2)



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'test9'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
# --- Show participant info dialog --
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
    originPath='C:\\Psychopy\\Tasks\\Nback\\test9_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "i_eoec" ---
key_resp_3 = keyboard.Keyboard()
text_4 = visual.TextStim(win=win, name='text_4',
    text='This experiment is about thoughts and feelings that you may experience during rest. \n\nYou will be asked to relax with your eyes open for 3 minutes, then closed for 3 minutes.\n\nRelax, move as little as possible and try not to fall asleep. \n\nWhen the time is up, you will be presented with statements on the computer about thoughts and feelings that you may have experienced. Your task is then to indicate the extent to which you agree with the given statements on a scale from "Completely disagree (--)" to "Completely agree (++). If you have any questions about the experiment, please ask them now."\n',
    font='Open Sans',
    pos=(0, 0), height=0.033, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()
h_eoec = visual.TextStim(win=win, name='h_eoec',
    text='EOEC',
    font='Open Sans',
    pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "oci" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "oc" ---
text_8 = visual.TextStim(win=win, name='text_8',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_10 = keyboard.Keyboard()

# --- Initialize components for Routine "w" ---
img_whte = visual.ImageStim(
    win=win,
    name='img_whte', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "b" ---
img_black = visual.ImageStim(
    win=win,
    name='img_black', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "i_arsq" ---
text_5 = visual.TextStim(win=win, name='text_5',
    text='Now follows a number of statements about possible feelings, physical sensations and thoughts during the eyes-closed rest period.\n\nPlease, indicate the extent to which you agree with each statement using the mouse.\n\nPress any key to continue.\n',
    font='Open Sans',
    pos=(0, 0), height=0.0333, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
h_arsq = visual.TextStim(win=win, name='h_arsq',
    text='ARSQ',
    font='Open Sans',
    pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "question" ---
slider = visual.Slider(win=win, name='slider',
    startValue=None, size=(1.0, 0.05), pos=(0, -0.2), units=None,
    labels=('--\nfully disagree','-','0\nneutral','+','++\nfully agree'), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.04,
    flip=False, ori=0.0, depth=0, readOnly=False)
text = visual.TextStim(win=win, name='text',
    text='',
    font='Open Sans',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_9 = keyboard.Keyboard()

# --- Initialize components for Routine "i_nback" ---
instrText = visual.TextStim(win=win, name='instrText',
    text=None,
    font='Arial',
    pos=(-0.3,0), height=0.045, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
h_nback = visual.TextStim(win=win, name='h_nback',
    text=None,
    font='Arial',
    pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);
instrResp = keyboard.Keyboard()
instrImg = visual.ImageStim(
    win=win,
    name='instrImg', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "nb_trail" ---
trialResp = keyboard.Keyboard()
trialSquare = visual.Rect(
    win=win, name='trialSquare',
    width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1.0, depth=-1.0, interpolate=True)
trialFix = visual.TextStim(win=win, name='trialFix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=0.0, 
    languageStyle='LTR',
    depth=-2.0);
# Run 'Begin Experiment' code from trialCode
gridColor = [1,1,1]
play_sounds=False
provide_color_feedback=False
mySound_goed = sound.Sound('sounds/goed.wav')
mySound_fout= sound.Sound('sounds/fout.wav')
gridLine1 = visual.Rect(
    win=win, name='gridLine1',
    width=(0.6, 0.001)[0], height=(0.6, 0.001)[1],
    ori=0.0, pos=(0, 0.3), anchor='center',
    lineWidth=1.5,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-4.0, interpolate=True)
gridLine2 = visual.Rect(
    win=win, name='gridLine2',
    width=(0.6, 0.001)[0], height=(0.6, 0.001)[1],
    ori=0.0, pos=(0, 0.096), anchor='center',
    lineWidth=1.5,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-5.0, interpolate=True)
gridLine3 = visual.Rect(
    win=win, name='gridLine3',
    width=(0.6, 0.001)[0], height=(0.6, 0.001)[1],
    ori=0.0, pos=(0, -0.096), anchor='center',
    lineWidth=1.5,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-6.0, interpolate=True)
gridLine4 = visual.Rect(
    win=win, name='gridLine4',
    width=(0.6, 0.001)[0], height=(0.6, 0.001)[1],
    ori=0.0, pos=(0, -0.3), anchor='center',
    lineWidth=1.5,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-7.0, interpolate=True)
gridLine5 = visual.Rect(
    win=win, name='gridLine5',
    width=(0.6, 0.001)[0], height=(0.6, 0.001)[1],
    ori=90.0, pos=(-0.3, 0), anchor='center',
    lineWidth=1.5,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-8.0, interpolate=True)
gridLine6 = visual.Rect(
    win=win, name='gridLine6',
    width=(0.6, 0.001)[0], height=(0.6, 0.001)[1],
    ori=90.0, pos=(-0.096, 0), anchor='center',
    lineWidth=1.5,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-9.0, interpolate=True)
gridLine7 = visual.Rect(
    win=win, name='gridLine7',
    width=(0.6, 0.001)[0], height=(0.6, 0.001)[1],
    ori=90.0, pos=(0.096, 0), anchor='center',
    lineWidth=1.5,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-10.0, interpolate=True)
gridLine8 = visual.Rect(
    win=win, name='gridLine8',
    width=(0.6, 0.001)[0], height=(0.6, 0.001)[1],
    ori=90.0, pos=(0.3, 0), anchor='center',
    lineWidth=1.5,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-11.0, interpolate=True)

# --- Initialize components for Routine "nb_end" ---
endText = visual.TextStim(win=win, name='endText',
    text='This is the end this part of the experiment. Thank you for your time.\n\nif this is the first session, now the environmental conditions will be changed.\n\nif this is the second session, we now follow up with a movie.',
    font='Open Sans',
    pos=(0, 0), height=0.033, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# --- Initialize components for Routine "i_movie" ---
text_6 = visual.TextStim(win=win, name='text_6',
    text='Information about Movie',
    font='Open Sans',
    pos=(0, 0), height=0.03333, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()
h_movie = visual.TextStim(win=win, name='h_movie',
    text='Movie',
    font='Open Sans',
    pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "showmovie" ---
key_resp_8 = keyboard.Keyboard()
movie = visual.MovieStim3(
    win=win, name='movie', units='',
    noAudio = False,
    filename='movies/Jack_and_the_Beanstalk_512kb.mp4',
    ori=0.0, pos=(0, 0), opacity=None,
    loop=False, anchor='center',
    size=(0.5, 0.5),
    depth=-1.0,
    )

# --- Initialize components for Routine "the_end" ---
text_7 = visual.TextStim(win=win, name='text_7',
    text='This is the end of this run. Thank you!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "i_eoec" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# setup some python lists for storing info about the mouse_2
gotValidClick = False  # until a click is received
# keep track of which components have finished
i_eoecComponents = [key_resp_3, text_4, mouse_2, h_eoec]
for thisComponent in i_eoecComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "i_eoec" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_3.started')
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['y','n','left','right','space','c','s'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_4.started')
        text_4.setAutoDraw(True)
    # *mouse_2* updates
    if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_2.frameNStart = frameN  # exact frame index
        mouse_2.tStart = t  # local t and not account for scr refresh
        mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mouse_2.started', t)
        mouse_2.status = STARTED
        mouse_2.mouseClock.reset()
        prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
    if mouse_2.status == STARTED:  # only update if started and not finished!
        buttons = mouse_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False  # abort routine on response    
    # *h_eoec* updates
    if h_eoec.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        h_eoec.frameNStart = frameN  # exact frame index
        h_eoec.tStart = t  # local t and not account for scr refresh
        h_eoec.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(h_eoec, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'h_eoec.started')
        h_eoec.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in i_eoecComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "i_eoec" ---
for thisComponent in i_eoecComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
x, y = mouse_2.getPos()
buttons = mouse_2.getPressed()
thisExp.addData('mouse_2.x', x)
thisExp.addData('mouse_2.y', y)
thisExp.addData('mouse_2.leftButton', buttons[0])
thisExp.addData('mouse_2.midButton', buttons[1])
thisExp.addData('mouse_2.rightButton', buttons[2])
thisExp.nextEntry()
# Run 'End Routine' code from code_3
skip_this_routine=False

if key_resp_3.keys is not None:
    if 's' == key_resp_3.keys:
        skip_this_routine=True
    
# print(key_resp_3.keys)
# print('c' in key_resp_3.keys)
# the Routine "i_eoec" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
eoecloop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('csv/eoc.csv'),
    seed=None, name='eoecloop')
thisExp.addLoop(eoecloop)  # add the loop to the experiment
thisEoecloop = eoecloop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEoecloop.rgb)
if thisEoecloop != None:
    for paramName in thisEoecloop:
        exec('{} = thisEoecloop[paramName]'.format(paramName))

for thisEoecloop in eoecloop:
    currentLoop = eoecloop
    # abbreviate parameter names if possible (e.g. rgb = thisEoecloop.rgb)
    if thisEoecloop != None:
        for paramName in thisEoecloop:
            exec('{} = thisEoecloop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "oci" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    text_2.setText(eocinstr)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # Run 'Begin Routine' code from code_4
    if skip_this_routine:
        continueRoutine=False
    # Run 'Begin Routine' code from code_17
    send_the_code(eocmarker1)
    
    # keep track of which components have finished
    ociComponents = [text_2, key_resp]
    for thisComponent in ociComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "oci" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.started')
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.stopped')
                text_2.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.stopped')
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['s'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ociComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "oci" ---
    for thisComponent in ociComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    eoecloop.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        eoecloop.addData('key_resp.rt', key_resp.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
    # --- Prepare to start Routine "oc" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp_10.keys = []
    key_resp_10.rt = []
    _key_resp_10_allKeys = []
    # Run 'Begin Routine' code from code_20
    if skip_this_routine:
        continueRoutine=False
    # Run 'Begin Routine' code from code_21
    send_the_code(eocmarker3)
    
    # keep track of which components have finished
    ocComponents = [text_8, key_resp_10]
    for thisComponent in ocComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "oc" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_8.started')
            text_8.setAutoDraw(True)
        if text_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_8.tStartRefresh + 180-frameTolerance:
                # keep track of stop time/frame for later
                text_8.tStop = t  # not accounting for scr refresh
                text_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_8.stopped')
                text_8.setAutoDraw(False)
        
        # *key_resp_10* updates
        waitOnFlip = False
        if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_10.frameNStart = frameN  # exact frame index
            key_resp_10.tStart = t  # local t and not account for scr refresh
            key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_10.started')
            key_resp_10.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_10.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_10.getKeys(keyList=['s'], waitRelease=False)
            _key_resp_10_allKeys.extend(theseKeys)
            if len(_key_resp_10_allKeys):
                key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
                key_resp_10.rt = _key_resp_10_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ocComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "oc" ---
    for thisComponent in ocComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_10.keys in ['', [], None]:  # No response was made
        key_resp_10.keys = None
    eoecloop.addData('key_resp_10.keys',key_resp_10.keys)
    if key_resp_10.keys != None:  # we had a response
        eoecloop.addData('key_resp_10.rt', key_resp_10.rt)
    # the Routine "oc" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'eoecloop'


# set up handler to look after randomisation of conditions etc
wakeup = data.TrialHandler(nReps=4.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='wakeup')
thisExp.addLoop(wakeup)  # add the loop to the experiment
thisWakeup = wakeup.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisWakeup.rgb)
if thisWakeup != None:
    for paramName in thisWakeup:
        exec('{} = thisWakeup[paramName]'.format(paramName))

for thisWakeup in wakeup:
    currentLoop = wakeup
    # abbreviate parameter names if possible (e.g. rgb = thisWakeup.rgb)
    if thisWakeup != None:
        for paramName in thisWakeup:
            exec('{} = thisWakeup[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "w" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code
    win.color=[-1, -1, -1]
    if skip_this_routine:
        continueRoutine=False
    # Run 'Begin Routine' code from code_19
    # Set Bit 0, Pin 2 of the Output(to Amp) connector
    #port.write([100])
    #time.sleep(PulseWidth)
    
    # Reset Bit 0, Pin 2 of the Output(to Amp) connector
    #port.write([0x00])
    #time.sleep(PulseWidth)
    
    # keep track of which components have finished
    wComponents = [img_whte]
    for thisComponent in wComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "w" ---
    while continueRoutine and routineTimer.getTime() < 0.2:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *img_whte* updates
        if img_whte.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            img_whte.frameNStart = frameN  # exact frame index
            img_whte.tStart = t  # local t and not account for scr refresh
            img_whte.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(img_whte, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'img_whte.started')
            img_whte.setAutoDraw(True)
        if img_whte.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > img_whte.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                img_whte.tStop = t  # not accounting for scr refresh
                img_whte.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'img_whte.stopped')
                img_whte.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "w" ---
    for thisComponent in wComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    win.color=[0, 0, 0]
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.200000)
    
    # --- Prepare to start Routine "b" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_2
    win.color=[1, 1, 1]
    if skip_this_routine:
        continueRoutine=False
    # keep track of which components have finished
    bComponents = [img_black]
    for thisComponent in bComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "b" ---
    while continueRoutine and routineTimer.getTime() < 0.2:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *img_black* updates
        if img_black.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            img_black.frameNStart = frameN  # exact frame index
            img_black.tStart = t  # local t and not account for scr refresh
            img_black.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(img_black, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'img_black.started')
            img_black.setAutoDraw(True)
        if img_black.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > img_black.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                img_black.tStop = t  # not accounting for scr refresh
                img_black.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'img_black.stopped')
                img_black.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in bComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "b" ---
    for thisComponent in bComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_2
    win.color=[0, 0, 0]
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.200000)
    thisExp.nextEntry()
    
# completed 4.0 repeats of 'wakeup'


# --- Prepare to start Routine "i_arsq" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# setup some python lists for storing info about the mouse
gotValidClick = False  # until a click is received
# keep track of which components have finished
i_arsqComponents = [text_5, key_resp_4, mouse, h_arsq]
for thisComponent in i_arsqComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "i_arsq" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_5.started')
        text_5.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_4.started')
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['y','n','left','right','space','c','s'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # *mouse* updates
    if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse.frameNStart = frameN  # exact frame index
        mouse.tStart = t  # local t and not account for scr refresh
        mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mouse.started', t)
        mouse.status = STARTED
        mouse.mouseClock.reset()
        prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
    if mouse.status == STARTED:  # only update if started and not finished!
        buttons = mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False  # abort routine on response    
    # *h_arsq* updates
    if h_arsq.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        h_arsq.frameNStart = frameN  # exact frame index
        h_arsq.tStart = t  # local t and not account for scr refresh
        h_arsq.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(h_arsq, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'h_arsq.started')
        h_arsq.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in i_arsqComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "i_arsq" ---
for thisComponent in i_arsqComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
x, y = mouse.getPos()
buttons = mouse.getPressed()
thisExp.addData('mouse.x', x)
thisExp.addData('mouse.y', y)
thisExp.addData('mouse.leftButton', buttons[0])
thisExp.addData('mouse.midButton', buttons[1])
thisExp.addData('mouse.rightButton', buttons[2])
thisExp.nextEntry()
# Run 'End Routine' code from code_6
skip_this_routine=False

if key_resp_4.keys is not None:
    if 's' == key_resp_4.keys:
        skip_this_routine=True
    
# the Routine "i_arsq" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
questions = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('csv/questions_english.csv'),
    seed=None, name='questions')
thisExp.addLoop(questions)  # add the loop to the experiment
thisQuestion = questions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisQuestion.rgb)
if thisQuestion != None:
    for paramName in thisQuestion:
        exec('{} = thisQuestion[paramName]'.format(paramName))

for thisQuestion in questions:
    currentLoop = questions
    # abbreviate parameter names if possible (e.g. rgb = thisQuestion.rgb)
    if thisQuestion != None:
        for paramName in thisQuestion:
            exec('{} = thisQuestion[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "question" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    slider.reset()
    text.setText(itemtext)
    # Run 'Begin Routine' code from code_7
    if skip_this_routine:
        continueRoutine=False
    key_resp_9.keys = []
    key_resp_9.rt = []
    _key_resp_9_allKeys = []
    # Run 'Begin Routine' code from code_24
    send_the_code(itemnumber + 100)
    # keep track of which components have finished
    questionComponents = [slider, text, key_resp_9]
    for thisComponent in questionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "question" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *slider* updates
        if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider.frameNStart = frameN  # exact frame index
            slider.tStart = t  # local t and not account for scr refresh
            slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider.started')
            slider.setAutoDraw(True)
        
        # Check slider for response to end routine
        if slider.getRating() is not None and slider.status == STARTED:
            continueRoutine = False
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            text.setAutoDraw(True)
        # Run 'Each Frame' code from code_9
        if slider.getRT() is not None:
            response_time = slider.getRT()
        
        # *key_resp_9* updates
        waitOnFlip = False
        if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_9.frameNStart = frameN  # exact frame index
            key_resp_9.tStart = t  # local t and not account for scr refresh
            key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_9.started')
            key_resp_9.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_9.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_9.getKeys(keyList=['s'], waitRelease=False)
            _key_resp_9_allKeys.extend(theseKeys)
            if len(_key_resp_9_allKeys):
                key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
                key_resp_9.rt = _key_resp_9_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in questionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "question" ---
    for thisComponent in questionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    questions.addData('slider.response', slider.getRating())
    questions.addData('slider.rt', slider.getRT())
    # Run 'End Routine' code from code_10
    if not skip_this_routine:
        
        # send the response code plz
        send_the_code(slider.getRating())
        
        ISI = core.StaticPeriod()
        ISI.start(0.2)  # start a period of 0.5s
        # stim.image = 'largeFile.bmp'  # could take some time
        ISI.complete()  # finish the 0.5s, taking into account one 60Hz frame
    # check responses
    if key_resp_9.keys in ['', [], None]:  # No response was made
        key_resp_9.keys = None
    questions.addData('key_resp_9.keys',key_resp_9.keys)
    if key_resp_9.keys != None:  # we had a response
        questions.addData('key_resp_9.rt', key_resp_9.rt)
    # Run 'End Routine' code from code_16
    if key_resp_9.keys is not None:
        if 's' == key_resp_9.keys:
            skip_this_routine=True
            break
            
    # the Routine "question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'questions'


# set up handler to look after randomisation of conditions etc
nb_taskloop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('taskCond.xlsx'),
    seed=None, name='nb_taskloop')
thisExp.addLoop(nb_taskloop)  # add the loop to the experiment
thisNb_taskloop = nb_taskloop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNb_taskloop.rgb)
if thisNb_taskloop != None:
    for paramName in thisNb_taskloop:
        exec('{} = thisNb_taskloop[paramName]'.format(paramName))

for thisNb_taskloop in nb_taskloop:
    currentLoop = nb_taskloop
    # abbreviate parameter names if possible (e.g. rgb = thisNb_taskloop.rgb)
    if thisNb_taskloop != None:
        for paramName in thisNb_taskloop:
            exec('{} = thisNb_taskloop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "i_nback" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    instrText.setText('')
    h_nback.setText('')
    instrResp.keys = []
    instrResp.rt = []
    _instrResp_allKeys = []
    instrImg.setPos((0, 0))
    # Run 'Begin Routine' code from instrCode
    # set the header with and f-string:
    h_nback.text = f'{nbackInstruction } BACK'
    
    if condsFile == "nBack1Cond.xlsx":
        instrImg.pos = (0.5, -0.3)
        instrImg.image = '1back.png'
        instrText.text = "In this task you will be required to press ‘space’ if the white square appeared in the same location as the location on the last trial. For example if the square was in the left down corner on trial 1 and then it appeared in the same location on trial 2, press ‘space’. Otherwise, do not respond. Press ‘c’ to continue."
    elif condsFile == "nBack2Cond.xlsx":
        instrImg.pos = (0.5, -0.15)
        instrImg.image = '2back.png'
        instrText.text = "This is the end of 1-back trials. You are about to start 2-back trials. This means that instead of pressing ‘space’ whenever the square appears in the same position as on the position on one trial before, you are required to press ‘space’ whenever the square appears in the same position as on the position two trials before. For example if the square appeared in left down corner on trial 1, you should press ‘space’ if the square appears in the left down corner on trial 3. Press ‘c’ to continue."
    elif condsFile == "nBack3Cond.xlsx":
        instrImg.pos = (0.5, 0)
        instrImg.image = '3back.png'
        instrText.text = "This is the end of 2-back trials. You are about to start 3-back trials. This means that instead of pressing ‘space’ whenever the square appears in the same position as on the position on two trials before, you are required to press ‘space’ whenever the square appears in the same position as on the position three trials before. For example if the square appeared in left down corner on trial 1, you should press ‘space’ if the square appears in the left down corner on trial 4. Press ‘c’ to continue."
    else: 
        instrImg.pos = (0.5, 0)
        instrImg.image = '3back.png'
        instrText.text = "This is the end of 2-back trials. You are about to start 3-back trials. This means that instead of pressing ‘space’ whenever the square appears in the same position as on the position on two trials before, you are required to press ‘space’ whenever the square appears in the same position as on the position three trials before. For example if the square appeared in left down corner on trial 1, you should press ‘space’ if the square appears in the left down corner on trial 4. Press ‘c’ to continue."
    # Run 'Begin Routine' code from code_11
    # continueRoutine=True
    # skip_this_routine=False
    
    # Run 'Begin Routine' code from code_25
    send_the_code(nbackInstruction + 50 + 2)
    # keep track of which components have finished
    i_nbackComponents = [instrText, h_nback, instrResp, instrImg]
    for thisComponent in i_nbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "i_nback" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instrText* updates
        if instrText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instrText.frameNStart = frameN  # exact frame index
            instrText.tStart = t  # local t and not account for scr refresh
            instrText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instrText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instrText.started')
            instrText.setAutoDraw(True)
        
        # *h_nback* updates
        if h_nback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            h_nback.frameNStart = frameN  # exact frame index
            h_nback.tStart = t  # local t and not account for scr refresh
            h_nback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(h_nback, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'h_nback.started')
            h_nback.setAutoDraw(True)
        
        # *instrResp* updates
        waitOnFlip = False
        if instrResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instrResp.frameNStart = frameN  # exact frame index
            instrResp.tStart = t  # local t and not account for scr refresh
            instrResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instrResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instrResp.started')
            instrResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instrResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instrResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instrResp.status == STARTED and not waitOnFlip:
            theseKeys = instrResp.getKeys(keyList=['c','s'], waitRelease=False)
            _instrResp_allKeys.extend(theseKeys)
            if len(_instrResp_allKeys):
                instrResp.keys = _instrResp_allKeys[-1].name  # just the last key pressed
                instrResp.rt = _instrResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *instrImg* updates
        if instrImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instrImg.frameNStart = frameN  # exact frame index
            instrImg.tStart = t  # local t and not account for scr refresh
            instrImg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instrImg, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instrImg.started')
            instrImg.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in i_nbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "i_nback" ---
    for thisComponent in i_nbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_11
    skip_this_routine=False
    
    if instrResp.keys is not None:
        if 's' == instrResp.keys:
            skip_this_routine=True
        
    # print(key_resp_3.keys)
    # print('c' in key_resp_3.keys)
    # the Routine "i_nback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    nb_trials = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(condsFile),
        seed=None, name='nb_trials')
    thisExp.addLoop(nb_trials)  # add the loop to the experiment
    thisNb_trial = nb_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisNb_trial.rgb)
    if thisNb_trial != None:
        for paramName in thisNb_trial:
            exec('{} = thisNb_trial[paramName]'.format(paramName))
    
    for thisNb_trial in nb_trials:
        currentLoop = nb_trials
        # abbreviate parameter names if possible (e.g. rgb = thisNb_trial.rgb)
        if thisNb_trial != None:
            for paramName in thisNb_trial:
                exec('{} = thisNb_trial[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "nb_trail" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        trialResp.keys = []
        trialResp.rt = []
        _trialResp_allKeys = []
        trialSquare.setPos((loc1, loc2))
        # Run 'Begin Routine' code from trialCode
        gridColor = [1,1,1]
        sound_playing=False
        nback_trig_sent=False
        # Run 'Begin Routine' code from code_12
        if skip_this_routine:
            continueRoutine=False
            break
        # Run 'Begin Routine' code from code_26
        send_the_code(200+trialsNum)
        # keep track of which components have finished
        nb_trailComponents = [trialResp, trialSquare, trialFix, gridLine1, gridLine2, gridLine3, gridLine4, gridLine5, gridLine6, gridLine7, gridLine8]
        for thisComponent in nb_trailComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "nb_trail" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *trialResp* updates
            waitOnFlip = False
            if trialResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialResp.frameNStart = frameN  # exact frame index
                trialResp.tStart = t  # local t and not account for scr refresh
                trialResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialResp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trialResp.started')
                trialResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(trialResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(trialResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if trialResp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trialResp.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    trialResp.tStop = t  # not accounting for scr refresh
                    trialResp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'trialResp.stopped')
                    trialResp.status = FINISHED
            if trialResp.status == STARTED and not waitOnFlip:
                theseKeys = trialResp.getKeys(keyList=['space','s'], waitRelease=False)
                _trialResp_allKeys.extend(theseKeys)
                if len(_trialResp_allKeys):
                    trialResp.keys = _trialResp_allKeys[-1].name  # just the last key pressed
                    trialResp.rt = _trialResp_allKeys[-1].rt
            
            # *trialSquare* updates
            if trialSquare.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialSquare.frameNStart = frameN  # exact frame index
                trialSquare.tStart = t  # local t and not account for scr refresh
                trialSquare.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialSquare, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trialSquare.started')
                trialSquare.setAutoDraw(True)
            if trialSquare.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trialSquare.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    trialSquare.tStop = t  # not accounting for scr refresh
                    trialSquare.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'trialSquare.stopped')
                    trialSquare.setAutoDraw(False)
            
            # *trialFix* updates
            if trialFix.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                trialFix.frameNStart = frameN  # exact frame index
                trialFix.tStart = t  # local t and not account for scr refresh
                trialFix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialFix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trialFix.started')
                trialFix.setAutoDraw(True)
            if trialFix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trialFix.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    trialFix.tStop = t  # not accounting for scr refresh
                    trialFix.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'trialFix.stopped')
                    trialFix.setAutoDraw(False)
            # Run 'Each Frame' code from trialCode
            if corrAns == 'space' and (trialResp.keys == 'space'):
                
                if not nback_trig_sent:
                    send_the_code(200 + trialsNum + 10)
                    nback_trig_sent=True
                if provide_color_feedback:
                    gridColor = [-1.000,1.000,-1.000]
                    
                if not sound_playing and play_sounds:
                    sound_playing=True
                    mySound_goed.volume=0.6
                    mySound_goed.play()
                    
                    
            if not(corrAns == 'space') and (trialResp.keys == 'space'):
                
                if not nback_trig_sent:
            
                    send_the_code(200 + trialsNum + 11)
                    nback_trig_sent=True
                
                if provide_color_feedback:
                    gridColor = [1.000,-1.000,-1.000]
                    
                if not sound_playing and play_sounds:
                    sound_playing=True
                    mySound_fout.volume=1
                    mySound_fout.play()
                    
                    
            
            
            # *gridLine1* updates
            if gridLine1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                gridLine1.frameNStart = frameN  # exact frame index
                gridLine1.tStart = t  # local t and not account for scr refresh
                gridLine1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(gridLine1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'gridLine1.started')
                gridLine1.setAutoDraw(True)
            if gridLine1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > gridLine1.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    gridLine1.tStop = t  # not accounting for scr refresh
                    gridLine1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'gridLine1.stopped')
                    gridLine1.setAutoDraw(False)
            if gridLine1.status == STARTED:  # only update if drawing
                gridLine1.setFillColor(gridColor, log=False)
                gridLine1.setLineColor(gridColor, log=False)
            
            # *gridLine2* updates
            if gridLine2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                gridLine2.frameNStart = frameN  # exact frame index
                gridLine2.tStart = t  # local t and not account for scr refresh
                gridLine2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(gridLine2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'gridLine2.started')
                gridLine2.setAutoDraw(True)
            if gridLine2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > gridLine2.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    gridLine2.tStop = t  # not accounting for scr refresh
                    gridLine2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'gridLine2.stopped')
                    gridLine2.setAutoDraw(False)
            if gridLine2.status == STARTED:  # only update if drawing
                gridLine2.setFillColor(gridColor, log=False)
                gridLine2.setLineColor(gridColor, log=False)
            
            # *gridLine3* updates
            if gridLine3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                gridLine3.frameNStart = frameN  # exact frame index
                gridLine3.tStart = t  # local t and not account for scr refresh
                gridLine3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(gridLine3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'gridLine3.started')
                gridLine3.setAutoDraw(True)
            if gridLine3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > gridLine3.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    gridLine3.tStop = t  # not accounting for scr refresh
                    gridLine3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'gridLine3.stopped')
                    gridLine3.setAutoDraw(False)
            if gridLine3.status == STARTED:  # only update if drawing
                gridLine3.setFillColor(gridColor, log=False)
                gridLine3.setLineColor(gridColor, log=False)
            
            # *gridLine4* updates
            if gridLine4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                gridLine4.frameNStart = frameN  # exact frame index
                gridLine4.tStart = t  # local t and not account for scr refresh
                gridLine4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(gridLine4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'gridLine4.started')
                gridLine4.setAutoDraw(True)
            if gridLine4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > gridLine4.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    gridLine4.tStop = t  # not accounting for scr refresh
                    gridLine4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'gridLine4.stopped')
                    gridLine4.setAutoDraw(False)
            if gridLine4.status == STARTED:  # only update if drawing
                gridLine4.setFillColor(gridColor, log=False)
                gridLine4.setLineColor(gridColor, log=False)
            
            # *gridLine5* updates
            if gridLine5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                gridLine5.frameNStart = frameN  # exact frame index
                gridLine5.tStart = t  # local t and not account for scr refresh
                gridLine5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(gridLine5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'gridLine5.started')
                gridLine5.setAutoDraw(True)
            if gridLine5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > gridLine5.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    gridLine5.tStop = t  # not accounting for scr refresh
                    gridLine5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'gridLine5.stopped')
                    gridLine5.setAutoDraw(False)
            if gridLine5.status == STARTED:  # only update if drawing
                gridLine5.setFillColor(gridColor, log=False)
                gridLine5.setLineColor(gridColor, log=False)
            
            # *gridLine6* updates
            if gridLine6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                gridLine6.frameNStart = frameN  # exact frame index
                gridLine6.tStart = t  # local t and not account for scr refresh
                gridLine6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(gridLine6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'gridLine6.started')
                gridLine6.setAutoDraw(True)
            if gridLine6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > gridLine6.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    gridLine6.tStop = t  # not accounting for scr refresh
                    gridLine6.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'gridLine6.stopped')
                    gridLine6.setAutoDraw(False)
            if gridLine6.status == STARTED:  # only update if drawing
                gridLine6.setFillColor(gridColor, log=False)
                gridLine6.setLineColor(gridColor, log=False)
            
            # *gridLine7* updates
            if gridLine7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                gridLine7.frameNStart = frameN  # exact frame index
                gridLine7.tStart = t  # local t and not account for scr refresh
                gridLine7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(gridLine7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'gridLine7.started')
                gridLine7.setAutoDraw(True)
            if gridLine7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > gridLine7.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    gridLine7.tStop = t  # not accounting for scr refresh
                    gridLine7.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'gridLine7.stopped')
                    gridLine7.setAutoDraw(False)
            if gridLine7.status == STARTED:  # only update if drawing
                gridLine7.setFillColor(gridColor, log=False)
                gridLine7.setLineColor(gridColor, log=False)
            
            # *gridLine8* updates
            if gridLine8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                gridLine8.frameNStart = frameN  # exact frame index
                gridLine8.tStart = t  # local t and not account for scr refresh
                gridLine8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(gridLine8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'gridLine8.started')
                gridLine8.setAutoDraw(True)
            if gridLine8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > gridLine8.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    gridLine8.tStop = t  # not accounting for scr refresh
                    gridLine8.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'gridLine8.stopped')
                    gridLine8.setAutoDraw(False)
            if gridLine8.status == STARTED:  # only update if drawing
                gridLine8.setFillColor(gridColor, log=False)
                gridLine8.setLineColor(gridColor, log=False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in nb_trailComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "nb_trail" ---
        for thisComponent in nb_trailComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if trialResp.keys in ['', [], None]:  # No response was made
            trialResp.keys = None
        nb_trials.addData('trialResp.keys',trialResp.keys)
        if trialResp.keys != None:  # we had a response
            nb_trials.addData('trialResp.rt', trialResp.rt)
        # Run 'End Routine' code from code_12
        if trialResp.keys is not None:
            if 's' == trialResp.keys:
                skip_this_routine=True        
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'nb_trials'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'nb_taskloop'


# --- Prepare to start Routine "nb_end" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
nb_endComponents = [endText, key_resp_5]
for thisComponent in nb_endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "nb_end" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endText* updates
    if endText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endText.frameNStart = frameN  # exact frame index
        endText.tStart = t  # local t and not account for scr refresh
        endText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'endText.started')
        endText.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_5.started')
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['y','n','left','right','space','s'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in nb_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "nb_end" ---
for thisComponent in nb_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.nextEntry()
# Run 'End Routine' code from code_15
skip_this_routine=False

if key_resp_5.keys is not None:
    if 's' == key_resp_5.keys:
        skip_this_routine=True

# skip_this_routine=False

# the Routine "nb_end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "i_movie" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# Run 'Begin Routine' code from code_13
if skip_this_routine:
    continueRoutine=False
# Run 'Begin Routine' code from code_27
send_the_code(56)
# keep track of which components have finished
i_movieComponents = [text_6, key_resp_6, h_movie]
for thisComponent in i_movieComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "i_movie" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_6.started')
        text_6.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_6.started')
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['y','n','left','right','space','s'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *h_movie* updates
    if h_movie.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        h_movie.frameNStart = frameN  # exact frame index
        h_movie.tStart = t  # local t and not account for scr refresh
        h_movie.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(h_movie, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'h_movie.started')
        h_movie.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in i_movieComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "i_movie" ---
for thisComponent in i_movieComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.nextEntry()
# Run 'End Routine' code from code_13
# skip_this_routine=False
# 
# if key_resp_6.keys is not None:
#     if 's' == key_resp_6.keys:
#        skip_this_routine=True

# skip_this_routine=False

# the Routine "i_movie" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "showmovie" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# Run 'Begin Routine' code from code_14
if skip_this_routine:
    continueRoutine=False
# Run 'Begin Routine' code from code_28
send_the_code(200)
# keep track of which components have finished
showmovieComponents = [key_resp_8, movie]
for thisComponent in showmovieComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "showmovie" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_8.started')
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['s'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *movie* updates
    if movie.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        movie.frameNStart = frameN  # exact frame index
        movie.tStart = t  # local t and not account for scr refresh
        movie.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(movie, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'movie.started')
        movie.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in showmovieComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "showmovie" ---
for thisComponent in showmovieComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.nextEntry()
movie.stop()
# the Routine "showmovie" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "the_end" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
the_endComponents = [text_7, key_resp_7]
for thisComponent in the_endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "the_end" ---
while continueRoutine and routineTimer.getTime() < 2.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_7.started')
        text_7.setAutoDraw(True)
    if text_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_7.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            text_7.tStop = t  # not accounting for scr refresh
            text_7.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_7.stopped')
            text_7.setAutoDraw(False)
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_7.started')
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_7.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_7.tStop = t  # not accounting for scr refresh
            key_resp_7.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_7.stopped')
            key_resp_7.status = FINISHED
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['y','n','left','right','space'], waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in the_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "the_end" ---
for thisComponent in the_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.nextEntry()
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-2.000000)
# Run 'End Experiment' code from code_17
# Reset the port to its default state
#port.write([0xFF])
#time.sleep(PulseWidth)


# Terminate the read thread
#Connected = False
#thread.join(1.0)

# Close the serial port
#port.close()

# --- End experiment ---
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
