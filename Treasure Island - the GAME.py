print('''
*******************************************************************************
 ,d                                                                       
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8  
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88          
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88          
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88          
                                                                           
                                                                           
                                                               
              88           88                                 88  
              ""           88                                 88  
                           88                                 88                
 ,adPPYba,    88 ,adPPYba, 88 ,adPPYYba, 8b,dPPYba,   ,adPPYb,88  
a8P_____88    88 I8[    "" 88 ""     `Y8 88P'   `"8a a8"    `Y88  
8PP"""""""    88  `"Y8ba,  88 ,adPPPPP88 88       88 8b       88  
"8b,   ,aa    88 aa    ]8I 88 88,    ,88 88       88 "8a,   ,d88  
 `"Ybbd8"'    88 `"YbbdP"' 88 `"8bbdP"Y8 88       88  `"8bbdP"Y8 

                           ****
                         ********
                        **  ******
                         *   ******     ******
                             ******   *********
                              ****  *****   ***
                              ***  ***     **
                        *************       *
                      ******************
                     *****   H*****H*******
                     ***     H-___-H  *********
                      ***    H     H      *******
                       **    H-___-H        *****
                         *   H     H         ****
                             H     H         ***
                             H-___-H         **
                             H     H         *
                             H-___-H    

  
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Find the treasure or meet your DOOM!") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("You are at a crossroads. You can go left or right.")
choice1 = input('Which way do you want to go? Type "Left" or "Right".').lower()

if choice1 == "left":
  choice2 = input("You have come to a lake. There is an island in the middle of the lake.Do you want to swim or wait?").lower()
  if choice2 == "wait":
    choice3 = input('''The lake drains and reveals a House. You go inside and fine three doors. Which door do you want to open? Red, Yellow or Blue?  
                __________
               |  __  __  |
               | |  ||  | |
               | |  ||  | |
               | |__||__| |
               |  __  __()|
               | |  ||  | |
               | |  ||  | |
               | |  ||  | |
               | |  ||  | |
               | |__||__| |
               |__________|''').lower()
    if choice3 == "red":
      print("It's Just a Red Roo- Oops you fell in a hole. Game Over!")
    elif choice3=="yellow":
        print('''You have found the treasure!  
                 __-----__
            ..;;;--'~~~`--;;;..
          /;-~IN GOD WE TRUST~-.\
         //      ,;;;;;;;;      \\
       .//      ;;;;;    \       \\
       ||       ;;;;(   /.|       ||
       ||       ;;;;;;;   _\      ||
       ||       ';;  ;;;;=        ||
       ||LIBERTY | ''\;;;;;;      ||
        \\     ,| '\  '|><| 1995 //
         \\   |     |      \  A //
          `;.,|.    |      '\.-'/
            ~~;;;,._|___.,-;;;~'
                ''=--'
                    You win!''')
    elif choice3=="blue":
      print('''You have have to fight the Island King and his 800 Monsters. 
             .---.     .---.
            ( -o- )---( -o- )
            ;-...-`   `-...-;
           /                 \
          /                   \
         | /_               _\ |
         \`'.`'"--.....--"'`.'`/
          \  '.   `._.`   .'  /
       _.-''.  `-.,___,.-`  .''-._
      `--._  `'-._______.-'`  _.--`
           /                 \
          /.-'`\   .'.   /`'-.\
         `      '.'   '.'      `
               Game over!''')
  else:
    print('''You have been attacked by a trout.
                 |
                ,|.
               ,\|/.
             ,' .V. `.
            / .     . \
            /_`       '_\
          ,' .:     ;, `.
          |@)|  . .  |(@|
     ,-._ `._';  .  :`_,' _,-.
    '--  `-\ /,-===-.\ /-'  --`
   (----  _|  ||___||  |_  ----)
    `._,-'  \  `-.-'  /  `-._,'
             `-.___,-'  
             Game over!''')
else:
  print("You have fell into the Abyss.Game Over!")


    

  