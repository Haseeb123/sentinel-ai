class RiskEngine:

    def score(self, plan):

        joined = " ".join(plan).lower()

        if "delete" in joined:

            return 95

        return 15