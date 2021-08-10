import os


def get_env_bool(env_name):
    """
    :arg env_name 환경변수 명
    :return true or false
    :raise bool 이 아닌경우 에러 발생
    """
    # 환경변수명에 따라 해당 값 가져오기
    env = os.environ.get(env_name)
    # str 형태를 bool 로 반환
    if env == "True":
        return True
    elif env == "False":
        return False
    # 예외 발생
    elif env is None:
        raise ValueError(f"env var is null : {env}")
    else:
        raise ValueError(f"env vars is not bool : {env}")