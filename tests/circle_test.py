import unittest  # Импортирование модуля для юнит-тестирования
import circle  # Импортирование модуля с функциями для вычисления площади и периметра круга

class CircleTestCase(unittest.TestCase):  # Определение класса тестов для кругов, наследующего от TestCase

    def test_circle_area_yes(self):  # Тестирование корректности вычисления площади круга
        rst = circle.area(3)  # Вычисление площади круга радиусом 3
        self.assertEqual(rst, 28.274333882308138)  # Проверка, соответствует ли результат ожидаемому значению

    def test_circle_neg_area(self):  # Тестирование обработки отрицательного радиуса
        res = circle.area(-5)  # Вычисление площади для отрицательного радиуса
        self.assertEqual(res, "area cannot be negative")  # Проверка ожидаемого значения (некорректное поведение)

    def test_circle_area_float_numb(self):  # Тестирование вычисления площади для вещественного числа
        res = circle.area(3.35)  # Вычисление площади с радиусом 3.35
        self.assertEqual(res, 35.25652355491146)  # Проверка соответствия результата

    def test_circle_zero_area(self):  # Тестирование обработки радиуса 0
        res = circle.area(0)  # Вычисление площади для радиуса 0
        self.assertEqual(res, 0)  # Проверка, что площадь равна 0

    def test_circle_perimeter_yes(self):  # Тестирование корректности вычисления периметра круга
        res = circle.perimeter(5)  # Вычисление периметра круга радиусом 5
        self.assertEqual(res, 31.41592653589793)  # Проверка результата

    def test_circle_perimeter_no(self):  # Тестирование обработки отрицательного радиуса для периметра
        res = circle.perimeter(-3)  # Вычисление периметра для отрицательного радиуса
        self.assertEqual(res, "perimeter cannot be negative")  # Проверка на отрицательное значение (некорректное поведение)

    def test_circle_perimeter_float_num(self):  # Тестирование периметра для вещественного числа
        res = circle.perimeter(3.35)  # Вычисление периметра с радиусом 3.35
        self.assertEqual(res, 21.048670779051616)  # Проверка результата

    def test_circle_perimeter_zero(self):  # Тестирование обработки радиуса 0 для периметра
        res = circle.perimeter(0)  # Вычисление периметра для радиуса 0
        self.assertEqual(res, 0)  # Проверка, что периметр равен 0

if __name__ == "__main__":  # Проверка, что скрипт запущен напрямую
    unittest.main()  # Запуск всех тестов
circ_tests = CircleTestCase  # Создание экземпляра тестов (необязательно, так как тесты уже запускаются выше)