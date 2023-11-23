#!/bin/bash


dbus-send --system --dest=ru.basealt.alterator --print-reply --type=method_call /ru/basealt/alterator ru.basealt.alterator.manager.SetEnvValue string:'DISPLAY' string:':0'
dbus-send --system --dest=ru.basealt.alterator --print-reply --type=method_call /ru/basealt/alterator ru.basealt.alterator.manager.SetEnvValue string:'XAUTHORITY' string:'$XAUTHORITY'
dbus-send --system --dest=ru.basealt.alterator --print-reply --type=method_call /ru/basealt/alterator/auth ru.basealt.alterator.legacy.Run 
