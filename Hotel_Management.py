class hotelfarecal:

    def __init__(self, rt='', s=0, r=0, name='', address='', cindate='', coutdate='', rno=101):

        print("\n\n*****WELCOME TO Swami HOTEL*****\n")
        self.rt = rt
        self.r = r
        self.s = s
        self.name = name
        self.address = address
        self.cindate = cindate
        self.coutdate = coutdate
        self.rno = rno

    def inputdata(self):
        self.name = input("\nEnter your name:")
        self.address = input("\nEnter your address:")
        self.cindate = input("\nEnter your check in date:")
        self.coutdate = input("\nEnter your checkout date:")
        print("Your room no.:", self.rno, "\n")

    def roomrent(self):
        print("We have the following rooms for you:-")
        print("1.  type A Single: A room assigned to one person-> 6000 PN\-")
        print("2.  type B Double: A room assigned to two people->rs 5000 PN\-")
        print("3.  type C Triple: A room assigned to three people->rs 4000 PN\-")
        print("4.  type D Quad: A room assigned to four people->rs 3000 PN\-")
        x = int(input("Enter Your Choice Please->"))
        n = int(input("For How Many Nights Did You Stay:"))

        if (x == 1):
            print("you have opted room type A")
            self.s = 6000 * n
        elif (x == 2):
            print("you have opted room type B")
            self.s = 5000 * n
        elif (x == 3):
            print("you have opted room type C")
            self.s = 4000 * n
        elif (x == 4):
            print("you have opted room type D")
            self.s = 3000 * n
        else:

            print("please choose a room")

        print("your room rent is =", self.s, "\n")

    def restaurentbill(self):

        print("*****RESTAURANT MENU*****")

        print("1.water----->Rs20", "2.tea----->Rs10", "3.breakfast combo--->Rs90", "4.lunch---->Rs110",
              "5.dinner--->Rs150", "6.Exit")

        while (1):

            c = int(input("Enter your choice:"))

            if (c == 1):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 20 * d

            elif (c == 2):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 10 * d

            elif (c == 3):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 90 * d

            elif (c == 4):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 110 * d

            elif (c == 5):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 150 * d

            elif (c == 6):
                break;
            else:
                print("Invalid option")

        print("Total food Cost=Rs", self.r, "\n")


    def display(self):
        print("******HOTEL BILL******")
        print("Customer details:")
        print("Customer name:", self.name)
        print("Customer address:", self.address)
        print("Check in date:", self.cindate)
        print("Check out date", self.coutdate)
        print("Room no.", self.rno)
        print("Your Room rent is:", self.s)
        print("Your Food bill is:", self.r)

        self.rt = self.s + self.r

        print("Your sub total bill is:", self.rt)
        self.rno += 1


def main():
    a = hotelfarecal()

    while (1):
        print("1.Enter Customer Data")

        print("2.Calculate roomrent")

        print("3.Calculate restaurant bill")

        print("4.Show total cost")

        print("5.EXIT")

        b = int(input("\nEnter your choice:"))
        if (b == 1):
            a.inputdata()

        if (b == 2):
            a.roomrent()

        if (b == 3):
            a.restaurentbill()

        if (b == 4):
            a.display()

        if (b == 5):
            quit()


main()

