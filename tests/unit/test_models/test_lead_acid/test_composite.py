#
# Tests for the lead-acid composite model
#
import pybamm
import unittest


class TestLeadAcidComposite(unittest.TestCase):
    def test_well_posed(self):
        model = pybamm.lead_acid.Composite()
        model.check_well_posedness()

    def test_well_posed_average_first_order(self):
        model = pybamm.lead_acid.Composite({"first-order potential": "average"})
        model.check_well_posedness()

    def test_well_posed_with_convection(self):
        model = pybamm.lead_acid.Composite({"convection": True})
        model.check_well_posedness()


class TestLeadAcidCompositeCapacitance(unittest.TestCase):
    def test_well_posed_differential(self):
        options = {"capacitance": "differential"}
        model = pybamm.lead_acid.Composite(options)
        model.check_well_posedness()

    def test_well_posed_algebraic(self):
        options = {"capacitance": "algebraic"}
        model = pybamm.lead_acid.Composite(options)
        model.check_well_posedness()

    def test_default_solver(self):
        options = {"capacitance": "differential"}
        model = pybamm.lead_acid.Composite(options)
        self.assertIsInstance(model.default_solver, pybamm.ScikitsOdeSolver)
        options = {"capacitance": "algebraic"}
        model = pybamm.lead_acid.Composite(options)
        self.assertIsInstance(model.default_solver, pybamm.ScikitsDaeSolver)


if __name__ == "__main__":
    print("Add -v for more debug output")
    import sys

    if "-v" in sys.argv:
        debug = True
    unittest.main()
