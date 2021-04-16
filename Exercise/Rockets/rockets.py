################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: Apr 15, 2021
# Description This program uses Rocket and its subclass ReusableRocket object,
# and calculate its launch cost using method cost_per_launch.
################################################################################

class Rocket:
    name: str
    booster_cost: float
    upper_stage_cost: float
    fuel_cost: float

    # Superclass Default Constructor
    def __init__(self, name: str, booster_cost: float, upper_stage_cost: float, fuel_cost: float):
        self.name = name
        self.booster_cost = booster_cost
        self.upper_stage_cost = upper_stage_cost
        self.fuel_cost = fuel_cost

    def cost_per_launch(self):
        totalCost = self.booster_cost + self.upper_stage_cost + self.fuel_cost
        print(f"This {self.name} cost ${totalCost} million per launch.")



class ReusableRocket(Rocket):
    uses: int

    # Subclass default constructor
    def __init__(self, name: str, booster_cost: float, upper_stage_cost: float, fuel_cost: float, uses: int):
        # Calling Superclass Constructor.
        super().__init__(name, booster_cost, upper_stage_cost, fuel_cost)
        self.uses = uses

    # Overridden Method
    def cost_per_launch(self):
        totalCost = (self.booster_cost / self.uses) + self.upper_stage_cost + self.fuel_cost
        print(f"This {self.name} cost ${totalCost} million per launch.")



def main():
    AtlasV: Rocket = Rocket("Atlas V", 65.4, 42.6, 0.23)
    Ariane5: Rocket = Rocket("Ariane 5", 83.5, 55.6, 0.69)
    LongMarch3B: Rocket = Rocket("Long March 3B", 28.5, 19.0, 2.38)
    Soyuz2: Rocket = Rocket("Soyuz 2", 20.9, 13.9, 0.24)
    falcon9: ReusableRocket = ReusableRocket("Falcon 9", 43.0, 18.6, 0.45, 10)

    AtlasV.cost_per_launch()
    Ariane5.cost_per_launch()
    LongMarch3B.cost_per_launch()
    Soyuz2.cost_per_launch()
    falcon9.cost_per_launch()


if __name__ == '__main__':
    main()
