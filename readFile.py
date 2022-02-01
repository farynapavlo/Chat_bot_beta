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
