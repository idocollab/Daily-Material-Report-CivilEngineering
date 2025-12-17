from csv import DictReader
from helper import clean

class  Analyzer: 
    def __init__(self,data):   #Initialize vaiables needed
        self.data=data
        self.days=0
        self.total_cement=0
        self.total_sand=0
        self.total_aggregate=0
        self.total_cement_cost=0
        self.total_aggregate_cost=0
        self.total_sand_cost=0
        self.total_cost=0
        self.average=0
    def  calculations(self,data) :     # all calculations done here 
        for row in data:
            self.days +=1
            self.total_cement += int(row["CementBags"])
            self.total_sand += float(row["Sand-m3"])
            self.total_aggregate += float(row["Aggregate-m3"])
            self.total_aggregate_cost += float(row["AggregateCost"])
            self.total_cement_cost += float(row["CementCost"])
            self.total_sand_cost += float(row["SandCost"])
        self.total_cost=self.total_aggregate_cost+self.total_cement_cost+self.total_sand_cost
        self.average=self.total_cost/self.days
    def results(self):                 #results in output
        clean()
        print("-"*45)
        print("SITE MATERIAL USAGE SUMMARY")
        print("-"*45)
        print(" ")
        print(f"Total days loggged : {self.days}")
        print(" ")
        print("Material Consumption")
        print("-"*45)
        print(" ")
        print(f"Cement (bags)         :{self.total_cement:.4f}")
        print(f"Sand (m3)             :{self.total_sand:.4f}")
        print(f"Aggregate (m3)        :{self.total_aggregate:.4f}")
        print(" ")
        print("Cost Summary (NPR)")
        print("-"*45)
        print(f"Total Cement Cost     :NPR.{self.total_cement_cost:.4f}")
        print(f"Total Aggregate Cost  :NPR.{self.total_aggregate_cost:.4f}")
        print(f"Total Sand Cost       :NPR.{self.total_sand_cost:.4f}")
        print("-"*45)
        print(f"Total Site Cost       :{self.total_cost:.4f}")
        print(f"Average Cost Per Day  :{self.average:.4f}")
        print("-"*45)

def read_csv(file="data.csv"):       #csv reader   
    with open(file,"r") as f:
        r=list(DictReader(f))
    return r
def main():                          #main function to control the whole script
    data=read_csv()
    obj=Analyzer(data)
    obj.calculations(data)
    obj.results()

if __name__=="__main__":              # prevents running this code if this file is imported 
    main()          

        