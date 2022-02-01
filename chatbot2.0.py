#________________________________________________________________>
from tkinter import *


def LoadMyEntry(ChatLog, EntryText):
    if EntryText != '':
        ChatLog.config(state=NORMAL)
        if ChatLog.index('end') != None:
            LineNumber = float(ChatLog.index('end'))-1.0
            ChatLog.insert(END, "You: " + EntryText)
            ChatLog.tag_add("You", LineNumber, LineNumber+0.4)
            ChatLog.tag_config("You", foreground="blue", font=("Arial", 12, "bold"))
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)


def LoadBotEntry(ChatLog, EntryText):
    if EntryText != '':
        ChatLog.config(state=NORMAL)
        if ChatLog.index('end') != None:
            LineNumber = float(ChatLog.index('end'))-1.0
            ChatLog.insert(END, "Bot: " + EntryText)
            ChatLog.tag_add("Bot", LineNumber, LineNumber+0.4)
            ChatLog.tag_config("Bot", foreground="red", font=("Arial", 12, "bold"))
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)
#________________________________________________________________>


def read_file():
    file = open("phrases.txt", "r+")
    user_input = []
    bot_input = []
    lst = []
    help = []
    for line in file:
        if line[0] == "#":
            help.append(line[1:len(line)].rstrip("\n"))
        if line[0] == "-" and line[1] == "+" and line != "\n":
            d_s = line[2:len(line)].rstrip('\n')
            day_schedule = d_s.split(", ")
            bot_input.append(day_schedule)
        elif line[0] == "-" and line != "\n":
            bot_input.append(line[1:len(line)].rstrip('\n'))
        elif line[0] != "\n" and line[0] != "#":
            user_input.append(line.rstrip('\n'))

    lst = [user_input, bot_input, help]
    file.close()
    return lst


def teach(user, bot):
    file = open("phrases.txt", "a")
    file.write(user[0].upper()+user[1:len(user)] + "\n-" + bot[0].upper()+bot[1:len(bot)] + "\n")
    file.close()


def Bot_Answer(inp):
    user = read_file()[0]
    bot = read_file()[1]
    help = read_file()[2]

    que = inp.lower().rstrip('\n')
    ans = ''
    for i in range(len(user)):
        if que == user[i].lower():
            ans = bot[i]
            if isinstance(bot[i], list):
               ans = "\n" + "\n".join(bot[i])
            break
        elif que[0] == ">":
            ans = "You teach me!"
            teach_d = que[1:len(que)].split(">")
            if len(teach_d[1]) >= 1:
                teach(teach_d[0], teach_d[1])
            else:
                ans = "Try to teach me!"
            break
        elif que == "help()":
            ans = "\n" + "\n".join(help)
            break
        else:
            ans = "Sorry, can You repeat?"
    return ans + "\n"

#________________________________________________________________>


def ClickAction():
    EntryText = EntryBox.get("0.0", END)
    Entred = EntryText.lower().rstrip('\n')

    Answer = Bot_Answer(Entred)
    if Answer != "0" and Entred != "":
        LoadMyEntry(Chat, EntryText)
        LoadBotEntry(Chat, Answer)

    Chat.yview(END)
    EntryBox.delete("0.0", END)


def PressAction(event):
    EntryBox.config(state=NORMAL)
    ClickAction()


def DisableEntry(event):
    EntryBox.config(state=DISABLED)

# Root and geometry
root = Tk()
root.title("ChatBot Giraffe")
root.geometry('680x480')
root.resizable(width=FALSE, height=FALSE)
root["bg"] = "green"

# Giraffe image
img = PhotoImage(file="gir.png")
canv = Canvas(root, width=1250, height=620, bg='green')
canv.create_image(-70, 300, image=img)

# ChatBox
Chat = Text(root, bd=3, bg="yellow", height="8", width="53", font="Arial",)
Chat.config(state=DISABLED)

# ScrollBox
scroll = Scrollbar(root, command=Chat.yview)
Chat['yscrollcommand'] = scroll.set

# Button
photo=PhotoImage(file="message.png")
SendButton = Button(root, image=photo,
                    bd=0, bg="white", activebackground="yellow",
                    command=ClickAction, compound=LEFT)

# Entry Box
EntryBox = Text(root, bd=4, bg="white", fg="blue", width="29", height="5", font="Arial")

# Show all
scroll.place(x=570, y=6, height=380)
Chat.place(x=248,y=6, height=380, width=300)
EntryBox.place(x=248, y=401, height=50, width=300)
SendButton.place(x=570, y=401, width=50, height=50)
canv.place(x=0, y=0)

root.mainloop()
#________________________________________________________________>