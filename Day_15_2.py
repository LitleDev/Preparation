def group_compression(chars):

    if not chars:
        return 0

    previous = chars[0]
    count = 1
    write = 0

    for i in range(1, len(chars)):

        if chars[i] == previous:
            count += 1

        else:
            chars[write] = previous
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

            previous = chars[i]
            count = 1

    # Handle the last group
    chars[write] = previous
    write += 1

    if count > 1:
        for digit in str(count):
            chars[write] = digit
            write += 1

    return write


if __name__ == "__main__":

    chars = ["a", "b", "b", "b", "b"]

    length = group_compression(chars)

    print(length)
    print(chars[:length])
