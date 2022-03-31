class Employee:

    def __init__(self, name, schedule):
        self.name = name
        dict = {}
        listTemp = schedule.split(",")
        for elem in listTemp:
            dict[elem[:2]] = elem[2:]
        self.schedule = dict

    def __str__(self):
        return f'{self.name}={self.schedule}'

    def compare(self, otherEmployee):
        currDict = self.schedule
        otherDict = otherEmployee.schedule
        sameDays = list(set(currDict.keys()) & set(otherDict.keys()))
        ''' In order to check if employees meet in the same day, we have to compare the
        the time in which the employee who entered first, leaves work, with the hour the othe employee arrives to work.
        If the time the second employee enters work is less than the time the first employee leaves work, then they meet.
        Example:
        Rene: 10:00-16:00 
        Astrid: 12:00-14:00
        Since Rene entered first, we take the time they leave (16:00) and compare it to the time Astrid entered (12:00)
        Since 12:00 < 14:00, they meet.
        '''
        countMeeting = 0
        for day in sameDays:
            currSchedule = currDict[day]
            otherSchedule = otherDict[day]
            # First we compare who entered first
            if currSchedule[:2] >= otherSchedule[:2]:
                # Other employee entered first
                if otherSchedule[6:8] > currSchedule[:2]:
                    # print(f'They meet on {day}, {self.name} entered first')
                    countMeeting += 1
            else:
                # Current employee entered first
                if currSchedule[6:8] > otherSchedule[:2]:
                    # print(f'They meet on {day}, {otherEmployee.name} entered first')
                    countMeeting += 1

        return f'{self.name}-{otherEmployee.name}:{countMeeting}'
