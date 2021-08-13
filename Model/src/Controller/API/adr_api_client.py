"""
실질적으로 api를 요청해서 데이터를 가져오는 객체
"""
import logging
from typing import Optional
import requests

# 로거 생성
logger = logging.getLogger(__name__)


class ADR_API_Client:
    """
    open adr api 테스트
    """
    BASE_URL = 'http://222.122.224.225:9091/cems-api'
    version: Optional[str] = None
    count = 0

    def __init__(self, version: str = 'v1.0'):
        self.version = version

    @property
    def api_url(self) -> str:
        self.count = self.count + 1
        return f'{self.BASE_URL}/{self.version}'

    @property
    def header_data(self) -> dict:
        return {
            'Authorization': '1234qwer',
        }

    def call_requests(self, url):
        count = 0
        while count <= 0:
            try:
                response = requests.get(url, headers=self.header_data)
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

        response = self.call_requests(url)
        json_resp = response.json()
        result = json_resp.get("data", []).get("eqps")
        return result

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
        response = requests.get(url, headers=self.header_data)
        json_resp = response.json()
        data = json_resp.get("data", [])
        elecs = data.get("elecs")

        logger.debug(f"{response}({self.count}) - url: {url}")
        return elecs
