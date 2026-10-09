"""Descriptive statistics for a small example dataset."""
from statistics import mean, median, multimode, variance, stdev

DELIVERY_DAYS = [2, 3, 3, 4, 8]


def summarize(values):
    """Return common descriptive statistics for numeric values."""
    if not values:
        raise ValueError("values must not be empty")
    result = {
        "count": len(values),
        "mean": mean(values),
        "median": median(values),
        "mode": multimode(values),
        "minimum": min(values),
        "maximum": max(values),
    }
    if len(values) > 1:
        result["sample_variance"] = variance(values)
        result["sample_standard_deviation"] = stdev(values)
    return result


if __name__ == "__main__":
    for metric, value in summarize(DELIVERY_DAYS).items():
        print(f"{metric}: {value}")
