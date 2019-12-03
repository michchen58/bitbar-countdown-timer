#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# <bitbar.title>Countdown Timer 2</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Federico Ferri</bitbar.author>
# <bitbar.author.github>fferri</bitbar.author.github>
# <bitbar.desc>Simple countdown timer.</bitbar.desc>
# <bitbar.dependencies>python</bitbar.dependencies>
# <bitbar.image>https://raw.githubusercontent.com/fferri/bitbar-countdown-timer/master/screenshot.gif</bitbar.image>
# <bitbar.abouturl>https://github.com/fferri/bitbar-countdown-timer</bitbar.abouturl>

### TODO wishlist ###
# project names
# be able to set [shortcut] [custom time]
# External settings file to set shortcuts

# .gitignore log and resource files
# be able to enter hours or seconds
# prevent something like "9moose" from turning into 9 minutes
# out of time and datetime imports, only use one
# if i leave and come back after a while, the icon turns to "...", then it prompts and when i cancel it starts a 25m
# implement cancel/end command for alfred (bash in workflow script)

import os
import re
import subprocess
import sys
import time
import datetime
# import pyperclip
from decimal import * # prevents large integers from being converted to exps

icon='iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAYAAADhAJiYAAAAAXNSR0IArs4c6QAAAAlwSFlzAAAWJQAAFiUBSVIk8AAAAVlpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IlhNUCBDb3JlIDUuNC4wIj4KICAgPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICAgICAgPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIKICAgICAgICAgICAgeG1sbnM6dGlmZj0iaHR0cDovL25zLmFkb2JlLmNvbS90aWZmLzEuMC8iPgogICAgICAgICA8dGlmZjpPcmllbnRhdGlvbj4xPC90aWZmOk9yaWVudGF0aW9uPgogICAgICA8L3JkZjpEZXNjcmlwdGlvbj4KICAgPC9yZGY6UkRGPgo8L3g6eG1wbWV0YT4KTMInWQAAAxZJREFUWAntlluITVEYx8+4jbuQ++CFSC655Tau8aA8eFKaJzKvlHfFwzwg1+TVRJNQU5SSUAZNIyNyy4gQcikkJLn9/lnLrHXss9bee868zVe/sy7f9//WOmvvvdYqFLosvAIVYXfQW4n3JPRLiNpGX3NCf6d29Sf77xKszztyt7zCiK6z8kaGLRTWEvEY3JXaTXtoVJkzYD66IQGt3qM74E6oJhDfIddkM1ArpTupWbTr4IXxu5Ox9a/46mEZlMWqyPIT7ADDqWs16p0++b7DXTgNjXAV3oPVqWyBBZDbqlG6CTWxBnji9B+lvhAGQbH1pGMCbIa3YHPtpJ7LZqJqA5vILa/QvyhD1t7E7nJy7cmg9UL1eFbDWbATOuhFZGusJFyPV7nqskn9aL0fSnLI787Vsh+J8ulxZ7bzKCR+kFnpC3o5zVrqyvnR6UtVHWeEEk9Lpfg/SF/q8wS93kPl1SuR2vYRKdGR1Ao/cKTR64DVV+ea/Yq1oaYy3QA+gya0JpXCD+pjtLoJlLI3OJR/SqkAt3+eCf5BOdh1BOrd8ekaMhZ+QQOETJ+/JqS9yrOkU3muibhN+cGLTm4sN3GvKe/BMYidZ03EyPQHPEua0GgToZ05ZtJfghOgk78vHICYvTQBA4sDkyZkX0I9sphZvVblogleERPh13Eks2P9bfHb41+tvfLJVIe1d5WsadLb4QK8gsuwH2Jmbw+6FXiWNKFHJmKGF1m6sQNXC0yCNI9LmabqB9PNIGpjiNAXIGZHo/MFXDP5U9+9bxnB1nzjBVVVJrf+8IBgpONcZ0TPnL5yVfea3IezJrSPrSPXjuIxx5vJKPeoYmesXeuIs1zKQnm1t2kyx0NBId85k0DHwZJQYMSnr1kbqCbzFHKbDsqHoERiI2S16QhugPTfQO0OWSXq+2An1UR9aYqM2j7sISqtbhC6NQatIuj1ndqBtzhd2kCvQyu0gXZtnYNagWqYA9bOUNkE72xHucpVJGoEu1qxUkfJhiyDZ1khN+9EGtplF8MI0AanXF9Aq3ATTkEzdFlZV+APQ77IUZhTv+IAAAAASUVORK5CYII='

source_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'countdown_timer/data/source.txt')
data_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'countdown_timer/data/data.txt')

today = datetime.datetime.now()

