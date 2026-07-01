import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from todo_stats import count_checklist_items  # noqa: E402


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


if __name__ == "__main__":
    unittest.main()
