import time
from core_lms.models import Logger


class PerfTrackerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        formatted_float = "{:.2f}".format(time.time()-start_time)
        log = Logger()
        log.execution_time = formatted_float
        log.user_id = request.user.id
        log.path = request.get_full_path()
        log.query_params = list(request.GET.items())
        log.save()
        return response
