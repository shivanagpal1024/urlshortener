from django.core.exceptions import PermissionDenied
class FilterIPmiddleware(object):
    def requestIP(self,request):
        all_ips=['192.168.1.1','123.123.123.1']
        ip=request.META.get('REMOTE ADDR')
        print('ip'+ip)
        if ip not in all_ips:
            raise PermissionDenied
        return None
