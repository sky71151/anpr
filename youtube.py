import webbrowser
import time
import os

delay = 7.5
while True:

    webbrowser.open("https://www.youtube.com/shorts/HNXLdSiqouU",new=2)
    time.sleep(delay)
    webbrowser.open("https://www.youtube.com/watch?v=lEM2n0LKEcA",new=2)
    time.sleep(delay)
    webbrowser.open("https://www.youtube.com/watch?v=ldP8Vl7PtmE",new=2)
    time.sleep(delay)
    webbrowser.open("https://www.youtube.com/watch?v=H1nXTnC9JBk",new=2)
    time.sleep(delay)
    webbrowser.open("https://www.youtube.com/watch?v=Jk4QY_ehxPs",new=2)
    time.sleep(delay)
        
        
    
    os.system("taskkill /im chrome.exe /f")
    print("10 seconds passed")