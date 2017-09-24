class person:
    def __init__(self, name, prefList):
        self.prefList = prefList
        self.name = name
        self.paired = False

    def pair(self, partner):
        self.partner = partner
        self.paired = True

    def getPartner(self):
        return self.partner

    def getName(self):
        return self.name

    def getPrefList(self):
        return self.prefList

    def isPaired(self):
        return self.paired

    def swap(self, newPartner):
        self.partner = newPartner

    def __str__(self):
        return self.name + ": " + " ".join(str(x) for x in self.prefList)