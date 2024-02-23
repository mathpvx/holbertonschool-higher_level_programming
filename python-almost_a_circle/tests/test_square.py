#!/usr/bin.python3
"""
    Module of test of subclass Rectangle
"""

import unittest
from unittest.mock import patch
import io
import os
import sys
from pathlib import Path
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Square_attribut(unittest.TestCase):
    # tests on type attribut

    def test__sizeType(self):
        # test normal case size int
        sq1 = Square(2)
        self.assertTrue(type(sq1.size) is int)
        self.assertEqual(sq1.width, 2)
        self.assertEqual(sq1.height, 2)
        self.assertEqual(sq1.x, 0)
        self.assertEqual(sq1.y, 0)

    def test_SquareOneArg(self):
        # test id normal case of 2 square
        sq3 = Square(8)
        sq4 = Square(12)
        self.assertEqual(sq3.id, sq4.id - 1)

    def test_SquareTwoArg(self):
        # test id normal case if 2arg: size and x
        sq5 = Square(8, 2)
        sq6 = Square(12, 4)
        self.assertEqual(sq5.id, sq6.id - 1)
        self.assertEqual(sq5.x, 2)
        self.assertEqual(sq6.x, 4)

    def test_SquareThreeArg(self):
        # test id normal case if 3arg: size, x and y
        sq7 = Square(8, 2, 25)
        sq8 = Square(12, 4, 12)
        self.assertEqual(sq7.id, sq8.id - 1)
        self.assertEqual(sq7.x, 2)
        self.assertEqual(sq7.y, 25)
        self.assertEqual(sq8.x, 4)
        self.assertEqual(sq8.y, 12)

    def test_SquareForArg(self):
        # test id normal case if  4arg: size, x, y and id
        sq9 = Square(8, 2, 25, 8)
        sq10 = Square(12, 4, 16, 9)
        self.assertEqual(sq9.id, sq10.id - 1)
        self.assertEqual(sq9.x, 2)
        self.assertEqual(sq9.y, 25)
        self.assertEqual(sq9.id, 8)
        self.assertEqual(sq10.x, 4)
        self.assertEqual(sq10.y, 16)
        self.assertEqual(sq10.id, 9)

    def test_SquarePrivateSquare(self):
        # test if size private attribute
        sq11 = Square(10)


class Test_Square_attributRaise(unittest.TestCase):
    # tests on raise on attribut

    def test__sizeTypeError(self):
        # tests size not int
        with self.assertRaises(TypeError)as e:
            sq2 = Square('2')
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test__sizeValueError(self):
        # tests size negativ number
        with self.assertRaises(ValueError) as e:
            sq3 = Square(-2)
        self.assertEqual(str(e.exception), 'width must be > 0')

    def test_sizeZeroValueError(self):
        # tests size negativ number
        with self.assertRaises(ValueError) as e:
            sq3 = Square(0)
        self.assertEqual(str(e.exception), 'width must be > 0')

    def test_SquareNoArg(self):
        with self.assertRaises(TypeError):
            Square()

    def test_SquareXValueError(self):
        # tests x negativ number
        with self.assertRaises(ValueError) as e:
            sq4 = Square(2, -8)
        self.assertEqual(str(e.exception), 'x must be >= 0')

    def test_SquareXTypeError(self):
        # tests x not int
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Square(2, "8")

    def test_SquareYValueError(self):
        # tests x negativ number
        with self.assertRaises(ValueError) as e:
            sq4 = Square(2, 4, -8)
        self.assertEqual(str(e.exception), 'y must be >= 0')

    def test_SquareYTypeError(self):
        # tests y not int
        with self.assertRaises(TypeError) as e:
            rsq5 = Square(2, 8, "5")
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test_SquareFiveArgs(self):
        # if 5 Args to create square
        with self.assertRaises(TypeError):
            sq3 = Square(2, 3, 8, 2, 16)


class Test_Square_instance(unittest.TestCase):
    # Tests intantiation Square class

    def test_squareInstanceBase(self):
        # Square is an instance of clase Base
        self.assertIsInstance(Square(2), Base)

    def test_squareInstanceRectangle(self):
        # Square is an instance of clase Base
        self.assertIsInstance(Square(2), Rectangle)

    def test_squareInstanceSquare(self):
        # Square is an instance of clase Base
        self.assertIsInstance(Square(2), Square)


