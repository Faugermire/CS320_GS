class person:

    def __init__(self, name, prefList):
        self.paired = False
        self.prefList = prefList
        self.name = name
        self.partner = None

    def pair(self, partner):
        self.paired = True
        self.partner = partner

    def getPartner(self):
        return self.partner

    def isPaired(self):
        return self.paired

    def getName(self):
        return self.name

    def getPrefList(self):
        return self.prefList

    def swap(self, newPartner):
        oldPartner = self.partner
        self.partner = newPartner
        return oldPartner

    def __str__(self):
        return self.name + ": " + " ".join(str(x) for x in self.prefList) + " " + self.partner.getName()