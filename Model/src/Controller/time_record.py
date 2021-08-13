import time


class Record:
    def __init__(self, name):
        self.name = name
        self.min = None
        self.max = 0
        self.total = 0
        self.average = 0
        self.count = 0

    def __repr__(self):
        return f"{self.name}(count({self.count}): total({self.total}) - [{self.average}, {self.min}, {self.max}])"

    def insert_recode(self, api_time):
        self.count += 1
        self.total += api_time

        # 최대 최소 기록
        if self.min is None or api_time < self.min:
            self.min = api_time
        elif api_time > self.max:
            self.max = api_time

        # 평균 기록
        self.average = self.total / self.count


def record_decorator(f):
    def wrapper(self, *args, **kwargs):
        # 시간 기록
        start_time = time.time()
        # 함수 매핑
        func = f(self, *args, **kwargs)
        end_time = time.time()
        # 자신의 객체에 기록 저장
        self.record.insert_recode(end_time - start_time)

        return func
    return wrapper

        

