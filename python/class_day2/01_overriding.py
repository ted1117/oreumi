class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def speak(self):
        print("동물이 소리를 냅니다.")

class Dog(Animal):
    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color

    def speak(self):
        super().speak()    # 부모 클래스의 메서드 실행
        print("개가 짖습니다.")

my_dog = Dog("스트", "검은색")
my_dog.speak()