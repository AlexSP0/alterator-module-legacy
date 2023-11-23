#!/usr/bin/env python3

from pydbus import SystemBus
from os import getenv
import sys

if(len(sys.argv) <= 1):
    sys.exit("legacy-runer: exactly one argument is required")

bus = SystemBus()
manager=bus.get("ru.basealt.alterator", "/ru/basealt/alterator")
obj=bus.get("ru.basealt.alterator", "/ru/basealt/alterator/" + sys.argv[1].split('/')[-1])

manager.SetEnvValue("DISPLAY", getenv("DISPLAY"))
manager.SetEnvValue("XAUTHORITY", getenv("XAUTHORITY"))
obj.Run()
