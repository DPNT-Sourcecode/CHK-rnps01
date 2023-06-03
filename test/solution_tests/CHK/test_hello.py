from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout_sum(self):
        assert checkout_solution.checkout("A B C A A") == 180

    def test_checkout_sum_2(self):
        assert checkout_solution.checkout("A A A A B B B B B") == 300

    def test_checkout_invalid(self):
        assert checkout_solution.checkout("A B C A A Z") == -1






