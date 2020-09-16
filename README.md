# cheater
This application is used to cheat in online protored exams. This is only meant for EDUCATION PURPOSE.

# NOTE
This application can only run on linux OS

# How to RUN:
1. clone the repository.
2. while connected to the wifi check the inet address by runing `ifconfig` on the terminal
3. Open the app.py file and replace the host address at line 22 with your inet address.
4. With this you connect to flask web app from any device as long as it is sharing the same wifi. If this method does not work try this from the doc https://flask.palletsprojects.com/en/1.1.x/quickstart/#public-server

## The bellow step is a little confusing its basically for making a keylogger  
5. Check the event for your keybord with `cat /proc/bus/input/devices`, find all "keybord" in name, along with its coresponding handler where you will find its event, reffer here if needed https://dzone.com/articles/how-to-create-a-keylogger-for-linux-using-python 
6. Check your event typing `cat /dev/input/event4`(in my case it was event4), Now press any key on your keybord, if you find any random output on the terminal then we are on right track.
7. Copy path to your event file and paste it in your cheeter.py file in variable file_name at line 135

It seems the pyautogui throws `Xlib.error.DisplayConnectionError` to troubleshoot the error faced while running cheeter.py file (refference https://github.com/mooz/xkeysnail)

8. `sudo pip3 install xkeysnail`
9.  Run this in terminal `xhost +SI:localuser:root`

10. `sudo python3 cheeter.py`
11. On another terminal run `python3 app.py`


# How to use: 
12. minimise your terminals 
13. Now while during test you want to execute your program press BACKSPACE on your keybord(this will reset the typed keys in your keylogger) just hover your mouse pointer at the start of the question and TYPE ON THE KEYBORD "hooded". This will then activate a screenshot function, then drag your mouse pointer to the end of the question and then press "x" to capture, remember the question should not have any pictures its only meant for text, for now.

13. It will then do a google search in the backend on your question and then take a screenshot from a few top websites.
14. This screen shot is now uploaded on the web app, just open your smart phone to that address your answers will be available there.
