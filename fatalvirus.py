import random

# 17 계산기 (제곱연산 추가)
def intCal():
    # num1 = int( input( '좌변값을 하나 입력하세요' ) )
    # num2 = int( input( '우변값을 하나 입력하세요' ) )
    num1 = 10
    num2 = 20
    fmt = '%d + %d = %d \n%d - %d = %d \n'
    fmt += '%d * %d = %d \n%d / %d = %.2f \n'
    fmt += '%d ** %d = %d'

    print( fmt % ( num1, num2, num1 + num2, \
                   num1, num2, num1 - num2, \
                   num1, num2, num1 * num2, \
                   num1, num2, num1 / num2, \
                   num1, num2, num1 ** num2 ) )

# 19 윤년여부
def isLeapYear():
    # year = int( input( '윤년여부를 알고 싶은 년도를 입력하세요.> ' ) )
    year = 2018
    isleap = '윤년이 아닙니다.'

    if year % 4 == 0 and year % 100 != 0:
        isleap = '윤년입니다.'
    elif year % 400 == 0:
        isleap = '윤년입니다.'

    print( "%d년은 %s" % ( year, isleap ) )

# 20 복권발행
def insertLucky():
    wrongtype = '잘못 입력하셨습니다!'
    while True:
        lucky1 = int(input('첫번째 복권번호를 입력하세요!(1 ~ 45)> '))
        if lucky1 > 0 and lucky1 < 46:
            break
        print(wrongtype)

    while True:
        lucky2 = int(input('두번째 복권번호를 입력하세요!(1 ~ 45)> '))
        if lucky2 != lucky1 and lucky2 > 0 and lucky2 < 46:
            break
        print(wrongtype)

    while True:
        lucky3 = int(input('세번째 복권번호를 입력하세요!(1 ~ 45)> '))
        if lucky3 != lucky2 and lucky3 != lucky1 and lucky3 > 0 and lucky3 < 46:
            break
        print(wrongtype)

    lucky = [lucky1, lucky2, lucky3]
    return lucky

def generateLotto():
    import random

    lotto1 = random.randint(1, 45)

    while True:
        lotto2 = random.randint(1, 45)
        if lotto2 != lotto1:
            break

    while True:
        lotto3 = random.randint(1, 45)
        if lotto3 != lotto2 and lotto3 != lotto1:
            break

    lotto = [lotto1, lotto2, lotto3]
    return lotto

def checkMatch(lucky, lotto):
    match = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if lucky[i] == lotto[j]:
                match += 1
    if match == 0:
        print('다음 기회에...')
    elif match == 3:
        print('축하합니다! 상금 백만원!!!')
    elif match == 2:
        print('축하합니다! 상금 만원!!')
    elif match == 1:
        print('축하합니다! 상금 천원!')

    print('복권번호 : ', lucky)
    print('당첨번호 : ', lotto)

def rouletlotto():

    # lucky = insertLucky()
    lucky = [15, 26, 34]

    lotto = generateLotto()

    checkMatch(lucky, lotto)