"""
Schedule DB SchedulerManager
실질적인 스캐줄 객체
"""
import logging

from apscheduler.schedulers.background import BackgroundScheduler

log = logging.getLogger(__name__)


class MainScheduler:

    def __init__(self):
        # 스캐줄 생성
        self.schedule = BackgroundScheduler()
        log.debug("SchedulerManager init Schedule")

    def create_job(self, method, schedule_id: str, **schedule_time):
        """
        반복적으로 실행할 작업 생성
        :param method: 실행할 함수
        :param schedule_id: str
        :param schedule_time: dict 형식의 시간 인자 - cron 참고
        :return:
        """
        self.schedule.add_job(method, 'cron', id=schedule_id, **schedule_time)
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
        log.debug("스케줄러 Run")
