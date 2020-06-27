# StudentCourse

we have 2 ways to run project :
1) without framework
2) with framework

# 1 (Without Framework)
    Steps to run server :
        1) go to path StudentCourse/tree/master/StudentServer/root
        2) run server.py
    
    basic language: python3.6 , htmls, css
  
    database : sqlite3
    
    
    outputWalkthrough WITHOUT framwork:

            Window#1:

                index.html :

                    3 links to add new (student, course, subscription)
                    3 links to Show details (student, course, subscription)

            Window#2:

                add_student.html

                    form is being shown (All fields are mandetory)

                    on click of submit POST call is made

            Window#3:

                add_course.html

                    form is being shown (All fields are mandetory)

                    on click of submit POST call is made


            Window#4:

                subscribe_courses.html

                    form is being shown with 2 dropdown  selections  first(student) and second(course)                
                    on click of submit POST call is made

           
                add_student.html

                    form is being shown (All fields are mandetory)

                    on click of submit POST call is made

            Window#5:

                Show Student
                    
                    Details of all students registered

            Window#6:

                Show course
                    
                    Details of all courses registered
    
    
            Window#7:

                Show subscriptions
                    
                    Details of all subscriptions registered
    
        
# 2 (With Framework)
Project Tech Used: 

    Framework : Django
  
    basic language: python3.6 , htmls, css
  
    database : sqlite3
     
    Please check below Code files :
      1) /StudentCourse/tree/master/root/StudentWeb/models.py
      2) /StudentCourse/tree/master/root/StudentWeb/urls.py
      3) /StudentCourse/tree/master/root/StudentWeb/views.py

    Note:  Please check above urls.py file and then follow the corresponding view method  for each url

    Please check below path for Static(Html) files: 
      1) StudentCourse/tree/master/root/templates/StudentWeb


    outputWalkthrough with Framwork:

            Window#1:

                index.html :

                    3 tables are shown All student-data,  All courses  and  All subscriptions

                    3 links to add new (student, course, subscription)

            Window#2:

                add_student.html

                    form is being shown (All fields are mandetory)

                    on click of submit POST call is made

            Window#3:

                add_course.html

                    form is being shown (All fields are mandetory)

                    on click of submit POST call is made


            Window#4:

                subscribe_courses.html

                    form is being shown with 2 dropdown  selections  first(student) and second(course)                
                    on click of submit POST call is made


