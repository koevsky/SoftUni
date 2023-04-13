from unittest import TestCase, main
from project.student import Student


class StudentTests(TestCase):

    def setUp(self) -> None:
        self.student = Student("TestName", {"TestCourse": ["a", "b"]})
        self.student2 = Student("TestName")

    def test_correct_init(self):

        self.assertEqual(self.student.name, "TestName")
        self.assertEqual(self.student.courses, {"TestCourse": ["a", "b"]})
        self.assertEqual(self.student2.courses, {})

    def test_enroll_when_course_name_present_in_courses(self):

        message = self.student.enroll("TestCourse", ["c", "d"])
        expected_message = "Course already added. Notes have been updated."
        expected_notes = ["a", "b", "c", "d"]

        self.assertEqual(message, expected_message)
        self.assertEqual(self.student.courses["TestCourse"], expected_notes)

    def test_enroll_when_course_name_not_present_in_courses_dict_and_y(self):

        message = self.student2.enroll("TestCourse", ["c", "d"], "Y")
        expected_message = "Course and course notes have been added."

        expected_notes = ["c", "d"]
        expected_dict = {"TestCourse": ["c", "d"]}

        self.assertEqual(message, expected_message)
        self.assertEqual(self.student2.courses, expected_dict)
        self.assertEqual(self.student2.courses["TestCourse"], expected_notes)

    def test_enroll_when_course_name_not_present_in_courses_dict_and_none(self):
        message = self.student2.enroll("TestCourse", ["c", "d"])
        expected_message = "Course and course notes have been added."

        expected_notes = ["c", "d"]
        expected_dict = {"TestCourse": ["c", "d"]}

        self.assertEqual(message, expected_message)
        self.assertEqual(self.student2.courses, expected_dict)
        self.assertEqual(self.student2.courses["TestCourse"], expected_notes)

    def test_enroll_when_course_name_not_present_in_courses_dict(self):

        message = self.student2.enroll("TestCourse", ["abc"], "n")
        expected_message = "Course has been added."

        self.assertEqual(expected_message, message)
        self.assertEqual(self.student2.courses["TestCourse"], [])

    def test_add_notes_invalid_course_name_raise_exception(self):

        with self.assertRaises(Exception) as ex:
            self.student.add_notes("NoName", ["a", "b"])

        self.assertEqual(str(ex.exception), "Cannot add notes. Course not found.")

    def test_add_notes_valid_course_name(self):

        message = self.student.add_notes("TestCourse", "abc")
        expected_message = "Notes have been updated"

        notes = self.student.courses["TestCourse"]
        expected_notes = ["a", "b", "abc"]

        self.assertEqual(notes, expected_notes)
        self.assertEqual(message, expected_message)

    def test_leave_course_invalid_course_name_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("abc")

        self.assertEqual(str(ex.exception), "Cannot remove course. Course not found.")

    def test_leave_course_valid_course_name(self):

        message = self.student.leave_course("TestCourse")
        expected_message = "Course has been removed"

        self.assertEqual(self.student.courses, {})
        self.assertEqual(message, expected_message)


if __name__ == '__main__':
    main()
