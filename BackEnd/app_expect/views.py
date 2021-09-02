import datetime

from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework.backends import DjangoFilterBackend
from requests.models import Response
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.views import APIView

from app_expect.models import predict_atv_power
from app_expect.serializers import Predict_atv_powerSerializer


class ELEC_Filter_View(RetrieveAPIView):
    queryset = predict_atv_power.objects.all()


class List_elec_View(ListAPIView):
    """
    임시로 list 로 출력
    추후 필터 추가
    아래는 임시 데이터
     site_id='ace', perf_id=230, ymdms=20200818
    """
    model = predict_atv_power
    serializer_class = Predict_atv_powerSerializer
    filter_backends = [DjangoFilterBackend]
    queryset = predict_atv_power.objects.filter(
        site_id='ace', perf_id=230,
        ymdms__year=2020,
        ymdms__month=8,
        ymdms__day=18)
    # queryset = predict_atv_power.objects.all()


class ELEC_Base_View(APIView):
    def get(self, req):
        # 모든 데이터 가져오기
        site_id = req.query_params.get("site_id")
        perf_id = req.query_params.get("perf_id")
        ymdms = req.query_params.get("ymdms")
        if ymdms:
            ymdms = datetime.datetime.strptime(ymdms, '%Y%m%d')
        refresh = req.query_params.get("refresh")
        print(f"{site_id}, {perf_id}, {ymdms}({ymdms.year}, {ymdms.month}, {ymdms.day})")
        queryset = predict_atv_power.objects.filter(
            site_id=site_id, perf_id=perf_id,
            ymdms__year=ymdms.year,
            ymdms__month=ymdms.month,
            ymdms__day=ymdms.day)
        print(queryset)
        serializer = Predict_atv_powerSerializer(queryset, many=True)
        print(serializer)
        return JsonResponse(serializer.data, safe=False)

        # return Response(serializer.data)

        #
        # # 파일 이름이 없으면 전체 리스트 가져오기
        # if field_id is None:
        #     queryset = FileInfo.objects.all()
        #     print("전체 리스트 출력")
        # else:
        #     try:
        #         queryset = FileInfo.objects.filter(file_field=field_id)
        #         print(f"일부분 출력 id: {field_id}")
        #     except Field.DoesNotExist:
        #         content = {
        #             '오류': '파일 저장 실패',
        #             '상세': f'id: {field_id}이라는 현장은 존재하지 않습니다.'
        #         }
        #         return Response(content, status=status.HTTP_400_BAD_REQUEST)
        # # 직렬화
        # serializer = FileSerializer(queryset, many=True)
        # return Response(serializer.data)
