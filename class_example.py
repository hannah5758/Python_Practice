class bending_machine(object):
    def __init__(self):
        self.drink = {
            'coak':500,
            'sprite':400,
            'fanta':600
        }
        self.money = 0
        
    def put_money(self):
        self.money = int(input("돈 투입:"))
        print(f"투입 금액: {self.money}")
        
    def choose(self):
        choice = int(input("번호 선택 (종료: 0): "))
        
        if choice == 0:
            pass
        
        elif choice == 1:
            print('구매 완료 coak')
            self.money = self.money - self.drink['coak']
            print(f'잔액: {self.money}')
        
        elif choice == 2:
            print('구매 완료 sprite')
            self.money = self.money - self.drink['sprite']
            print(f'잔액: {self.money}')
        
        elif choice == 3:
            print('구매 완료 fanta')
            self.money = self.money - self.drink['fanta']
            print(f'잔액: {self.money}')

wannadrink = bending_machine()
wannadrink.put_money()
wannadrink.choose()
