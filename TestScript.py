import WebScrape
import time
building = "BE"
day = "10/06/2022"
startT = "08:00AM"
endT = "10:00PM"

def test():
    s = WebScrape.Scraper(building, day, startT, endT)

    s.start()

    # go to the calendar frame
    s.switchToCal()

    # gets the classrooms by switching frames
    rooms = WebScrape.getClassrooms(s)

    # gets the calendar again
    s.switchToDefault()
    s.switchToCal()

    availRooms = []
    time.sleep(10)
    for r in rooms:
        if WebScrape.enterInformation(s, r):
            availRooms.append(r)

    print("The available rooms are")
    for ar in availRooms:
        print(ar)

    s.quit()