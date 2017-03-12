'''
Created on Feb 14, 2017

@author: Razvan
'''
from src.ui.console import Console
from src.ctrl.student_controller import StudentController
from src.repo.repository import Repository
from src.domain.student_validator import StudentValidator
from src.domain.grade_validator import GradeValidator
from src.ctrl.grade_controller import GradeController
from src.repo.repository_file import FileRepository
from src.domain.validator import Validator
from src.ctrl.assignment_controller import AssignmentCotroller
from src.domain.assignment_validator import AssignmentValidator

if __name__ == '__main__':
    
    studentsFile = "students"
    gradesFile = "grades"
    assignmentFile = "assignment"
    
    studentRepository = FileRepository(StudentValidator, studentsFile)
    studentController = StudentController(studentRepository)
     
    gradeRepository = FileRepository(GradeValidator, gradesFile)
    gradeController = GradeController(gradeRepository)
    
    assignmentRepository = FileRepository(AssignmentValidator, assignmentFile)
    assignmentController = AssignmentCotroller(assignmentRepository, gradeRepository, studentRepository)
     
    console = Console(studentController, gradeController, assignmentController)
    console.run()
     
    print("Bye bye")
    