class Hero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        print(f"I am {self.name}, protecting {self.city} with my {self.power}!")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")


class Superhero(Hero):
    def __init__(self, name, power, city, special_move):
        super().__init__(name, power, city)
        self.special_move = special_move

    def use_special(self):
        print(f"{self.name} unleashes their ultimate move: {self.special_move}!")


class Villain(Hero):
    def __init__(self, name, power, city, evil_plan):
        super().__init__(name, power, city)
        self.__evil_plan = evil_plan  

    def reveal_plan(self):
        print(f"{self.name}'s evil plan is: {self.__evil_plan} (Shh!)")

hero1 = Superhero("Night Falcon", "super speed", "Metropolis", "Lightning Strike")
villain1 = Villain("Shadow Fang", "dark magic", "Metropolis", "Steal the city’s power grid")

hero1.introduce()
hero1.use_special()

villain1.introduce()
villain1.reveal_plan()
