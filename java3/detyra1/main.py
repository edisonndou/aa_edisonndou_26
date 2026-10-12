"""Organizational Hierarchy Analysis - te pese problemet me rekursion."""

import json
from pathlib import Path
from typing import TypedDict


class Employee(TypedDict):
    id: int
    name: str
    position: str
    salary: int | float
    supervisor_id: int | None


class EmployeeData(TypedDict):
    employees: list[Employee]


class Subordinate(TypedDict):
    id: int
    name: str
    relative_depth: int


class CommonManager(TypedDict):
    manager_id: int
    manager_name: str
    distance_to_emp1: int
    distance_to_emp2: int


def _index_by_id(employees: list[Employee]) -> dict[int, Employee]:
    return {employee["id"]: employee for employee in employees}


def _index_children(employees: list[Employee]) -> dict[int, list[Employee]]:
    children: dict[int, list[Employee]] = {}

    for employee in employees:
        supervisor_id = employee["supervisor_id"]

        if supervisor_id is not None:
            children.setdefault(supervisor_id, []).append(employee)

    return children


def getEmployeeDepth(employees: list[Employee], employeeId: int) -> int:
    """CEO = 0; ID i panjohur, zinxhir i prishur ose cikel = -1."""
    by_id = _index_by_id(employees)
    visited: set[int] = set()

    def depth(employee_id: int) -> int:
        if employee_id not in by_id or employee_id in visited:
            return -1

        employee = by_id[employee_id]
        visited.add(employee_id)
        supervisor_id = employee["supervisor_id"]

        if supervisor_id is None:
            return 0

        supervisor_depth = depth(supervisor_id)

        # Mos e shnderro gabimin -1 ne nje thellesi te vlefshme.
        if supervisor_depth == -1:
            return -1

        return supervisor_depth + 1

    return depth(employeeId)


def getAllSubordinates(employees: list[Employee], managerId: int) -> list[Subordinate]:
    """Vartesit pa menaxherin, te renditur sipas (relative_depth, id)."""
    by_id = _index_by_id(employees)

    if managerId not in by_id:
        return []

    children = _index_children(employees)
    subordinates: list[Subordinate] = []
    visited = {managerId}

    def collect(manager_id: int, relative_depth: int) -> None:
        for employee in children.get(manager_id, []):
            employee_id = employee["id"]

            if employee_id in visited:
                continue

            visited.add(employee_id)
            subordinates.append({
                "id": employee_id,
                "name": employee["name"],
                "relative_depth": relative_depth,
            })
            collect(employee_id, relative_depth + 1)

    collect(managerId, 1)
    subordinates.sort(key=lambda employee: (employee["relative_depth"], employee["id"]))

    return subordinates


def getPathToCeo(employees: list[Employee], employeeId: int) -> list[int]:
    """Rruga employee -> CEO; zinxhir i panjohur, i prishur ose ciklik = []."""
    by_id = _index_by_id(employees)
    visited: set[int] = set()
    path: list[int] = []

    def walk(employee_id: int) -> bool:
        if employee_id not in by_id or employee_id in visited:
            return False

        visited.add(employee_id)
        path.append(employee_id)
        supervisor_id = by_id[employee_id]["supervisor_id"]

        if supervisor_id is None:
            return True

        return walk(supervisor_id)

    # Nje zinxhir i pavlefshem nuk duhet te ktheje rruge te pjesshme.
    return path if walk(employeeId) else []


def findLowestCommonManager(
    employees: list[Employee], empId1: int, empId2: int
) -> CommonManager | None:
    """Paraardhesi i perbashket me i afert; secili eshte paraardhes i vetes."""
    by_id = _index_by_id(employees)

    if empId1 not in by_id or empId2 not in by_id:
        return None

    path1 = getPathToCeo(employees, empId1)
    path2 = getPathToCeo(employees, empId2)

    if not path1 or not path2:
        return None

    ancestors2 = set(path2)
    distances2 = {employee_id: distance for distance, employee_id in enumerate(path2)}

    def find_common(distance: int) -> CommonManager | None:
        if distance == len(path1):
            return None

        employee_id = path1[distance]

        if employee_id in ancestors2:
            return {
                "manager_id": employee_id,
                "manager_name": by_id[employee_id]["name"],
                "distance_to_emp1": distance,
                "distance_to_emp2": distances2[employee_id],
            }

        return find_common(distance + 1)

    return find_common(0)


def calculateTeamSalary(employees: list[Employee], managerId: int) -> int | float:
    """Paga e menaxherit plus te gjithe vartesit; ID i panjohur = 0."""
    by_id = _index_by_id(employees)

    if managerId not in by_id:
        return 0

    children = _index_children(employees)
    visited: set[int] = set()

    def team_salary(employee_id: int) -> int | float:
        if employee_id in visited:
            return 0

        visited.add(employee_id)
        total = by_id[employee_id]["salary"]

        for child in children.get(employee_id, []):
            total += team_salary(child["id"])

        return total

    return team_salary(managerId)


def main() -> None:
    data_path = Path(__file__).with_name("employees.json")

    with data_path.open(encoding="utf-8") as source:
        data: EmployeeData = json.load(source)

    employees = data["employees"]
    print("1. Thellesia e Liam (12):", getEmployeeDepth(employees, 12))
    print("\n2. Vartesit e Bob (2):")
    print(json.dumps(getAllSubordinates(employees, 2), indent=2, ensure_ascii=False))
    print("\n3. Rruga e Liam (12) deri te CEO:", getPathToCeo(employees, 12))
    print("\n4. Menaxheri i perbashket i Liam (12) dhe Ivy (9):")
    print(json.dumps(findLowestCommonManager(employees, 12, 9), indent=2))
    print("\n5. Paga totale e organizates:", calculateTeamSalary(employees, 1))


if __name__ == "__main__":
    main()
