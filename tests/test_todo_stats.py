import io
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from todo_stats import (  # noqa: E402
    count_checklist_items,
    main,
    percent_complete,
    remaining_items,
)


class CountChecklistItemsTest(unittest.TestCase):
    def test_counts_done_and_total(self):
        lines = [
            "# heading",
            "",
            "- [x] done item",
            "- [ ] pending item",
            "- [x] another done item",
            "not a checklist line",
        ]
        done, total = count_checklist_items(lines)
        self.assertEqual(done, 2)
        self.assertEqual(total, 3)

    def test_empty_input(self):
        self.assertEqual(count_checklist_items([]), (0, 0))

    def test_no_checklist_lines(self):
        lines = ["# heading", "some text", ""]
        self.assertEqual(count_checklist_items(lines), (0, 0))


class RemainingItemsTest(unittest.TestCase):
    def test_returns_only_pending_item_text(self):
        lines = [
            "# heading",
            "- [x] done item",
            "- [ ] pending item one",
            "- [ ] pending item two",
            "not a checklist line",
        ]
        self.assertEqual(
            remaining_items(lines), ["pending item one", "pending item two"]
        )

    def test_no_pending_items(self):
        lines = ["- [x] done item"]
        self.assertEqual(remaining_items(lines), [])

    def test_empty_input(self):
        self.assertEqual(remaining_items([]), [])


class PercentCompleteTest(unittest.TestCase):
    def test_computes_rounded_percentage(self):
        self.assertEqual(percent_complete(1, 3), 33)
        self.assertEqual(percent_complete(2, 3), 67)

    def test_all_done(self):
        self.assertEqual(percent_complete(5, 5), 100)

    def test_no_items_is_zero(self):
        self.assertEqual(percent_complete(0, 0), 0)


class MainTest(unittest.TestCase):
    def _write_todo(self, tmp_dir):
        path = Path(tmp_dir) / "TODO.md"
        path.write_text(
            "# heading\n"
            "- [x] done item\n"
            "- [ ] pending item one\n"
            "- [ ] pending item two\n"
        )
        return path

    def test_default_output(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            path = self._write_todo(tmp_dir)
            out = io.StringIO()
            with redirect_stdout(out):
                exit_code = main(["todo_stats.py", str(path)])
            self.assertEqual(exit_code, 0)
            self.assertEqual(out.getvalue(), "1/3 tasks done (2 remaining)\n")

    def test_remaining_flag(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            path = self._write_todo(tmp_dir)
            out = io.StringIO()
            with redirect_stdout(out):
                exit_code = main(["todo_stats.py", "--remaining", str(path)])
            self.assertEqual(exit_code, 0)
            self.assertEqual(
                out.getvalue(), "pending item one\npending item two\n"
            )

    def test_percent_flag(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            path = self._write_todo(tmp_dir)
            out = io.StringIO()
            with redirect_stdout(out):
                exit_code = main(["todo_stats.py", "--percent", str(path)])
            self.assertEqual(exit_code, 0)
            self.assertEqual(out.getvalue(), "33%\n")


if __name__ == "__main__":
    unittest.main()
