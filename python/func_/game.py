import random

player_name = "지삐"
player_health = 100
player_attack = 10

enemy_name = "별이"
enemy_health = 50
enemy_attack = 5

def player_turn():
    global enemy_health

    action = input("어떤 행동을 하겠습니까? 건초어택/사료스킬")

    match action:
        case "건초어택":
                attack_dmg = random.randint(1, player_attack)
                attack(player_name, attack_dmg)
                enemy_health -= attack_dmg
                current_health(enemy_name, enemy_health)
        case "사료스킬":
                skill_dmg = random.randint(1, player_attack + 5)
                attack(player_name, skill_dmg)
                enemy_health -= skill_dmg
                current_health(enemy_name, enemy_health)
        case _:
                print("잘못된 입력입니다. 다시 입력해주세요!")
                player_turn()

def enemy_turn():
    global player_health
    enemy_attack_dmg = random.randint(1, enemy_attack + 5)
    attack(enemy_name, enemy_attack_dmg)
    player_health -= enemy_attack_dmg
    current_health(player_name, player_health)

def attack(character_name, attack_dmg):
    print(f"{character_name}의 공격! 적에게 {attack_dmg}의 피해를 입혔습니다!")

def current_health(character_name, remain_health):
     print(f"{character_name}에 체력이 {remain_health}만큼 남았습니다.")
while player_health > 0 and enemy_health > 0:
    print(f"{player_name}의 차례입니다.")
    player_turn()

    print(f"{enemy_name}의 차례입니다.")
    enemy_turn()

if player_health > 0:
    print("승리했습니다.")
else:
    print("패배했습니다.")