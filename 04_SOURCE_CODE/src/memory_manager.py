from logger import (
    log_info,
    log_success,
    log_warning,
)


class MemoryManager:
    def __init__(self) -> None:
        self.memories: dict[str, str] = {}

    def store_memory(
        self,
        key: str,
        value: str
    ) -> None:

        self.memories[key] = value

        log_info(f"Stored memory: {key}")

    def retrieve_memory(
        self,
        key: str
    ) -> str | None:

        memory = self.memories.get(key)

        if memory is None:
            log_warning(
                f"Memory not found: {key}"
            )
            return None

        log_success(
            f"Retrieved memory: {key}"
        )

        return memory

    def delete_memory(
        self,
        key: str
    ) -> bool:

        if key not in self.memories:
            log_warning(
                f"Cannot delete missing memory: {key}"
            )
            return False

        del self.memories[key]

        log_success(
            f"Deleted memory: {key}"
        )

        return True

    def get_memory_count(self) -> int:
        return len(self.memories)