from loadEntry import *
from botAnswer import *

name_bot = "Bot"
name_user = "You"

# Settings
def SetgAction():
    def Save_exit():
        global name_user
        global name_bot

        EntryT1 = entry_box1.get("0.0", END)
        Entred1 = EntryT1.rstrip('\n')

        EntryT2 = entry_box2.get("0.0", END)
        Entred2 = EntryT2.rstrip('\n')
        if Entred1 != "" and len(Entred1) < 9:
            name_user = Entred1
        if Entred2 != "" and len(Entred2) < 9:
            name_bot = Entred2

        settings.destroy()

    def Cancel_exit():
        settings.destroy()

    # Settings and geometry
    settings = Tk()
    settings.title("Settings")
    settings.geometry('680x480')
    settings.resizable(width=FALSE, height=FALSE)
    settings["bg"] = "green"

    text1 = Label(settings, bd=1, bg="yellow", height="8", width="53", font="Arial", text="User name")
    text2 = Label(settings, bd=1, bg="yellow", height="8", width="53", font="Arial", text="Bot name")
    hint = Label(settings, bd=0, bg="green", height="3", font="Arial", text="(Between 1 and 8 symbols)")
    hint2 = Label(settings, bd=0, bg="green", height="3", font="Arial", text="(Between 1 and 8 symbols)")

    entry_box1 = Text(settings, bd=2, bg="white", width="29", height="15", font="Arial")
    entry_box2 = Text(settings, bd=2, bg="white", width="29", height="15", font="Arial")

    save_but = Button(settings, bd=2, text="Apply", font="Arial", bg="yellow", fg="blue", activebackground="yellow",
                            command=Save_exit, compound=LEFT)

    exit_but = Button(settings, bd=2, text="Cancel", font="Arial", bg="yellow", fg="blue", activebackground="yellow",
                      command=Cancel_exit, compound=LEFT)

    # show all
    text1.place(x=20, y=50, width=100, height=30)
    text2.place(x=20, y=90, width=100, height=30)
    hint.place(x=265, y=50, width=200, height=30)
    hint2.place(x=265, y=90, width=200, height=30)

    entry_box1.place(x=125, y=50, width=140, height=30)
    entry_box2.place(x=125, y=90, width=140, height=30)

    exit_but.place(x=450, y=401, width=80, height=50)
    save_but.place(x=550, y=401, width=80, height=50)
    settings.mainloop()


def ClickAction():
    global name_bot
    global name_user
    EntryText = EntryBox.get("0.0", END)
    Entred = EntryText.lower().rstrip('\n')

    Answer = Bot_Answer(Entred)
    if Answer != "0" and Entred != "":
        LoadMyEntry(Chat, EntryText, name_user)
        LoadBotEntry(Chat, Answer, name_bot)

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

# Button send
photo = PhotoImage(file="message.png")
SendButton = Button(root, image=photo,
                    bd=0, bg="white", activebackground="yellow",
                    command=ClickAction, compound=LEFT)
# Button settings
photo1 = PhotoImage(file="settings.png")
SettingsButton = Button(root, image=photo1,
                        bd=0, bg="white", activebackground="yellow",
                        command=SetgAction, compound=LEFT)

# Entry Box
EntryBox = Text(root, bd=4, bg="white", fg="blue", width="29", height="5", font="Arial")

# Show all
scroll.place(x=570, y=6, height=380)
Chat.place(x=248,y=6, height=380, width=300)
EntryBox.place(x=248, y=401, height=50, width=300)
SettingsButton.place(x=630, y=401, width=50, height=50)
SendButton.place(x=570, y=401, width=50, height=50)
canv.place(x=0, y=0)

root.mainloop()