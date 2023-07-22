class Display:
    def printmsg(self,x,y):
        if(type(x) ==int):
           print("Integer Message :- ",x);
        else:
           print("Character Message :- ",x);
a = Display();
a.printmsg(20,"Shreya D. mane")
a.printmsg("Shreya D. mane",20)

