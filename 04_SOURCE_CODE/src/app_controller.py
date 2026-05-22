from logger import (
    log_info,
    log_success,
    log_warning,
)


class AppController:
    def __init__(self) -> None:
        self.systems: dict[str, str] = {}
        self.running = False

    def register_system(
        self,
        system_name: str,
        status: str = "inactive"
    ) -> None:

        self.systems[system_name] = status

        log_info(
            f"System registered: "
            f"{system_name} [{status}]"
        )

    def initialize(self) -> bool:
        log_info("Initializing Hexforge systems...")

        if not self.systems:
            log_warning("No systems registered.")

        self.running = True

        log_success(
            "Application controller initialized."
        )

        return True

    def shutdown(self) -> None:
        log_info("Shutting down Hexforge...")

        self.running = False

        log_success("Shutdown complete.")

    def get_registered_systems(self) -> dict[str, str]:
        return self.systems