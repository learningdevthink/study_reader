dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "": "아무것도 아닌 값입니다."
}

# 사용자로부터 입력을 받습니다.
key = "name" # input("키를 입력해주세요. : ")

# 출력합니다
if key in dictionary:
    print(dictionary[key])
else:
    print("존재하지 않는 값입니다.")