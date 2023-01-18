import json

from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Coupon
from core.utils.migrate import participating_queue, wating_queue


class CouponEventView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(responses={200: 'Success', 400: 'Fail'})
    def get(self, request):
        try:
            wating_queue.put(
                json.dumps(
                    {'participant': 'wating'},
                )
            )

            element = json.loads(participating_queue.get(block=True, timeout=30))
            print(element['participant'])
            if element['participant'] > 10:
                return Response({'detail': '이벤트 쿠폰이 모두 소진되었습니다.'}, status=400)

            coupon = Coupon.objects.create()
            number = coupon.number

            return Response({'coupon': number}, status=200)
        except Exception as e:
            return Response({'error': e}, status=400)
