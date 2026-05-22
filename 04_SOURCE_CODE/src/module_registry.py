from logger import log_info, log_success


class ModuleRegistry:
    def __init__(self) -> None:
        self.modules: dict[str, str] = {}

    def register(self, name: str, status: str = "inactive") -> None:
        self.modules[name] = status
        log_info(f"Registered module: {name} [{status}]")

    def list_modules(self) -> dict[str, str]:
        return self.modules

    def validate_registry(self) -> bool:
        if not self.modules:
            log_info("No modules registered yet.")
            return True

        log_success(f"{len(self.modules)} module(s) registered.")
        return True