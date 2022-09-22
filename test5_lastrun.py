#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Mon 15 Aug 2022 04:54:15 PM CEST
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, parallel
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'test5'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
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
    originPath='/home/electrobrain/lighteeg/new_task_ARSQ/test5_lastrun.py',
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
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "i_eoec"
i_eoecClock = core.Clock()
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

# Initialize components for Routine "eo"
eoClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Eyes Open',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "ec"
ecClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Eyes Closed',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "w"
wClock = core.Clock()
img_whte = visual.ImageStim(
    win=win,
    name='img_whte', 
    image=None, mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "b"
bClock = core.Clock()
img_black = visual.ImageStim(
    win=win,
    name='img_black', 
    image=None, mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "i_arsq"
i_arsqClock = core.Clock()
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

# Initialize components for Routine "question"
questionClock = core.Clock()
slider = visual.Slider(win=win, name='slider',
    startValue=None, size=(1.0, 0.05), pos=(0, -0.2), units=None,
    labels=('--\nfully disagree','-','0\nneutral','+','++\nfully agree'), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.04,
    flip=False, depth=0, readOnly=False)
text = visual.TextStim(win=win, name='text',
    text='',
    font='Open Sans',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "i_nback"
i_nbackClock = core.Clock()
instrText = visual.TextStim(win=win, name='instrText',
    text=None,
    font='Arial',
    pos=(-0.3,0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
instrResp = keyboard.Keyboard()
instrImg = visual.ImageStim(
    win=win,
    name='instrImg', 
    image=None, mask=None,
    ori=0.0, pos=[0,0], size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "nb_trail"
nb_trailClock = core.Clock()
trialResp = keyboard.Keyboard()
trialSquare = visual.Rect(
    win=win, name='trialSquare',
    width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1.0, depth=-1.0, interpolate=True)
trialFix = visual.TextStim(win=win, name='trialFix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=0.0, 
    languageStyle='LTR',
    depth=-2.0);
gridColor = [1,1,1]
play_sounds=True
mySound_goed = sound.Sound('sounds/goed.wav')
mySound_fout= sound.Sound('sounds/fout.wav')
gridLine1 = visual.Line(
    win=win, name='gridLine1',
    start=(-(0.6, 0.6)[0]/2.0, 0), end=(+(0.6, 0.6)[0]/2.0, 0),
    ori=0.0, pos=(0, 0.3),
    lineWidth=1.5,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-4.0, interpolate=True)
gridLine2 = visual.Line(
    win=win, name='gridLine2',
    start=(-(0.6, 0.6)[0]/2.0, 0), end=(+(0.6, 0.6)[0]/2.0, 0),
    ori=0.0, pos=(0, 0.096),
    lineWidth=1.5,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-5.0, interpolate=True)
gridLine3 = visual.Line(
    win=win, name='gridLine3',
    start=(-(0.6, 0.6)[0]/2.0, 0), end=(+(0.6, 0.6)[0]/2.0, 0),
    ori=0.0, pos=(0, -0.096),
    lineWidth=1.5,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-6.0, interpolate=True)
gridLine4 = visual.Line(
    win=win, name='gridLine4',
    start=(-(0.6, 0.6)[0]/2.0, 0), end=(+(0.6, 0.6)[0]/2.0, 0),
    ori=0.0, pos=(0, -0.3),
    lineWidth=1.5,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-7.0, interpolate=True)
gridLine5 = visual.Line(
    win=win, name='gridLine5',
    start=(-(0.6, 0.6)[0]/2.0, 0), end=(+(0.6, 0.6)[0]/2.0, 0),
    ori=90.0, pos=(-0.3, 0),
    lineWidth=1.5,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-8.0, interpolate=True)
gridLine6 = visual.Line(
    win=win, name='gridLine6',
    start=(-(0.6, 0.6)[0]/2.0, 0), end=(+(0.6, 0.6)[0]/2.0, 0),
    ori=90.0, pos=(-0.096, 0),
    lineWidth=1.5,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-9.0, interpolate=True)
gridLine7 = visual.Line(
    win=win, name='gridLine7',
    start=(-(0.6, 0.6)[0]/2.0, 0), end=(+(0.6, 0.6)[0]/2.0, 0),
    ori=90.0, pos=(0.096, 0),
    lineWidth=1.5,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-10.0, interpolate=True)
gridLine8 = visual.Line(
    win=win, name='gridLine8',
    start=(-(0.6, 0.6)[0]/2.0, 0), end=(+(0.6, 0.6)[0]/2.0, 0),
    ori=90.0, pos=(0.3, 0),
    lineWidth=1.5,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-11.0, interpolate=True)

# Initialize components for Routine "nb_end"
nb_endClock = core.Clock()
endText = visual.TextStim(win=win, name='endText',
    text='This is the end this part of the experiment. Thank you for your time.\n\nif this is the first session, now the environmental conditions will be changed.\n\nif this is the second session, we now follow up with a movie.',
    font='Open Sans',
    pos=(0, 0), height=0.033, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "i_movie"
i_movieClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Information about Movie',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "movie"
movieClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "i_eoec"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# setup some python lists for storing info about the mouse_2
gotValidClick = False  # until a click is received
# keep track of which components have finished
i_eoecComponents = [key_resp_3, text_4, mouse_2]
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
i_eoecClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "i_eoec"-------
while continueRoutine:
    # get current time
    t = i_eoecClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=i_eoecClock)
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
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['y', 'n', 'left', 'right', 'space', 'c', 's'], waitRelease=False)
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
        text_4.setAutoDraw(True)
    # *mouse_2* updates
    if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_2.frameNStart = frameN  # exact frame index
        mouse_2.tStart = t  # local t and not account for scr refresh
        mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
        mouse_2.status = STARTED
        mouse_2.mouseClock.reset()
        prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
    if mouse_2.status == STARTED:  # only update if started and not finished!
        buttons = mouse_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # abort routine on response
                continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in i_eoecComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "i_eoec"-------
for thisComponent in i_eoecComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_2.getPos()
buttons = mouse_2.getPressed()
thisExp.addData('mouse_2.x', x)
thisExp.addData('mouse_2.y', y)
thisExp.addData('mouse_2.leftButton', buttons[0])
thisExp.addData('mouse_2.midButton', buttons[1])
thisExp.addData('mouse_2.rightButton', buttons[2])
thisExp.addData('mouse_2.started', mouse_2.tStart)
thisExp.addData('mouse_2.stopped', mouse_2.tStop)
thisExp.nextEntry()
skip_this_routine=False

if key_resp_3.keys is not None:
    if 's' == key_resp_3.keys:
        skip_this_routine=True
    
# print(key_resp_3.keys)
# print('c' in key_resp_3.keys)
# the Routine "i_eoec" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "eo"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
if skip_this_routine:
    continueRoutine=False
# keep track of which components have finished
eoComponents = [text_2, key_resp]
for thisComponent in eoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
eoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "eo"-------
while continueRoutine:
    # get current time
    t = eoClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=eoClock)
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
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 180-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['c'], waitRelease=False)
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
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in eoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "eo"-------
for thisComponent in eoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "eo" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ec"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
if skip_this_routine:
    continueRoutine=False
# keep track of which components have finished
ecComponents = [text_3, key_resp_2]
for thisComponent in ecComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ecClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ec"-------
while continueRoutine:
    # get current time
    t = ecClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ecClock)
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
    if text_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_3.tStartRefresh + 180-frameTolerance:
            # keep track of stop time/frame for later
            text_3.tStop = t  # not accounting for scr refresh
            text_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
            text_3.setAutoDraw(False)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['c'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ecComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ec"-------
for thisComponent in ecComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "ec" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
    
    # ------Prepare to start Routine "w"-------
    continueRoutine = True
    routineTimer.add(0.200000)
    # update component parameters for each repeat
    win.color=[-1, -1, -1]
    if skip_this_routine:
        continueRoutine=False
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
    wClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "w"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = wClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=wClock)
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
            img_whte.setAutoDraw(True)
        if img_whte.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > img_whte.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                img_whte.tStop = t  # not accounting for scr refresh
                img_whte.frameNStop = frameN  # exact frame index
                win.timeOnFlip(img_whte, 'tStopRefresh')  # time at next scr refresh
                img_whte.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "w"-------
    for thisComponent in wComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    wakeup.addData('img_whte.started', img_whte.tStartRefresh)
    wakeup.addData('img_whte.stopped', img_whte.tStopRefresh)
    win.color=[0, 0, 0]
    
    # ------Prepare to start Routine "b"-------
    continueRoutine = True
    routineTimer.add(0.200000)
    # update component parameters for each repeat
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
    bClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "b"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = bClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=bClock)
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
            img_black.setAutoDraw(True)
        if img_black.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > img_black.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                img_black.tStop = t  # not accounting for scr refresh
                img_black.frameNStop = frameN  # exact frame index
                win.timeOnFlip(img_black, 'tStopRefresh')  # time at next scr refresh
                img_black.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in bComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "b"-------
    for thisComponent in bComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    wakeup.addData('img_black.started', img_black.tStartRefresh)
    wakeup.addData('img_black.stopped', img_black.tStopRefresh)
    win.color=[0, 0, 0]
    thisExp.nextEntry()
    
# completed 4.0 repeats of 'wakeup'


# ------Prepare to start Routine "i_arsq"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# setup some python lists for storing info about the mouse
gotValidClick = False  # until a click is received
# keep track of which components have finished
i_arsqComponents = [text_5, key_resp_4, mouse]
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
i_arsqClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "i_arsq"-------
while continueRoutine:
    # get current time
    t = i_arsqClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=i_arsqClock)
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
        text_5.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['y', 'n', 'left', 'right', 'space', 'c', 's'], waitRelease=False)
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
        mouse.status = STARTED
        mouse.mouseClock.reset()
        prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
    if mouse.status == STARTED:  # only update if started and not finished!
        buttons = mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # abort routine on response
                continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in i_arsqComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "i_arsq"-------
