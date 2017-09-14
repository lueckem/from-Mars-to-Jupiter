import cx_Freeze
import os

os.environ['TCL_LIBRARY'] = "C:\\Users\\Marvins Pc\\AppData\\Local\\Programs\\Python\\Python36\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\Marvins Pc\\AppData\\Local\\Programs\\Python\\Python36\\tcl\\tk8.6"

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="from Mars to Jupiter",
    options={"build_exe": {"packages":["pygame","random"],
                           "include_files":["highscores.txt","LICENSE.txt", "README.md", "images",
                                            "C:\\Users\\Marvins Pc\\AppData\\Local\\Programs\\Python\\Python36\\Lib\\site-packages\\pygame\\freesansbold.ttf"]}},
    executables = executables

    )



#"highscores.txt","LICENSE.txt", "README.md","images\asteroid_large.png",
#                                            "images\asteroid_medium.png", "images\asteroid_small.png", "images\ship.png",
#                                            "images\shipicon.png","images\tutorial.png"
