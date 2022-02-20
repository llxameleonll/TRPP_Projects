class ElectricMeter:
    T1 = {}  # Дневные показатели
    T2 = {}  # Ночные показатели

    def addT1(self, date, value):
        self.T1[date] = value
        return self.T1

    def addT2(self, date, value):
        self.T2[date] = value
        return self.T2

    def __str__(self):
        s = "T1:\n"
        for key, value in self.T1.items():
            s += "Date: {}, Value: {}\n".format(key, value)

        s += "T2:\n"
        for key, value in self.T2.items():
            s += "Date: {}, Value: {}\n".format(key, value)

        return s
