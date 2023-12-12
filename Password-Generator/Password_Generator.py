import random
import time
import os

from pystyle import Colors, Write


def skip():
    print("""





    """)

def creator():
    skip()
    print("""




    """)
    Write.Print("                                    ",Colors.white_to_blue, interval=0)
    Write.Print("This Tool Was Made By 42.4c.41.43.4b.20.46.55.43.4b",Colors.white, interval=0.01)
    time.sleep(0.5)
    os.system("cls")
creator()

def error():
    Write.Print("""                                         ᲼_______᲼______᲼______᲼᲼᲼_____᲼᲼______᲼᲼\n""",
                Colors.red_to_yellow, interval=0.00001)
    Write.Print("""                                         (_______|_____᲼(_____᲼\᲼/᲼___᲼\(_____᲼\\\n""",
                Colors.red_to_yellow, interval=0.00001)
    Write.Print("""                                         ᲼_____᲼᲼᲼_____)᲼)____)᲼)᲼|᲼᲼᲼|᲼|_____) )\n""",
                Colors.red_to_yellow, interval=0.00001)
    Write.Print("""                                         |᲼᲼___)᲼(_____᲼(_____᲼(|᲼|᲼᲼᲼|᲼(_____ ( \n""",
                Colors.red_to_yellow, interval=0.00001)
    Write.Print("""                                         |᲼|_____᲼᲼᲼᲼᲼᲼|᲼|᲼᲼᲼᲼|᲼|᲼|___|᲼|᲼᲼᲼᲼᲼| |\n""",
                Colors.red_to_yellow, interval=0.00001)
    Write.Print("""                                         |_______)᲼᲼᲼᲼᲼|_|᲼᲼᲼᲼|_|\_____/᲼᲼᲼᲼᲼᲼|_|\n""",
                Colors.red_to_yellow, interval=0.00001)
    print()

def text():
    skip()
    Write.Print("""                                  ᲼╔═╗╔═╗╔═╗╔═╗╦᲼╦╔═╗╦═╗╔╦╗᲼᲼╔═╗╔═╗╔╗╔╔═╗╦═╗╔═╗╔╦╗╔═╗╦═╗\n""",
                Colors.white_to_blue, interval=0.0001)
    Write.Print("""                                  ᲼╠═╝╠═╣╚═╗╚═╗║║║║᲼║╠╦╝᲼║║᲼᲼║᲼╦║╣᲼║║║║╣᲼╠╦╝╠═╣᲼║᲼║᲼║╠╦╝\n""",
                Colors.white_to_blue, interval=0.0001)
    Write.Print("""                                  ᲼╩᲼᲼╩᲼╩╚═╝╚═╝╚╩╝╚═╝╩╚══╩╝᲼᲼╚═╝╚═╝╝╚╝╚═╝╩╚═╩᲼╩᲼╩᲼╚═╝╩╚═\n""",
                Colors.white_to_blue, interval=0.0001)
    print()

def password_generator():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "0123456789"
    symbols = """[]{}()*;/,._-'"!@#$%^&*"""
    all = lower + upper + number + symbols
    while True:
        try:
            text()
            Write.Print("                                                  ", Colors.white, interval=0)
            how_many = int(Write.Input("How Many Passwords? -> "
                                       , Colors.white_to_blue,interval=0.01))
            os.system("cls")
            text()
            Write.Print("                                                   (Max = 84 Min = 7)\n", Colors.white_to_green, interval=0)
            Write.Print("                                                ", Colors.white, interval=0)
            lenght0 = int(Write.Input("How Many characters -> ",
                            Colors.white_to_blue, interval=0.0001))
            if lenght0 >= 85:
                os.system("cls")
                skip()
                error()
                Write.Print("                                                     ", Colors.white, interval=0)
                Write.Print(" Password is too Long!\n",
                            Colors.red_to_yellow, interval=0.00001)
                time.sleep(0.7)
                os.system("cls")
            elif lenght0 <= 7:
                os.system("cls")
                skip()
                error()
                Write.Print("                                                     ", Colors.white, interval=0)
                Write.Print("Password is too Short!\n",
                            Colors.red_to_yellow, interval=0.00001)
                time.sleep(0.7)
                os.system("cls")
            else:
                break
        except:
            os.system("cls")
            skip()
            error()
            Write.Print("                                                     ", Colors.white, interval=0)
            Write.Print("Invalid Option!",
                        Colors.red_to_yellow, interval=0.00001)
            time.sleep(0.7)
            os.system("cls")
    print()
    with open("Passwords.txt", "a") as f:
        f.write("___________________________________________________________________________________NEW_LINE___________________________________________________________________________________\n")
    for i in range(how_many):
        length1 = (lenght0)
        password = "".join(random.sample(all, length1))
        mid_screen = password.center(123)
        print(mid_screen + "\n")
        time.sleep(0.002)
        with open("Passwords.txt", "a") as f:

            f.write(password + "\n")
    with open("Passwords.txt", "a") as f:
        f.write("___________________________________________________________________________________END_LINE___________________________________________________________________________________")
    time.sleep(0.5)
    os.system("cls")
    text()
    Write.Print("                                                    ",Colors.white_to_blue, interval=0)
    Write.Print("Saving Passwords...", Colors.white_to_blue, interval=0.03)
    time.sleep(0.5)
    os.startfile("Passwords.txt")

try:
    open ("Passwords.txt", "r")
    while True:
        try:
            text()
            Write.Print("                                             ", Colors.white_to_blue, interval=0)
            deletefile = Write.Input("Delete Old Password File? y/n-> ", Colors.white_to_blue, interval=0.01)
            if deletefile == "y":
                try:
                    os.remove("Passwords.txt")
                    os.system("cls")
                    break
                except:
                    os.system("cls")
                    skip()
                    error()
                    Write.Print("                                               ", Colors.white_to_blue, interval=0)
                    Write.Print("The File Is Already Deleted!", Colors.white_to_blue, interval=0.004)
                    time.sleep(0.7)
                    os.system("cls")
                    break
            elif deletefile == "n":
                os.system("cls")
                break
            else:
                error()
                Write.Print("                                           ", Colors.white_to_blue, interval=0)
                Write.Print("You Did Not Enter A Valid Option!", Colors.white_to_blue, interval=0.004)
        except KeyboardInterrupt:
            os.system("cls")
            skip()
            error()
            Write.Print("                                                       You pressed Ctrl+C!",
                        Colors.red_to_yellow,
                        interval=0.00001)
            time.sleep(0.7)
            os.system("cls")
except:
    ()

try:
    password_generator()
except:
    os.system("cls")
    skip()
    error()
    Write.Print("                                                       You pressed Ctrl+C!", Colors.red_to_yellow,
                interval=0.00001)
    time.sleep(0.7)
    os.system("cls")
finally:
    os.system("cls")
    text()
    Write.Print("                                                 Resestting in 5 seconds...", Colors.white_to_red,
                interval=0.001)
    time.sleep(5)
    os.system("cls")
    password_generator()