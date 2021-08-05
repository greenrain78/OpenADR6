from src.Controller.Schedule.schedule_manager import MainScheduler


def schedule_registration(scheduler: MainScheduler):
    """
    필요한 일정들을 등록
    :return:
    """
    # 예시) 매 0초에 hello 출력
    # scheduler.create_job(test_hello, "test hello", second=0)


def test_hello():
    # 안녕
    print("hello")
