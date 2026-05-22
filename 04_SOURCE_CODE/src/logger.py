from datetime import datetime
from pathlib import Path

from rich.console import Console

console = Console()


def get_project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def get_log_file() -> Path:
    logs_dir = get_project_root() / "08_OUTPUTS" / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)

    date_stamp = datetime.now().strftime("%Y-%m-%d")
    return logs_dir / f"hexforge_{date_stamp}.log"


def write_to_file(level: str, message: str) -> None:
    log_file = get_log_file()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with log_file.open("a", encoding="utf-8") as file:
        file.write(f"{timestamp} [{level}] {message}\n")


def log_info(message: str) -> None:
    console.print(f"[cyan][INFO][/cyan] {message}")
    write_to_file("INFO", message)


def log_success(message: str) -> None:
    console.print(f"[green][SUCCESS][/green] {message}")
    write_to_file("SUCCESS", message)


def log_warning(message: str) -> None:
    console.print(f"[yellow][WARNING][/yellow] {message}")
    write_to_file("WARNING", message)


def log_error(message: str) -> None:
    console.print(f"[red][ERROR][/red] {message}")
    write_to_file("ERROR", message)