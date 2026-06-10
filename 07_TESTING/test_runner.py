import subprocess
import sys
import time
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]

PLANNING_TESTS = [
    "07_TESTING/test_planning_task_handler.py",
    "07_TESTING/test_direct_planning_execution.py",
    "07_TESTING/test_startup_planning_registration.py",
    "07_TESTING/test_runtime_planning_execution.py",
    "07_TESTING/test_missing_planning_route.py",
    "07_TESTING/test_missing_planning_handler.py",
    "07_TESTING/test_invalid_planning_payload_execution.py",
    "07_TESTING/test_planning_task_status_transitions.py",
    "07_TESTING/test_planning_task_result_errors.py",
]


def run_test(
    test_path: str,
) -> dict:
    start_time = time.perf_counter()

    completed_process = subprocess.run(
        [
            sys.executable,
            test_path,
        ],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
    )

    duration = time.perf_counter() - start_time

    return {
        "test_path": test_path,
        "passed": completed_process.returncode == 0,
        "duration": duration,
        "stdout": completed_process.stdout,
        "stderr": completed_process.stderr,
    }


def run_tests(
    test_paths: list[str],
) -> list[dict]:
    results = []

    for test_path in test_paths:
        results.append(
            run_test(test_path)
        )

    return results


def print_results(
    results: list[dict],
) -> None:
    print()
    print("Hexforge Test Runner")
    print("====================")
    print()

    passed_count = 0

    for result in results:
        status = "PASS" if result["passed"] else "FAIL"

        if result["passed"]:
            passed_count += 1

        print(
            f"{status} | "
            f"{result['duration']:.2f}s | "
            f"{result['test_path']}"
        )

        if not result["passed"]:
            print()
            print("STDOUT:")
            print(result["stdout"])
            print()
            print("STDERR:")
            print(result["stderr"])
            print()

    print()
    print(
        f"Summary: {passed_count}/{len(results)} tests passed."
    )


def main() -> int:
    results = run_tests(
        PLANNING_TESTS
    )

    print_results(
        results
    )

    if all(result["passed"] for result in results):
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(
        main()
    )