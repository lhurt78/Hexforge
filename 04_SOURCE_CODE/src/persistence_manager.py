import json
from pathlib import Path

from logger import (
    log_info,
    log_success,
    log_warning,
)


class PersistenceManager:
    def save_json(
        self,
        file_path: Path,
        data: dict | list
    ) -> bool:

        try:
            file_path.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            with file_path.open(
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    data,
                    file,
                    indent=4
                )

            log_success(
                f"Saved JSON: {file_path}"
            )

            return True

        except Exception as error:
            log_warning(
                f"Failed to save JSON: {error}"
            )

            return False

    def load_json(
        self,
        file_path: Path
    ) -> dict | list | None:

        if not file_path.exists():
            log_warning(
                f"JSON file not found: "
                f"{file_path}"
            )
            return None

        try:
            with file_path.open(
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

            log_success(
                f"Loaded JSON: {file_path}"
            )

            return data

        except Exception as error:
            log_warning(
                f"Failed to load JSON: {error}"
            )

            return None