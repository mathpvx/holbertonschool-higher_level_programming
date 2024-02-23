#!/usr/bin.python3
"""
    Module of test of subclass Rectangle
"""

import unittest
from pathlib import Path
import os
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class Test_Rectangle_attribut(unittest.TestCase):
    # tests on type attribut

    def test__widthType(self):
        # test type width int
        rect1 = Rectangle(2, 8, 1, 2)
        self.assertTrue(type(rect1.width) is int)

    def test__heightType(self):
        # test type height int
        rect1 = Rectangle(2, 8, 1, 2)
        self.assertTrue(type(rect1.height) is int)

    def test__xType(self):
        # test type x int
        rect1 = Rectangle(2, 8, 1, 2)
        self.assertTrue(type(rect1.x) is int)

    def test__yType(self):
        # test type y int
        rect1 = Rectangle(2, 8, 1, 2)
        self.assertTrue(type(rect1.y) is int)


class Test_Rectangle_attributRaise(unittest.TestCase):
    # tests on raise on attribut

    def test__widthTypeError(self):
        # tests width not int
        with self.assertRaises(TypeError)as e:
            rect2 = Rectangle('2', 8, 1, 2)
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test__widthValueError(self):
        # tests width negativ number
        with self.assertRaises(ValueError) as e:
            rect3 = Rectangle(-2, 8, 0, 0)
        self.assertEqual(str(e.exception), 'width must be > 0')

    def test__widthValueError(self):
        # tests width = 0
        with self.assertRaises(ValueError) as e:
            rect3 = Rectangle(0, 8, 0, 0)
        self.assertEqual(str(e.exception), 'width must be > 0')

    def test__heightTypeError(self):
        # tests height not int
        with self.assertRaises(TypeError) as e:
            rect4 = Rectangle(2, '8', 0, 0)
        self.assertEqual(str(e.exception), 'height must be an integer')

    def test__heightValueError(self):
        # tests height negativ number
        with self.assertRaises(ValueError) as e:
            rect4 = Rectangle(2, -8, 0, 0)
        self.assertEqual(str(e.exception), 'height must be > 0')

    def test__heightValueError(self):
        # tests height = 0
        with self.assertRaises(ValueError) as e:
            rect4 = Rectangle(2, 0, 0, 0)
        self.assertEqual(str(e.exception), 'height must be > 0')

    def test__xTypeError(self):
        # tests x not int
        with self.assertRaises(TypeError) as e:
            rect5 = Rectangle(2, 8, "8", 0)
        self.assertEqual(str(e.exception), 'x must be an integer')

    def test__yTypeError(self):
        # tests y not int
        with self.assertRaises(TypeError) as e:
            rect6 = Rectangle(2, 8, 0, "5")
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test__xValueError(self):
        # tests x negativ number
        with self.assertRaises(ValueError) as e:
            rect7 = Rectangle(2, 8, -2, 0)
        self.assertEqual(str(e.exception), 'x must be >= 0')

    def test__yValueError(self):
        # tests y negativ number
        with self.assertRaises(ValueError) as e:
            rect8 = Rectangle(2, 8, 2, -10)
        self.assertEqual(str(e.exception), 'y must be >= 0')


