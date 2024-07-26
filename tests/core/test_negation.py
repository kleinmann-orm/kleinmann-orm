import unittest

from kleinmann_core import Tables
from kleinmann_core import functions as fn
from kleinmann_core.terms import ValueWrapper


class NegationTests(unittest.TestCase):
    table_abc, table_efg = Tables("abc", "efg")

    def test_negate_wrapped_float(self):
        q = -ValueWrapper(1.0)

        self.assertEqual("-1.0", q.get_sql())

    def test_negate_wrapped_int(self):
        q = -ValueWrapper(1)

        self.assertEqual("-1", q.get_sql())

    def test_negate_field(self):
        q = -self.table_abc.foo

        self.assertEqual('-"abc"."foo"', q.get_sql(with_namespace=True, quote_char='"'))

    def test_negate_function(self):
        q = -fn.Sum(self.table_abc.foo)

        self.assertEqual('-SUM("abc"."foo")', q.get_sql(with_namespace=True, quote_char='"'))
