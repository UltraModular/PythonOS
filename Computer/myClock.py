import time

class MyTime:
    def __init__(self, number:int):
        if number == 1:
            timed = time.time()
        if number == 2:
            timed = time.localtime()
        self.timed = timed
        

    # Gives you the time
    def mTime(self):
        hour = self.timed[3]
        minute = self.timed[4]
        if minute < 10:
            minute = f"0{minute}"
        if hour == 0:
            hour += 12
        elif hour > 12:
            return f"{str(hour - 12)}:{str(minute)} pm"
        return f"{str(hour)}:{minute} am"


    # Gives you the weekday
    def mWeekDate(self):
        weekdays = {
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday"
        }
        weekday = self.timed[6]
        return f"{weekdays[weekday]}"

    # Gives you the date
    def mDate(self):
        year = self.timed[0]
        month = self.timed[1]
        day = self.timed[2]
        return f"{day}/{month}/{year}"


    # Gives you the amount of weeks that have passed since this year
    def mWeeks(self):
        weeks = self.timed[7]
        return f"{round(weeks / 7)}"

'''
class CSpoken(MyTime):
    def __init__(self, number):
        super().__init__(number)
        
    
    # Just gives the time as what would have been said by a person
    def CSpokenTime():
        return f"Today is {MyTime.mWeekDate()}, {MyTime.mDate()}. It is {MyTime.mTime()}."
'''

timed = MyTime(2)
# timid = CSpoken(2)
print(f"Week {timed.mWeeks()}")
print(timed.mDate())
print(timed.mWeekDate())
print(timed.mTime())
# print(timid.CSpokenTime())

