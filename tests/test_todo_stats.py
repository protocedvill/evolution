import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from todo_stats import count_checklist_items, percent_complete, remaining_items  # noqa: E402


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


if __name__ == "__main__":
    unittest.main()
