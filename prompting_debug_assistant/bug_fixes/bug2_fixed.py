def get_average(numbers):
    """Return the average of a non-empty list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate the average of an empty list")

    total = sum(numbers)
    return total / len(numbers)


def print_class_average(student_scores):
    """Print the average score for the class."""
    scores = []
    for student, score in student_scores.items():
        scores.append(score)

    average = get_average(scores)
    print("Class average:", average)


def main():
    grades = {
        "Amina": 88,
        "Murad": 92,
        "Leyla": 79
    }
    print_class_average(grades)


if __name__ == "__main__":
    main()