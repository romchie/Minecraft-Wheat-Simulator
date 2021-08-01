import time
import random

class Wheat:
    def __init__(self):
        self.stage = 0

    def plant(self):
        plant_input = str(input("Type [p] to plant the seeds: "))
        if plant_input == "p":
            print("The wheat has begun growing! (Now Stage 1)")
            self.stage += 1

    def plantedStatus(self):
        if self.stage < 1:
            planted = False
        else:
            planted = True
        return planted

    def grow(self):
        if self.stage > 0 and self.stage < 5:
            time.sleep(random.randrange(1, 5))
            self.stage += 1
            print("The wheat has grown! (Now stage " + str(self.stage) + ")")

    def growthStatus(self):
        if self.stage < 5:
            growing = True
        else:
            growing = False
            print("The wheat is fully grown and ready to be harvested!")
        return growing


def main():
    w = Wheat()

    while not w.plantedStatus():
        w.plant()

    while w.growthStatus():
        w.grow()

main()
