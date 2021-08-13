"""
실질적으로 api를 요청해서 데이터를 가져오는 객체
"""
import logging
import time
from typing import Optional
import requests

# 로거 생성
from src.Controller.time_record import Record

logger = logging.getLogger(__name__)


class ADR_API_Client:
    """
    open adr api 테스트
    """
    BASE_URL = 'http://222.122.224.225:9091/cems-api'
    version: Optional[str] = None
    # api 정보
    eqps_recode = Record("eqps")
    elec_recode = Record("elec")

    def __init__(self, version: str = 'v1.0'):
        self.version = version

    @property
    def api_url(self) -> str:
        return f'{self.BASE_URL}/{self.version}'

    @property
    def header_data(self) -> dict:
        return {
            'Authorization': '1234qwer',
        }

    def call_requests(self, url, recode: Record):
        # 시간 기록
        start_time = time.time()

        count = 0
        while count >= 0:
            try:
                # 실질 api 요청
                response = requests.get(url, headers=self.header_data)
                # api 호출 시간 기록
                recode.insert_recode(time.time() - start_time)
                return response

            # 해당 오류가 발생시 무한 재시도 - 에러메세지 발생
            except requests.exceptions.ConnectionError:
                logger.error(f"요청 실패 재시도 {count} {url}")
                count += 1
            except Exception as e:
                logger.error(f"api 요청중 예상치 못한 오류 발생: {e}")
                raise e

    def fetch_eqps(self, siteId: str):
        """
        :param siteId:
        :return:
        - eqpCode 설비코드
        - eqpName 설비명
        - eqpType 설비 타입
        - perfId 성능 아이디
        """
        url = f'{self.api_url}/ems/eqps/{siteId}'
        # api 요청
        response = self.call_requests(url, self.eqps_recode)
        # 필요한 데이터만 선별
        json_resp = response.json()
        data = json_resp.get("data", [])
        eqps = data.get("eqps")

        logger.debug(f"{response} : {url}")
        return eqps

    def fetch_elec(self, siteId: str, perfId, ymd):
        """
        :param siteId:
        :param perfId:
        :param ymd:
        :return:
        - pnName     : 판넬명
        - eqpName    : 설비명
        - perfId        : 성능 ID
        - ymdms       : 일시
        - amPere       : 전류
        - arPower      : 피상전력
        - atvPower     : 유효전력
        - ratPower      : 무효전력
        - pwFactor      : 역률
        - accruePower  : 누적전력량
        - voltagerS      : RS선간전압
        - voltagesT      : ST선간전압
        - voltagetR      : TR선간전압
        - temperature   :온도
        """
        url = f'{self.api_url}/ems/elec/{siteId}/{perfId}/{ymd}'
        # api 요청
        response = self.call_requests(url, self.elec_recode)
        # 필요한 데이터만 선별
        json_resp = response.json()
        data = json_resp.get("data", [])
        elecs = data.get("elecs")

        logger.debug(f"{response} : {url}")
        return elecs

    def __repr__(self):
        return f"API Client \n" \
               f"{self.eqps_recode} \n" \
               f"{self.elec_recode} \n"
