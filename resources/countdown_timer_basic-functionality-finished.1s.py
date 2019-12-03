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
# be able to enter hours or seconds
# global var debug_mode which sets default time to 5s
# flag to show seconds? or if the time entered is 1m or less then auto-show
# prevent something like "9moose" from turning into 9 minutes

import os
import re
import subprocess
import sys
import time

icon='iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAYAAADhAJiYAAAAAXNSR0IArs4c6QAAAAlwSFlzAAAWJQAAFiUBSVIk8AAAAVlpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IlhNUCBDb3JlIDUuNC4wIj4KICAgPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICAgICAgPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIKICAgICAgICAgICAgeG1sbnM6dGlmZj0iaHR0cDovL25zLmFkb2JlLmNvbS90aWZmLzEuMC8iPgogICAgICAgICA8dGlmZjpPcmllbnRhdGlvbj4xPC90aWZmOk9yaWVudGF0aW9uPgogICAgICA8L3JkZjpEZXNjcmlwdGlvbj4KICAgPC9yZGY6UkRGPgo8L3g6eG1wbWV0YT4KTMInWQAAAxZJREFUWAntlluITVEYx8+4jbuQ++CFSC655Tau8aA8eFKaJzKvlHfFwzwg1+TVRJNQU5SSUAZNIyNyy4gQcikkJLn9/lnLrHXss9bee868zVe/sy7f9//WOmvvvdYqFLosvAIVYXfQW4n3JPRLiNpGX3NCf6d29Sf77xKszztyt7zCiK6z8kaGLRTWEvEY3JXaTXtoVJkzYD66IQGt3qM74E6oJhDfIddkM1ArpTupWbTr4IXxu5Ox9a/46mEZlMWqyPIT7ADDqWs16p0++b7DXTgNjXAV3oPVqWyBBZDbqlG6CTWxBnji9B+lvhAGQbH1pGMCbIa3YHPtpJ7LZqJqA5vILa/QvyhD1t7E7nJy7cmg9UL1eFbDWbATOuhFZGusJFyPV7nqskn9aL0fSnLI787Vsh+J8ulxZ7bzKCR+kFnpC3o5zVrqyvnR6UtVHWeEEk9Lpfg/SF/q8wS93kPl1SuR2vYRKdGR1Ao/cKTR64DVV+ea/Yq1oaYy3QA+gya0JpXCD+pjtLoJlLI3OJR/SqkAt3+eCf5BOdh1BOrd8ekaMhZ+QQOETJ+/JqS9yrOkU3muibhN+cGLTm4sN3GvKe/BMYidZ03EyPQHPEua0GgToZ05ZtJfghOgk78vHICYvTQBA4sDkyZkX0I9sphZvVblogleERPh13Eks2P9bfHb41+tvfLJVIe1d5WsadLb4QK8gsuwH2Jmbw+6FXiWNKFHJmKGF1m6sQNXC0yCNI9LmabqB9PNIGpjiNAXIGZHo/MFXDP5U9+9bxnB1nzjBVVVJrf+8IBgpONcZ0TPnL5yVfea3IezJrSPrSPXjuIxx5vJKPeoYmesXeuIs1zKQnm1t2kyx0NBId85k0DHwZJQYMSnr1kbqCbzFHKbDsqHoERiI2S16QhugPTfQO0OWSXq+2An1UR9aYqM2j7sISqtbhC6NQatIuj1ndqBtzhd2kCvQyu0gXZtnYNagWqYA9bOUNkE72xHucpVJGoEu1qxUkfJhiyDZ1khN+9EGtplF8MI0AanXF9Aq3ATTkEzdFlZV+APQ77IUZhTv+IAAAAASUVORK5CYII='

source_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'countdown_timer/source.txt')
data_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'countdown_timer/data.txt')

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

def notify(text, title, sound='Glass'):
    os.system('osascript -e \'display notification "{}" with title "{}" sound name "{}"\''.format(text, title, sound))

def entry(title='---', **kwargs):
    args = ' '.join('{}=\'{}\''.format(k,v) for k,v in kwargs.items() if v is not None)
    if args: args = '|' + args
    print(title + args)

