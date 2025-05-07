import unittest
import importlib

class TestAssignmentSix(unittest.TestCase):
    def test_01(self):
        self.assertEqual(answers.answer_01(1), 1)
        self.assertEqual(answers.answer_01(2), 2)
        self.assertEqual(answers.answer_01(3), 2)
        self.assertEqual(answers.answer_01(4), 3)
        self.assertEqual(answers.answer_01(5), 2)
        self.assertEqual(answers.answer_01(6), 4)
        self.assertEqual(answers.answer_01(7), 2)
    def test_02(self):
        self.assertFalse(answers.answer_02(1))
        self.assertFalse(answers.answer_02(4))
        self.assertFalse(answers.answer_02(6))
        self.assertFalse(answers.answer_02(8))
        self.assertFalse(answers.answer_02(9))
        self.assertTrue(answers.answer_02(2))
        self.assertTrue(answers.answer_02(3))
        self.assertTrue(answers.answer_02(5))
        self.assertTrue(answers.answer_02(7))
    def test_03(self):
        self.assertEqual(answers.answer_03([1, 2, 3, 4, 5]), [False, True, True, False, True])
        self.assertEqual(answers.answer_03([6, 7, 8, 9, 10]), [False, True, False, False, False])
        self.assertEqual(answers.answer_03([11, 12]), [True, False])
        self.assertEqual(answers.answer_03([13, 14]), [True, False])
        self.assertEqual(answers.answer_03([15, 16, 17]), [False, False, True])
    def test_04(self):
        self.assertEqual(answers.answer_04(1, 5), [1, 2, 'Fizz', 4, 'Buzz'])
        self.assertEqual(answers.answer_04(11, 15), [11, 'Fizz', 13, 14, 'Fizz Buzz'])
        self.assertEqual(answers.answer_04(25, 30), ['Buzz', 26, 'Fizz', 28, 29, 'Fizz Buzz'])
        self.assertEqual(answers.answer_04(31, 33), [31, 32, 'Fizz'])
        self.assertEqual(answers.answer_04(34, 35), [34, 'Buzz'])
    def test_05(self):
        self.assertEqual(answers.answer_05(99, 100), {'1': 1})
        self.assertEqual(answers.answer_05(99, 200), {'100': 1, '1': 1})
        self.assertEqual(answers.answer_05(99, 500), {'200': 2, '1': 1})
        self.assertEqual(answers.answer_05(99, 1000), {'500': 1, '200': 2, '1': 1})
        self.assertEqual(answers.answer_05(49, 50), {'1': 1})
        self.assertEqual(answers.answer_05(49, 100), {'50': 1, '1': 1})
        self.assertEqual(answers.answer_05(49, 200), {'100': 1, '50': 1, '1': 1})
        self.assertEqual(answers.answer_05(49, 500), {'200': 2, '50': 1, '1': 1})
        self.assertEqual(answers.answer_05(49, 1000), {'500': 1, '200': 2, '50': 1, '1': 1})
        self.assertEqual(answers.answer_05(119, 150), {'10': 3, '1': 1})
        self.assertEqual(answers.answer_05(119, 200), {'50': 1, '10': 3, '1': 1})
        self.assertEqual(answers.answer_05(119, 500), {'200': 1, '100': 1, '50': 1, '10': 3, '1': 1})
        self.assertEqual(answers.answer_05(119, 1000), {'500': 1, '200': 1, '100': 1, '50': 1, '10': 3, '1': 1})

chapter_name = "使用流程控制管理程式區塊的執行：迴圈"
answers = importlib.import_module("answers")
suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignmentSix)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print(f"您在「{chapter_name}」章節的 {number_of_test_runs} 道練習題中答對了 {number_of_successes} 題。")