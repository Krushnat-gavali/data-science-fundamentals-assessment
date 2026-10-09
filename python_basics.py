"""Basic Python exercises for the Data Science Fundamentals Assessment."""


def classify_score(score):
    """Return a simple category for a score from 0 to 100."""
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    if score >= 75:
        return "A"
    if score >= 60:
        return "B"
    if score >= 40:
        return "C"
    return "Needs improvement"


def calculate_average(values):
    """Calculate the average of a non-empty sequence of numbers."""
    if not values:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)


def demonstrate_collections():
    """Show common built-in collection types."""
    scores = [70, 82, 91]
    fixed_coordinates = (16.85, 74.58)
    student = {"name": "Asha", "score": 82}
    unique_scores = set(scores)
    scores.append(88)
    student["passed"] = True
    return scores, fixed_coordinates, student, unique_scores


if __name__ == "__main__":
    print("Grade:", classify_score(78))
    print("Average:", calculate_average([10, 20, 30]))
    print("Collections:", demonstrate_collections())
