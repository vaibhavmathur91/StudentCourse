PORT = 8080
DATABASE_PATH = r"StudentDB.db"

HTML_SUBSCRIPTION_START = """
  <div style="width: 30%; float: left;margin-right:10px">
  <table style="width: 90%; border: 1px solid black" >
    <div style="text-align: center;"> <b>Subscription Details</b></div>
    <tr>
      <th style="text-align: center">Student Name</th>
      <th style="text-align: center">Course Name</th>
    </tr>
"""

HTML_SUBSCRIPTION_END = """
  </table>
  </div>
"""


HTML_STUDENT_START = """
  <div style="width: 30%; float: left;margin-right:10px">
  <table style="width: 90%; border: 1px solid black" >
    <div style="text-align: center;"> <b>Student Details</b></div>
    <tr>
      <th style="text-align: center">Firstname</th>
      <th style="text-align: center">Lastname</th>
    </tr>
"""

HTML_STUDENT_END = """
  </table>
  </div>
"""


HTML_COURSE_START = """
  <div style="width: 30%; float: left;margin-right:10px">
  <table style="width: 90%; border: 1px solid black" >
    <div style="text-align: center;"> <b>Coures Details</b></div>
    <tr>
      <th style="text-align: center">Course Name</th>
      <th style="text-align: center">Course Details</th>
    </tr>
"""

HTML_COURSE_END = """
  </table>
  </div>
"""


HTML_SELECT_SUB_START = """

<div style="margin-top: 10%">
  <form action="post_subscribe_courses" method="post">

"""


HTML_SELECT_SUB_END = """
    </br>
    </br>
    <input type="submit">
  </form>
</div>
"""