from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout("A B C A A") == 180

    def test_checkout(self):
        assert checkout_solution.checkout("A B C A A Z") == -1




