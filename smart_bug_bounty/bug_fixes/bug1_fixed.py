def get_last_items(items, n):
    """Return the last n items from a list."""
    if n <= 0:
        return []
    return items[-n:]


def main():
    numbers = [10, 20, 30, 40, 50]
    assert get_last_items(numbers, 3) == [30, 40, 50]
    assert get_last_items(numbers, 1) == [50]
    assert get_last_items(numbers, 5) == [10, 20, 30, 40, 50]
    assert get_last_items(numbers, 10) == numbers
    assert get_last_items(numbers, 0) == []
    assert get_last_items(numbers, -2) == []
    print("All Python tests passed.")


if __name__ == "__main__":
    main()