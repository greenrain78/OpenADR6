import unittest
from unittest import TestSuite

from settings import IS_RUN_ALL_TEST
from test.DB.model.test_EquipInfo import EquipmentsInfoTest


def run_tests():
    if IS_RUN_ALL_TEST:
        # 테스트 코드 탐색
        loader = unittest.TestLoader()
        tests = loader.discover('.')
        # 테스트 실행
        testRunner = unittest.runner.TextTestRunner()
        testRunner.run(tests)
    else:
        # 테스트 코드 추기
        fast = TestSuite()
        fast.addTest(EquipmentsInfoTest('test_CRUD_one'))
        # 테스트 실행

        runner = unittest.TextTestRunner()
        runner.run(fast)
