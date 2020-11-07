from calc import *
import unittest


class TestCalcArg(unittest.TestCase):
    def test_from_query_rank(self):
        arg = CalcArg.from_query("p8")
        self.assertEqual(arg.rank, 8)
        self.assertEqual(arg.batch, None)
        self.assertEqual(arg.fps, None)
        self.assertEqual(arg.step_time, None)
        self.assertEqual(arg.none_num(), 3)

    def test_from_query_rank1(self):
        arg = CalcArg.from_query("R8")
        self.assertEqual(arg.rank, 8)
        self.assertEqual(arg.batch, None)
        self.assertEqual(arg.fps, None)
        self.assertEqual(arg.step_time, None)
        self.assertEqual(arg.none_num(), 3)

    def test_from_query_batch(self):
        arg = CalcArg.from_query("b1.6w")
        self.assertEqual(arg.rank, None)
        self.assertEqual(arg.batch, 16000)
        self.assertEqual(arg.fps, None)
        self.assertEqual(arg.step_time, None)
        self.assertEqual(arg.none_num(), 3)

    def test_from_query_fps(self):
        arg = CalcArg.from_query("f280w")
        self.assertEqual(arg.rank, None)
        self.assertEqual(arg.batch, None)
        self.assertEqual(arg.fps, 2800000)
        self.assertEqual(arg.step_time, None)
        self.assertEqual(arg.none_num(), 3)

    def test_from_query_t1(self):
        arg = CalcArg.from_query("t28.5ms")
        self.assertEqual(arg.rank, None)
        self.assertEqual(arg.batch, None)
        self.assertEqual(arg.fps, None)
        self.assertAlmostEqual(arg.step_time, 28.5)
        self.assertEqual(arg.none_num(), 3)

    def test_from_query_t2(self):
        arg = CalcArg.from_query("t28.5s")
        self.assertEqual(arg.rank, None)
        self.assertEqual(arg.batch, None)
        self.assertEqual(arg.fps, None)
        self.assertAlmostEqual(arg.step_time, 28500.0)
        self.assertEqual(arg.none_num(), 3)

    def test_from_query_t3(self):
        arg = CalcArg.from_query("t28.5")
        self.assertEqual(arg.rank, None)
        self.assertEqual(arg.batch, None)
        self.assertEqual(arg.fps, None)
        self.assertAlmostEqual(arg.step_time, 28.5)
        self.assertEqual(arg.none_num(), 3)

    def test_from_query_for_time(self):
        arg = CalcArg.from_query("p8 f280w b1.6w")
        self.assertEqual(arg.rank, 8)
        self.assertEqual(arg.batch, 16000)
        self.assertEqual(arg.fps, 2800000)
        self.assertEqual(arg.step_time, None)
        self.assertEqual(arg.none_num(), 1)