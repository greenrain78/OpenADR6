"""
Schedule DB SchedulerManager
실질적인 스캐줄 객체
"""
import logging
import time

from apscheduler.schedulers.background import BackgroundScheduler

log = logging.getLogger(__name__)


class MainScheduler:

    def __init__(self, name: str = "default"):
        # 스캐줄 생성
        self.name = name
        self.schedule = BackgroundScheduler()
        log.info(f"SchedulerManager init Schedule : {self.name}")

    def create_job(self, method, schedule_id: str, *method_args, **schedule_time):
        """
        반복적으로 실행할 작업 생성
        :param method: 실행할 함수
        :param schedule_id: str
        :param schedule_time: dict 형식의 시간 인자 - cron 참고
        :return:
        """
        print(f"method : {method}")
        print(f"schedule_id : {schedule_id}")
        print(f"method_args : {method_args}")
        print(f"schedule_time : {schedule_time}")

        self.schedule.add_job(method, 'cron',  method_args, id=schedule_id, **schedule_time)
        log.debug(f"SchedulerManager create_job : {schedule_id}")

    def delete_job(self, schedule_id: str):
        """
        스케줄에 등록되어 있는 작업을 제거
        :param schedule_id: 스케줄 id
        :return:
        """
        self.schedule.resume_job(schedule_id)
        log.debug(f"SchedulerManager delete_schedule: {schedule_id}")

    def run(self):
        self.schedule.start()
        log.debug(f"스케줄러 {self.name} Run")


# 모듈 수준의 스캐줄러 생성
module_scheduler = MainScheduler('module_scheduler')


def schedule_start():
    module_scheduler.run()


# args 사용 불가 - 중요!
def add_schedule(func=None, **decorator_base_kwargs):
    # 속성을 미기입 - > decorator 호출
    if func:
        return schedule_decorators(func, **decorator_base_kwargs)
    # 속성을 기입 - > wrapper 로 감싼후 decorator 호출
    else:
        # 아무 인자도 들어오지 않음
        def base_wrapper(function):
            # 이중 Decorator 해결
            wrapped = schedule_decorators(function, **decorator_base_kwargs)()
            return wrapped

        return base_wrapper


# 실행 시 에만 동작
class schedule_decorators(object):
    scheduler = MainScheduler('decorators scheduler')

    # Decorator 생성
    # args 사용 금지 - 불가능
    def __init__(self, func, **init_kwargs):
        self.func = func
        self.args = init_kwargs

    # Decorator 호출
    def __call__(self):
        decorator_self = self
        print(f"self.scheduler : {self.scheduler.name}")

        # 스캐줄러 등록
        self.scheduler.create_job(self.func, self.func.__name__,  self.scheduler, **self.args)

        # 함수 Decorator 실행
        def wrapper(*args, **kwargs):
            print("call decorators_class")
            function = self.func(*args, **kwargs)
            return function

        return wrapper

    @classmethod
    def get_schedule(cls):
        """
        주의 일정 등록을 전부 등록후 사용
        해당 모듈을 import 되어 있어야함
        """
        # class 변수 반환
        return cls.scheduler

    @classmethod
    def run_schedule(cls):
        cls.scheduler.run()

