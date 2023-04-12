class Human:
    name = None
    age = None
    sex = None

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def get_data(self):
        print(f"Config: {self.name}, {self.age}, {self.sex}")