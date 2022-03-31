class Employee:

    def __init__(self, name, schedule):
        self.name = name
        self.schedule = self.makeSchedule(schedule)

    def __str__(self):
        return f'{self.name}={self.schedule}'

    def makeSchedule(self, schedule):
        try:
            tempDict = {}
            listTemp = schedule.split(",")
            for elem in listTemp:
                tempDict[elem[:2]] = {
                    "start":
                        {
                            "hh": int(elem[2:].split("-")[0].split(":")[0]),
                            "mm": int(elem[2:].split("-")[0].split(":")[1])
                        },
                    "end":
                        {
                            "hh": int(elem[2:].split("-")[1].split(":")[0]),
                            "mm": int(elem[2:].split("-")[1].split(":")[1])
                        }
                }

            return tempDict
        except ValueError:
            raise
        except IndexError:
            raise

    def compare(self, otherEmployee):
        try:
            currDict = self.schedule
            otherDict = otherEmployee.schedule
            sameDays = list(set(currDict.keys()) & set(otherDict.keys()))
            countMeeting = 0
            for day in sameDays:
                currSchedule = currDict[day]
                otherSchedule = otherDict[day]
                if currSchedule["start"]["hh"] in range(otherSchedule["start"]["hh"], otherSchedule["end"]["hh"]):
                    countMeeting += 1
                elif otherSchedule["start"]["hh"] in range(currSchedule["start"]["hh"], currSchedule["end"]["hh"]):
                    countMeeting += 1

            return f'{self.name}-{otherEmployee.name}:{countMeeting}'

        except AttributeError:
            raise ValueError("Received unexpected class")
