"""Rastet e testimit te kerkuara shprehimisht ne Problemin 5."""

import json
from pathlib import Path
import unittest

from main import EmployeeData, calculateTeamSalary


class TeamSalaryTests(unittest.TestCase):
    def setUp(self) -> None:
        data_path = Path(__file__).with_name("employees.json")

        with data_path.open(encoding="utf-8") as source:
            data: EmployeeData = json.load(source)

        self.employees = data["employees"]

    def test_ceo_includes_entire_organization(self) -> None:
        self.assertEqual(calculateTeamSalary(self.employees, 1), 1490000)

    def test_middle_manager_includes_all_descendants(self) -> None:
        self.assertEqual(calculateTeamSalary(self.employees, 4), 505000)

    def test_leaf_employee_includes_own_salary(self) -> None:
        self.assertEqual(calculateTeamSalary(self.employees, 12), 50000)

    def test_nonexistent_employee_returns_zero(self) -> None:
        self.assertEqual(calculateTeamSalary(self.employees, 999), 0)


if __name__ == "__main__":
    unittest.main()
