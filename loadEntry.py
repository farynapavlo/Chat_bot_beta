from tkinter import *


def LoadMyEntry(ChatLog, EntryText, name="You"):
    if EntryText != '':
        ChatLog.config(state=NORMAL)
        if ChatLog.index('end') != None:
            LineNumber = float(ChatLog.index('end'))-1.0
            ChatLog.insert(END, name + ": " + EntryText)
            ChatLog.tag_add(name, LineNumber, LineNumber+(len(name)+1)/10)
            ChatLog.tag_config(name, foreground="blue", font=("Arial", 12, "bold"))
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)


def LoadBotEntry(ChatLog, EntryText, name="Bot"):
    if EntryText != '':
        ChatLog.config(state=NORMAL)
        if ChatLog.index('end') != None:
            LineNumber = float(ChatLog.index('end'))-1.0
            ChatLog.insert(END, name + ": " + EntryText)
            ChatLog.tag_add(name, LineNumber, LineNumber+(len(name)+1)/10)
            ChatLog.tag_config(name, foreground="red", font=("Arial", 12, "bold"))
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)
