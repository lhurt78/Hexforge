from logger import log_error, log_success
from startup import run_startup_sequence


def main() -> None:
    try:
        success = run_startup_sequence()

        if not success:
            log_error("Hexforge startup failed.")
            raise SystemExit(1)

        log_success("Hexforge is ready.")

    except Exception as error:
        log_error(f"Unhandled startup error: {error}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()