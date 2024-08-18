from playsound import playsound # a function

# note on playsound: you need to install a specific version on your machine.
# in cmd, type: pip install playsound==1.2.2

import time

ALARM_SOUND = 'C:\\Users\\don_s\\OneDrive\\Documents\\Website & Timesheets\\on-the-go\\alarm\\alarm.mp3'
CLEAR = "\033[2J" # characters based on ASCII -- clears terminal
CLEAR_AND_RETURN = "\033[H" # returns cursor to home position


def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1) #adds a 1 second delay 
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60 # integer divsision e.g. 125 // 60 = 2
        seconds_left = time_left % 60 

        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}") #02d makes it two digits by adding a leading 0 on one-digit numbers
    
    playsound(ALARM_SOUND)

minutes = int(input("How many minutes do you want to wait: "))
seconds = int(input("How many minutes do you want to wait: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)