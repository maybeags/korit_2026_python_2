# ch04_class_static -> bank -> main.py
print()
'''
과제

은행 계좌를 관리하는 BankAccount 클래스를 작성하시오. 이 클래스는 계좌 소유자 이름, 계좌 번호, 잔액을 인스턴스
변수로 가집니다.

지시 사항.
    1. BankAccount 클래스를 정의하고 '생성자를 통해' owner, account_num, balance를 초기화하시오.
    3. 입금 기능을 하는 인스턴스 메서드(deposit())를 구현하시오 -> 입금 금액을 입력 받아 잔액을 증가시킵니다.
        -> 입금 금액이 0원 이하라면 입금이 불가능하도록 로직을 작성해야 합니다.
    4. 출금 기능을하는 인스턴스 메서드(withdraw())를 구현하시오 -> 출금 금액을 입력 받아 잔액을 감소시킵니다.
        -> 잔액 - 출금금액이 0원 미만이라면 출금이 불가능하도록 로직을 작성해야 합니다.
    5. 계좌 정보를 출력하는 인스턴스 메서드 print_account_info()를 구현하시오. -> 실행 예 참조
    6. 두 개의 계좌를 생성하고, 입금과 출금을 수행한 후 계좌 정보를 출력하시오.

실행 예
계좌 소유자 : 홍길동
계좌 번호 : 123-456-789
현재 잔액 : 100000원                 (십만원)

계좌 소유자 : 신사임당
계좌 번호 : 987-654-321
현재 잔액 : 500000원                 (오십만원)

50000원이 입금되었습니다. 현재 잔액 : 150000원            # account1에 대한 입금(오만원 입금)
잔액이 부족하여 출금할 수 없습니다.                        # account1에서 200000원 출금 시도 실패 사례(이십만원 출금 실패사례)
100000원이 출금되었습니다. 현재 잔액 : 50000원            # account1에 대한 출금 (십만원 출금 성공)

100000원이 출금되었습니다. 현재 잔액 : 400000원           # account2에 대한 출금(십만원 출금)
200000원이 입금되었습니다. 현재 잔액 : 600000원           # account2에 대한 입금(이십만원 입금)

최종 계좌 정보
계좌 소유자 : 홍길동
계좌 번호 : 123-456-789
현재 잔액 : 50000원                 (오만원)

계좌 소유자 : 신사임당
계좌 번호 : 987-654-321
현재 잔액 : 600000원                 (육십만원)
'''
class BankAccount:
    #클래스 변수
    bank_name = "코리아아이티은행"

    # 클래스 메서드
    @classmethod
    def introduce(cls, city):
        print(f'{cls.bank_name} {city} 지점')

    # 정적 메서드
    @staticmethod
    def cheerup():
        print(f'파이팅 ❤️')

    # 생성자 정의
    def __init__(self, owner,  account_num, balance):
        self.owner = owner
        self.account_num = account_num
        self.balance = balance
    # print_account_info()
    def print_account_info(self):
        print(f'계좌 소유자 : {self.owner}\n계좌 번호 : {self.account_num}\n현재 잔액 : {self.balance}\n')

    # call2()로 할지 call4()로 할지 그것도 아니면 call1() 한 다음에 input써서 int() 적용해서 계산할지 등등
    # 풀이는 call2() 유형으로 하겠습니다.
    def deposit(self, money):
        if money <= 0:
            print(f"{money} 원은 입금할 수 없는 금액입니다.")
            return                      # method에서 return 쓰고 뒤에 아무것도 안쓰면 그대로 종료
        #그리고 여기가 실행된다면 money는 0원 초과
        self.balance += money
        print(f"{money}원이 입금되었습니다. 현재 잔액 : {self.balance}원") # 더해지고 나서 출력해야 입금금액만큼 더한 값이 나오니까 이렇게 썼습니다.
    def withdraw(self, money):
        if money <= 0:
            print(f"{money} 원은 출금할 수 없는 금액입니다.")    # return을 안 쓰려면 전체를 조건문으로 작성할 수도 있겠네요.
        elif self.balance < money:
            print(f'잔액이 부족하여 출금할 수 없습니다.')
        else:
            self.balance -= money
            print(f"{money}원이 출금되었습니다. 현재 잔액 : {self.balance}원")

#  객체 생성 파트
account1 = BankAccount("홍길동", "123-456-789", 100000)
account2 = BankAccount("신사임당", "987-654-321", 500000)
account1.print_account_info()
account2.print_account_info()
account1.deposit(50000)
account1.withdraw(200000)
account1.withdraw(100000)

account2.withdraw(100000)
account2.deposit(200000)

account1.print_account_info()
account2.print_account_info()

BankAccount.introduce('부산진구')
BankAccount.cheerup()