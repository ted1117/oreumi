import random

class Player:
    def __init__(self, name, health, attack) -> None:
        self.name = name
        self.health = health
        self.attack = attack

class Game:
    def __init__(self) -> None:
        self.player = Player("지삐", 100, 10)
        self.enemy = Player("별이", 50, 5)
    
        while self.player.health > 0 and self.enemy.health > 0:
            print(f"{self.player.name}의 차례입니다.")
            self.player_turn()
            print(f"{self.enemy.name}의 차례입니다.")
            self.enemy_turn()

        if self.player.health > 0:
            print("승리했습니다.")
        else:
            print("패배했습니다.")

    def player_turn(self):
        action = input("어떤 행동을 하겠습니까? 건초어택/사료스킬 ")

        match action:
            case "건초어택":
                    attack_dmg = random.randint(1, self.player.attack)
                    self.attack(self.player.name, attack_dmg)
                    self.enemy.health -= attack_dmg
                    self.current_health(self.enemy.name, self.enemy.health)
            case "사료스킬":
                    skill_dmg = random.randint(1, self.player.attack + 5)
                    self.attack(self.player.name, skill_dmg)
                    self.enemy.health -= skill_dmg
                    self.current_health(self.enemy.name, self.enemy.health)
            case _:
                    print("잘못된 입력입니다. 다시 입력해주세요!")
                    self.player_turn()

    def enemy_turn(self):
        global player_health
        enemy_attack_dmg = random.randint(1, self.enemy.attack + 5)
        self.attack(self.enemy.name, enemy_attack_dmg)
        self.player.health -= enemy_attack_dmg
        self.current_health(self.player.name, self.player.health)

    def attack(self, character_name, attack_dmg):
        print(f"{character_name}의 공격! 적에게 {attack_dmg}의 피해를 입혔습니다!")

    def current_health(self, character_name, remain_health):
        print(f"{character_name}에 체력이 {remain_health}만큼 남았습니다.")
    


game = Game()