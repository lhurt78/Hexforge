from logger import log_info


def on_startup_begin(data: dict) -> None:
    status = data.get("status", "unknown")

    log_info(
        f"Runtime event received: startup_begin ({status})"
    )
    
def on_startup_complete(data: dict) -> None:
    status = data.get("status", "unknown")

    log_info(
        f"Runtime event received: startup_complete ({status})"
    )

def on_startup_failed(data: dict) -> None:
    status = data.get("status", "unknown")

    log_info(
        f"Runtime event received: startup_failed ({status})"
    )