def get_last_items(items, n):
    """
    Return the last n items from a list.
    """
    if n <= 0:
        return []

    if n > len(items):
        return items

    return items[-n + 1:]


def main():
    numbers = [10, 20, 30, 40, 50]

    print(get_last_items(numbers, 3))
    print(get_last_items(numbers, 1))
    print(get_last_items(numbers, 5))


if __name__ == "__main__":
    main()