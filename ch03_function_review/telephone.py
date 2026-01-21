# telephone.py
'''
딕셔너리 기반의 연락처 관리

사용자로부터 3 명의 이름과 전화번호를 입력 받아 딕셔너리에 저장한 뒤, 입력한 정보를 추출하는
프로그램을 작성하시오.

실행 예
1 번째 사람의 이름의 입력하세요 >>> 김일
1 번째 사람의 연락처를 입력하세요 >>> 010-1234-5678
2 번째 사람의 이름의 입력하세요 >>> 김이
2 번째 사람의 연락처를 입력하세요 >>> 010-2345-6789
3 번째 사람의 이름의 입력하세요 >>> 김삼
3 번째 사람의 연락처를 입력하세요 >>> 010-3456-7890

입력 받은 연락처는 {'김일':'010-1234-5678', '김이':'010-2345-6789', '김삼':'010-3456-7890'}입니다.
'''
# phones = {}
# for i in range(1, 4):
#     dict_key = input(f"{i} 번째 사람의 이름을 입력하세요 >>> ")
#     dict_value = input(f"{i} 번째 사람의 연락처를 입력하세요 >>> ")
#     phones[dict_key] = dict_value

# print(f"입력 받은 연락처는 {phones}입니다.")
print("함수화했습니다 -----")
def write_phone_numbers1(names, phone_numbers):
    phones = {}
    for i in range(len(names)):
        phones[names[i]] = phone_numbers[i]
    print(f"입력 받은 연락처는 {phones}입니다.")

def write_phone_numbers2(names, phone_numbers):
    phones = dict(zip(names, phone_numbers))
    print(f"입력 받은 연락처는 {phones}입니다.")


write_phone_numbers2(["김일", "김이", "김삼"], ["010-1234-5678", "010-2345-6789", "010-3456-7890"])
'''
입력 받은 연락처는 {'김일':'010-1234-5678', '김이':'010-2345-6789', '김삼':'010-3456-7890'}입니다.
'''
