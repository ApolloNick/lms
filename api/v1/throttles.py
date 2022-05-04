from rest_framework import throttling


class AnonTeacherThrottle(throttling.BaseThrottle):
    scope = 'teachers'

    def allow_request(self, request, view):
        return 1
