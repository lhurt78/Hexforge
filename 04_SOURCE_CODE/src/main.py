from startup import run_startup_sequence


def main() -> None:
    success = run_startup_sequence()

    if not success:
        raise SystemExit(1)


if __name__ == "__main__":
    main()