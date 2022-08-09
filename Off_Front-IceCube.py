# Off_Front-IceCube
'''
Written by: Mikhail Patricio Ortiz-Lunyov
for the:    IceCube AfterSchool 2021-2022 Virtual Internship

This program is released under GPLv3 License:
    
    "Offline Front-End for Icecube" is a terminal program written in python that acts as a CLI (and optionally offline) front-end for the IceCube website.
    Copyright (C) 2022  Mikhail P. Ortiz-Lunyov

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
import time
import os
from urllib.request import urlopen

# Function below prints a small error messege
def InvalidInput():
    print("Invalid Input, please enter a number option!\n")

# Functioj below allows for cross-platform clearing of the screen
def ClearScreen():
    # If Windows OS, 'clr'
    if os.name == 'nt':
        os.system('cls')
    # Else UNIX, 'clear'
    else:
        os.system('clear')

# Function below allows for resuming or cutting of other functions as the user wants
def Resume():
    resume = input(" : ")
    if resume == "main" or resume == "\"main\"":
        main_menu()

# Function below prints a small splash screen with instructions to the user
def Reminder():
    print(" ----------------------------------------------------------------------------------------------")
    print("| In order to return to main menu, type \"main\" in any prompt. Otherwise, press any other key |")
    print(" ----------------------------------------------------------------------------------------------")

# Function below reads local saved webpages
def Read_Page(filename):
    ClearScreen()
    ReadPage = open(filename, "r")
    for line in ReadPage:
        if line.startswith('<p>'):
            TEXT = line
            clean_TEXT0 = TEXT.replace("<p>","")
            clean_TEXT1 = clean_TEXT0.replace(" <a href=","")
            clean_TEXT2 = clean_TEXT1.replace("</a>","")
            clean_TEXT3 = clean_TEXT2.replace("</p>","")
            clean_TEXT4 = clean_TEXT3.replace("&#8217;","")
            clean_TEXT5 = clean_TEXT4.replace("data-type=\"page\" data-id=\"373\"", "")
            clean_TEXT6 = clean_TEXT5.replace("target=\"_blank\" rel=\"noreferrer noopener\"","")
            clean_TEXT7 = clean_TEXT6.replace("&nbsp;","")
            fTEXT = clean_TEXT7.replace(">"," ")
            print(fTEXT)
    input("---\nIf you are done, press [Enter] to continue\n")
    Saved_Pages()

# Function below checks files for .IceBit file extension
def File_Check(filecheck,fileaction,fileperform):
    if ".IceBit" not in filecheck != "1":
        print("Cannot access files without \'.IceBit\' extension")
    else:
        if fileaction == "read":
            Read_Page(fileperform)
        elif fileaction == "delete":
            os.remove(fileperform)
            print("File Deleted")
            time.sleep(2)

# Function below manages downloaded webpages
def Saved_Pages():
    ClearScreen()
    print("\n [ ^-Main>Website>Saved_Pages ]\n")
    while True:
        print("Choose any option to manage your locally-saved webpages:")
        Manage_Saved = input("\n [1] Select to Read\n [2] Print All Saved\n [3] Delete\n [4] Delete All(!)\n [5] List Directory\n ---\n [6] Clean up the Screen\n [7] Back\n [8] Main menu\n > ")
        if Manage_Saved == "1":
            print(os.listdir(path='.'))
            while True:
                print("Type accurately! Names are Case-Sensitive, include file extension. If you feel unsure, type \"back\".")
                Read_One = input(" Insert name:\n < ")
                if Read_One == "\"back\"" or Read_One == "back" or Read_One == "\"Back\"" or Read_One == "Back":
                    Saved_Pages()
                    break
                elif Read_One == "Off_Front-IceCube.py" or Read_One == "\"Off_Front-IceCube.py\"":
                    print("You cannot destroy the program file!")
                else:
                    if os.path.exists(Read_One) == True:
                        File_Check(Read_One, "read", Read_One)
                        break
                    else:
                        print("File does not exist, Try again!")
                        continue
        elif Manage_Saved == "2":
            print("/ -All saved:- \ ")
            print(os.listdir(path='.'))
            print("\              /\n")
        elif Manage_Saved == "3":
            print(os.listdir(path='.'))
            while True:
                print("Type accurately! Names are Case-Sensitive, include file extension. If you feel unsure, type \"back\". ")
                Del_One = input(" Insert name:\n < ")
                if Del_One == "\"back\"" or Del_One == "back" or Del_One == "Back" or Del_One == "\"Back\"":
                    Saved_Pages()
                    break
                elif Del_One == "Off_Front-IceCube.py" or Del_One == "\"Off_Front-IceCube.py\"" or Del_One == "README.txt" or Del_One == "\"README.txt\"" or Del_One == "GPLv3_Full_License.txt" or Del_One == "\"GPLv3_Full_License.txt\"":
                    print("You cannot destroy the program or other vital files!")
                else:
                    if os.path.exists(Del_One) == True:
                        File_Check(Del_One, "delete", Del_One)
                        break
                    else:
                        print("File does not exist, Try again!")
                        continue
        elif Manage_Saved == "4":
            print("WARNING! YOU HAVE JUST SELECTED TO DELETE ALL OF YOUR SAVED FILES!.\nIn order to get them again, you will have to have an internet connection!!")
            Del_All = input("Are you sure you want to DELETE ALL saved pages?\n [1] No\n [2] Yes\n > ")
            if Del_All == "1":
                Saved_Pages()
            elif Del_All == "2":
                for item in os.listdir(path='.'):
                    if item.endswith(".IceBit"):
                        os.remove(os.path.join('.', item))
                print("All files deleted!")
            else:
                InvalidInput()
        elif Manage_Saved == "5":
            print(os.listdir(path='.'))
        elif Manage_Saved == "6":
            Saved_Pages()
        elif Manage_Saved == "7":
            Website_Hub()
        elif Manage_Saved == "8":
            main_menu()
        else:
            InvalidInput()
            continue

# Function below prints likely questions and answers that end users may have
def FAQ():
    ClearScreen()
    print("\n [ ^-Main>FAQ ]\n")
    Reminder()
    time.sleep(1)
    print("\nI do not understand how to navigate this program.")
    time.sleep(2)
    print(" In the Main Menu, the second option [2] describes exactly how to use this program and navigate it.")
    Resume()
    print("\nWhat is IceCube?")
    time.sleep(2)
    print(" The IceCube Neutrino Observatory is a telescope in Antarctica that searches for Neutrinos")
    Resume()
    print("\nWhat are neutrinos?")
    time.sleep(2)
    print(" Neutrinos are subatomic particles that rarely, if ever interact with any other matter in space.")
    time.sleep(2)
    print(" (Fun Fact: There may be as many as at least 65 million neutrinos passing through your fingernail by the time that you are reading this peice of text!)")
    Resume()
    print("\nHow is this program released?")
    time.sleep(2)
    print(" Offline Front-End for IceCube is released as Free/Libre and Open-Source Software")
    Resume()
    print("\nUnder what license is this program under?")
    time.sleep(2)
    print(" This program is licensed under the GNU Public License, a free software license.")
    print(" To learn more, please go to the Legal & License menu.")
    Resume()
    print("\nWhat are my usage, redistribution, and overall editing/remixing rights to this program?")
    time.sleep(2)
    print(" In short, you may remix/fork this program as long as the code is also open-source and credits the original author (Mikhail P. Ortiz-Lunyov)")
    time.sleep(1)
    print(" HOWEVER, please reference the GNU Public License provided in the Legal & License menu in the program.\n It is under the the option of [4] in the main menu")
    Resume()
    print("\nDoes this Program have a Privacy Policy? If so, what is it?")
    time.sleep(2)
    print(" This program does have a privacy policy. You may check it under the Legal & License page.")
    time.sleep(1)
    print(" Directory: [ Legal&License -> Privacy_Policy ]")
    Resume()
    time.sleep(3)
    input("You will now return back to Main Menu:\n")
    main_menu()

# Function below prints instructions to the user on how to use the program
def Tutorial():
    ClearScreen()
    print("\n [ ^-Main>Tutorial ]\n")
    Reminder()
    print("This program allows you to download and save text from the IceCube Website.")
    Resume()
    print("There is a variety of symbols that one will encounter in this program.")
    time.sleep(1)
    print(" Essentially, they are \" : \" for any input,\n\" > \" for specific options listed,\n modifications of the previous symbol indicates a deeper set of options from the previous menu,\n and\n \" < \" for a custom input, depending on the curcumstances (This is seen the rarest)")
    Resume()
    print("There is a menu system that allows to go to other, smaller menus to do different tasks.")
    Resume()
    print("You can see a path of the menus above every new screen you go to. The Main Menu's path is [ ^-Main] .")
    Resume()
    print("This current page's path is visible above")
    Resume()
    print("When you go to the Website-Hub and go to download webpages, there will be a series of presets available to optimise your download experience.")
    Resume()
    print("Parts of the Website-Hub also deal with reading and managing the downloaded webpages.")
    Resume()
    print("Please note that the python program uses the local directory that the user is executing it from,\n so be sure to use this program  when in the same folder.")
    Resume()
    print("In order to properly read the files, you need to use the read function of this program.")
    Resume()
    print("The .IceBit (a play-on words of \'IceCube\' and computer \'bit\') files contain the raw HTML of the specific pages, so the read function filters it out.")
    Resume()
    print("One can delete saved pages in the Website-Hub.")
    Resume()
    print("However, it may just be more convenient to delete them using a terminal or file-manager.")
    Resume()
    print("Just be careful not to delete the .py program file! :)")
    Resume()
    print("It is also possible to use a custom URL in the Website-Hub if provided,\n but this is sub-optimal and it is strongly encouraged to use the presets available for greater convenience.")
    Resume()
    print("You may notice that there are three dashes \" --- \" above certain options in any menu.")
    Resume()
    print("This is to indicate that these options deal with changing menus and cleaning up the screen.")
    Resume()
    print("These are the basics on how to use this program. For the Frequently Asked Questions, go to option [3] in the main menu.")
    Resume()
    input("You will now return back to Main Menu:\n")
    main_menu()

# Function below prints the full GPLv3 License
def Full_License():
    ClearScreen()
    print("\n [^-Main>Legal&License>Full_GPLv3]\n")
    Reminder()
    ReadFullLicense = open("GPLv3_Full_License.txt", "r")
    print(ReadFullLicense.read())
    Resume()
    input("---\nYou will now return to the Legal & License page.\n")
    Legal_n_License()

# Function below gives added usability to the Legal_n_License() function below
def Short_License():
    ClearScreen()
    print("\n [^-Main>Legal&License>Short_Form]\n")
    while True:
        print("\"Offline Front-End for IceCube\" Copyright (C) 2022 Mikhail P. Ortiz-Lunyov")
        print("This program comes with ABSOLUTELY NO WARRANTY; for details, select option [1].")
        print("This is free software, and you are welcome to redistribute it")
        print("under certain conditions; select option [2] for more details")
        Sh_Legal_Input = input("\n [1] Warrenty Information\n [2] Redistribution Conditions\n ---\n [3] Back\n [4] Main Menu\n > ")
        if Sh_Legal_Input == "1":
            print("[In Development]")
            continue
        elif Sh_Legal_Input == "2":
            print("[In Development]")
            continue
        elif Sh_Legal_Input == "3":
            Legal_n_License()
        elif Sh_Legal_Input == "4":
            main_menu()
        else:
            InvalidInput()
            continue

# Function below prints out the Privacy Policy of this program
def Privacy_Policy():
    ClearScreen()
    print("\n [^-Main>Legal&License>Privacy_Policy]\n")
    Reminder()
    print(" This program does not record, sell, or redistribute any user data in any way.")
    Resume()
    print(" The developer (Mikhail Patricio Ortiz-Lunyov) has no way to know about how the user interacts this program, as well as the Operating system (OS),\n desktop environment, etc that this program may be situated in.")
    Resume()
    print(" This program only uses internet connection and bandwidth in order to fufill its job (extracting data from the IceCube Neutrino Observatory website),\n and for nothing else.")
    Resume()
    print(" All of above promises and statements can be verified, as this program is released as Free/Libre and Open-Source Software.")
    Resume()
    print(" Please see information about this license this under the Legal & License menu")
    input("---\nYou will now return to the Legal & License page.\n")
    Legal_n_License()

# Function below helps explain the legal license that this program is under, as well as its terms and conditions
def Legal_n_License():
    ClearScreen()
    print("\n [ ^-Main>Legal&License ]\n")
    while True:
        print("This program is licensed under the GNU Public License Version 3 (GPLv3). To learn more, continue below:")
        Legal_Input = input("\n [1] Short Form \n [2] Full GPLv3\n [3] Privacy Policy\n ---\n [4] Main Menu\n > ")
        if Legal_Input == "1":
            Short_License()
        elif Legal_Input == "2":
            Full_License()
        elif Legal_Input == "3":
            Privacy_Policy()
        elif Legal_Input == "4":
            main_menu()
        else:
            InvalidInput()
            continue

# Function below allows for usability of Preset_Saves() function
def Preset_Save_Prepare(filename_s,filename_var, weeknumber, var_name_Pre, var_name_HTML, var_name_HTML_Pre, URL):
    #CheckPath = 'Saved_Pages/'+ filename_s
    if os.path.exists(filename_s) == True:
        print("Already exists")
    else:
        # Creates/Overwrites existing file
        filename_var = open(filename_s, "w")
        # Accesses URL
        var_name_Pre = urlopen(URL)
        # Extracts HTML Raw Data
        var_name_HTML_Pre = var_name_Pre.read()
        # Decodes HTML Data into better format
        var_name_HTML = var_name_HTML_Pre.decode("utf-8")
        # Writes HTML Data into file
        filename_var.write(var_name_HTML)
        # Closes file
        filename_var.close()

# Function below adds usability to the Page_Save() function
def Preset_Saves():
    ClearScreen()
    print("\n [ ^-Main>Website-Hub>Page_Save>Presets ]\n")
    while True:
        print("\nThis is where one can saved pre-ordered pages. This can be used to test if everything is working, or just a simple way to easily access certain pages.\n There are several options below:")
        print("  (The following are ready to download/update)")
        Preset_Options = input("\n [1] Life @ Pole\n [2] Outreach\n [3] Science\n [4] About Us\n [5] Download All\n ---\n [6] Clear Screen \n [7] Back\n [8] Main Menu\n > ")
        # Life @ Pole
        if Preset_Options == "1":
            while True:
                Preset_Options1 = input("\n| [1] Antarctic Animals\n| [2] Weather in Antartica\n| [3] Working at the Pole\n| [4] Daily Life\n ---\n| [5] Back\n \_> ")
                if Preset_Options1 == "1":
                    Preset_Save_Prepare("Antarctic_Animals.IceBit", "AA_Page", 0, "AA_Page_Pre", "AA_Page_HTML_Pre", "AA_Page_HTML", "https://icecube.wisc.edu/pole/animals/")
                elif Preset_Options1 == "2":
                    Preset_Save_Prepare("Antarctic_Weather.IceBit", "AW_Page", 0, "AW_Page_Pre", "AW_Page_HTML_Pre", "AW_Page_HTML", "https://icecube.wisc.edu/pole/weather/")
                elif Preset_Options1 == "3":
                    Preset_Save_Prepare("WorkingatPole.IceBit", "WP_Page", 0, "WP_Page_Pre", "WP_Page_HTML_Pre", "WP_Page_HTML", "https://icecube.wisc.edu/pole/work/")
                elif Preset_Options1 == "4":
                    Preset_Save_Prepare("Daily_Life.IceBit", "DL_Page", 0, "DL_Page_Pre", "DL_Page_HTML_Pre", "DL_Page__HTML", "https://icecube.wisc.edu/pole/daily-life/")
                elif Preset_Options1 == "5":
                    Preset_Saves()
                else:
                    InvalidInput()
                    continue
        # Outreach
        elif Preset_Options == "2":
            while True:    
                Preset_Options2 = input("\n| [1] IceCube and Neutrinos\n| [2] Educational Programs\n| [3] Activities and Resources\n| [4] Connect with Us\n ---\n| [5] Back\n \_> ")
                if Preset_Options2 == "1":
                    Preset_Save_Prepare("IceCube_&_Neutrinos.IceBit", "IcN_Page", 0, "IcN_Page_Pre", "IcN_Page_HTML_Pre", "IcN_Page_HTML", "https://icecube.wisc.edu/outreach/neutrinos/")
                elif Preset_Options2 == "2":
                    Preset_Save_Prepare("Educational_Programs.IceBit", "EP_Page", 0, "EP_Page_Pre", "EP_Page_HTML_Pre", "EP_Page_HTML", "https://icecube.wisc.edu/outreach/students/")
                elif Preset_Options2 == "3":
                    Preset_Save_Prepare("Activities_and_Resources.IceBit", "AR_Page", 0, "AR_Page_Pre", "AR_Page_HTML_Pre", "AR_Page_HTML", "https://icecube.wisc.edu/outreach/activities/")
                elif Preset_Options2 == "4":
                    Preset_Save_Prepare("Connect_with_Us.IceBit", "CU_Page", 0, "CU_Page_Pre", "CU_Page_HTML_Pre", "CU_Page_HTML", "https://icecube.wisc.edu/outreach/connect/")
                elif Preset_Options2 == "5":
                    Preset_Saves()
                else:
                    InvalidInput()
                    continue
        # Science
        elif Preset_Options == "3":
            while True:
                Preset_Options3 = input("\n| [1] Research Highlights\n| [2] IceCube\n| [3] Beyond IceCube\n| [4] Data Releases\n| [5] Real-Time Alerts\n ---\n| [6] Back\n \_> ")
                if Preset_Options3 == "1":
                    Preset_Save_Prepare("Research_Highlights.IceBit", "RH_Page", 0, "RH_Page_Pre", "RH_Page_HTML_Pre", "RH_Page_HTML", "https://icecube.wisc.edu/science/research/")
                elif Preset_Options3 == "2":
                    Preset_Save_Prepare("IceCube.IceBit", "Ice_Page", 0, "Ic_Page_Pre", "Ic_Page_HTML_Pre", "Ic_Page_HTML", "https://icecube.wisc.edu/science/icecube/")
                elif Preset_Options3 == "3":
                    Preset_Save_Prepare("Beyond_IceCube.IceBit", "BIc_Page", 0, "BIc_Page_Pre", "BIc_Page_HTML_Pre", "BIc_Page_HTML", "https://icecube.wisc.edu/science/beyond/")
                elif Preset_Options3 == "4":
                    Preset_Save_Prepare("Data_Releases.IceBit", "DR_Page", 0, "DR_Page_Pre", "DR_Page_HTML_Pre", "DR_PAGE_HTML", "https://icecube.wisc.edu/science/data-releases/")
                elif Preset_Options3 == "5":
                    Preset_Save_Prepare("Real-Time_Alerts.IceBit", "RTA_Page", 0, "RTA_Page_Pre", "RTA_Page_HTML_Pre", "RTA_Page_HTML", "https://icecube.wisc.edu/science/real-time-alerts/")
                elif Preset_Options3 == "6":
                    Preset_Saves()
                else:
                    InvalidInput()
                    continue
        # About Us
        elif Preset_Options == "4":
            while True:
                Preset_Options4 = input("\n| [1] IceCube Overview\n| [2] Press Guide\n| [3] FAQs\n| [4] IceCube Quick Facts\n| [5] #IceCube10\n ---\n| [6] Back\n \_>")
                if Preset_Options4 == "1":
                    Preset_Save_Prepare("IceCube_Overview.IceBit", "IcO_Page", 0, "IcO_Page_Pre", "IcO_Page_HTML_Pre", "IcO_Page_HTML", "https://icecube.wisc.edu/about-us/overview/")
                elif Preset_Options4 == "2":
                    Preset_Save_Prepare("Press_Guide.IceBit", "PG_Page", 0, "PG_Page_Pre", "PG_Page_HTML_Pre", "PG_Page_HTML", "https://icecube.wisc.edu/press-guide/")
                elif Preset_Options4 == "3":
                    Preset_Save_Prepare("FAQs.IceBit", "FAQ_Page", 0, "FAQ_Page_Pre", "FAQ_Page_HTML_Pre", "FAQ_Page_HTML", "https://icecube.wisc.edu/about-us/faq/")
                elif Preset_Options4 == "4":
                    Preset_Save_Prepare("IceCube_Quick_Facts.IceBit", "IcQF_Page", 0, "IcQF_Page_Pre", "IcQF_Page_HTML_Pre", "IcQF_Page_HTML", "https://icecube.wisc.edu/about-us/facts/")
                elif Preset_Options4 == "5":
                    Preset_Save_Prepare("IceCube10.IceBit", "Ic10_Page", 0, "Ic10_Page_Pre", "Ic10_Page_HTML_Pre", "Ic10_Page_HTML", "https://icecube.wisc.edu/icecube10/")
                elif Preset_Options4 == "6":
                    Preset_Saves()
                else:
                    InvalidInput()
                    continue
        # Download All
        elif Preset_Options == "5":
            print("Preparing full download, be patient:")
            Preset_Save_Prepare("Antarctic_Animals.IceBit", "AA_Page", 0, "AA_Page_Pre", "AA_Page_HTML_Pre", "AA_Page_HTML", "https://icecube.wisc.edu/pole/animals/")
            Preset_Save_Prepare("Antarctic_Weather.IceBit", "AW_Page", 0, "AW_Page_Pre", "AW_Page_HTML_Pre", "AW_Page_HTML", "https://icecube.wisc.edu/pole/weather/")
            Preset_Save_Prepare("WorkingatPole.IceBit", "WP_Page", 0, "WP_Page_Pre", "WP_Page_HTML_Pre", "WP_Page_HTML", "https://icecube.wisc.edu/pole/work/")
            Preset_Save_Prepare("Daily_Life.IceBit", "DL_Page", 0, "DL_Page_Pre", "DL_Page_HTML_Pre", "DL_Page__HTML", "https://icecube.wisc.edu/pole/daily-life/")
            Preset_Save_Prepare("IceCube_&_Neutrinos.IceBit", "IcN_Page", 0, "IcN_Page_Pre", "IcN_Page_HTML_Pre", "IcN_Page_HTML", "https://icecube.wisc.edu/outreach/neutrinos/")
            Preset_Save_Prepare("Educational_Programs.IceBit", "EP_Page", 0, "EP_Page_Pre", "EP_Page_HTML_Pre", "EP_Page_HTML", "https://icecube.wisc.edu/outreach/students/")
            Preset_Save_Prepare("Activities_and_Resources.IceBit", "AR_Page", 0, "AR_Page_Pre", "AR_Page_HTML_Pre", "AR_Page_HTML", "https://icecube.wisc.edu/outreach/activities/")
            Preset_Save_Prepare("Connect_with_Us.IceBit", "CU_Page", 0, "CU_Page_Pre", "CU_Page_HTML_Pre", "CU_Page_HTML", "https://icecube.wisc.edu/outreach/connect/")
            Preset_Save_Prepare("Research_Highlights.IceBit", "RH_Page", 0, "RH_Page_Pre", "RH_Page_HTML_Pre", "RH_Page_HTML", "https://icecube.wisc.edu/science/research/")
            Preset_Save_Prepare("IceCube.IceBit", "Ice_Page", 0, "Ic_Page_Pre", "Ic_Page_HTML_Pre", "Ic_Page_HTML", "https://icecube.wisc.edu/science/icecube/")
            Preset_Save_Prepare("Beyond_IceCube.IceBit", "BIc_Page", 0, "BIc_Page_Pre", "BIc_Page_HTML_Pre", "BIc_Page_HTML", "https://icecube.wisc.edu/science/beyond/")
            Preset_Save_Prepare("Data_Releases.IceBit", "DR_Page", 0, "DR_Page_Pre", "DR_Page_HTML_Pre", "DR_PAGE_HTML", "https://icecube.wisc.edu/science/data-releases/")
            Preset_Save_Prepare("Real-Time_Alerts.IceBit", "RTA_Page", 0, "RTA_Page_Pre", "RTA_Page_HTML_Pre", "RTA_Page_HTML", "https://icecube.wisc.edu/science/real-time-alerts/")
            Preset_Save_Prepare("IceCube_Overview.IceBit", "IcO_Page", 0, "IcO_Page_Pre", "IcO_Page_HTML_Pre", "IcO_Page_HTML", "https://icecube.wisc.edu/about-us/overview/")
            Preset_Save_Prepare("Press_Guide.IceBit", "PG_Page", 0, "PG_Page_Pre", "PG_Page_HTML_Pre", "PG_Page_HTML", "https://icecube.wisc.edu/press-guide/")
            Preset_Save_Prepare("FAQs.IceBit", "FAQ_Page", 0, "FAQ_Page_Pre", "FAQ_Page_HTML_Pre", "FAQ_Page_HTML", "https://icecube.wisc.edu/about-us/faq/")
            Preset_Save_Prepare("IceCube_Quick_Facts.IceBit", "IcQF_Page", 0, "IcQF_Page_Pre", "IcQF_Page_HTML_Pre", "IcQF_Page_HTML", "https://icecube.wisc.edu/about-us/facts/")
            Preset_Save_Prepare("IceCube10.IceBit", "Ic10_Page", 0, "Ic10_Page_Pre", "Ic10_Page_HTML_Pre", "Ic10_Page_HTML", "https://icecube.wisc.edu/icecube10/")
            print(" ---\n Done!")
            time.sleep(2)
            Preset_Saves()
        elif Preset_Options == "6":
            Preset_Saves()
        elif Preset_Options == "7":
            Page_Save()
        elif Preset_Options == "8":
            main_menu()
        else:
            InvalidInput()
            continue

# Function below retreives webpages and saves their content on a local file
def Page_Save():
    ClearScreen()
    print("\n [ ^-Main>Website-Hub>Page_Save ]\n")
    while True:
        print("\nThis is where one can download, update, and save local pages.\n There are several options below:")
        Save_Options = input("\n [1] Presets\n [2] Custom\n ---\n [3] Back\n [4] Main Menu\n > ")
        if Save_Options == "1":
            Preset_Saves()
        elif Save_Options == "2":    
            print("\nPlease Keep in mind that there are Presets available for\n you to use in order to simplify the experience of downloading webpages.\n Are you sure you want to continue?")
            confirmAll = input("[y]es/[N]o\n > ")
            if confirmAll.lower() == "y" or confirmAll.lower() == "yes":
                CustomURL = input(" Type your custom URL bwlow:\n \_< ")
                Preset_Save_Prepare("Custom_Download.IceBit", "Custom_Page", 0, "Custom_Page_Pre", "Custom_Page_HTML_Pre", "Custom_Page_HTML", CustomURL)
                print(" ---\n Done!")
                time.sleep(2)
                Page_Save()
            elif confirmAll.lower() == "n" or confirmAll.lower() == "no":
                print("")
            else:
                InvalidInput()
                time.sleep(1)
                Page_Save()
        elif Save_Options == "3":
            Website_Hub()
        elif Save_Options == "4":
            main_menu()

# Function below is the hub where the end-user can manage or download webpages
def Website_Hub():
    ClearScreen()
    print("\n [ ^-Main>Website-Hub ]\n")
    while True:
        print("\nThis is the main hub where one interacts with the IceCube Website\n There are several options below:")
        Web_Options = input("\n [1] Save Pages\n [2] Manage Downloaded Pages\n ---\n [3] Main Menu\n > ")
        if Web_Options == "1":
            Page_Save()
        elif Web_Options == "2":
            Saved_Pages()
        elif Web_Options == "3":
            main_menu()
        else:
            InvalidInput()

# Function below prints a splashscreen that can be drawn anytime
def SplashScreen():
    '''
    For color:
     : \033[1;37;49m (WHITE)
     : \033[1;34;49m (BLUE)
    Planned Design (May have slight changes):
     : # = White
     : 0 = Blue
             ######0##
           /######000##\
          /########0####\
         /###############\
        /##0##############\
       /##000######0#######\
      (####0####0#000#######)
       \#####000###0#######/
        \###0##0##0#######/
         \#0#0###0#######/
          \#000#0#######/
            #0#########
    '''
    print("\033[1;37;49m       ######\033[1;34;49m0\033[1;37;49m##    ")
    print("\033[1;37;49m     /######\033[1;34;49m000\033[1;37;49m##\   ")
    print("\033[1;37;49m    /########\033[1;34;49m0\033[1;37;49m####\  ")
    print("\033[1;37;49m   /###############\ ")
    print("\033[1;37;49m  /##\033[1;34;49m0\033[1;37;49m##############\ ")
    print("\033[1;37;49m /##\033[1;34;49m000\033[1;37;49m####\033[1;34;49m0\033[1;37;49m#########\ ")
    print("\033[1;37;49m(####\033[1;34;49m0\033[1;37;49m######\033[1;34;49m0\033[1;37;49m#########) ")
    print("\033[1;37;49m \#########\033[1;34;49m000\033[1;37;49m#######/ ")
    print("\033[1;37;49m  \###\033[1;34;49m0\033[1;37;49m##\033[1;34;49m0\033[1;37;49m##\033[1;34;49m0\033[1;37;49m#######/ ")
    print("\033[1;37;49m   \#\033[1;34;49m0\033[1;37;49m#\033[1;34;49m0\033[1;37;49m###\033[1;34;49m0\033[1;37;49m#######/ ")
    print("\033[1;37;49m    \#\033[1;34;49m000\033[1;37;49m#\033[1;34;49m0\033[1;37;49m#######/ ")
    print("\033[1;37;49m      #\033[1;34;49m0\033[1;37;49m######### ")

# Function below acts as the main menu for the entire program
def main_menu():
    ClearScreen()
    main_active = True
    while main_active == True:
        print("Off_Front-Icecube\n")
        SplashScreen()
        print("\n [ ^-Main ]\n")
        Menu_Input = input("\n [1] Website-Hub\n [2] Usage Tutorial\n [3] Frequently Asked Questions\n [4] License & Legal\n [5] Clean up Main Menu\n ---\n [6] Quit\n> ")
        if Menu_Input == "1":
            Website_Hub()
        elif Menu_Input == "2":
            Tutorial()
        elif Menu_Input == "3":
            FAQ()
        elif Menu_Input == "4":
            Legal_n_License()
        elif Menu_Input == "5":
            ClearScreen()
            main_menu()
        elif Menu_Input == "6":
            ClearScreen()
            quit()
        else:
            InvalidInput()

# Just a friendly reminder for optomisation of experience
ClearScreen()
print("                This program works optimally with the terminal at full screen.")
print("|-----------------RECOMMENDED AT LEAST THIS WIDE---------------------------------------------------------------------------------------------------------|")
print("First time users may want to go to the Usage Tutorial.")
time.sleep(3)
SplashScreen()
input("---\nPress [Enter] to continue.\n")
# Executes Main Menu
main_menu()