# build filename
today_month = today.month if today.month > 9 else '0{}'.format(today.month)
today_day = today.day if today.day > 9 else '0{}'.format(today.day)

log_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'countdown_timer/logs/{}/{}'.format(
    today.year,
    today_month
))
log_file = '{}/{}.js'.format(log_folder, today_day)


### UTIL FUNCTIONS ###

def prompt(text='', defaultAnswer='', icon='note', buttons=('Cancel','Ok'), defaultButton=1):
    try:
        d = locals()
        d['buttonsStr'] = ', '.join('"%s"' % button for button in buttons)
        d['defaultButtonStr'] = isinstance(defaultButton, int) and buttons[defaultButton] or defaultButton

        return subprocess.check_output(['osascript', '-l', 'JavaScript', '-e', '''
            const app = Application.currentApplication()
            app.includeStandardAdditions = true
            const response = app.displayDialog("{text}", {{
                defaultAnswer: "{defaultAnswer}",
                withIcon: "{icon}",
                buttons: [{buttonsStr}],
                defaultButton: "{defaultButtonStr}"
            }})
            response.textReturned
        '''.format(**d)]).rstrip()
    except subprocess.CalledProcessError:
        pass

def notify(text, title='', sound='Glass'):
    os.system('osascript -e \'display notification "{}" with title "{}" sound name "{}"\''.format(text, title, sound))

def entry(title='---', **kwargs):
    args = ' '.join('{}=\'{}\''.format(k,v) for k,v in kwargs.items() if v is not None)
    if args:
        args = '|' + args

    print(title + args)

def render_time(t, show_seconds=False):
    t = int(t) # because round() requires a float

    if t < 60 and show_seconds is False:
        return '<1m'

    h = t // 3600
    t -= h * 3600
    m = t // 60
    t -= m * 60
    k, v = 'hms', [h, m, t]

    # %d is the number, %s is the string indicating the time type (h/m/s)
    return ''.join('%d%s' % (v[i], k[i]) for i in range(2 if show_seconds is False else 3) if i == 2 or any(v[:i+1]))



### DATA FILE FUNCTIONS #######################################################

def write_data_file(t, task=None, show_seconds=False, source_str=''): # t is in minutes
    t_in_seconds = int(t)
    t = time.time() + int(t)
    with open(data_file, 'wt') as f:
        f.write('{:f}\n{}\n{}\n{}'.format(t, task or '', show_seconds, source_str.replace('"', '\\"')))

def read_data_file(filename):
    with open(data_file, 'rt') as f:
        lines = f.readlines()
    t = float(lines[0])
    task = lines[1]
    show_seconds = True if lines[2].rstrip() == 'True' else False
    source_str = lines[3]
    return t, task, show_seconds, source_str

### SOURCE FILE FUNCTIONS ####################################################

def write_source_file(source_str=''):
    with open(source_file, 'wt') as f:
        f.write(source_str)

def prompt_new_task(prevTask):
    line = prompt('Input task and time', prevTask)
    if line is not None: # pressed cancel on prompt
        write_source_file(line)

def read_source_file(filename):
    with open(data_file, 'rt') as f:
        lines = f.readlines()
    t = float(lines[0])
    task = lines[1].rstrip() if len(lines) > 1 else None
    return t, task

### LOG FUNCTIONS ###

def log_entry(t, task):
    if task is not '':
        file_start = ''
        # if folder does not exist
        if os.path.isdir(log_folder) is False:
            os.makedirs(log_folder)

        # if file does not exist
        if os.path.isfile(log_file) is False:
            file_start = 'let data = [\n'
        else:
            # delete last line (arr close bracket)
            with open(log_file, 'rb+') as f:
                f.seek(-1, os.SEEK_END)
                f.truncate()

        # prevents log from breaking bc of quotes
        task = task.replace('"','\\"')

        # write new line
        with open(log_file, 'a') as f:
            f.write('{}{{time: {}, task: "{}", duration: "{}m"}},\n]'.format(
                file_start, # opening bracket
                Decimal(round(time.time() * 1000)), # timestamp
                task,
                t
            ))
            f.close()




### FILE BODY #################################################################

