from http.server import HTTPServer, BaseHTTPRequestHandler
import re
from urllib.parse import unquote_plus
import html

headers_data = ''
respose_data = ''
code_data = '200'

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    # headers_data = ''
    # global headers_data

    def template(self):
        global headers_data
        global respose_data
        global code_data
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
                        code_data = post_data.split('&headerInput=')[0].split('codeInput=')[1]
                        if code_data == '':
                            code_data = '200'
                        respose = post_data.split('headerInput=')[1].split('&bodyInput=')
                        headers_data = respose[0]
                        respose_data = respose[1]
                    except:
                        pass

                    code_data_escaped = html.escape(code_data)  # 对响应码进行转义
                    headers_data_escaped = html.escape(headers_data)  # 对响应头进行转义
                    response_data_escaped = html.escape(respose_data)  # 对响应体进行转义

                    content = f.read()
                    content = content.replace(b'{{code_data}}', code_data_escaped.encode())  # 替换html占位符
                    content = content.replace(b'{{headers_data}}', headers_data_escaped.encode())
                    content = content.replace(b'{{body_data}}', response_data_escaped.encode())
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(content)
                return

        self.log_request(int(code_data))
        self.send_response_only(int(code_data), None)
        headers_list = headers_data.split('\r\n')
        # 通过获取的响应头，构造对应数据
        if 'Content-Length' not in headers_list:
            self.send_header('Content-Length', str(len(respose_data)))
        if '' in headers_list:
            headers_list.remove('')

        for header in headers_list:
            info = header.split(':')  # 根据:分割响应头, 并去除值开头空格
            while info[1][0] == ' ':
                info[1] = info[1][1:]
            self.send_header(info[0], info[1])

        self.end_headers()
        self.wfile.write(respose_data.encode())

    def do_GET(self):
        self.template()

    def do_POST(self):
        self.template()


httpd = HTTPServer(('0.0.0.0', 8888), SimpleHTTPRequestHandler)
httpd.serve_forever()
