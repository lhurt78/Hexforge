from event_system import EventSystem

from logger import (
    log_info,
    log_success,
    log_warning,
)


class ServiceManager:
    def __init__(
        self,
        event_system: EventSystem,
    ) -> None:
        self.services: dict[str, str] = {}
        self.event_system = event_system

    def register_service(
        self,
        service_name: str,
        status: str = "offline"
    ) -> None:

        self.services[service_name] = status

        self.event_system.emit(
            "service_registered",
            {
                "service_name": service_name,
                "status": status,
            }
        )

        log_info(
            f"Service registered: "
            f"{service_name} [{status}]"
        )

    def start_service(self, service_name: str) -> bool:
        if service_name not in self.services:
            self.event_system.emit(
                "service_start_failed",
                {
                    "service_name": service_name,
                    "reason": "unknown_service",
                }
            )

            log_warning(
                f"Cannot start unknown service: "
                f"{service_name}"
            )
            return False

        self.services[service_name] = "online"

        self.event_system.emit(
            "service_started",
            {
                "service_name": service_name,
                "status": "online",
            }
        )

        log_success(
            f"Service started: {service_name}"
        )

        return True

    def stop_service(self, service_name: str) -> bool:
        if service_name not in self.services:
            self.event_system.emit(
                "service_stop_failed",
                {
                    "service_name": service_name,
                    "reason": "unknown_service",
                }
            )

            log_warning(
                f"Cannot stop unknown service: "
                f"{service_name}"
            )
            return False

        self.services[service_name] = "offline"

        self.event_system.emit(
            "service_stopped",
            {
                "service_name": service_name,
                "status": "offline",
            }
        )

        log_success(
            f"Service stopped: {service_name}"
        )

        return True

    def get_services(self) -> dict[str, str]:
        return self.services