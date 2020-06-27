import http.server as http_server
import socketserver
from constants import (PORT, HTML_STUDENT_START, HTML_STUDENT_END,
                       HTML_COURSE_START, HTML_COURSE_END,
                       HTML_SELECT_SUB_START, HTML_SELECT_SUB_END,
                       HTML_SUBSCRIPTION_START, HTML_SUBSCRIPTION_END)
from database import StudentDatabase


class StartServer(http_server.SimpleHTTPRequestHandler, StudentDatabase):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
            return http_server.SimpleHTTPRequestHandler.do_GET(self)
        elif self.path == '/show_students':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            students = self.get_students()
            HTML_STUDENT_MID = ""
            for student in students:
                HTML_STUDENT_MID += """
                    <tr>
                        <td style="text-align: center">""" + str(student[1]) + """</td>
                        <td style="text-align: center">""" + str(student[2]) + """</td>
                    </tr>
                """
            result = HTML_STUDENT_START + HTML_STUDENT_MID + HTML_STUDENT_END
            self.wfile.write(bytes(result, "utf8"))
            return
        elif self.path == '/show_courses':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            courses = self.get_courses()
            HTML_COURSE_MID = ""
            for course in courses:
                HTML_COURSE_MID += """
                    <tr>
                        <td style="text-align: center">""" + str(course[1]) + """</td>
                        <td style="text-align: center">""" + str(course[2]) + """</td>
                    </tr>
                """
            result = HTML_COURSE_START + HTML_COURSE_MID + HTML_COURSE_END
            self.wfile.write(bytes(result, "utf8"))
            return
        elif self.path == '/show_subscriptions':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            subscriptions = self.get_subscriptions()
            HTML_SUBSCRIPTION_MID = ""
            for subscription in subscriptions:
                HTML_SUBSCRIPTION_MID += """
                    <tr>
                        <td style="text-align: center">""" + str(subscription[2]) + ' ' + str(subscription[3]) +  """</td>
                        <td style="text-align: center">""" + str(subscription[1]) + """</td>
                    </tr>
                """
            result = HTML_SUBSCRIPTION_START + HTML_SUBSCRIPTION_MID + HTML_SUBSCRIPTION_END
            self.wfile.write(bytes(result, "utf8"))
            return
        elif self.path == '/add_student':
            self.path = 'add_student.html'
            return http_server.SimpleHTTPRequestHandler.do_GET(self)
        elif self.path == '/add_course':
            self.path = 'add_course.html'
            return http_server.SimpleHTTPRequestHandler.do_GET(self)
        elif self.path == '/subscribe_courses':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            students = self.get_students()
            courses = self.get_courses()
            HTML_SELECT_SUB_MID = ""
            HTML_SELECT_SUB_MID += """<select id="student" name="student" required>"""
            for student in students:
                HTML_SELECT_SUB_MID += """<option value=""" + str(student[0]) + """
                >""" + str(student[1]) + ' ' + str(student[2]) + """</option>"""
            HTML_SELECT_SUB_MID += """</select>"""
            HTML_SELECT_SUB_MID += """<select id="course" name="course" required>"""
            for course in courses:
                HTML_SELECT_SUB_MID += """<option value=""" + str(course[0]) + """
                >""" + str(course[1]) + ' : ' + str(course[2]) + """</option>"""
            HTML_SELECT_SUB_MID += """</select>"""
            result = HTML_SELECT_SUB_START + HTML_SELECT_SUB_MID + HTML_SELECT_SUB_END
            self.wfile.write(bytes(result, "utf8"))
            return

        else:
            self.send_error(404, "File not found")

    def do_POST(self):
        if self.path == '/post_add_student':
            content_len = int(self.headers['Content-Length'])
            post_body = (self.rfile.read(content_len)).decode('utf-8')
            request = {x[0] : x[1] for x in [x.split("=") for x in post_body.split("&") ]}
            f_name = request["first_name"]
            l_name = request["last_name"]
            dob = request["date_of_birth"]
            phone = request["number"]
            self.update_student((f_name, l_name, phone, dob))
            print("POSt", self.path)
            self.path = ""
            return http_server.SimpleHTTPRequestHandler.do_GET(self)
        elif self.path == '/post_add_course':
            content_len = int(self.headers['Content-Length'])
            post_body = (self.rfile.read(content_len)).decode('utf-8')
            request = {x[0]: x[1] for x in [x.split("=") for x in post_body.split("&") ]}
            print(request)
            course = request["course_name"]
            details = request["course_details"]
            self.update_course((course, details))
            print("POSt", self.path)
            self.path = ""
            return http_server.SimpleHTTPRequestHandler.do_GET(self)
        elif self.path == '/post_add_course':
            content_len = int(self.headers['Content-Length'])
            post_body = (self.rfile.read(content_len)).decode('utf-8')
            request = {x[0]: x[1] for x in [x.split("=") for x in post_body.split("&") ]}
            print(request)
            course = request["course_name"]
            details = request["course_details"]
            self.update_course((course, details))
            print("POSt", self.path)
            self.path = ""
            return http_server.SimpleHTTPRequestHandler.do_GET(self)
        elif self.path == '/post_subscribe_courses':
            content_len = int(self.headers['Content-Length'])
            post_body = (self.rfile.read(content_len)).decode('utf-8')
            request = {x[0]: x[1] for x in [x.split("=") for x in post_body.split("&") ]}
            print(request)
            course = request["course"]
            student = request["student"]
            self.update_subscription((int(course), int(student)))
            print("POSt", self.path)
            self.path = ""
            return http_server.SimpleHTTPRequestHandler.do_GET(self)



handler = StartServer
student_server = socketserver.TCPServer(("", PORT), handler)
student_server.serve_forever()
