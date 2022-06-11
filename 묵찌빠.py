from random import choice

#determine(x,y) : x와 y중 누가 이긴지 결정
def determine(pc, player):
    if pc == player: return "비김"
    if pc == "바위" or pc == "묵":
        if player == "가위" or player == "찌":
            return "pc"
        if player == "보" or player == "빠":
            return "player"
    if pc == "가위" or pc == "찌":
        if player == "바위" or player == "묵":
            return "player"
        if player == "보" or player == "빠":
            return "pc"
    if pc == "보" or pc == "빠":
        if player == "가위" or player == "찌":
            return "player"
        if player == "바위" or player == "묵":
            return "pc"

rock_scissor_paper = ["가위","바위","보"]
muk_jji_bba = ["묵", "찌", "빠"]

print("""가위, 바위, 보 중 한개의 단어를 입력해주세요.""")
while True:
    print(", ".join(rock_scissor_paper))
    computers_choice = choice(rock_scissor_paper)
    players_choice = input("플레이어 : ")
    if players_choice not in rock_scissor_paper:
        print("잘못된 값을 입력하셨습니다. 다시 입력해주세요.\n")
        continue
    print(f"컴퓨터 : {computers_choice}")
    d = determine(computers_choice, players_choice)
    if d == "비김":
        print("비겼습니다. 다시 시도하세요.\n")
        continue
    else: break

while True:
    print("")
    if d == "pc":
        print("이번에 비기면 플레이어의 패배입니다.")
        print(", ".join(muk_jji_bba))
        computers_choice = choice(muk_jji_bba)
        players_choice = input("플레이어 : ")
        if players_choice not in muk_jji_bba:
            print("잘못된 값을 입력하셨습니다. 다시 입력해주세요.")
            continue
        print(f"컴퓨터 : {computers_choice}")
        d = determine(computers_choice, players_choice)
        if d == "비김":
            print("플레이어의 패배입니다.")
            break
    if d == "player":
        print("이번에 비기면 플레이어의 승리입니다.")
        print(", ".join(muk_jji_bba))
        computers_choice = choice(muk_jji_bba)
        players_choice = input("플레이어 : ")
        if players_choice not in muk_jji_bba:
            print("잘못된 값을 입력하셨습니다. 다시 입력해주세요.")
            continue
        print(f"컴퓨터 : {computers_choice}")
        d = determine(computers_choice, players_choice)
        if d == "비김":
            print("플레이어의 승리입니다.")
            break