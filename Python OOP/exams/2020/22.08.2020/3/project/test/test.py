from project.student_report_card import StudentReportCard
from  unittest import TestCase, main


class StudentReportCardTests(TestCase):

    def setUp(self) -> None:

        self.student_card = StudentReportCard("TestName", 12)
        self.student_card2 = StudentReportCard("Tn", 1)
        self.student_card3 = StudentReportCard("tn2", 10)
    def test_correct_init(self):

        self.assertEqual(self.student_card.student_name, "TestName")
        self.assertEqual(self.student_card.school_year, 12)
        self.assertEqual(self.student_card.grades_by_subject, {})

        self.assertEqual(self.student_card2.school_year, 1)
        self.assertEqual(self.student_card3.school_year, 10)

    def test_school_year_setter(self):
        self.assertEqual(self.student_card.school_year, 12)

    def test_name_setter(self):
        self.assertEqual(self.student_card.student_name, "TestName")

    def test_student_name_empty_value_raise_ValueError(self):

        with self.assertRaises(ValueError) as ve:
            self.student_card.student_name = ""

        self.assertEqual(str(ve.exception), "Student Name cannot be an empty string!")

    def test_invalid_school_year_zero_raise_ValueError(self):

        with self.assertRaises(ValueError) as ve:
            self.student_card.school_year = 0

        self.assertEqual(str(ve.exception), "School Year must be between 1 and 12!")

    def test_invalid_school_year_over_twelve_raise_ValueError(self):

        with self.assertRaises(ValueError) as ve:
            self.student_card.school_year = 13

        self.assertEqual(str(ve.exception), "School Year must be between 1 and 12!")

    def test_add_grade_subject_present(self):

        self.student_card.grades_by_subject = {"a": [4, 6], "b": [3, 4], "c": [4, 5]}

        self.student_card.add_grade("b", 5.10)

        self.assertEqual(self.student_card.grades_by_subject, {"a": [4, 6], "b": [3, 4, 5.10], "c": [4, 5]})
        self.assertIn(5.10, self.student_card.grades_by_subject['b'])

    def test_add_grade_subject_not_present(self):

        self.student_card.grades_by_subject = {"a": [4, 6], "b": [3, 4]}

        self.student_card.add_grade("c", 5.10)

        self.assertDictEqual(self.student_card.grades_by_subject, {"a": [4, 6], "b": [3, 4], "c": [5.10]})
        self.assertIn("c", self.student_card.grades_by_subject)
        self.assertIn(5.10, self.student_card.grades_by_subject["c"])

    def test_average_grade_by_subject(self):

        self.student_card.grades_by_subject = {"a": [4, 6], "b": [3, 4, 5]}
        result = self.student_card.average_grade_by_subject()
        expected_res = f"a: 5.00\nb: 4.00"
        expected_dict = {"a": [4, 6], "b": [3, 4, 5]}

        self.assertEqual(result, expected_res)
        self.assertEqual(self.student_card.grades_by_subject, expected_dict)

    def test_average_grade_by_subject_empty_dict(self):
        self.student_card.grades_by_subject = {}
        result = self.student_card.average_grade_by_subject()
        expected_res = ""

        self.assertEqual(result, expected_res)

    def test_average_grade_for_all_subjects(self):
        self.student_card.grades_by_subject = {"a": [4, 6], "b": [3, 4, 5]}

        result = self.student_card.average_grade_for_all_subjects()
        expected_result = f"Average Grade: 4.40"

        self.assertEqual(result, expected_result)

    def test_repr(self):
        self.student_card.grades_by_subject = {"a": [4, 6], "b": [3, 4, 5]}

        expected_report = f"Name: {self.student_card.student_name}\n" \
                 f"Year: {self.student_card.school_year}\n" \
                 f"----------\n" \
                 f"{self.student_card.average_grade_by_subject()}\n" \
                 f"----------\n" \
                 f"{self.student_card.average_grade_for_all_subjects()}"

        self.assertEqual(repr(self.student_card), expected_report)


if __name__ == "__main__":
    main()


