import unittest
from datetime import datetime, timedelta
from carRental import carRental, Customer


class carRentalTest(unittest.TestCase):
    def test_car_Rental_diplays_correct_stock(self):
        shop1 = carRental()
        shop2 = carRental(10)
        self.assertEqual(shop1.displaystock(), 0)
        self.assertEqual(shop2.displaystock(), 10)

    def test_rentcarOnHourlyBasis_for_negative_number_of_cars(self):
        shop = carRental(10)
        self.assertEqual(shop.rentcarOnHourlyBasis(-1), None)

    def test_rentcarOnHourlyBasis_for_zero_number_of_cars(self):
        shop = carRental(10)
        self.assertEqual(shop.rentcarOnHourlyBasis(0), None)

    def test_rentcarOnHourlyBasis_for_valid_positive_number_of_cars(self):
        shop = carRental(10)
        hour = datetime.now().hour

    def test_rentcarOnHourlyBasis_for_invalid_positive_number_of_cars(self):
        shop = carRental(10)
        self.assertEqual(shop.rentcarOnHourlyBasis(11), None)

    def test_rentcarOnDailyBasis_for_negative_number_of_cars(self):
        shop = carRental(10)
        self.assertEqual(shop.rentcarOnDailyBasis(-1), None)

    def test_rentcarOnDailyBasis_for_zero_number_of_cars(self):
        shop = carRental(10)
        self.assertEqual(shop.rentcarOnDailyBasis(0), None)

    def test_rentcarOnDailyBasis_for_valid_positive_number_of_cars(self):
        shop = carRental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.rentcarOnDailyBasis(2).hour, hour)

    def test_rentcarOnDailyBasis_for_invalid_positive_number_of_cars(self):
        shop = carRental(10)
        self.assertEqual(shop.rentcarOnDailyBasis(11), None)

    def test_rentcarOnWeeklyBasis_for_negative_number_of_cars(self):
        shop = carRental(10)
        self.assertEqual(shop.rentcarOnWeeklyBasis(-1), None)

    def test_rentcarOnWeeklyBasis_for_zero_number_of_cars(self):
        shop = carRental(10)
        self.assertEqual(shop.rentcarOnWeeklyBasis(0), None)

    def test_rentcarOnWeeklyBasis_for_valid_positive_number_of_cars(self):
        shop = carRental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.rentcarOnWeeklyBasis(2).hour, hour)

    def test_rentcarOnWeeklyBasis_for_invalid_positive_number_of_cars(self):
        shop = carRental(10)
        self.assertEqual(shop.rentcarOnWeeklyBasis(11), None)

    def test_returncar_for_invalid_rentalTime(self):
        # create a shop and a customer
        shop = carRental(10)
        customer = Customer()  # let the customer not rent a car a try to return one.
        request = customer.returncar()
        self.assertIsNone(shop.returncar(request))  # manually check return function with error values
        self.assertIsNone(shop.returncar((0, 0, 0)))


    def test_returncar_for_invalid_rentalBasis(self):
        # create a shop and a customer
        shop = carRental(10)
        customer = Customer()
        # create valid rentalTime and cars
        customer.rentalTime = datetime.now()
        customer.cars = 3  # create invalid rentalbasis
        customer.rentalBasis = 7
        request = customer.returncar()
        self.assertEqual(shop.returncar(request), 0)

    def test_returncar_for_invalid_numOfcars(self):
        # create a shop and a customer
        shop = carRental(10)
        customer = Customer()

        # create valid rentalTime and rentalBasis
        customer.rentalTime = datetime.now()
        customer.rentalBasis = 1  # create invalid cars
        customer.cars = 0
        request = customer.returncar()
        self.assertIsNone(shop.returncar(request))


    def test_returncar_for_valid_credentials(self):
        # create a shop and a various customers
        shop = carRental(50)
        customer1 = Customer()
        customer2 = Customer()
        customer3 = Customer()
        customer4 = Customer()
        customer5 = Customer()
        customer6 = Customer()
        # create valid rentalBasis for each customer
        customer1.rentalBasis = 1  # hourly
        customer2.rentalBasis = 1  # hourly
        customer3.rentalBasis = 2  # daily
        customer4.rentalBasis = 2  # daily
        customer5.rentalBasis = 3  # weekly
        customer6.rentalBasis = 3  # weekly        # create valid cars for each customer
        customer1.cars = 1
        customer2.cars = 5  # eligible for family discount 30%
        customer3.cars = 2
        customer4.cars = 8
        customer5.cars = 15
        customer6.cars = 30  # create past valid rental times for each customer

        customer1.rentalTime = datetime.now() + timedelta(hours=-4)
        customer2.rentalTime = datetime.now() + timedelta(hours=-23)
        customer3.rentalTime = datetime.now() + timedelta(days=-4)
        customer4.rentalTime = datetime.now() + timedelta(days=-13)
        customer5.rentalTime = datetime.now() + timedelta(weeks=-6)
        customer6.rentalTime = datetime.now() + timedelta(weeks=-12)  # make all customers return their cars
        request1 = customer1.returncar()
        request2 = customer2.returncar()
        request3 = customer3.returncar()
        request4 = customer4.returncar()
        request5 = customer5.returncar()
        request6 = customer6.returncar()  # check if all of them get correct bill
        self.assertEqual(shop.returncar(request1), 20)
        self.assertEqual(shop.returncar(request2), 402.5)
        self.assertEqual(shop.returncar(request3), 160)
        self.assertEqual(shop.returncar(request4), 2080)
        self.assertEqual(shop.returncar(request5), 5400)
        self.assertEqual(shop.returncar(request6), 21600)


class CustomerTest(unittest.TestCase):

    def test_return_car_with_valid_input(self):
        # create a customer
        customer = Customer()

        # create valid rentalTime, rentalBasis, cars
        now = datetime.now()
        customer.rentalTime = now
        customer.rentalBasis = 1
        customer.cars = 4
        self.assertEqual(customer.returncar(), (now, 1, 4))

    def test_return_car_with_invalid_input(self):
        # create a customer
        customer = Customer()

        # create valid rentalBasis and cars

        customer.rentalBasis = 1
        customer.cars = 0  # create invalid rentalTime
        customer.rentalTime = 0
        self.assertEqual(customer.returncar(), (0, 0, 0))
        if __name__ == '__main__':

    unittest.main()