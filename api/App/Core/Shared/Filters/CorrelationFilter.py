from typing import List


class CorrelationFilter:
    def execute(self, first_values: List[float], second_values: List[float]) -> float:
        [first_average, second_average] = [
            sum(values) / len(values) for values in [first_values, second_values]
        ]
        numerator = sum(
            ((first_values[i] - first_average) for i in range(len(first_values)))
        ) * sum(
            ((second_values[i] - second_average) for i in range(len(second_values)))
        )

        denominator = (
            sum(
                (first_values[i] - first_average) ** 2 for i in range(len(first_values))
            )
            * sum(
                (second_values[i] - second_average) ** 2
                for i in range(len(second_values))
            )
        ) ** 0.5

        if denominator == 0:
            return 0.0

        coefficient = numerator / denominator

        return coefficient
