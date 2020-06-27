import sqlite3
from sqlite3 import Error
from constants import DATABASE_PATH


class StudentDatabase:

    def create_connection(self, db_files):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file name
        :return: Connection object or None
        """
        connection = None
        try:
            connection = sqlite3.connect(db_files)
            return connection
        except Error as e:
            print(e)

        return connection

    def update_student(self, task):
        """
        add a student
        :param conn:
        :param task:
        :return:
        """
        conn = self.create_connection(DATABASE_PATH)
        sql = ''' INSERT INTO StudentWeb_student(first_name,last_name,contact_number,birth_date) VALUES(?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, task)
        conn.commit()
        # print(cur.execute("SELECT name FROM sqlite_master WHERE type='table';"))
        # print(cur.fetchall())
        # print(cur.execute("SELECT * From 'StudentWeb_student'"))
        # print(cur.fetchall())

        return cur.lastrowid

    def update_course(self, task):
        """
        add a course
        :param conn:
        :param task:
        :return:
        """
        conn = self.create_connection(DATABASE_PATH)
        sql = ''' INSERT INTO StudentWeb_course(course_name,course_details) VALUES(?,?) '''
        cur = conn.cursor()
        cur.execute(sql, task)
        conn.commit()
        return cur.lastrowid

    def update_subscription(self, task):
        """
        add a course to a student
        :param conn:
        :param task:
        :return:
        """
        conn = self.create_connection(DATABASE_PATH)
        sql = ''' INSERT INTO StudentWeb_studentcourses(course_id,student_id) VALUES(?,?) '''
        cur = conn.cursor()
        cur.execute(sql, task)
        conn.commit()
        return cur.lastrowid

    def get_students(self):
        """
        Get all students
        :param conn:
        :param task:
        :return:
        """
        conn = self.create_connection(DATABASE_PATH)
        sql = ''' SELECT * FROM StudentWeb_student'''
        cur = conn.cursor()
        cur.execute(sql)
        # conn.commit()
        return cur.fetchall()

    def get_courses(self):
        """
        Get all course
        :param conn:
        :param task:
        :return:
        """
        conn = self.create_connection(DATABASE_PATH)
        sql = ''' SELECT * FROM StudentWeb_course'''
        cur = conn.cursor()
        cur.execute(sql)
        # conn.commit()
        return cur.fetchall()

    def get_subscriptions(self):
        """
        Get all course
        :param conn:
        :param task:
        :return:
        """
        conn = self.create_connection(DATABASE_PATH)
        sql = '''
        SELECT StudentCourse.id, Course.course_name, Student.first_name, Student.last_name From StudentWeb_studentcourses StudentCourse
        JOIN StudentWeb_course Course on StudentCourse.course_id=Course.id
        JOIN StudentWeb_student Student on StudentCourse.student_id=Student.id
        '''
        cur = conn.cursor()
        cur.execute(sql)
        # conn.commit()
        return cur.fetchall()
