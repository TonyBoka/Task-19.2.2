import pytest

from api.calculator import Calculator

class TestCalc:
   def setup(self):
       self.calc = Calculator

   def test_adding_success(self):
       assert self.calc.adding(self, 6, 3) == 9         #сложение

   def test_subtraction_success(self):
       assert self.calc.subtraction(self, 6, 3) == 3     #вычитание

   def test_division_success(self):
        assert self.calc.division(self, 6, 3) == 2.0     #деление

   def test_multiply_success(self):
        assert self.calc.multiply(self, 6, 3) == 18      #умножение

   def teardown(self):
       print ('Задание выполнено.')