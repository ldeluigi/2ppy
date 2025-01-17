import unittest
from tuprolog.core import Atom, Integer, Var
from tuprolog.core import AbstractTermVisitor


class TestVisitors(unittest.TestCase):

    def test_term_visitor(self):
        class MyVisitor(AbstractTermVisitor):
            def defaultValue(self, term):
                return 'a'
        visitor = MyVisitor()
        for term in [Atom.of('a'), Integer.of(1), Var.of("X")]:
            self.assertEqual(term.accept(visitor), 'a')
