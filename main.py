import json
import os


class Bugsy:


    def __init__(self,name):
        self.name=name
        self.energy=100
        self.mood="Happy"
        self.score=0
        self.level=1
        self.debug_cost = 15
        self.debug_points = 10
        self.knowledge=[]
        self.missions = [{"name": "Fix 3 Bugs", "target": 3, "progress": 0, "reward": 30},
        {"name": "Reach Score 100", "target": 100, "progress": 0, "reward": 50}]


    def feed(self):
        if self.energy < 100:
            self.energy+=10
            if self.energy >100:
                self.energy=100

            print(f"{self.name} ate some food :-) ")
            print(f"Energy : {self.energy}")
        
        else :
            print(f"{self.name} is already full ")


    def update_missions(self):
        for mission in self.missions:
            
            if mission.get("completed", False):
                continue

            if mission["name"] == "Fix 3 Bugs":
                mission["progress"] += 1
            
            elif mission["name"] == "Reach Score 100":
                mission["progress"] = self.score

            if mission["progress"]>=mission["target"]:
                mission["completed"]=True
                self.score+=mission["reward"]
                print(f"Mission completed: {mission['name']}")
                print(f"Reward: {mission['reward']} points")


    def check_level(self):
        while self.score >= self.level * 50:
            self.level += 1
            print(f"Level Up! Your level is now {self.level}")


    def debug(self):
        if self.energy >= self.debug_cost:
            self.energy -= self.debug_cost
            self.score += self.debug_points
            self.mood = "Happy"

            print(f"{self.name} fixed a bug!")
            self.update_missions()
            self.check_level()
            print(f"Energy: {self.energy}")
            print(f"Score: {self.score}")

        else:
            self.mood = "Tired"
            print(f"{self.name} is too tired to debug :-( ")        


    def sleep(self):
        if self.energy < 100:
            self.energy+=20
            if self.energy > 100:
                self.energy=100

            print(f"{self.name} slept :-) ")
            print(f"Energy : {self.energy}")

        else:
            print(f"{self.name} is doesn't want to sleep")


    def show_profile(self):
        print("="*50)
        print("BUGSY PROFILE".center(50))
        print("="*50)
        print(f"Name : {self.name}")
        print(f"Energy : {self.energy}")
        print(f"Mood : {self.mood}")
        print(f"Score : {self.score}")
        print(f"Level : {self.level}")
        print("="*50)


    def teach(self):
        skill = input("Enter a skill : ").strip()

        if not skill:
            print("Skill cannot be empty!")
        
        elif skill not in self.knowledge:
            self.knowledge.append(skill)
            print(f"Bugsy learned : {skill}")
        else:
            print("Bugsy already knows this !")

    def show_knowledge(self):
        if self.knowledge:
            print("Bugsy's Skills : ")
            for skill in self.knowledge:
                print(f"- {skill}")
        else:
            print("Bugsy hasn't learned any skills yet :-( ") 


    def save_data(self):
        data={
            "name":self.name,
            "character_type": type(self).__name__,
            "energy":self.energy,
            "mood":self.mood,
            "score":self.score,
            "level":self.level,
            "debug_cost": self.debug_cost,
            "debug_points": self.debug_points,
            "knowledge":self.knowledge,
            "missions":self.missions
        }

        file=open("bugsy_data.json", "w")
        json.dump(data,file,indent=4)
        file.close()
        print("Game saved successfully!")


    def load_data(self):
        try:
            file=open("bugsy_data.json", "r")
            data=json.load(file)
            self.name = data["name"]
            self.energy = data["energy"]
            self.mood = data["mood"]
            self.score = data["score"]
            self.level = data["level"]
            self.knowledge = data["knowledge"]
            self.missions = data.get("missions", self.missions)
            file.close()
            print("Data loaded successfully!")
            print(f"Welcome back, {self.name}!")

        except FileNotFoundError:
            print("There is no Bugsy saved !")
            print("Starting a new Bugsy !")
        except json.JSONDecodeError:
            print("Save file is empty or invalid ! \nStarting a new Bugsy ! ")


    def show_missions(self):
        print("=-=-=-=  MISSIONS  =-=-=-=".center(50))

        for mission in self.missions:
            status="Completed" if mission.get("completed",False) else "In Progress"
            print(f"Mission: {mission['name']}")
            print(f"Progress: {mission['progress']}/{mission['target']}")
            print(f"Status: {status}")


####################################################################


class SmartBugsy(Bugsy):

    def __init__(self, name):
        super().__init__(name)
        self.debug_points=15

    def debug(self):
        print("Smart Bugsy is debugging!")
        super().debug()    

    

####################################################################


class LazyBugsy(Bugsy):

    def __init__(self, name):
        super().__init__(name)
        self.debug_cost=10
    
    def debug(self):
        print("Lazy Bugsy is debugging!")
        super().debug()        
        

####################################################################


def create_bugsy():
    try:
        with open("bugsy_data.json", "r") as file:
            data = json.load(file)

        character_type = data.get("character_type", "Bugsy")

        classes = {
            "Bugsy": Bugsy,
            "SmartBugsy": SmartBugsy,
            "LazyBugsy": LazyBugsy
        }

        bug_class = classes.get(character_type, Bugsy)
        bug = bug_class(data.get("name", "Bugsy"))
        bug.load_data()
        return bug

    except (FileNotFoundError, json.JSONDecodeError):
        print("Starting a new Bugsy!")

        print("Choose your Bugsy type:".center(50))
        print("-"*50)
        print("1 - Normal Bugsy")
        print("2 - Smart Bugsy")
        print("3 - Lazy Bugsy")

        choice = input("Choose: ")

        classes = {
            "1": Bugsy,
            "2": SmartBugsy,
            "3": LazyBugsy
        }

        bug_class = classes.get(choice, Bugsy)
        return bug_class("Bugsy")


def start_new_game():
    if os.path.exists("bugsy_data.json"):
        os.remove("bugsy_data.json")

    print("Starting a new game!")
    
    print("Choose your Bugsy type:".center(50))
    print("-" * 50)
    print("1 - Normal Bugsy")
    print("2 - Smart Bugsy")
    print("3 - Lazy Bugsy")

    choice = input("Choose: ")

    classes = {
        "1": Bugsy,
        "2": SmartBugsy,
        "3": LazyBugsy
    }

    bug_class = classes.get(choice, Bugsy)
    name = input("Enter Bugsy's name: ").strip()

    if not name:
        name = "Bugsy"

    return bug_class(name)


bug = create_bugsy()

while True:
    print("Bugsy".center(50,"="),"\n")
    print("1 - Feed")
    print("2 - Debug")
    print("3 - Sleep")
    print("4 - Show Profile")
    print("5 - Teach Bugsy")
    print("6 - Show Skills")
    print("7 - Show Missions")
    print("8 - Save Game")
    print("9 - Start a New Game")
    print("0 - Exit\n")

    choice=input("Choose : ")

    if choice == "1":
        bug.feed()

    elif choice == "2":
        bug.debug()

    elif choice == "3":
        bug.sleep()

    elif choice == "4":
        bug.show_profile()

    elif choice == "5":
        bug.teach()    

    elif choice == "6":
        bug.show_knowledge()

    elif choice == "7":
        bug.show_missions()

    elif choice == "8":
        bug.save_data()

    elif choice == "9":
        bug=start_new_game()   

    elif choice == "0":
        bug.save_data()
        print("With My Best Wishes".center(50))
        print("ENG : Ahmed Ali Said".center(50))
        print("Goodbye!".center(50))
        break

    else:
        print("Invalid choice!")