class Test_Rectangle_method(unittest.TestCase):
    # tests on method

    @staticmethod
    def captureOutput(rect, method):
        """
            Capture and return text printed in stdout
            for method print and display
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return (capture)

    def test_area(self):
        # normal calcul of area
        rect9 = Rectangle(2, 3)
        self.assertEqual(Rectangle.area(rect9), 6)

    def test_str(self):
        # normal return str method
        rect10 = Rectangle(2, 3, 0, 5, 8)
        self.assertEqual(Rectangle.__str__(rect10),
                         "[Rectangle] (8) 0/5 - 2/3")

    def test_RectangleDisplayWithoutXY(self):
        # normal return display method without x, y
        rect11 = Rectangle(1, 2)
        capture = Test_Rectangle_method.captureOutput(rect11, "display")
        self.assertEqual("#\n#\n", capture.getvalue())
        self.assertEqual(rect11.x, 0)
        self.assertEqual(rect11.y, 0)

    def test_RectangleDisplayZeroXY(self):
        # normal return display method without x and y
        rect = Rectangle(3, 2, 0, 0)
        capture = Test_Rectangle_method.captureOutput(rect, "display")
        self.assertEqual('###\n###\n', capture.getvalue())

    def test_RectangleDisplayXonly(self):
        # normal return display method with only x
        rect11 = Rectangle(1, 2, 4)
        capture = Test_Rectangle_method.captureOutput(rect11, "display")
        self.assertEqual("    #\n    #\n", capture.getvalue())

    def test_RectangleDisplayYonly(self):
        # normal return display method with only y
        rect11 = Rectangle(1, 2, 0, 1)
        capture = Test_Rectangle_method.captureOutput(rect11, "display")
        self.assertEqual("\n#\n#\n", capture.getvalue())

    def test_RectangleDisplayOneArg(self):
        # return display if one Arg
        rect11 = Rectangle(1, 2, 0, 1)
        with self.assertRaises(TypeError):
            rect11.display(12)

    def test_toDictionaryOutput(self):
        # normal return dict
        rect12 = Rectangle(8, 2, 1, 9, 5)
        answer = {'width': 8, 'height': 2, 'x': 1, 'y': 9, 'id': 5}
        self.assertDictEqual(answer, rect12.to_dictionary())

    def test_uptdateOneArg(self):
        # normal test update value of rectangle
        rect13 = Rectangle(1, 1, 1, 1, 1)
        rect13.update(54)
        self.assertEqual("[Rectangle] (54) 1/1 - 1/1", str(rect13))

    def test_uptdateTwoArg(self):
        # normal test update value of rectangle
        rect13 = Rectangle(1, 1, 1, 1, 1)
        rect13.update(54, 12)
        self.assertEqual("[Rectangle] (54) 1/1 - 12/1", str(rect13))

    def test_uptdateThreeArg(self):
        # normal test update value of rectangle
        rect13 = Rectangle(1, 1, 1, 1, 1)
        rect13.update(54, 12, 24)
        self.assertEqual("[Rectangle] (54) 1/1 - 12/24", str(rect13))

    def test_uptdateForArg(self):
        # normal test update value of rectangle
        rect13 = Rectangle(1, 1, 1, 1, 1)
        rect13.update(54, 12, 24, 8)
        self.assertEqual("[Rectangle] (54) 8/1 - 12/24", str(rect13))

    def test_uptdateFiveArg(self):
        # normal test update value of rectangle
        rect13 = Rectangle(1, 1, 1, 1, 1)
        rect13.update(54, 12, 24, 8, 5)
        self.assertEqual("[Rectangle] (54) 8/5 - 12/24", str(rect13))

    def test_uptdateOneKwargs(self):
        # normal test update value of rectangle
        rect13 = Rectangle(1, 1, 1, 1, 1)
        rect13.update(**{"width": 2})
        self.assertEqual("[Rectangle] (1) 1/1 - 2/1", str(rect13))

    def test_uptdateTwoKwargs(self):
        # normal test update value of rectangle
        rect13 = Rectangle(1, 1, 1, 1, 1)
        rect13.update(**{'width': 2, 'height': 24})
        self.assertEqual("[Rectangle] (1) 1/1 - 2/24", str(rect13))

    def test_uptdateThreeKwargs(self):
        # normal test update value of rectangle
        rect13 = Rectangle(1, 1, 1, 1, 1)
        rect13.update(**{'width': 2, 'height': 24, 'id': 48})
        self.assertEqual("[Rectangle] (48) 1/1 - 2/24", str(rect13))

    def test_uptdateForKwargs(self):
        # normal test update value of rectangle
        rect13 = Rectangle(1, 1, 1, 1, 1)
        rect13.update(**{'width': 2, 'x': 16, 'height': 24, 'id': 48})
        self.assertEqual("[Rectangle] (48) 16/1 - 2/24", str(rect13))

    def test_uptdateFiveKwargs(self):
        # normal test update value of rectangle
        rect13 = Rectangle(1, 1, 1, 1, 1)
        rect13.update(**{'y': 2, 'width': 2, 'x': 16, 'height': 24, 'id': 48})
        self.assertEqual("[Rectangle] (48) 16/2 - 2/24", str(rect13))


class Test_Base_Create(unittest.TestCase):
    # test method class Base to create

    def test_createRectangle(self):
        rect14 = Rectangle(14, 14, 14, 14, 14)
        rect14_dict = rect14.to_dictionary()
        rect15 = Rectangle.create(**rect14_dict)
        self.assertEqual("[Rectangle] (14) 14/14 - 14/14", str(rect14))

    def test_createRectangleNew(self):
        rect14 = Rectangle(14, 14, 14, 14, 14)
        rect14_dict = rect14.to_dictionary()
        rect15 = Rectangle.create(**rect14_dict)
        self.assertEqual("[Rectangle] (14) 14/14 - 14/14", str(rect15))

    def test_createRectangleDiffFirst(self):
        rect14 = Rectangle(14, 14, 14, 14, 14)
        rect14_dict = rect14.to_dictionary()
        rect15 = Rectangle.create(**rect14_dict)
        self.assertIsNot(rect15, rect14)

    def test_createRectangleNotEqualFirst(self):
        rect14 = Rectangle(14, 14, 14, 14, 14)
        rect14_dict = rect14.to_dictionary()
        rect15 = Rectangle.create(**rect14_dict)
        self.assertNotEqual(rect15, rect14)


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

    def test_RectangleSaveToFileNone(self):
        # save to file if no list_obj
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertTrue("[]", file.read())

    def test_RectangleSaveToFile_none(self):
        # test2 save to file if no list_obj
        self.assertEqual(Rectangle.save_to_file(None), None)

    def test_RectangleSaveToFileEmpty(self):
        # save to file if empty list_obj
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertTrue("[]", file.read())

    def test_RectangleSaveToFile_empty(self):
        # test2 save to file if empty list_obj
        self.assertEqual(Rectangle.save_to_file([]), None)

    def test_OneRectangleSaveToFile(self):
        # save 1 rect to file
        rect16 = Rectangle(12, 6, 2, 4, 8)
        Rectangle.save_to_file([rect16])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 53)

    def test_TwoRectangleSaveToFile(self):
        # save 2 rect to file
        rect16 = Rectangle(12, 6, 2, 4, 8)
        rect17 = Rectangle(24, 48, 16, 8, 25)
        Rectangle.save_to_file([rect16, rect17])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 109)

    def test_NoArgSaveToFile(self):
        # if no args
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_RectangleLoadFromFileNoFile(self):
        # if file doesn't exist
        answer = Rectangle.load_from_file()
        path = Path('Rectangle.json')
        self.assertFalse(path.is_file())

    def test_RectangleLoadFromFileExistFile(self):
        # if file exist
        rect18 = Rectangle(12, 6, 2, 4, 54)
        rect19 = Rectangle(48, 16, 8, 25, 78)
        Rectangle.save_to_file([rect18, rect19])
        answer = Rectangle.load_from_file()
        self.assertTrue(all(type(form)) == Rectangle for form in answer)


if __name__ == '__main__':
    unittest.main()
