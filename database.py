import t
import time
import random
def prg():
    t.clear()

    def que(q, a, b, d="N/A", e="N/A"):
            global c
            print(q)
            time.sleep(1)
            print("1. " + a)
            time.sleep(0.1)
            print("2. " + b)
            time.sleep(0.1)
            print("3. " + d)
            time.sleep(0.1)
            print("4. " + e)
            time.sleep(0.1)
            c = input()
            t.clear()

    def ugh():
            print("Not recognized. Aborting program.")
            input("Press Enter to start over")
            t.clear()
            prg()

    que("Welcome to the offical Fair Use Informative Database (FUID). Choose an option.", "General Info", "Creator Database", "Fun Facts", "3-D Printing")

    if c == "1":
            print("Copyright and Fair Use laws were first put into efffect in 1710, by British Parliament.")
            print("The United States of America first had copyright laws in 1789, thirteen years after the country was formed.")
            print("Today, most violation of fair use law comes from piracy, and people stealing videos and images, and declaring them theirs.")
            print("Anyone can help in the fight for fair use, from reporting stolen content, to donating to content creators.")
            print("The internet has brought upon us many gifts of entertainment, and fair use seeks to protect the sources of these gifts.")
            que("Would you like to learn more?", "Sure", "Nah")
            if c == "1":
                    print("The United States has had copyright laws in place since only thirteen years after it's formation.")
                    print("In modern times, it has a very content-creator-friendly stance. It prohibits plagarism and pirating of content,")
                    print("from music, to movies, to videos. However, it is still easy to get around the laws, as both plagarism and piracy still thrive.")
                    input("Press Enter to start over")
                    t.clear()
                    prg()
            elif c == "2":
                    input("Press Enter to start over")
                    t.clear()
                    prg()
    elif c == "2":
            que("What type of info?", "Legality", "Types of Violations", "Can I do this?")
            if c == "1":
                    que("Explain further:", "How to report illegal content", "I may have accidentally made a copyright infringement", "Someone stole my content")
                    if c == "1":
                            print("Many sites have a built-in reporting feature. Use that, or email the site owner and content creator if possible.")
                            input("Press Enter to start over")
                            t.clear()
                            prg()
                    elif c == "2":
                            print("Uh oh! Take the video down and contact the actual creator of the content you stole, and apologize!")
                            input("Press Enter to start over")
                            t.clear()
                            prg()
                    elif c == "3":
                            print("Contact them and the site owner! Report them if the site has a built-in reporting system!")
                            input("Press Enter to start over")
                            t.clear()
                            prg()
                    else:
                            ugh()
            elif c == "2":
                    print("There are a few types of copyright infringement;")
                    print("1. Using a free video, but not giving the source")
                    print("2. Claiming a free video as your own")
                    print("3. Stealing a paid video without paying for it")
                    print("4. And many more, too numerous to list here.")
                    input("Press Enter to start over")
                    t.clear()
                    prg()
            elif c == "3":
                    que("What purpose do you wish to use the video for?", "Educational", "Commercial", "Personal", "Journalism")
                    if c == "1":
                            que("Is the entire video relevent to the topic?", "Yes", "No")
                            if c == "1":
                                    print("You are free to use this video, for educational purposes!")
                                    input("Press Enter to start over")
                                    t.clear()
                                    prg()
                            elif c == "2":
                                    print("Try and cut out the parts of the video you need, and it should then be okay for educational purposes.")
                                    input("Press Enter to start over")
                                    t.clear()
                                    prg()
                            else:
                                    ugh()
                    elif c == "2":
                            que("Do you have permissions to use this video?", "Yes", "No")
                            if c == "1":
                                    print("You are free to use this video, for commercial purposes!")
                                    input("Press Enter to start over")
                                    t.clear()
                                    prg()
                            elif c == "2":
                                    print("You must gain permission from the creator to use this video for commercial purposes.")
                                    input("Press Enter to start over")
                                    t.clear()
                                    prg()
                            else:
                                    ugh()
                    elif c == "3":
                            que("Will you profit from use of the video?", "Yes", "No")
                            if c == "1":
                                    print("This is not personal use. Please see commercial use.")
                                    input("Press Enter to start over")
                                    t.clear()
                                    prg()
                            elif c == "2":
                                    print("You are free to use this video, for personal purposes!")
                                    input("Press Enter to start over")
                                    t.clear()
                                    prg()
                            else:
                                    ugh()
                    elif c == "4":
                            print("Using a video for journalism is always fair use of any video.")
                            print("You are free to use this video, for journalism purposes!")
                            input("Press Enter to start over")
                            t.clear()
                            prg()
                    else:
                            ugh()
                            
    elif c == "3":
            print("Here's a random fun fact on Fair Use!")
            ffarray = ["Fair use laws were first implemented in the 1700s, by British Parliament.", "Many countries and provinces have fair use laws in effect today, making content creators' lives less prone to content theft.", "Piracy is a form of fair use violation, and very illegal."]
            random.shuffle(ffarray)
            print(ffarray[0])
            input("Press Enter to start over")
            t.clear()
            prg()
            
    elif c == "4":
            que("What about 3-D Printing would you like to know about?", "Public File Licensing", "How It Works", "Educational Uses", "Cost Effiency")
            if c == "1":
                    print("Files follow the same rules as other types of content. Make sure to follow the guidelines")
                    print("in the other sections of this database. Lots of these files also use a system called Creative")
                    print("Commons, which is a unified form of content protection.")
                    que("Would you like to learn more on Creative Commons?", "Sure", "Nah")
                    if c == "1":
                            print("Some parts of creative commons are “no derivatives,”(no editing the design) “noncommercial,”(you can’t sell or profit from their design),")
                            print("“share-alike,”(if the design is redistributed with or without changes, it must be under the same license, no more restrictive)")
                            print("and “attribution”(you must credit the original creator).")
                            input("Press Enter to start over")
                            t.clear()
                            prg()
                    else:
                            input("Press Enter to start over")
                            t.clear()
                            prg()
                                  
            elif c == "2":
                    print("FDM (Fused Deposition Modeling) is how most 3-D printers work. Modelers create a model of what they want to print, be it art, replacement parts, or prototypes for new designs. Then, the model is put through a slicer software. This converts the model to a format that the printer can read (usually .gcode) including print settings, coordinates, and what the printer does when it's finished. Then, the printer prints the object by layering melted thermoplastics to build the desired objects. These plastics are called filaments, and they can be PLA, ABS, Nylon, or even Carbon Fiber.")
                    input("Press Enter to start over")
                    t.clear()
                    prg()
                                  
            elif c == "3":
                    print("3-D Printing is very useful in an educational setting. It can be used in a variety of ways,")
                    print("including making physical models of things like the atom and the Solar System, teaching")
                    print("students how to make digital models of things and then seeing their productions in real life,")
                    print("and, surprisingly, making mouthpieces for instruments.")
                    input("Press Enter to start over")
                    t.clear()
                    prg()
                                  
            elif c == "4":
                    print("The filament used for 3-D printing can be somewhat costly, but there are ways to alleviate this.")
                    print("One way that a school or individual could make some money to pay for this is simple; making keychains,")
                    print("and selling them as a fundraiser.")
                    input("Press Enter to start over")
                    t.clear()
                    prg()
                                  
            else:
                    ugh()
                                  
    else:
            ugh()
prg()