import google.generativeai as genai
import CRED
import genai
import os
from datetime import datetime
import platform
import time as t 

print(" ")
print(" ")
print(" ")
print("Terminal version ==>> 0.0.1 \n ")
print(" ")
print(" ")
print(" ")



username = os.getlogin()

API = "b1e97386b32ebf958a9c462b1a20cf55-b70eb1e7-a8d6-4d3b-aff1-a6fd86fe99fb"

AI_name = "ALPIX"

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'



def help():
    print(" ---- To check Version ---->> " + color.GREEN + " v- info " + color.END)
    print(" ---- To Close Terminal ---->>"  + color.GREEN + " exit " + color.END)
    print(" ---- To start calculator ---->> " + color.GREEN + " ca.ex " + color.END)
    print(" ---- To use Terminal " + color.BLUE + "AI" + color.END + color.RED +" still in development progress " + color.END)
    print(" ---- To open any files ---->>> " + color.GREEN + " f- open " + color.END)
    print(" ---- To scan all the folders from the desktop ====>>> " + color.GREEN + "d- scan" + color.END)
    print(" ---- To check Time ---->>" +color.GREEN + " t- c" + color.END)
    print(" ---- To check about system ---->>  " +color.BLUE + "sys- info" + color.END)
    print(" ---- To Update Terminal ==>> " + color.BLUE + "Terminal- up" + color.END)


def version():
    print(" --- current version is " + color.BLUE + "0.0.1 " + color.END +"---" )
    print(" Under " + color.RED + "DEVELOPMENT" + color.END)


def calculator():
    f_1 = int(input("Please enter the first number \n"))
    op = str(input("choose the operation \n "))
    f_2 = int(input("Please enter the second number \n"))
    if op == "+":
        print(" ")
        print(f_1 + f_2 , " \n ")




def AI(command2):
    import genai
    
    genai.configure(api_key=CRED.KEY)
    # Set up the model
    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }
    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]
    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                   generation_config=generation_config,
                                   safety_settings=safety_settings)
    convo = model.start_chat(history=[
        {
            "role": "user",
            "parts": (CRED.intro)
        },
        {
            "role": "model",
            "parts": (CRED.intro)
        },
    ])





    received = convo.send_message(command2)
    rev = convo.last.text
    f_1 = (rev.replace("*"," "))
  #  DATABASE(JARVIS=f_1)
    print(f"{AI_name}" +  f_1)


def file():
    raw = str(input(" ENTER THE " + color.BLUE + "FILE" + color.END  + " name == >> "))
    try:
        os.startfile(fr"C:\Users\{username}\OneDrive\Desktop\{raw}")
        print(f"file opened " + color.GREEN + str(raw) + color.END)
    except:
        print(f"unnable to find " + color.RED + str(raw) + color.END)

def pri():
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    folders = [folder for folder in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, folder))]
    for folder in folders:
        print(folder)

def print_system_info():
    print("System Information:")
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"Python Version: {platform.python_version()}")
    print(f"Processor: {platform.processor()}")
    print(f"Machine: {platform.machine()}")





def update():
    print(" This may take some " + color.RED + "TIME" + color.END)
    t.sleep(4)
    i = 0 
    while i < 100:
        print("CHECKING FOR " + color.BLUE + "UPDATE" +color.END)
        if i == 50:
            print("CHECKING FOR " + color.RED + "UPDATE" +color.END)
      
        i = i +1



def time():
    current_time = datetime.now().strftime('%I:%M:%S %p')
    print("Current" + color.BLUE + " Time" + color.END + " Is " + current_time)
while True:
    print(" ")
    command = str(input(f" TERMINAL / {username} / ==>>> "))
    if command == "v- info":
        version()
    elif command =="help":
        help()
    elif command =="ca.ex":
        calculator()
    elif command == "AI":
        command2 = input(" CHAT WITH AI == > ")
        AI(command2)
    elif command == "f- open":
        file()
    elif command =="d- scan":
        pri()
    elif command =="t- c":
        time()
    elif command =="sys- info":
        print_system_info()
    elif command == "Terminal- up":
        update()
    elif command =="exit" or command =="close":
        print(color.RED + " CLOSING TERMINAL " + color. END)
        exit()
    else:
        print( color.RED + " Unknown Command Please choose correct one or enter help " + color.END)