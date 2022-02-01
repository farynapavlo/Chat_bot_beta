from readFile import read_file
from Teach import teach

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
