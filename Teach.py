def teach(user, bot):
    file = open("phrases.txt", "a")
    file.write(user[0].upper()+user[1:len(user)] + "\n-" + bot[0].upper()+bot[1:len(bot)] + "\n")
    file.close()
