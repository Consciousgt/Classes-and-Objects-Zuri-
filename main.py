class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)
    
    print("Details of the new student")
    def change_name(self, newname):
        self.name = newname
        print("My name is", self.name)
    
    def change_age(self, newage):
        self.age = newage
        print("And my age is", self.age)

    def add_tracks(self, new_track):
        self.tracks.append(new_track)
        print("I m offering tracks", self.tracks)

    def get_score(self):
        return self.score

Bob = Student(name="Bob", age=26, tracks=["FE","BE"], score=20.90)

# Expected methods
Bob.change_name("Joshua Conscious")
Bob.change_age(24)
Bob.add_tracks("Python")
Bob.get_score()
