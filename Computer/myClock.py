import time

class MyTime:
    def __init__(self, numbertime:int) -> str:
        if numbertime == 1:
            timed = time.time()
        if numbertime == 2:
            timed = time.localtime()
        self.timed = timed
        

    # Gives you the time
    def mTime(self, hourtime:int):
        hour = self.timed[3]
        minute = self.timed[4]
        if minute < 10:
            minute = f"0{minute}"
        if hourtime == 1:
            if hour == 0:
                hour += 12
            elif hour > 12:
                return f"{str(hour - 12)}:{str(minute)} pm"
            return f"{str(hour)}:{minute} am"
        elif hourtime == 2:
            return  f"{str(hour)}:{minute}"
        else:
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


class CSpoken(MyTime):
    def __init__(self, number, options):
        self.options = options
        super().__init__(number)
        
    
    # Just gives the time as what would have been said by a person
    def FTime(self):
        return f"Today is {MyTime.mWeekDate(self)}, {MyTime.mDate(self)}. It is {MyTime.mTime(self, self.options)}."
    
    def SpokenTime(self):
        return f"It is currently {MyTime.mTime(self, self.options)}."

    def Date(self):
        return f"Today is {MyTime.mDate(self)}." 

    def WDate(self):
        return f"Today is {MyTime.mWeekDate(self)}."

    def Week(self):
        if self.options in ["", 1]:
            return f"Week {MyTime.mWeeks(self)}."
        if self.options == 2:
            return f"It is Week {MyTime.mWeeks(self)}."


timed = MyTime(2)
timid = CSpoken(2, 1)
TIMeD = CSpoken(2, 2)
print(timed.mDate())
print(timed.mWeekDate())
print(timed.mTime(2))
print(timid.FTime())
print(TIMeD.SpokenTime())
print(TIMeD.WDate())
print(TIMeD.Date())
print(TIMeD.Week())
