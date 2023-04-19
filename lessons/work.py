class course:
    def __init__(self, name, level, req):
        self.name = name
        self.level = level 
        self.req = req


    def find_courses(course_list: list[str], req: str):
        new_courses: list = []
        for course in course_list:
            if course.level >= 400 and req in course.req:
                new_courses.append(course)
        return new_courses

