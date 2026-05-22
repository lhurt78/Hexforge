from rich.console import Console

console = Console()


def log_info(message: str) -> None:
    console.print(f"[cyan][INFO][/cyan] {message}")


def log_success(message: str) -> None:
    console.print(f"[green][SUCCESS][/green] {message}")


def log_warning(message: str) -> None:
    console.print(f"[yellow][WARNING][/yellow] {message}")


def log_error(message: str) -> None:
    console.print(f"[red][ERROR][/red] {message}")