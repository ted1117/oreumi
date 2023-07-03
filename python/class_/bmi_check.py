class HealthCheck:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def check_health(self):
        bmi = self.calculate_bmi()
        result = self.get_result(bmi)
        self.bmi = bmi

        print("=== 건강검진 결과 ===")
        print(f"이름: {self.name}")
        print(f"나이: {self.age}")
        print(f"신장: {self.height}cm")
        print(f"체중: {self.weight}kg")
        print(f"BMI: {bmi:.2f}")
        print(f"결과: {result}")

    def calculate_bmi(self):
        height_in_meters = self.height / 100
        bmi = self.weight / (height_in_meters ** 2)
        return bmi

    def get_result(self, bmi):
        if bmi < 18.5:
            return "저체중"
        elif 18.5 <= bmi < 23:
            return "정상체중"
        elif 23 <= bmi < 25:
            return "과체중"
        elif 25 <= bmi < 30:
            return "경도비만"
        else:
            return "고도비만"
    
    def backup_records(self):
        with open("output.txt", "w") as f:
            f.write(f"이름: {self.name}\n")
            f.write(f"나이: {self.age}\n")
            f.write(f"신장: {self.height}\n")
            f.write(f"체중: {self.weight}\n")
            f.write(f"BMI: {self.bmi}\n")
            f.write(f"비만 여부: {self.get_result(self.bmi)}")

a = HealthCheck("홍길동", 17, 173, 65)
b = HealthCheck("홍길순", 23, 160, 53)
c = HealthCheck("가나다", 30, 171, 60)
d = HealthCheck("라마바", 27, 166, 56)
e = HealthCheck("아자차", 38, 169, 64)

a_list = [a, b, c, d, e]
age_mean, age_sum = 0, 0
for member in a_list:
    age_sum += member.age
age_mean = age_sum / len(a_list)
print(age_mean)
