import threading
import tkinter as tk
from tkinter import ttk
from pathlib import Path
from datetime import datetime
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
TESTING_PATH = PROJECT_ROOT / "07_TESTING"
REPORTS_PATH = TESTING_PATH / "test_reports"
LATEST_REPORT_PATH = REPORTS_PATH / "latest_test_report.txt"

sys.path.insert(0, str(TESTING_PATH))

from test_runner import (
    PLANNING_TESTS,
    RUNTIME_TESTS,
    ALL_TESTS,
    run_tests,
) 


class TestRunnerGUI:
    def __init__(
        self,
        root: tk.Tk,
    ) -> None:
        self.root = root
        self.root.title("Hexforge Test Runner")
        self.root.geometry("900x600")

        self.run_button = ttk.Button(
            root,
            text="Run Planning Tests",
            command=self.run_planning_tests,
        )
        self.run_button.pack(
            padx=10,
            pady=10,
            anchor="w",
        )

        self.runtime_button = ttk.Button(
            root,
            text="Run Runtime Tests",
            command=self.run_runtime_tests,
        )
        self.runtime_button.pack(
            padx=10,
            pady=0,
            anchor="w",
        )
        
        self.all_button = ttk.Button(
            root,
            text="Run All Tests",
            command=self.run_all_tests,
        )
        self.all_button.pack(
            padx=10,
            pady=0,
            anchor="w",
        )

        self.clear_button = ttk.Button(
            root,
            text="Clear Output",
            command=self.clear_results,
        )
        self.clear_button.pack(
            padx=10,
            pady=0,
            anchor="w",
        )

        self.export_button = ttk.Button(
            root,
            text="Export Report",
            command=self.export_report,
        )
        self.export_button.pack(
            padx=10,
            pady=0,
            anchor="w",
        )

        self.summary_label = ttk.Label(
            root,
            text="No tests run.",
        )
        self.summary_label.pack(
            padx=10,
            pady=5,
            anchor="w",
        )
        self.results_tree = ttk.Treeview(
            root,
            columns=(
                "status",
                "duration",
                "test",
            ),
            show="headings",
        )

        self.results_tree.heading(
            "status",
            text="Status",
        )
        self.results_tree.heading(
            "duration",
            text="Duration",
        )
        self.results_tree.heading(
            "test",
            text="Test",
        )

        self.results_tree.column(
            "status",
            width=100,
        )
        self.results_tree.column(
            "duration",
            width=100,
        )
        self.results_tree.column(
            "test",
            width=650,
        )

        self.results_tree.pack(
            padx=10,
            pady=10,
            fill="both",
            expand=True,
        )

        self.output_text = tk.Text(
            root,
            height=12,
            wrap="word",
        )
        self.output_text.pack(
            padx=10,
            pady=10,
            fill="both",
        )

        self.latest_results = []

    def run_planning_tests(
        self,
    ) -> None:
        self.run_button.config(
            state="disabled"
        )

        self.clear_results()

        thread = threading.Thread(
            target=self._run_tests_thread,
            daemon=True,
        )
        thread.start()

    def _run_tests_thread(
        self,
    ) -> None:
        results = run_tests(
            PLANNING_TESTS
        )

        self.root.after(
            0,
            lambda: self.display_results(results),
        )

    def run_runtime_tests(
        self,
    ) -> None:
        self.run_button.config(
            state="disabled"
        )
        self.runtime_button.config(
            state="disabled"
        )
        self.all_button.config(
            state="disabled"
        )

        self.clear_results()

        thread = threading.Thread(
            target=lambda: self._run_specific_tests(
                RUNTIME_TESTS
            ),
            daemon=True,
        )
        thread.start()


    def run_all_tests(
        self,
    ) -> None:
        self.run_button.config(
            state="disabled"
        )
        self.runtime_button.config(
            state="disabled"
        )
        self.all_button.config(
            state="disabled"
        )

        self.clear_results()

        thread = threading.Thread(
            target=lambda: self._run_specific_tests(
                ALL_TESTS
            ),
            daemon=True,
        )
        thread.start()


    def _run_specific_tests(
        self,
        test_list,
    ) -> None:
        results = run_tests(
            test_list
        )

        self.root.after(
            0,
            lambda: self.display_results(
                results
            ),
        )

    def clear_results(
        self,
    ) -> None:
        for item in self.results_tree.get_children():
            self.results_tree.delete(item)

        self.output_text.delete(
            "1.0",
            tk.END,
        )

        self.summary_label.config(
            text="No tests run."
        )

    def export_report(
        self,
    ) -> None:
        REPORTS_PATH.mkdir(
            exist_ok=True
        )

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        report_lines = [
            "Hexforge Test Report",
            "====================",
            f"Generated: {timestamp}",
            "",
        ]

        if not self.latest_results:
            report_lines.append(
                "No test results available."
            )
        else:
            passed_count = sum(
                1
                for result in self.latest_results
                if result["passed"]
            )

            report_lines.append(
                f"Summary: {passed_count}/{len(self.latest_results)} tests passed."
            )
            report_lines.append("")

            for result in self.latest_results:
                status = "PASS" if result["passed"] else "FAIL"

                report_lines.append(
                    f"{status} | "
                    f"{result['duration']:.2f}s | "
                    f"{result['test_path']}"
                )

                if not result["passed"]:
                    report_lines.append("")
                    report_lines.append("STDOUT:")
                    report_lines.append(result["stdout"])
                    report_lines.append("")
                    report_lines.append("STDERR:")
                    report_lines.append(result["stderr"])
                    report_lines.append("")

        LATEST_REPORT_PATH.write_text(
            "\n".join(report_lines),
            encoding="utf-8",
        )

        self.output_text.insert(
            tk.END,
            f"\nReport exported to: {LATEST_REPORT_PATH}\n",
        )

    def display_results(
        self,
        results: list[dict],
    ) -> None:
        self.latest_results = results

        passed_count = 0

        for result in results:
            status = "PASS" if result["passed"] else "FAIL"

            if result["passed"]:
                passed_count += 1

            self.results_tree.insert(
                "",
                tk.END,
                values=(
                    status,
                    f"{result['duration']:.2f}s",
                    result["test_path"],
                ),
            )

            if not result["passed"]:
                self.output_text.insert(
                    tk.END,
                    f"FAILED: {result['test_path']}\n\n",
                )
                self.output_text.insert(
                    tk.END,
                    "STDOUT:\n",
                )
                self.output_text.insert(
                    tk.END,
                    result["stdout"],
                )
                self.output_text.insert(
                    tk.END,
                    "\nSTDERR:\n",
                )
                self.output_text.insert(
                    tk.END,
                    result["stderr"],
                )
                self.output_text.insert(
                    tk.END,
                    "\n\n",
                )

        self.output_text.insert(
            tk.END,
            f"Summary: {passed_count}/{len(results)} tests passed.\n",
        )

        if passed_count == len(results):
            self.summary_label.config(
                text=f"PASS: {passed_count}/{len(results)} tests passed."
            )
        else:
            self.summary_label.config(
                text=f"FAIL: {passed_count}/{len(results)} tests passed."
            )

        self.run_button.config(
            state="normal"
        )

        self.runtime_button.config(
            state="normal"
        )

        self.all_button.config(
            state="normal"
        )

def main() -> None:
    root = tk.Tk()
    app = TestRunnerGUI(
        root
    )
    root.mainloop()


if __name__ == "__main__":
    main()