class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
"""
rectangle = Rectangle(width=4, height=5)
print(f"너비: {rectangle.width}, 높이: {rectangle.height}")
print(rectangle.area())
"""
class Animal:
    # def __init__(self, name) -> None:
    #     self.name = name

    def sound_play(self):
        pass

class Cat(Animal):
    # 인자에 기본값을 설정할 때 해당 인자는 가장 마지막에 위치
    def __init__(self, sound, name, legs=4) -> None:
        self.legs = legs
        self.sound = sound
        self.name = name

    def sound_play(self):
        return f"{self.name}: {self.sound} * 2"
    
class Dog(Animal):
    def __init__(self, sound, name, legs=4) -> None:
        self.legs = legs
        self.sound = sound
        self.name = name

    def sound_play(self):
        return self.sound * 3


animals = [Cat(name="르미", sound="Meow"), Dog(name="스트", sound="Bark")]
for animal in animals:
    print(animal.sound_play())