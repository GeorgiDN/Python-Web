import time

from django.utils.deprecation import MiddlewareMixin


def measure_time_execution(get_response):
    def middleware(request, *args, **kwargs):
        start_time = time.time()
        response = get_response(request, *args, **kwargs)
        end_time = time.time()

        print(f"Total time with function {end_time - start_time}")

        return response

    return middleware


# class MeasureTimeExecution:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request, *args, **kwargs):
#         start_time = time.time()
#         response = self.get_response(request, *args, **kwargs)
#         end_time = time.time()
#
#         print(f"Total time with class {end_time - start_time}")
#
#         return response


class MeasureTimeExecution(MiddlewareMixin):
    def process_request(self, request):
        self.start_time = time.time()

    def process_view(self, request, view, *args, **kwargs):
        print("Its processing")

    def process_template_response(self, request, response):
        print("It is in process of template response")
        return response

    def process_exception(self, request, exception):
        print(f"Its exception - {exception}")

    def process_response(self, request, response):
        self.end_time = time.time()
        total_time = self.end_time - self.start_time
        print(f"New class measure time {total_time}")
        return response
