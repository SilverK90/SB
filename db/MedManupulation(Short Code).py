import dbfread

class Medicine:
    def __init__(self):
        self.table = dbfread.DBF('C:/Users/HP/Desktop/Bills/20-21/medical(20-21)/INMAS.DBF', load=True)

    def Diff(self, L):
        ExpM = L[0]
        ExpY = L[1]
        return (ExpM-11)+12*(ExpY-2020)

    def MonthnYearOfDate(self, exp):
        Month = {
            "JAN": 1,
            "FEB": 2,
            "MAR": 3,
            "APR": 4,
            "MAY": 5,
            "JUN": 6,
            "JUL": 7,
            "AUG": 8,
            "SEP": 9,
            "OCT": 10,
            "NOV": 11,
            "DEC": 12
        }
        if len(exp)==7:
            m = exp[0:3]
            return self.Diff([Month[m.upper()], int(exp[3:])])
        else:
            return "does not Expire."
        
    def CheckExpire(self):
        Expired = list()
        NExpired = list()
        DExpired = list()
        for Dict in self.table.records:
            data = self.MonthnYearOfDate(Dict["EXP"])
            if type(data)==int:
                if data>0:
                    NExpired.append(Dict)
                else:
                    Expired.append(Dict)
            else:
                DExpired.append(Dict)
        
        return [NExpired,Expired,DExpired]

Med = Medicine()
DATA = Med.CheckExpire()
print("Total Medicine {} which will expire in November 2020\n".format(len(DATA[0])))
for D in DATA[0]:
    print("Medicine : {}\nExpiry Date : {}".format(D["INAME"], D["EXP"]))
    print("\n")

print("Total Medicine {} which are expired.\n".format(len(DATA[1])))
for D in DATA[1]:
    print("Medicine : {}\nExpired : {}".format(D["INAME"], D["EXP"]))
    print("\n")

print("These {} are not Medicine.\n".format(len(DATA[2])))
for D in DATA[2]:
    print("Item : {}".format(D["INAME"]))