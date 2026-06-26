# engine/optimization/solver.py

from typing import List, Dict

from ortools.linear_solver import pywraplp

from utils.logger import get_logger


logger = get_logger(__name__)


class OptimizationSolver:
    """
    Uses linear optimization to select best users
    under constraints (budget, limit, etc.).
    """

    def solve(self, users: List[Dict], budget: float = None) -> List[Dict]:
        logger.info("Starting optimization...")

        solver = pywraplp.Solver.CreateSolver("SCIP")

        if not solver:
            raise RuntimeError("Solver not created")

        # Decision variables
        x = [solver.BoolVar(f"x_{i}") for i in range(len(users))]

        # Objective: maximize score
        solver.Maximize(
            solver.Sum(x[i] * users[i].get("score", 0) for i in range(len(users)))
        )

        # Constraint: budget (optional)
        if budget:
            solver.Add(
                solver.Sum(x[i] * users[i].get("expected_revenue", 0)
                           for i in range(len(users))) <= budget
            )

        status = solver.Solve()

        selected = []

        if status == pywraplp.Solver.OPTIMAL:
            for i in range(len(users)):
                if x[i].solution_value() == 1:
                    selected.append(users[i])

        logger.info(f"Optimization selected {len(selected)} users")

        return selected