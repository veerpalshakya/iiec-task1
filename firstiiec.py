import os
print("\t\t\t Welcome To My First Python Application Program")
print("\t\t\t\t******************************")
while True:
   print("\t Tell Me What I Can Help You:",end="")
   v=input()
   
   if (("run" in v) or ("launch" in v)) and (("browser" in v) or ("chrome" in v)):
     os.system("chrome")
   
   elif (("run" in v) or ("launch" in v)) and ("wmplayer" in v) :
     os.system("wmplayer")
   
   
   elif (("run" in v) or ("launch" in v)) and (("camera" in v) or ("camera" in v)):
     os.system("camera")

   elif (("run" in v) or ("launch" in v)) and (("team" in v) or ("viewer" in v)):
     os.system("TeamViewer")

   elif (("run" in v) or ("launch" in v)) and ("calculator" in v) :
     os.system("calculator")
 
   elif (("run" in v) or ("launch" in v)) and (("vlc" in v) or ("videoplayer" in v)):
     os.system("vlc player")
  
   elif (("run" in v) or ("launch" in v)) and ("calendar" in v) :
     os.system("calendar")
   elif ("exit" in v) and ("back" in v) :
        print("we are closing the program! ")
        os.system(exit())
        break