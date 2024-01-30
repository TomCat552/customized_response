from http.server import HTTPServer, BaseHTTPRequestHandler
import re
from urllib.parse import unquote_plus

headers_data = ''
respose_data = ''


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    # headers_data = ''
    # global headers_data

    def template(self):
        global headers_data
        global respose_data
        routes = [
            r'^/api/v1/config$',  # 配置路径
            # 添加更多路由规则...
            # r'^/static/js'  # 本地静态js
        ]

        for route in routes:
            if re.match(route, self.path):
                with open('static/html/config.html', 'rb') as f:

                    try:  # 首次get访问时无参数跳过
                        # 获取config请求参数
                        content_length = int(self.headers.get('Content-Length', 0))
                        post_data = unquote_plus(self.rfile.read(content_length).decode('utf-8'))

                        respose = post_data.split('headerInput=')[1].split('&bodyInput=')
                        headers_data = respose[0]
                        respose_data = respose[1]
                    except:
                        pass

                    # post_data = self.rfile.read(content_length).decode('utf-8')
                    # headers_data = unquote_plus(post_data)  # 解码 headerInput 参数

                    content = f.read()
                    content = content.replace(b'{{headers_data}}', headers_data.encode())  # 替换html占位符
                    content = content.replace(b'{{body_data}}', respose_data.encode())  # 替换html占位符
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(content)
                return
        self.log_request(101)
        self.send_response_only(101, None)

        # 通过获取的响应头，构造对应数据
        for header in headers_data.split('\r\n'):
            info = header.split(': ')
            self.send_header(info[0], info[1])

        self.end_headers()
        self.wfile.write(respose_data.encode())

    def do_GET(self):

        self.template()

    def do_POST(self):

        self.template()


httpd = HTTPServer(('0.0.0.0', 8888), SimpleHTTPRequestHandler)
httpd.serve_forever()
