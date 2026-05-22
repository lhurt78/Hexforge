from logger import (
    log_info,
    log_success,
    log_warning,
)


class ServiceManager:
    def __init__(self) -> None:
        self.services: dict[str, str] = {}

    def register_service(
        self,
        service_name: str,
        status: str = "offline"
    ) -> None:

        self.services[service_name] = status

        log_info(
            f"Service registered: "
            f"{service_name} [{status}]"
        )

    def start_service(self, service_name: str) -> bool:
        if service_name not in self.services:
            log_warning(
                f"Cannot start unknown service: "
                f"{service_name}"
            )
            return False

        self.services[service_name] = "online"

        log_success(
            f"Service started: {service_name}"
        )

        return True

    def stop_service(self, service_name: str) -> bool:
        if service_name not in self.services:
            log_warning(
                f"Cannot stop unknown service: "
                f"{service_name}"
            )
            return False

        self.services[service_name] = "offline"

        log_success(
            f"Service stopped: {service_name}"
        )

        return True

    def get_services(self) -> dict[str, str]:
        return self.services