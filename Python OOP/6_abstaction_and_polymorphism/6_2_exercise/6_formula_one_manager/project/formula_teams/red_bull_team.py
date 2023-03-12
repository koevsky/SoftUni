from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):

    EXPANSES = -250_000

    def calculate_revenue_after_race(self, race_pos: int):

        revenue = RedBullTeam.EXPANSES

        if race_pos == 1:
            revenue += 1_520_000

        elif race_pos == 2:
            revenue += 820_000

        elif race_pos in [3, 4, 5, 6, 7, 8]:
            revenue += 20_000

        elif race_pos in [9, 10]:
            revenue += 10_000

        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"