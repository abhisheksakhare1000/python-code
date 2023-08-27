class dict_parse:
    def __init__(self,d):
        self.d = d
    def key_dict(self):
        for i in self.d.keys():
            print(i)
    def value_dict(self):
        for i in self.d.values():
            print(i)
    def dict_check():
        if type(d)!=dict:
            raise Exception ("input is invalid")
    def userinput(self):
        self.d = eval(input())
        print(self.d, type(self.d))
        print(self.getkeys())
        print(self.getvalues())
    
    def insertion(self, key,value):
        self.d[key] = value
        return self.d
            