from project.team import Team
from unittest import TestCase, main


class TeamTests(TestCase):

    def setUp(self) -> None:
        self.team_1 = Team('TeamOne')
        self.team_2 = Team('TeamTwo')

    def test_correct_init(self):
        self.assertEqual(self.team_1.name, 'TeamOne')
        self.assertEqual(self.team_1.members, {})

    def test_name_with_number_raise_VE(self):
        with self.assertRaises(ValueError) as ve:
            self.team_1.name = "Team1"

        self.assertEqual(str(ve.exception), "Team Name can contain only letters!")

    def test_add_member_all_unique(self):
        self.team_1.members = {"Ivan": 23, 'Dimitar': 55}
        names = {'Petkan': 25, "Dragan": 34}
        message = self.team_1.add_member(**names)
        expected_message = "Successfully added: Petkan, Dragan"

        self.assertEqual(message, expected_message)
        self.assertEqual(self.team_1.members, {"Ivan": 23,'Dimitar': 55, 'Petkan': 25, "Dragan": 34})

    def test_add_member_already_added(self):
        self.team_1.members = {"Ivan": 23, 'Mitak': 21}
        names = {"Ivan": 30, 'Petkan': 25, "Dragan": 34}

        message = self.team_1.add_member(**names)
        expected_message = "Successfully added: Petkan, Dragan"

        self.assertEqual(message, expected_message)
        self.assertEqual(self.team_1.members, {"Ivan": 23, 'Mitak': 21, 'Petkan': 25, "Dragan": 34})

    def test_remove_member_existing(self):
        self.team_1.members = {"Ivan": 30, 'Petkan': 25, "Dragan": 34}
        message = self.team_1.remove_member('Ivan')
        expected_message = "Member Ivan removed"

        self.assertEqual(message, expected_message)
        self.assertEqual(self.team_1.members, {'Petkan': 25, "Dragan": 34})
        self.assertNotIn("Ivan", self.team_1.members)

    def test_remove_member_non_existing(self):
        self.team_1.members = {"Ivan": 30, 'Petkan': 25, "Dragan": 34}
        message = self.team_1.remove_member('Koki')
        expected_message = "Member with name Koki does not exist"

        self.assertEqual(message, expected_message)
        self.assertEqual(self.team_1.members, {"Ivan": 30, 'Petkan': 25, "Dragan": 34})

    def test_gt_True(self):
        self.team_1.members = {"Ivan": 22, 'Petkan': 33}
        self.team_2.members = {'A': 12, "B": 34, "C": 22, 'D': 13}

        result = len(self.team_1.members) < len(self.team_2.members)
        expected_result = self.team_1 < self.team_2

        self.assertEqual(expected_result, result)

    def test_gt_false(self):
        self.team_1.members = {"Ivan": 22, 'Petkan': 33}
        self.team_2.members = {'A': 12, "B": 34, "C": 22, 'D': 13}

        result = len(self.team_1.members) > len(self.team_2.members)
        expected_result = self.team_1 > self.team_2

        self.assertEqual(expected_result, result)

    def test_len(self):
        self.team_1.members = {"Ivan": 30, 'Petkan': 25, "Dragan": 34}
        result = len(self.team_1)
        expected_result = 3
        self.assertEqual(result, expected_result)
        self.assertEqual(len(self.team_1), len(self.team_1.members))

    def test_add_two_teams(self):
        self.team_1.members = {'Petkan': 28, "Dragan": 34}
        self.team_2.members = {"Ivan": 30, 'Petkan': 25}

        result_team = self.team_1.__add__(self.team_2)
        new_name = 'TeamOneTeamTwo'
        new_members = {'Petkan': 28, "Dragan": 34, "Ivan": 30,}

        self.assertEqual(result_team.name, new_name)
        self.assertEqual(result_team.members, new_members)
        self.assertTrue(isinstance(result_team, Team))

    def test_str(self):

        self.team_1.members = {"Ivan": 30, 'Petkan': 25, "Dragan": 34}

        result = [f"Team name: {self.team_1.name}"]
        members = list(sorted(self.team_1.members.items(), key=lambda x: (-x[1], x[0])))
        result.extend([f"Member: {x[0]} - {x[1]}-years old" for x in members])
        expected_result = "\n".join(result)

        self.assertEqual(str(self.team_1), expected_result)


if __name__ == '__main__':
    main()