for thisComponent in i_arsqComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
x, y = mouse.getPos()
buttons = mouse.getPressed()
thisExp.addData('mouse.x', x)
thisExp.addData('mouse.y', y)
thisExp.addData('mouse.leftButton', buttons[0])
thisExp.addData('mouse.midButton', buttons[1])
thisExp.addData('mouse.rightButton', buttons[2])
thisExp.addData('mouse.started', mouse.tStart)
thisExp.addData('mouse.stopped', mouse.tStop)
thisExp.nextEntry()
skip_this_routine=False

if key_resp_4.keys is not None:
    if 's' == key_resp_4.keys:
        skip_this_routine=True
    
# the Routine "i_arsq" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
qustions = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('csv/questions_english.csv'),
    seed=None, name='qustions')
thisExp.addLoop(qustions)  # add the loop to the experiment
thisQustion = qustions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisQustion.rgb)
if thisQustion != None:
    for paramName in thisQustion:
        exec('{} = thisQustion[paramName]'.format(paramName))

for thisQustion in qustions:
    currentLoop = qustions
    # abbreviate parameter names if possible (e.g. rgb = thisQustion.rgb)
    if thisQustion != None:
        for paramName in thisQustion:
            exec('{} = thisQustion[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "question"-------
    continueRoutine = True
    # update component parameters for each repeat
    slider.reset()
    text.setText(itemtext)
    if skip_this_routine:
        continueRoutine=False
    # keep track of which components have finished
    questionComponents = [slider, text]
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
    questionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "question"-------
    while continueRoutine:
        # get current time
        t = questionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=questionClock)
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
            text.setAutoDraw(True)
        if slider.getRT() is not None:
            response_time = slider.getRT()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in questionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "question"-------
    for thisComponent in questionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    qustions.addData('slider.response', slider.getRating())
    qustions.addData('slider.rt', slider.getRT())
    qustions.addData('slider.started', slider.tStartRefresh)
    qustions.addData('slider.stopped', slider.tStopRefresh)
    qustions.addData('text.started', text.tStartRefresh)
    qustions.addData('text.stopped', text.tStopRefresh)
    if not skip_this_routine:
        ISI = core.StaticPeriod()
        ISI.start(0.2)  # start a period of 0.5s
        # stim.image = 'largeFile.bmp'  # could take some time
        ISI.complete()  # finish the 0.5s, taking into account one 60Hz frame
    # the Routine "question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'qustions'


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
    
    # ------Prepare to start Routine "i_nback"-------
    continueRoutine = True
    # update component parameters for each repeat
    instrText.setText('')
    instrResp.keys = []
    instrResp.rt = []
    _instrResp_allKeys = []
    instrImg.setPos((0, 0))
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
    # continueRoutine=True
    # skip_this_routine=False
    
    # keep track of which components have finished
    i_nbackComponents = [instrText, instrResp, instrImg]
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
    i_nbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "i_nback"-------
    while continueRoutine:
        # get current time
        t = i_nbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=i_nbackClock)
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
            instrText.setAutoDraw(True)
        
        # *instrResp* updates
        waitOnFlip = False
        if instrResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instrResp.frameNStart = frameN  # exact frame index
            instrResp.tStart = t  # local t and not account for scr refresh
            instrResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instrResp, 'tStartRefresh')  # time at next scr refresh
            instrResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instrResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instrResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instrResp.status == STARTED and not waitOnFlip:
            theseKeys = instrResp.getKeys(keyList=['c', 's'], waitRelease=False)
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
            instrImg.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in i_nbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "i_nback"-------
    for thisComponent in i_nbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    nb_taskloop.addData('instrText.started', instrText.tStartRefresh)
    nb_taskloop.addData('instrText.stopped', instrText.tStopRefresh)
    nb_taskloop.addData('instrImg.started', instrImg.tStartRefresh)
    nb_taskloop.addData('instrImg.stopped', instrImg.tStopRefresh)
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
        
        # ------Prepare to start Routine "nb_trail"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        trialResp.keys = []
        trialResp.rt = []
        _trialResp_allKeys = []
        trialSquare.setPos((loc1, loc2))
        gridColor = [1,1,1]
        sound_playing=False
        
        if skip_this_routine:
            continueRoutine=False
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
        nb_trailClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "nb_trail"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = nb_trailClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=nb_trailClock)
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
                    win.timeOnFlip(trialResp, 'tStopRefresh')  # time at next scr refresh
                    trialResp.status = FINISHED
            if trialResp.status == STARTED and not waitOnFlip:
                theseKeys = trialResp.getKeys(keyList=['space'], waitRelease=False)
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
                trialSquare.setAutoDraw(True)
            if trialSquare.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trialSquare.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    trialSquare.tStop = t  # not accounting for scr refresh
                    trialSquare.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(trialSquare, 'tStopRefresh')  # time at next scr refresh
                    trialSquare.setAutoDraw(False)
            
            # *trialFix* updates
            if trialFix.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                trialFix.frameNStart = frameN  # exact frame index
                trialFix.tStart = t  # local t and not account for scr refresh
                trialFix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialFix, 'tStartRefresh')  # time at next scr refresh
                trialFix.setAutoDraw(True)
            if trialFix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trialFix.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    trialFix.tStop = t  # not accounting for scr refresh
                    trialFix.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(trialFix, 'tStopRefresh')  # time at next scr refresh
                    trialFix.setAutoDraw(False)
            if corrAns == 'space' and (trialResp.keys == 'space'):
                gridColor = [-1.000,1.000,-1.000]
                if not sound_playing and play_sounds:
                    sound_playing=True
                    mySound_goed.play()
                    
            if not(corrAns == 'space') and (trialResp.keys == 'space'):
                gridColor = [1.000,-1.000,-1.000]
                if not sound_playing and play_sounds:
                    sound_playing=True
                    mySound_fout.play()
            
            
            # *gridLine1* updates
            if gridLine1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                gridLine1.frameNStart = frameN  # exact frame index
                gridLine1.tStart = t  # local t and not account for scr refresh
                gridLine1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(gridLine1, 'tStartRefresh')  # time at next scr refresh
                gridLine1.setAutoDraw(True)
            if gridLine1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > gridLine1.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    gridLine1.tStop = t  # not accounting for scr refresh
                    gridLine1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(gridLine1, 'tStopRefresh')  # time at next scr refresh
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
                gridLine2.setAutoDraw(True)
            if gridLine2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > gridLine2.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    gridLine2.tStop = t  # not accounting for scr refresh
                    gridLine2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(gridLine2, 'tStopRefresh')  # time at next scr refresh
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
                gridLine3.setAutoDraw(True)
            if gridLine3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > gridLine3.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    gridLine3.tStop = t  # not accounting for scr refresh
                    gridLine3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(gridLine3, 'tStopRefresh')  # time at next scr refresh
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
                gridLine4.setAutoDraw(True)
            if gridLine4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > gridLine4.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    gridLine4.tStop = t  # not accounting for scr refresh
                    gridLine4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(gridLine4, 'tStopRefresh')  # time at next scr refresh
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
                gridLine5.setAutoDraw(True)
            if gridLine5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > gridLine5.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    gridLine5.tStop = t  # not accounting for scr refresh
                    gridLine5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(gridLine5, 'tStopRefresh')  # time at next scr refresh
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
                gridLine6.setAutoDraw(True)
            if gridLine6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > gridLine6.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    gridLine6.tStop = t  # not accounting for scr refresh
                    gridLine6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(gridLine6, 'tStopRefresh')  # time at next scr refresh
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
                gridLine7.setAutoDraw(True)
            if gridLine7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > gridLine7.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    gridLine7.tStop = t  # not accounting for scr refresh
                    gridLine7.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(gridLine7, 'tStopRefresh')  # time at next scr refresh
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
                gridLine8.setAutoDraw(True)
            if gridLine8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > gridLine8.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    gridLine8.tStop = t  # not accounting for scr refresh
                    gridLine8.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(gridLine8, 'tStopRefresh')  # time at next scr refresh
                    gridLine8.setAutoDraw(False)
            if gridLine8.status == STARTED:  # only update if drawing
                gridLine8.setFillColor(gridColor, log=False)
                gridLine8.setLineColor(gridColor, log=False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in nb_trailComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "nb_trail"-------
        for thisComponent in nb_trailComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if trialResp.keys in ['', [], None]:  # No response was made
            trialResp.keys = None
        nb_trials.addData('trialResp.keys',trialResp.keys)
        if trialResp.keys != None:  # we had a response
            nb_trials.addData('trialResp.rt', trialResp.rt)
        nb_trials.addData('trialResp.started', trialResp.tStartRefresh)
        nb_trials.addData('trialResp.stopped', trialResp.tStopRefresh)
        nb_trials.addData('trialSquare.started', trialSquare.tStartRefresh)
        nb_trials.addData('trialSquare.stopped', trialSquare.tStopRefresh)
        nb_trials.addData('trialFix.started', trialFix.tStartRefresh)
        nb_trials.addData('trialFix.stopped', trialFix.tStopRefresh)
        nb_trials.addData('gridLine1.started', gridLine1.tStartRefresh)
        nb_trials.addData('gridLine1.stopped', gridLine1.tStopRefresh)
        nb_trials.addData('gridLine2.started', gridLine2.tStartRefresh)
        nb_trials.addData('gridLine2.stopped', gridLine2.tStopRefresh)
        nb_trials.addData('gridLine3.started', gridLine3.tStartRefresh)
        nb_trials.addData('gridLine3.stopped', gridLine3.tStopRefresh)
        nb_trials.addData('gridLine4.started', gridLine4.tStartRefresh)
        nb_trials.addData('gridLine4.stopped', gridLine4.tStopRefresh)
        nb_trials.addData('gridLine5.started', gridLine5.tStartRefresh)
        nb_trials.addData('gridLine5.stopped', gridLine5.tStopRefresh)
        nb_trials.addData('gridLine6.started', gridLine6.tStartRefresh)
        nb_trials.addData('gridLine6.stopped', gridLine6.tStopRefresh)
        nb_trials.addData('gridLine7.started', gridLine7.tStartRefresh)
        nb_trials.addData('gridLine7.stopped', gridLine7.tStopRefresh)
        nb_trials.addData('gridLine8.started', gridLine8.tStartRefresh)
        nb_trials.addData('gridLine8.stopped', gridLine8.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'nb_trials'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'nb_taskloop'


# ------Prepare to start Routine "nb_end"-------
continueRoutine = True
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
nb_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "nb_end"-------
while continueRoutine:
    # get current time
    t = nb_endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=nb_endClock)
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
        endText.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
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
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in nb_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "nb_end"-------
for thisComponent in nb_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('endText.started', endText.tStartRefresh)
thisExp.addData('endText.stopped', endText.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "nb_end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "i_movie"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
i_movieComponents = [text_6, key_resp_6]
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
i_movieClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "i_movie"-------
while continueRoutine:
    # get current time
    t = i_movieClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=i_movieClock)
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
        text_6.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['y', 'n', 'left', 'right', 'space', 's'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in i_movieComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "i_movie"-------
for thisComponent in i_movieComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
skip_this_routine=False

if instrResp.keys is not None:
    if 's' == instrResp.keys:
        skip_this_routine=True
    
# the Routine "i_movie" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "movie"-------
continueRoutine = True
# update component parameters for each repeat
if skip_this_routine:
    continueRoutine=False
# keep track of which components have finished
movieComponents = []
for thisComponent in movieComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
movieClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "movie"-------
while continueRoutine:
    # get current time
    t = movieClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=movieClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in movieComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "movie"-------
for thisComponent in movieComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "movie" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
