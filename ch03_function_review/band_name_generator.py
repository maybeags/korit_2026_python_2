# band_name_generator.py

# 변수명은 pants_color / last_food / band_name

'''
실행 예
지금 입고 있는 하의 색깔을 입력하세요 >>> 카키
마지막으로 먹은 음식을 입력하세요 >>> 브레드
당신의 밴드 이름은 카키 브레드입니다.

다 만들었으면 generate_band() 로 함수화하시오.
'''

def generate_band():
    pants_color = input("지금 입고 있는 하의 색깔을 입력하세요 >>> ")
    last_food = input("마지막으로 먹은 음식을 입력하세요 >>> ")
    print(f"당신의 밴드 이름은 {pants_color} {last_food}입니다.")

generate_band()

