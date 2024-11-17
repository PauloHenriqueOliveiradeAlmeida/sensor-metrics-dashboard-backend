from typing import List


class StandardDeviationFilter:
    def execute(self, values: List[float]) -> float:
        average = sum(values) / len(values)
        variance = sum((x - average) ** 2 for x in values) / len(values)
        standard_deviation = variance**0.5

        return standard_deviation