class Test_Square_method(unittest.TestCase):
    # tests on method

    def test_str(self):
        # normal return str method
        sq12 = Square(2, 0, 5, 8)
        self.assertEqual(Square.__str__(sq12),
                         "[Square] (8) 0/5 - 2")

    def test_toDictionaryOutput(self):
        # normal return dict
        sq13 = Square(8, 2, 1, 9)
        answer = {'size': 8, 'x': 2, 'y': 1, 'id': 9}
        self.assertDictEqual(answer, sq13.to_dictionary())

    def test_uptdateOneArg(self):
        # normal test update value of square
        sq14 = Square(1, 1, 1, 1)
        sq14.update(54)
        self.assertEqual("[Square] (54) 1/1 - 1", str(sq14))

    def test_uptdateTwoArg(self):
        # normal test update value of square
        sq14 = Square(1, 1, 1, 1)
        sq14.update(54, 12)
        self.assertEqual("[Square] (54) 1/1 - 12", str(sq14))

    def test_uptdateThreeArg(self):
        # normal test update value of square
        sq14 = Square(1, 1, 1, 1)
        sq14.update(54, 12, 24)
        self.assertEqual("[Square] (54) 24/1 - 12", str(sq14))

    def test_uptdateForArg(self):
        # normal test update value of square
        sq14 = Square(1, 1, 1, 1)
        sq14.update(54, 12, 24, 8)
        self.assertEqual("[Square] (54) 24/8 - 12", str(sq14))

    def test_uptdateOneKwargs(self):
        # normal test update value of square
        sq14 = Square(1, 1, 1, 1)
        sq14.update(**{"size": 2})
        self.assertEqual("[Square] (1) 1/1 - 2", str(sq14))

    def test_uptdateTwoKwargs(self):
        # normal test update value of square
        sq14 = Square(1, 1, 1, 1)
        sq14.update(**{"size": 2, "id": 8})
        self.assertEqual("[Square] (8) 1/1 - 2", str(sq14))

    def test_uptdateThreeKwargs(self):
        # normal test update value of square
        sq14 = Square(1, 1, 1, 1)
        sq14.update(**{"y": 54, "size": 2, "id": 8})
        self.assertEqual("[Square] (8) 1/54 - 2", str(sq14))

    def test_uptdateForKwargs(self):
        # normal test update value of square
        sq14 = Square(1, 1, 1, 1)
        sq14.update(**{"y": 54, "size": 2, "x": 8, "id": 8})
        self.assertEqual("[Square] (8) 8/54 - 2", str(sq14))


class Test_Base_method(unittest.TestCase):
    # test method class Base to create square

    def test_createSquare(self):
        sq15 = Square(15, 15, 15, 15)
        sq15_dict = sq15.to_dictionary()
        sq15 = Square.create(**sq15_dict)
        self.assertEqual("[Square] (15) 15/15 - 15", str(sq15))

    def test_createSqareNew(self):
        sq15 = Square(15, 15, 15, 15)
        sq15_dict = sq15.to_dictionary()
        sq15 = Square.create(**sq15_dict)
        self.assertEqual("[Square] (15) 15/15 - 15", str(sq15))

    def test_createSquareDiffFirst(self):
        sq15 = Square(15, 15, 15, 15)
        sq15_dict = sq15.to_dictionary()
        sq16 = Square.create(**sq15_dict)
        self.assertIsNot(sq15, sq16)

    def test_createSquareNotEqualFirst(self):
        sq15 = Square(15, 15, 15, 15)
        sq15_dict = sq15.to_dictionary()
        sq16 = Square.create(**sq15_dict)
        self.assertNotEqual(sq15, sq16)


class Test_Base_MethodeWithFile(unittest.TestCase):
    # test method class Base save to file
    # before testing, remove any create file

    @classmethod
    def tearDown(self):
        """Delete file"""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_SquareSaveToFileEmpty(self):
        # save to file if list_obj is empty
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual("[]", file.read())

    def test_SquareSaveToFileNone(self):
        # save to file if None as Arg
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual('[]', file.read())

    def test_OneSquareSaveToFile(self):
        # save 1 rect to file
        sq17 = Square(12, 6, 2, 4)
        Square.save_to_file([sq17])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 39)

    def test_TwoSquareSaveToFile(self):
        # save 2 rect to file
        sq17 = Square(12, 6, 2, 4)
        sq18 = Square(48, 16, 8, 25)
        Square.save_to_file([sq17, sq18])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 80)

    def test_NoArgSaveToFile(self):
        # save to file if empty list as Arg
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertTrue("[]", file.read())

    def test_SquareLoadFromFileNoFile(self):
        # if file doesn't exist
        answer = Square.load_from_file()
        path = Path('Square.json')
        self.assertFalse(path.is_file())

    def test_SquareLoadFromFileExistFile(self):
        # if file exist
        sq17 = Square(12, 6, 2, 4)
        sq18 = Square(48, 16, 8, 25)
        Square.save_to_file([sq17, sq18])
        answer = Square.load_from_file()
        self.assertTrue(all(type(form)) == Square for form in answer)


if __name__ == '__main__':
    unittest.main()
