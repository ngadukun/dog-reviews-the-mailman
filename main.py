"""One-line entry: The Dog Reviews the Mailman."""

LINE = "One star. He comes every day, smells like every dog in town, and never once brings me the mail."

MAX_CHARS = 200


def main() -> None:
    if len(LINE) > MAX_CHARS:
        raise SystemExit(f"line is {len(LINE)} chars, cap is {MAX_CHARS}")
    print(LINE)


if __name__ == "__main__":
    main()
