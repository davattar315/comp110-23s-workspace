"""File to define River class."""


__author__ = '730480676'


from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """Init river class."""
    fish: list[Fish] 
    bears: list[Bear]
    day: int

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checking ages."""
        new_fish_list: list[Fish] = []
        new_bear_list: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                new_bear_list.append(bear)    
        for fish in self.fish:
            if fish.age <= 3: 
                new_fish_list.append(fish)
        self.bears = new_bear_list
        self.fish = new_fish_list

    def remove_fish(self, amount: int):
        """Getting rid of eaten fish."""
        idx: int = 0
        while idx < amount:
            self.fish.pop(0)
            idx += 1
        return None

    def bears_eating(self):
        """Simulating bears eating."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
                  
    def check_hunger(self) -> None:
        """Checking bear hunger."""
        surviving_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)
            self.bears = surviving_bears  
        return None
        
    def repopulate_fish(self) -> None:
        """Repopulating fish."""
        num_fish = len(self.fish)
        new_fish = (num_fish // 2) * 4
        idx = 0
        while idx < new_fish:
            self.fish.append(Fish())
            idx += 1
        return None
    
    def repopulate_bears(self) -> None:
        """Repopulating bears."""
        num_bears = len(self.bears)
        new_bears: num_bears // 2 
        new_bears = Bear()
        self.bears.append(new_bears)
        return None
    
    def view_river(self) -> None:
        """River Stats."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
        
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """River in a week."""
        idx: int = 0
        while idx < 7:
            self.one_river_day()
            idx += 1
        return None
            
