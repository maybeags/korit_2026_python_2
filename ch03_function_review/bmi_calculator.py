# bmi_calculator.py

# height / weight / bmi / answer
'''
실행 예
당신의 키는 몇 cm입니까? >>> 172
당신의 몸무게는 몇 kg입니까? >>> 68
당신의 bmi 지수는 23.0이고 비만전단계 입니다.

함수화 했을 시 함수명 calc_bmi()
'''
def calc_bmi():
    logo = '''
     ____   ___ ___  ____ 
|    \ |   |   ||    |
|  o  )| _   _ | |  | 
|     ||  \_/  | |  | 
|  O  ||   |   | |  | 
|     ||   |   | |  | 
|_____||___|___||____|
                      
    '''
    print(logo)

    height = float(input("당신의 키는 몇 cm입니까? >>> ")) / 100
    weight = float(input("당신의 몸무게는 몇 kg입니까? >>> "))
    bmi = weight / height**2
    '''
    a**3 : a x a x a
    그럼 여기 밑에는 bmi를 기준으로하는 조건문을 작성하면 되겠네요.
    '''
    if bmi < 18.5:
        answer = "저체중"
    elif bmi < 23:
        answer = "정상"
    elif bmi < 25:
        answer = "비만 전 단계"
    elif bmi < 30:
        answer = "1단계 비만"
    elif bmi < 35:
        answer = "2단계 비만"
    else:
        answer = "3단계 비만"

    print(f"당신의 bmi 지수는 {round(bmi, 2)}이고 {answer} 입니다.")
'''
round() : 첫 번째 argument를 반올림함, 두 번째 argument 만큼의 소수점을 표기함.
'''

calc_bmi()