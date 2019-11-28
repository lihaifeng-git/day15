from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect,HttpResponse
class AuthMD(MiddlewareMixin):
    white_list=['/app01/login/',]
    black_list=['/app01/black/',]

    def process_request(self,request):
        next_url=request.path_info
        if next_url in self.black_list:
            return HttpResponse('这是一个错误的url')
        elif next_url in self.white_list or request.session.get("user"):
            return
        else:
            return redirect("/app01/login/?return={}".format(next_url))