from pokemon_data import pokemon_data

#todo - 1 : pokemon_data.py에 있는 pokemon_data를 main.py로 가져 와서  "피카츄"라는 str 데이터를 콘솔에 출력하시오.

print(pokemon_data[24][1])

'''
ctrl + alt + s 
왼쪽의 메뉴 중 Python 클릭 -> interpreter
메인 파트의 좌측 상단 보시면 + 있습니다.
검색창에 prettytable

+------+----------+-----------+
| 번호 |   이름   |    타입   |
+------+----------+-----------+
|  1   | 이상해씨 |   풀/독   |
|  2   | 이상해풀 |   풀/독   |
|  3   | 이상해꽃 |   풀/독   |
|  4   |  파이리  |    불꽃   |
|  5   |  리자드  |    불꽃   |
|  6   |  리자몽  | 불꽃/비행 |
|  7   |  꼬부기  |     물    |
|  8   | 어니부기 |     물    |
|  9   |  거북왕  |     물    |
|  10  |  캐터피  |    벌레   |
|  11  |  단데기  |    벌레   |
|  12  |  버터플  | 벌레/비행 |
|  13  |  뿔충이  |  벌레/독  |
|  14  |  딱충이  |  벌레/독  |
|  15  |  독침붕  |  벌레/독  |
|  16  |   구구   | 노말/비행 |
|  17  |   피죤   | 노말/비행 |
|  18  |  피죤투  | 노말/비행 |
|  19  |   꼬렛   |    노말   |
|  20  |  레트라  |    노말   |
|  21  |  깨비참  |     독    |
|  22  |  독파리  |  독/비행  |
|  23  |   아보   |     독    |
|  24  |  아보크  |     독    |
|  25  |  피카츄  |    전기   |
|  26  |  라이츄  |    전기   |
+------+----------+-----------+
'''
from prettytable import PrettyTable

table = PrettyTable()

table.field_names = [ "번호", "이름", "타입"]
# table.add_row((1, "이상해씨", "풀/독"))
# table.add_row(pokemon_data[1])
# table.add_row(pokemon_data[2])
# table.add_row(pokemon_data[3])
# for i in range(len(pokemon_data)):           # index 넘버만 바뀌니까 in 반복가능객체가 아니라 in range() 사용
#     table.add_row(pokemon_data[i])          # 이 부분은 반복해서 .add_row()라는 메서드 호출
#
# print(table)                                                # 집어넣은 table 출력

# 문제 2 / in range() 안쓰고 in pokemon_data를 기준으로 반복문 작성해서 동일한 결과를 만드시오.

for pokemon in pokemon_data:    # list에서 반복문 돌리면 내부 element가 그대로 나옵니다.
    table.add_row(pokemon)  #pokemon의 자료형은 tuple이니까 그대로 argument로 써도 되지 않을까요

table.add_rows(pokemon_data)        # add_rows는 tuple을 내부 element로 가지는 전체 list를 통째로 다 집어넣을 수도 있습니다.
print(table)

'''
ch06_coffee_machine -> pop_version 패키지 생성 -> main.py
'''












