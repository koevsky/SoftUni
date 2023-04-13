from unittest import TestCase, main


class WorkerTests(TestCase):

    def setUp(self) -> None:
        self.worker = Worker("TestGuy", 1000, 100)

    def test_correct_init(self):
        self.assertEqual("TestGuy", self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_worker_energy_equal_or_less_than_zero_exception_raise(self):

        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker_money_increase_with_one_salary_after_work(self):

        self.worker.work()
        self.assertEqual(1000, self.worker.money)

    def test_worker_energy_decrease_after_work(self):
        self.worker.work()
        self.assertEqual(99, self.worker.energy)

    def test_energy_increase_after_rest(self):

        self.worker.rest()
        self.assertEqual(101, self.worker.energy)

    def test_get_worker_info(self):
        self.assertEqual('TestGuy has saved 0 money.', self.worker.get_info())


if __name__ == '__main__':
    main()