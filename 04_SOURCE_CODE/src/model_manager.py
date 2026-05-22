from logger import (
    log_info,
    log_success,
    log_warning,
)


class ModelManager:
    def __init__(self) -> None:
        self.models: dict[str, dict] = {}
        self.active_model: str | None = None

    def register_model(
        self,
        model_name: str,
        provider: str,
        status: str = "offline"
    ) -> None:

        self.models[model_name] = {
            "provider": provider,
            "status": status,
        }

        log_info(
            f"Model registered: "
            f"{model_name} [{provider}]"
        )

    def activate_model(
        self,
        model_name: str
    ) -> bool:

        if model_name not in self.models:
            log_warning(
                f"Unknown model: {model_name}"
            )
            return False

        self.active_model = model_name

        self.models[model_name]["status"] = "online"

        log_success(
            f"Active model set: {model_name}"
        )

        return True

    def get_active_model(self) -> str | None:
        return self.active_model

    def get_registered_models(self) -> dict[str, dict]:
        return self.models