def parse_time(s):
    m = re.match('^((\d+)h)?((\d+)m)?((\d+)s?)?$', s)
    if m is None: raise Exception('invalid time: %s' % s)
    h, m, s = map(int, (m.group(i) or 0 for i in (2, 4, 6)))
    return s + 60 * (m + 60 * h)

def render_time(t):
    t = float(t) # because round() requires a float
    t = int(round(t))
    h = t // 3600
    t -= h * 3600
    m = t // 60
    t -= m * 60
    k, v = 'hms', (h, m, t)

    show_seconds = True # for debugging purposes only

    if h < 1 and m < 1 and show_seconds is False:
        return '<1m'

    # %d is the number, %s is the string indicating the time type (h/m/s)
    return ''.join('%d%s' % (v[i], k[i]) for i in range(2 if show_seconds is False else 3) if i == 2 or any(v[:i+1]))

### DATA FILE FUNCTIONS ###

def write_data_file(t, task=None): # t is in minutes
    t = time.time() + int(t) * 60
    with open(data_file, 'wt') as f:
        f.write('{:f}{}{}'.format(t, '\n' if task else '', task or ''))

def read_data_file(filename):
    with open(data_file, 'rt') as f:
        lines = f.readlines()
    t = float(lines[0])
    task = lines[1].rstrip() if len(lines) > 1 else None
    return t, task

### SOURCE FILE FUNCTIONS ###

def write_source_file(source_str=''):
    with open(source_file, 'wt') as f:
        f.write(source_str)

def prompt_new_task(task):
    line = prompt('Input task and time in minutes', task or '')
    write_source_file(line)

def read_source_file(filename):
    with open(data_file, 'rt') as f:
        lines = f.readlines()
    t = float(lines[0])
    task = lines[1].rstrip() if len(lines) > 1 else None
    return t, task

## FILE BODY ##

if len(sys.argv) == 1:
    if os.path.isfile(source_file): # is there is a source file
        with open(source_file, 'rt') as f: # read from source file
            lines = f.readlines()
        if len(lines) > 0:
            source_str = lines[0]
        else:
            source_str = ''

        # TODO seconds and hours - line below searches for minutes only
        matches = re.search('(.*?)?((\d+)?m)?$', source_str)

        # defaults
        task = None
        t = None

        if matches is not None:
            if matches.group(3) is not None: #has both time and task
                task = matches.group(1)
                t = matches.group(3)
            else: # has only one
                single_str = matches.group(1)
                matches = re.search('(\d+)m', single_str);
                if matches is not None: # is a time
                    t = matches.group(1)
                else: # is plain text (task)
                    task = single_str

        if t is None:
            t = 25

        # shortcuts
        if task is None or task is "":
            task = ''
        elif task is "?":
            task = 'waid'
            t = 10
        elif task is "@":
            task = 'ask'
            t = 10

        # TODO implement cancel/end command for alfred (bash in workflow script)

        title = '{}{}{}'.format(task or '', task and ': ' or '', render_time(int(t) * 60))
        entry(title)
        write_data_file(t, task)
        os.remove(source_file)
    elif os.path.isfile(data_file): # no source file, so read from data file
        t, task = read_data_file(data_file)
        remain = int(round(max(0, t - time.time())))
        if remain == 0: # prompt on timer end
            notify('Times up!', task or 'Times up!')
            prompt_new_task(task)
            os.remove(data_file)
        title = '{}{}{}'.format(task or '', task and ': ' or '', render_time(remain))

        # TODO make a new 5m or 10m task ALREADY START as red or orange
        entry(title, color=('red' if remain <= 300 else 'orange' if remain < 600 else None))
        entry('---') # this prevents first entry from also being a menu item
        entry('Cancel timer', bash=__file__, param1='cancel', terminal='false')
        entry('Set timer', bash=__file__, param1='set', terminal='false')
    else: # no data nor source file
        entry('|templateImage=\'%s\'' % icon)
        entry('---') # this prevents first entry from also being a menu item
        entry('Use Alfred keyword \'t\' to activate')
        entry('Set timer', bash=__file__, param1='set', terminal='false')
elif len(sys.argv) == 2 and sys.argv[1] == 'set':
    prompt_new_task('')
elif len(sys.argv) == 2 and sys.argv[1] == 'cancel':
    os.remove(data_file)
