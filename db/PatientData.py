import dbfread

class Detail:
    def __init__(self, name, age, date1, date2):
        self.DATAOFRHIMS = dbfread.DBF('C:/Users/hp/OneDrive/Desktop/Ayush/db/SALPUR_RHIMS.DBF', load=True)
        self.DATAOFMEDICOS = dbfread.DBF('C:/Users/hp/OneDrive/Desktop/Ayush/db/SALPUR_MEDICOS.DBF', load=True)
        self.name = name
        self.age = age
        self.date1 = date1
        self.date2 = date2
        
    def Search(self):
        ADD, dr, G = "", "", ""
        for data in self.DATAOFRHIMS.records:
            if data["PNAME"] == self.name and data["AGE"] == self.age:
                ADD = data["PADD1"]+" "+data["PADD2"]
                dr = "Dr. " + data["PCITY"]
                G = data["SEX"]

        return "Name : {}\nAge : {}\nAddress : {}\nGender : {}\nTreatment under : {}".format(self.name, self.age, ADD, G, dr)

    def SearchBillsinRHIMS(self):
        billList = list()
        NumList = list()
        BNDList = list()
        for data in self.DATAOFRHIMS.records:
            if data["PNAME"] == self.name and data["AGE"] == self.age:
                NumList.append(data["BILNO"])
                date = data["DATE"]
                BNDList.append(date.strftime("%m-%d-%Y"))
                billList.append(data["AMT"])

        return [NumList, billList, BNDList]

    def SearchBillsinMEDICOS(self):
        billList = list()
        NumList = list()
        BNDList = list()
        for data in self.DATAOFMEDICOS.records:
            if data["PNAME"] == self.name and data["AGE"] == self.age:
                NumList.append(data["BILNO"])
                date = data["DATE"]
                BNDList.append(date.strftime("%m-%d-%Y"))
                billList.append(data["AMT"])

        return [NumList, billList, BNDList]

    def Adddate(self, Date):
        d = int(Date[3:5]) + 1
        m = Date[:2]
        y = Date[-4:]
        if d < 10:
            D = m + "-" + str(0) + str(d) + "-" + y
        else:
            D = m + "-" + str(d) + "-" + y

        return D

    def FindIndexr1(self, List):
        date = self.date1
        for i in range(len(List)):
            if date not in List:
                date = self.Adddate(date)
            else:
                r = List.index(date)
                break
        else:
            r = 404

        return r

    def FindIndexr2(self, List):
        date = self.date2
        for i in range(len(List)):
            if date not in List:
                date = self.Adddate(date)
            else:
                r = len(List) - 1 - List[::-1].index(date)
                break
        else:
            r = 404

        return r

    def SearchBillsinRHIMSBW(self):
        billList = list()
        NumList = list()
        BNDList = list()
        for data in self.DATAOFRHIMS.records:
            if data["PNAME"] == self.name and data["AGE"] == self.age:
                NumList.append(data["BILNO"])
                date = data["DATE"]
                BNDList.append(date.strftime("%m-%d-%Y"))
                billList.append(data["AMT"])

        R1 = self.FindIndexr1(BNDList)
        R2 = self.FindIndexr2(BNDList)
        if R1 == R2 and R1 == 404:
            noteofrhims = "The Dates you entered are not Valid for this user. Please Enter Valid date.\nFrom RHIMS"
        elif R2 == 404 or R1 == R2:
            R2 = len(BNDList)
        elif R1 == 404:
            R1 = 0
        
        return [NumList[R1:R2+1], billList[R1:R2+1], BNDList[R1:R2+1]]

    def SearchBillsinMEDICOSBW(self):
        billList = list()
        NumList = list()
        BNDList = list()
        for data in self.DATAOFMEDICOS.records:
            if data["PNAME"] == self.name and data["AGE"] == self.age:
                NumList.append(data["BILNO"])
                date = data["DATE"]
                BNDList.append(date.strftime("%m-%d-%Y"))
                billList.append(data["AMT"])

        R1 = self.FindIndexr1(BNDList)
        R2 = self.FindIndexr2(BNDList)
        # AI FOR SLICING
        if R1 == R2 and R1 == 404:
            noteofmedicos = "The Dates you entered are not Valid for this user. Please Enter Valid date.\nFrom MEDICOS"
        elif R2 == 404 or R1 == R2:
            R2 = len(BNDList)
        elif R1 == 404:
            R1 = 0
        return [NumList[R1:R2+1], billList[R1:R2+1], BNDList[R1:R2+1]]

    def ShowBills(self):
        RHIMSLIST = self.SearchBillsinRHIMS()
        MEDICOSLIST = self.SearchBillsinMEDICOS()
        print("Showing Bills for",self.name)
        print("Showing Bills of RHIMS")
        print("Bill No.    Bill Date     Bill Amount")
        for (num, amt, Date) in zip(RHIMSLIST[0], RHIMSLIST[2], RHIMSLIST[1]):
            print("{}.      {}      {}".format(num, amt, Date))
        print("Total amount of RHIMS is {}".format(sum(RHIMSLIST[1])))
        print("="*120)
        print("Showing Bills of MEDICOS")
        print("Bill No.    Bill Date     Bill Amount")
        for (num, amt, Date) in zip(MEDICOSLIST[0], MEDICOSLIST[2], MEDICOSLIST[1]):
            print("{}.       {}      {}".format(num, amt, Date))
        print("Total amount of MEDICOS is {}".format(sum(MEDICOSLIST[1])))
        print("Total Bills : ",sum(RHIMSLIST[1]) + sum(MEDICOSLIST[1]))

    def ShowBillsbetweendates(self):
        RHIMSLIST = self.SearchBillsinRHIMSBW()
        MEDICOSLIST = self.SearchBillsinMEDICOSBW()
        for (num, amt, Date) in zip(RHIMSLIST[0], RHIMSLIST[2], RHIMSLIST[1]):
            print("{}.            {}             {}".format(num, amt, Date))
        print("Total amount of RHIMS is {}".format(sum(RHIMSLIST[1])))
        print("="*120)
        print("Showing Bills of MEDICOS")
        print("Bill No.    Bill Date     Bill Amount")
        for (num, amt, Date) in zip(MEDICOSLIST[0], MEDICOSLIST[2], MEDICOSLIST[1]):
            print("{}.            {}             {}".format(num, amt, Date))
        print("Total amount of MEDICOS is {}".format(sum(MEDICOSLIST[1])))
        print("="*120)
        print("Total Bills : ",sum(RHIMSLIST[1]) + sum(MEDICOSLIST[1]))

def Search_js():
    P = Detail(Name, int(Age), date1, date2)
    return P.Search()

"""if not date1=="" and not date2=="":
    P.ShowBillsbetweendates()
else:
    P.ShowBills()"""
