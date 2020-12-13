import unittest

from src.secret_santa import SecretSanta, SecretSantaResults


class SecretSantaTests(unittest.TestCase):
    def test_john_jack_jill(self):
        names = ["John", "Jack", "Jill"]
        results: SecretSantaResults = SecretSanta(names).draw_gifters_and_recipients()
        print(results)

        # Verify everybody was assigned a recipient
        self.assertTrue("John" in results.gifters(), "John should give a gift")
        self.assertTrue("Jack" in results.gifters(), "Jack should give a gift")
        self.assertTrue("Jill" in results.gifters(), "Jill should give a gift")

        # Verify everybody will receive a gift
        self.assertTrue("John" in results.recipients(), "John should be a recipient")
        self.assertTrue("Jack" in results.recipients(), "Jack should be a recipient")
        self.assertTrue("Jill" in results.recipients(), "Jill should be a recipient")

        # Verify nobody gives a gift to themself
        self.assertFalse(
            "John" == results.get_recipient_of_gifter("John"),
            "John should not have to give a gift to themself",
        )
        self.assertFalse(
            "Jack" == results.get_recipient_of_gifter("Jack"),
            "Jack should not have to give a gift to themself",
        )
        self.assertFalse(
            "Jill" == results.get_recipient_of_gifter("Jill"),
            "Jill should not have to give a gift to themself",
        )

    def test_long_list_1(self):
        names = ["John", "Jack", "Jill", "Adam", "Bruce", "Kaitlin", "Hannah"]
        results: SecretSantaResults = SecretSanta(names).draw_gifters_and_recipients()
        print(results)

        for name in names:
            # Verify everybody was assigned a recipient
            self.assertTrue(
                name in results.gifters(), "{} should give a gift".format(name)
            )

            # Verify everybody will receive a gift
            self.assertTrue(
                name in results.recipients(), "{} should be a recipient".format(name)
            )

            # Verify nobody gives a gift to themself
            self.assertFalse(
                name == results.get_recipient_of_gifter(name),
                "{} should not have to give a gift to themself".format(name),
            )

    def test_long_list_multiple_draws(self):
        names = [
            "John",
            "Jack",
            "Jill",
            "Adam",
            "Bruce",
            "Kaitlin",
            "Hannah",
            "Mac",
            "Charlie",
            "Dennis",
        ]
        self.verify_with_multiple_iterations(names)

    def test_group_of_3_multiple_draws(self):
        names = ["John", "Jack", "Jill"]
        self.verify_with_multiple_iterations(names)

    def verify_with_multiple_iterations(self, names):
        for i in range(0, 25000):
            results: SecretSantaResults = SecretSanta(
                names
            ).draw_gifters_and_recipients()
            for name in names:
                # Verify everybody was assigned a recipient
                self.assertTrue(
                    name in results.gifters(),
                    "{} should give a gift, iteration [{}]".format(name, i),
                )

                # Verify everybody will receive a gift
                self.assertTrue(
                    name in results.recipients(),
                    "{} should be a recipient, iteration [{}]".format(name, i),
                )

                # Verify nobody gives a gift to themself
                self.assertFalse(
                    name == results.get_recipient_of_gifter(name),
                    "{} should not have to give a gift to themself, iteration [{}]".format(
                        name, i
                    ),
                )


if __name__ == "__main__":
    unittest.main()
