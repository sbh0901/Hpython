class 한글:
    def __init__(self):
        self.이프 = False
        self.와일 = True
        self.프린트 = 'print(self.s)'
        self.s = ''
        self.결과 = True
        self.부모결과 = True

    def 출력(self, s):
        print(str(s))
        return self

    def 정수(self, i):
        return int(i)

    def 글자(self, s):
        return str(s)

    def 소수(self, f):
        return float(f)

    def 연산자(self, b):
        return bool(b)

    def 튜플(self, t):
        return tuple(t)

    def 딕셔너리(self, d):
        return dict(d)

    def 리스트(self, l):
        return list(l)

    def 형태(self, t):
        if type(t) == str:
            return '글자'
        if type(t) == int:
            return '정수'
        if type(t) == float:
            return '소수'
        if type(t) == bool:
            return '연산자'
        if type(t) == tuple:
            return '튜플'
        if type(t) == dict:
            return '딕셔너리'
        if type(t) == list:
            return '리스트'
        return '없음'

    def 중지(self):
        self.와일 = False

    def 무한반복(self, tf: bool, q: str):
        self.와일 = bool(tf)
        q = f'''{q}'''
        print(q)
        while self.와일:
            exec(q)

    def 만약(self, 조건):
        def 데코레이터(함수):
            이전결과 = self.부모결과
            self.부모결과 = self.결과
            self.결과 = 조건 and self.부모결과

            if self.결과:
                함수(self)
            return self

        return 데코레이터

    def 함수(self, n, *args):
        d = f'def {n}({", ".join(args)}):\n'
        d += '    print("QNpfq")\n'

        namespace = {}
        exec(d, globals(), namespace)
        # def 함수생성(*args, **kwargs):
    def d(self, n, a, b, c):
        d = f'def {n}({a}, {b}, {c}):\n'
        d += f'\tprint("a, b, c")'
        print(d)
        exec(d)
        exec(f'{n}()')

    def 함수생성(self, 함수이름, *매개변수):
        일반매개변수 = []
        실행코드들 = []

        # 매개변수와 코드 분류
        for 항목 in 매개변수:
            if isinstance(항목, str):
                if 항목.startswith('>>>'):  # 실행 코드 식별
                    실행코드들.append(항목[3:])  # >>> 제거하고 저장
                else:
                    일반매개변수.append(항목)

        # 함수 정의 생성
        매개변수문자열 = ', '.join(['self'] + 일반매개변수)
        실행코드 = f"def {함수이름}({매개변수문자열}):\n"

        # 실행 코드 추가
        for 코드 in 실행코드들:
            실행코드 += f"    {코드}\n"

        # 반환 사전 생��
        반환사전 = [f"'{변수}': {변수}" for 변수 in 일반매개변수]
        if '결과 =' in ' '.join(실행코드들):  # 결과 변수가 있으면 포함
            반환사전.append("'결과': 결과")
        실행코드 += f"    return {{{', '.join(반환사전)}}}\n"

        namespace = {}
        exec(실행코드, globals(), namespace)

        def 실제함수(self, *args):
            이전결과 = self.부모결과
            self.부모결과 = self.결과

            매개변수사전 = namespace[함수이름](self, *args)

            for 변수, 값 in 매개변수사전.items():
                self.출력(f"{변수} = {값}")
            return self

        setattr(한글, 함수이름, 실제함수)
        return self

    # 사용 예시
if __name__ == '__main__':
    ㄱ = 한글()
# 여러 줄의 코드와 여러 변수를 사용하는 함수 생성
    ㄱ.함수생성('계산', 'a', 'b', 'c',
        '>>>임시 = a + b',
        '>>>결과 = 임시 * c')
    ㄱ.계산(2, 3, 4)  # a=2, b=3, c=4, 결과=20 출력

    # 조건문을 포함한 함수 생성
    ㄱ.함수생성('최대값', 'x', 'y',
        '>>>if x > y:',
        '>>>    결과 = x',
        '>>>else:',
        '>>>    결과 = y')
    ㄱ.최대값(5, 3)  # x=5, y=3, 결과=5 출력
    ''' # @ㄱ.만약(1 + 1 == 2)
    # def 첫번째(ㄱ):
    #     ㄱ.출력("첫 번째 조건 통과")
    #
    # @ㄱ.만약(1 + 1 == 2)
    # def 두번째(ㄱ):
    #     ㄱ.출력("두 번째 조건 통과")'''
