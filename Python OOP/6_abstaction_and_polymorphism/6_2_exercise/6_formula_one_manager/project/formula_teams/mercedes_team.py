from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):

    EXPANSES = -200_000

    def calculate_revenue_after_race(self, race_pos: int):

        revenue = MercedesTeam.EXPANSES

        if race_pos == 1:
            revenue += 1_100_000

        elif race_pos in [2, 3]:
            revenue += 600_000

        elif race_pos in [4, 5]:
            revenue += 100_000

        elif race_pos in [6, 7]:
            revenue += 50_000

        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"

