from mitmproxy import http

class GetHello:
    def match(self, flow: http.HTTPFlow) -> bool:
        return flow.request.method == 'GET' and flow.request.path == '/hello'
    
    class Action1:
        def request(self, flow: http.HTTPFlow) -> None:
            pass
    
        def response(self, flow: http.HTTPFlow) -> None:
            flow.response.set_text('''action1''')
        
    class Action2:
        def request(self, flow: http.HTTPFlow) -> None:
            pass
    
        def response(self, flow: http.HTTPFlow) -> None:
            flow.response.set_text('''action2''')

class PostHello:
    def match(self, flow: http.HTTPFlow) -> bool:
        return flow.request.method == 'POST' and flow.request.path == '/hello'
    
    class Action1:
        def request(self, flow: http.HTTPFlow) -> None:
            pass
    
        def response(self, flow: http.HTTPFlow) -> None:
            pass
