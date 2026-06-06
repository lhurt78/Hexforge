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


def on_state_loaded(data: dict) -> None:
    log_info(
        f"Runtime event received: state_loaded "
        f"(Memory: {data.get('memory_count', 0)} | "
        f"Knowledge: {data.get('knowledge_count', 0)} | "
        f"Research: {data.get('research_count', 0)})"
    )

def on_state_save_started(data: dict) -> None:
    log_info(
        "Runtime event received: state_save_started"
    )


def on_state_save_complete(data: dict) -> None:
    log_info(
        "Runtime event received: state_save_complete"
    )


def on_state_save_failed(data: dict) -> None:
    log_info(
        "Runtime event received: state_save_failed"
    )

def on_state_snapshot_started(data: dict) -> None:
    log_info(
        "Runtime event received: state_snapshot_started"
    )


def on_state_snapshot_complete(data: dict) -> None:
    log_info(
        f"Runtime event received: state_snapshot_complete "
        f"({data.get('snapshot_path', 'unknown')})"
    )


def on_state_snapshot_failed(data: dict) -> None:
    log_info(
        f"Runtime event received: state_snapshot_failed "
        f"({data.get('snapshot_path', 'unknown')})"
    )

def on_state_restore_started(data: dict) -> None:
    log_info(
        f"Runtime event received: state_restore_started "
        f"({data.get('snapshot_path', 'unknown')})"
    )


def on_state_restore_complete(data: dict) -> None:
    log_info(
        f"Runtime event received: state_restore_complete "
        f"({data.get('snapshot_path', 'unknown')})"
    )

def on_state_restore_failed(data: dict) -> None:
    log_info(
        f"Runtime event received: state_restore_failed "
        f"({data.get('snapshot_path', 'unknown')})"
    )

def on_task_route_registered(data: dict) -> None:
    log_info(
        f"Runtime event received: task_route_registered "
        f"({data.get('task_type', 'unknown')} -> "
        f"{data.get('handler_name', 'unknown')})"
    )


def on_task_route_resolved(data: dict) -> None:
    log_info(
        f"Runtime event received: task_route_resolved "
        f"({data.get('task_type', 'unknown')} -> "
        f"{data.get('handler_name', 'unknown')})"
    )


def on_task_route_missing(data: dict) -> None:
    log_info(
        f"Runtime event received: task_route_missing "
        f"({data.get('task_type', 'unknown')})"
    )

def on_service_registered(data: dict) -> None:
    log_info(
        f"Runtime event received: service_registered "
        f"({data.get('service_name', 'unknown')} "
        f"[{data.get('status', 'unknown')}])"
    )


def on_service_started(data: dict) -> None:
    log_info(
        f"Runtime event received: service_started "
        f"({data.get('service_name', 'unknown')} "
        f"[{data.get('status', 'unknown')}])"
    )


def on_service_stopped(data: dict) -> None:
    log_info(
        f"Runtime event received: service_stopped "
        f"({data.get('service_name', 'unknown')} "
        f"[{data.get('status', 'unknown')}])"
    )


def on_service_start_failed(data: dict) -> None:
    log_info(
        f"Runtime event received: service_start_failed "
        f"({data.get('service_name', 'unknown')} | "
        f"{data.get('reason', 'unknown')})"
    )


def on_service_stop_failed(data: dict) -> None:
    log_info(
        f"Runtime event received: service_stop_failed "
        f"({data.get('service_name', 'unknown')} | "
        f"{data.get('reason', 'unknown')})"
    )