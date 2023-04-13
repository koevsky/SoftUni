from project.plantation import Plantation
from unittest import TestCase, main


class PlantationTests(TestCase):

    def setUp(self) -> None:

        self.plantation = Plantation(10)

    def test_correct_init(self):

        self.assertEqual(self.plantation.size, 10)
        self.assertEqual(self.plantation.plants, {})
        self.assertEqual(self.plantation.workers, [])

    def test_incorrect_size_input_raise_VE(self):

        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -1

        self.assertEqual(str(ve.exception), "Size must be positive number!")

    def test_hire_worker_already_hired_raise_VE(self):
        self.plantation.workers = ["Ivan", "Petkan"]

        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker('Ivan')

        self.assertEqual(str(ve.exception), "Worker already hired!")

    def test_hire_worker_successfully(self):
        self.plantation.workers = ["Ivan", "Petkan"]

        result = self.plantation.hire_worker("Dragan")
        expected_res = f"Dragan successfully hired."

        self.assertEqual(result, expected_res)
        self.assertEqual(self.plantation.workers, ["Ivan", "Petkan", "Dragan"])

    def test_len_method(self):
        self.plantation.plants = {"a": [1, 2], "b": [3, 4, 5]}
        expected_res = 5
        result = len(self.plantation)

        self.assertEqual(result, expected_res)

    def test_planting_invalid_worker_raise_VA(self):

        self.plantation.workers = ["Ivan", "Petkan"]
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Dragan", "c")

        self.assertEqual(str(ve.exception), "Worker with name Dragan is not hired!")

    def test_full_plantation_raise_VE(self):
        self.plantation.workers = ["Ivan", "Petkan"]
        self.plantation.size = 5
        self.plantation.plants = {"Ivan": ["a", "b", "c"], 'Petkan': ["d", "e"]}

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Ivan", "f")

        self.assertEqual(str(ve.exception), "The plantation is full!")

    def test_worker_in_plants_keys(self):
        self.plantation.workers = ["Ivan", "Petkan"]
        self.plantation.plants = {"Ivan": ["a", "b", "c"], 'Petkan': ["d", "e"]}
        result = self.plantation.planting("Ivan", "m")
        expected_result = f"Ivan planted m."
        expected_dict = {"Ivan": ["a", "b", "c", "m"], 'Petkan': ["d", "e"]}

        self.assertEqual(result, expected_result)
        self.assertEqual(self.plantation.plants, expected_dict)
        self.assertEqual(self.plantation.plants["Ivan"], ["a", "b", "c", "m"])

    def test_worker_first_time_plant(self):
        self.plantation.workers = ["Ivan", "Petkan", "Dragan"]
        self.plantation.plants = {"Ivan": ["a", "b", "c"], 'Petkan': ["d", "e"]}
        result = self.plantation.planting("Dragan", "m")
        expected_result = "Dragan planted it's first m."
        expected_dict = {"Ivan": ["a", "b", "c"], 'Petkan': ["d", "e"], "Dragan": ["m"]}
        expected_lst = ["m"]

        self.assertEqual(result, expected_result)
        self.assertEqual(self.plantation.plants, expected_dict)
        self.assertEqual(self.plantation.plants["Dragan"], expected_lst)

    def test_str_return(self):
        self.plantation.workers = ["Ivan", "Petkan", "Dragan"]
        self.plantation.plants = {"Ivan": ["a", "b", "c"], 'Petkan': ["d", "e"]}

        expected_res = [f"Plantation size: {self.plantation.size}"]
        expected_res.append(f'{", ".join(self.plantation.workers)}')
        for worker, plants in self.plantation.plants.items():
            expected_res.append(f"{worker} planted: {', '.join(plants)}")

        final_res = "\n".join(expected_res)

        self.assertEqual(str(self.plantation), final_res)

    def test_repr_return(self):
        self.plantation.workers = ["Ivan", "Petkan", "Dragan"]
        self.plantation.plants = {"Ivan": ["a", "b", "c"], 'Petkan': ["d", "e"]}

        result = ''
        result += f'Size: {self.plantation.size}\n'
        result += f'Workers: {", ".join(self.plantation.workers)}'

        self.assertEqual(repr(self.plantation), result)



if __name__ == '__main__':
    main()
