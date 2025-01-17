import unittest
from tuprolog.core import atom, integer, real, var, TRUE, FALSE, FAIL, struct


class TestTermCreation(unittest.TestCase):

    def setUp(self):
        self.atom = atom('a')
        self.integer = integer(1)
        self.real = real(1.2)
        self.var = var("X")
        self.true = TRUE
        self.false = FALSE
        self.fail = FAIL
        self.struct = struct('f', self.atom, self.integer, self.real)
        self.struct2 = struct('f', [self.atom, self.integer, self.real])

    def test_simple_terms_creation(self):
        self.assertEqual(self.atom.value, 'a')
        self.assertEqual(self.integer.value.to_int(), 1)
        self.assertEqual(self.real.value.to_double(), 1.2)
        self.assertEqual(self.var.name, 'X')
        self.assertEqual(self.true.value, 'true')
        self.assertEqual(self.false.value, 'false')
        self.assertEqual(self.fail.value, 'fail')
        self.assertEqual(True, self.false.isTruth())
        self.assertEqual(True, self.true.isTruth())
        self.assertEqual(list(self.var.variables)[0], self.var)
        self.assertEqual(True, self.var.structurally_equals(var('Y')))
        self.assertEqual(True, self.false.is_truth)
        self.assertEqual(True, self.true.is_truth)

    def test_struct_creation(self):
        self.assertEqual(self.struct.functor, 'f')
        self.assertEqual(self.struct.arity, 3)
        self.assertEqual(self.struct.getArgAt(0), self.atom)
        self.assertEqual(self.struct.getArgAt(1), self.integer)
        self.assertEqual(self.struct.getArgAt(2), self.real)

        self.assertEqual(self.struct, self.struct2)