if len(sys.argv) == 1:
    if os.path.isfile(source_file): # is there is a source file
        with open(source_file, 'rt') as f: # read from source file
            lines = f.readlines()
        if len(lines) > 0:
            source_str = lines[0]
            source_str = source_str.replace('\n', '')
        else:
            source_str = ''

        # defaults
        task = None
        t = None # time in seconds
        show_seconds = False

        matches = re.search('(.*?)?((\d+)m)?((\d+)s)?$', source_str)
        if matches is not None:
            if matches.group(1) is not None and matches.group(1) is not "":
                if matches.group(3) is not None:
                    if matches.group(5) is not None: #task/mins/secs
                        task = matches.group(1)
                        t = int(matches.group(3)) * 60 + int(matches.group(5))
                        show_seconds = True
                        # notify('task/mins/secs {} {}'.format(task, t))
                    else: #task/mins
                        task = matches.group(1)
                        t = int(matches.group(3)) * 60
                        # notify('task/mins {} {}'.format(task, t))
                else:
                    if matches.group(5) is not None: #task/secs
                        task = matches.group(1)
                        t = matches.group(5)
                        show_seconds = True
                        # notify('task/secs {} {}'.format(task, t))
                    else: #task only
                        task = matches.group(1)
                        # notify('task {}'.format(task))
            else:
                if matches.group(3) is not None:
                    if matches.group(5) is not None: #mins/secs
                        t = int(matches.group(3)) * 60 + int(matches.group(5))
                        show_seconds = True
                        # notify('mins/secs {}'.format(t))
                    else:
                        t = int(matches.group(3)) * 60
                        # notify('mins {}'.format(t))
                elif matches.group(5) is not None: # has seconds
                    t = matches.group(5)
                    show_seconds = True
                    # notify('secs {}'.format(t))

        if t is None: # default time (if not defined) is 25 mins
            t = 25 * 60

        # shortcuts
        if task == None or task == "":
            # code ends up here if i press cancel on prompt??
            task = ''
        elif task == "?":
            task = 'waid'
            t = 10 * 60
        elif task == "@":
            task = 'ask'
            t = 10 * 60
        elif task == "...":
            task = 'idle'
            t = 10 * 60
        elif task == "smell":
            task = 'AbScent'
            t = 20
            show_seconds = True

        task = task.rstrip()

        # pyperclip.copy(task)

        title = '[ {}{}{} ]'.format(task or '', task and ': ' or '', render_time(t, show_seconds))
        entry(title, color=('red' if int(t) <= 300 else 'orange' if int(t) <= 600 else None))

        if matches.group(3) is '1': # if entering only one minute, default to show seconds
            show_seconds = True

        write_data_file(t, task, show_seconds, source_str)

        if task is not 'AbScent':
            log_entry(int(t) / 60, task)

        os.remove(source_file)
    elif os.path.isfile(data_file): # no source file, so read from data file
        t, task, show_seconds, source_str = read_data_file(data_file)
        remain = int(round(max(0, float(t) - time.time()))) # original
        if remain <= 0: # prompt on timer end
            os.remove(data_file)
            os.system('osascript -e beep')
            prompt_new_task(source_str)
            sys.exit()
        task = task.rstrip() # remove trailing spaces

        title = '[ {}{}{} ]'.format(task or '', task and ': ' or '', render_time(remain, show_seconds))
        entry(title, color=('red' if remain <= 300 else 'orange' if remain <= 600 else None))
        entry('---') # prevents first entry from also being a menu item
        entry('Set timer', bash=__file__, param1='set', terminal='false')
        entry('Cancel timer', bash=__file__, param1='cancel', terminal='false')
    else: # no data nor source file
        entry('|templateImage=\'%s\'' % icon)
        entry('---') # prevents first entry from also being a menu item
        entry('Use Alfred keyword \'t\' to set')
        entry('Set timer', bash=__file__, param1='set', terminal='false')
elif len(sys.argv) == 2 and sys.argv[1] == 'set':
    prompt_new_task('')
elif len(sys.argv) == 2 and sys.argv[1] == 'cancel':
    os.remove(data_file)
elif len(sys.argv) == 2 and sys.argv[1] == 'viz':
    viz_path = '{}/visualization/index.html'.format(os.path.dirname(os.path.realpath(sys.argv[0])))
    os.system("open " + viz_path)
elif len(sys.argv) == 2 and sys.argv[1] == 'log':
    log_path = '{}/countdown_timer/logs/{}/{}/{}.js'.format(os.path.dirname(os.path.realpath(__file__)), today.year, today_month, today_day)
    os.system("open " + log_path)
elif len(sys.argv) == 2 and sys.argv[1] == 'data':
    log_path = '{}/countdown_timer/data/data.txt'.format(os.path.dirname(os.path.realpath(__file__)))
    os.system("open " + log_path)
elif len(sys.argv) == 2 and sys.argv[1] == 'folder':
    log_path = '{}/'.format(os.path.dirname(os.path.realpath(__file__)))
    os.system("open " + log_path)

entry('---') # horizontal divider in menu

entry('Visualization', bash=__file__, param1='viz', terminal='false')
entry('Log file', bash=__file__, param1='log', terminal='false')
entry('Folder', bash=__file__, param1='folder', terminal='false')
