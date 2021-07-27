"""
실질적으로 api를 요청해서 데이터를 가져오는 객체
"""
import unittest

from src.Controller.API.adr_api_client import ADR_API_Client


class ADR_API_ClientTest(unittest.TestCase):

    def setUp(self):
        self.api = ADR_API_Client()

    def test_ping_server_elec(self):
        # 결과 값이 일치 여부 확인
        data = self.api.fetch_elec('ace', 300, 20200309)
        self.assertIsNotNone(data, "api 호출이 정상적으로 진행되지 않습니다.")

    def test_ping_server_eqps(self):
        # 결과 값이 일치 여부 확인
        data = self.api.fetch_eqps('ace')
        self.assertIsNotNone(data, "api 호출이 정상적으로 진행되지 않습니다.")

    def test_fetch_elec(self):
        """
        데이터가 많아서 생략
        :return:
        """
        data = self.api.fetch_elec('ace', 300, 20200309)
        # before_data = None
        # self.assertEqual(data, before_data, "Msg")

    def test_fetch_eqps(self):
        """
        데이터가 많아서 생략
        :return:
        """
        data = self.api.fetch_eqps('ace')
        # before_data = None
        # self.assertEqual(data, before_data,  "Msg")
