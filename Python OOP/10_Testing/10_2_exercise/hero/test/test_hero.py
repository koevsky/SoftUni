from unittest import TestCase, main
from project.hero import Hero


class HeroTest(TestCase):

    def setUp(self) -> None:
        self.hero = Hero("TestName", 2, 100, 50)
        self.enemy_hero = Hero("Test", 2, 100, 50)

    def test_correct_init(self):
        self.assertEqual(self.hero.username, "TestName")
        self.assertEqual(self.hero.level, 2)
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.damage, 50)

    def test_player_hero_name_equals_enemy_player_hero_name_raise_exception(self):

        self.enemy_hero.username = "TestName"

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)

        self.assertEqual(str(ex.exception), "You cannot fight yourself")

    def test_player_hero_health_less_or_equal_to_zero_value_error(self):

        self.hero.health = 0
        expected = "Your health is lower than or equal to 0. You need to rest"

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)

        self.assertEqual(str(ve.exception), expected)

    def test_enemy_player_hero_health_less_or_equal_to_zero_value_error(self):

        self.enemy_hero.health = 0
        expected = "You cannot fight Test. He needs to rest"

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)

        self.assertEqual(str(ve.exception), expected)

    def test_players_damage(self):

        player_damage = self.hero.damage * self.hero.level
        enemy_damage = self.enemy_hero.damage * self.enemy_hero.level

        self.assertEqual(player_damage, 100)
        self.assertEqual(enemy_damage, 100)

    def test_draw_condition(self):

        self.hero.battle(self.enemy_hero)
        self.assertEqual(self.hero.health, 0)
        self.assertEqual(self.enemy_hero.health, 0)

    def test_win_condition(self):
        self.enemy_hero.level = 1

        current_message = self.hero.battle(self.enemy_hero)
        expected_message = "You win"

        self.assertEqual(self.enemy_hero.health, 0)
        self.assertEqual(self.hero.level, 3)
        self.assertEqual(self.hero.health, 55)
        self.assertEqual(self.hero.damage, 55)
        self.assertEqual(current_message, expected_message)

    def test_lose_condition(self):
        self.hero.level = 1

        current_message = self.hero.battle(self.enemy_hero)
        expected_message = "You lose"

        self.assertEqual(self.hero.health, 0)
        self.assertEqual(self.enemy_hero.level, 3)
        self.assertEqual(self.enemy_hero.health, 55)
        self.assertEqual(self.enemy_hero.damage, 55)
        self.assertEqual(current_message, expected_message)

    def test_return_string_of_instance(self):
        expected = f"Hero TestName: 2 lvl\n" \
                    f"Health: 100\n" \
                    f"Damage: 50\n"

        self.assertEqual(str(self.hero), expected)


if __name__ == '__main__':
    main()