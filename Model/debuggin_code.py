import functools


def debugging(func):
    """디버깅용 코드 해당 함수에 대한 정보 확인"""

    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]  # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)  # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")  # 4
        return value

    return wrapper_debug


# args 사용 불가 - 중요!
def decorator_base(func=None, **decorator_base_kwargs):
    # 속성을 미기입 - > decorator 호출
    if func:
        return decorators_class(func, **decorator_base_kwargs)
    # 속성을 기입 - > wrapper 로 감싼후 decorator 호출
    else:
        # 아무 인자도 들어오지 않음
        def base_wrapper(function):
            # 이중 Decorator 해결
            wrapped = decorators_class(function, **decorator_base_kwargs)()
            return wrapped
        return base_wrapper


# 실행 시 에만 동작
class decorators_class(object):
    # Decorator 생성
    # args 사용 금지 - 불가능
    def __init__(self, func, **init_kwargs):
        self.func = func
        self.flag = init_kwargs['flag']

    # Decorator 호출
    def __call__(self):
        decorator_self = self

        # 함수 데코레이터
        def wrapper(*args, **kwargs):
            function = self.func(*args, **kwargs)
            return function

        return wrapper

# 추후 디버그용 보존
# # 속성 유무 분류
# # args 사용 불가 - 중요!
# def decorator_base(func=None, *decorator_base_args, **decorator_base_kwargs):
#     print(f"decorator_base func : {func}")
#     print(f"decorator_base args : {decorator_base_args}")
#     print(f"kwargs : {decorator_base_kwargs}")
#
#     # 속성을 미기입 - > 데코레이터 호출
#     if func:
#         return decorators_class(func, **decorator_base_kwargs)
#     # 속성을 기입 - > wrapper로 감싼후 데코레이터 호출
#     else:
#         def base_wrapper(function, *base_wrapper_args, **base_wrapper_kwargs):
#
#             print(f"base_wrapper_args : {base_wrapper_args}")
#             print(f"base_wrapper_kwargs : {base_wrapper_kwargs}")
#             return decorators_class(function, *base_wrapper_args, **decorator_base_kwargs)()
#
#         return base_wrapper
#
#
# # 실행 시 에만 동작
# class decorators_class(object):
#     # Decorator 생성
#     def __init__(self, func, flag, *init_args, **init_kwargs):
#         self.func = func
#         self.flag = flag
#         print("init decorators_class")
#         print(f"init_args : {init_args}")
#         print(f"init_kwargs : {init_kwargs}")
#
#     # Decorator 호출
#     def __call__(self, *call_args, **call_kwargs):
#         decorator_self = self
#         print('call decorators_class')
#         print(f"self : {decorator_self}")
#         print(f"flag : {decorator_self.flag}")
#         print(f"call_args : {call_args}")
#         print(f"call_args : {call_kwargs}")
#
#         # return self.func(*call_args, **call_kwargs)
#         # 함수 데코레이터
#         def wrapper(*args, **kwargs):
#             print(f"wrapper args : {args}")
#             print(f"wrapper kwargs : {kwargs}")
#             function = self.func(*args, **kwargs)
#             return function
#
#         return wrapper


# # 속성 확인
# # 단속 사용시 self 적용
# def check_empty(*deco_args, **deco_kwargs):
#     print(f"check_empty ")
#     print(f"deco_args : {deco_args}")
#     print(f"deco_kwargs : {deco_kwargs}")
#
#     # 함수 동작
#     def check_method(function, *method_args, **method_kwargs):
#         print("check_method")
#         print(f"method_args : {method_args}")
#         print(f"method_kwargs : {method_kwargs}")
#
#         # 함수 데코레이터
#         def wrapped(*args, **kwargs):
#             print(f"function : {function}")
#             print(f"args : {args}")
#             print(f"kwargs : {kwargs}")
#             func = function(*args, **kwargs)
#             return func
#
#         return wrapped
#
#     return check_method


# # 실행 시 에만 동작
# # 단독 사용시 self 적용
# class decorators_class_self(object):
#     def __init__(self, flag):
#         self.flag = flag
#
#         # args_repr = [dir(a) for a in self]  # 1
#
#         # print(f"init : {dir(self)}")
#
#         def wrapper(*args, **kwargs):
#             print(f"args : {args}")
#             print(f"kwargs : {kwargs}")
#             print(f"self : {self}")
#
#     def __call__(self, func):
#         decorator_self = self
#
#         def wrapper(*args, **kwargs):
#             print(f"self : {decorator_self}")
#             print(f"flag : {decorator_self.flag}")
#             print(f"func : {func}")
#             print(f"args : {args}")
#             print(f"kwargs : {kwargs}")
#
#             # try:
#             #     return func(*args, **kwargs)
#             # except Exception as e:
#             #     print(f'ERR {func.__name__}() : {str(e)}')
#             #     return decorator_self.flag
#
#         return wrapper
