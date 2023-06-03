from solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_sum_max(self):
        assert sum_solution.compute(100, 100) == 200

    def test_sum_min(self):
        assert sum_solution.compute(0, 0) == 0

