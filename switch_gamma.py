## switch_gamma - a program for flipping the desktop gamma between light and regular
## Written by Thomas Kocourek for Linux desktops
import sys
import subprocess

## Set this next line to 'False' if you intend to use the program in a terminal window
GUI_flag = True
# GUI_flag = False


try:
    import easygui
except Exception as e:
    print("Check your distribution for an 'easygui' module. Failed to import 'easygui'.")
    sys.exit()

light_gamma = '1.3'
regular_gamma = '1.0'

def test_gamma():
    try:
        testing = subprocess.Popen(["xgamma"], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL, text=True)
        return True
    except Exception as e:
        ## if the host is not available, trap error & do nothing
        ## if called from terminal window
        print("Error: ",e)
        print("xgamma cannot be found.")
        
        return False

#x = test_gamma()
if test_gamma():
    results = subprocess.run(["xgamma"],capture_output=True, text=True)
    ## 'results' is a sunprocess object. Convert to string object and process it.
    tmp = str(results)
    listing = tmp.split(', ')
    tmp = listing[4].split(' ')
    gamma = tmp[2]
    # print(gamma)
    if gamma == '1.000':
        if GUI_flag:
            message = "gamma is set to regular mode. Switching to light mode."
            easygui.msgbox(message, title="Action")
        results = subprocess.Popen(["xgamma","-gamma", light_gamma], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
    else:
        if GUI_flag:
            message = "gamma is set to light mode. Switching to regular mode."
            easygui.msgbox(message, title="Action")
        results = subprocess.call(["xgamma","-gamma", regular_gamma], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

