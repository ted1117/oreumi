class Car:
    wheel = 4
    window = 2
    # 생성자
    def __init__(self, people) -> None:
        self.people = people
        self.window = 2
        self.wheel = 4

    def brake(self):
        print(f"{self.people}(이)가 brake!")

    def accelerate(self):
        print("accelerate!")

my_car = Car("졸라맨")
my_car.brake()
print(dir(Car))