class Family:
    def introduce(self):
        print("저희는 가족입니다.")

    def run(self):
        print('2발')


class Person(Family):
    def introduce(self):
        # 기능 추가 및 수정
        super(Person, self).introduce()
        print("저는 가족의 구성원입니다.")

    def run(self):
        # 기능 재정의 및 수정
        print('4발')


a = Family()
b = Person()

a.introduce()
b.introduce()
b.run()

