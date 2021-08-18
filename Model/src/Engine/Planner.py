from typing import List

from src.Controller.Schedule.schedule_manager import MainScheduler
from src.Engine.TestEngine import TestEngine


def test_hello():
    # 안녕
    print("hello")


# test_engine = TestEngine()


def schedule_registration(scheduler: MainScheduler):
    """
    필요한 일정들을 등록
    :return:
    """
    # 예시) 매 0초에 hello 출력
    # scheduler.create_job(test_engine.print_hello, "test hello 8", second=0)


# 간단하게 리스트
def schedule_registration_list() -> List[dict]:
    return [
        {
            'func': test_hello,
            'id': 'test_hello',
            'args': {
                'second': 0
            }
        },
    ]


schedule_list = [
    {
        'func': test_hello,
        'id': 'test_hello',
        'args': {
            'second': 0
        }
    },
]
