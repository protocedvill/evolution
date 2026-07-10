import subprocess
import tempfile
import unittest
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent.parent / "scripts" / "check_todo_format.sh"


class CheckTodoFormatTest(unittest.TestCase):
    def _run(self, todo_contents):
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_todo = Path(tmp_dir) / "TODO.md"
            tmp_todo.write_text(todo_contents)

            return subprocess.run(
                [str(SCRIPT_PATH), str(tmp_todo)],
                capture_output=True,
                text=True,
            )

    def test_well_formed_checklist_exits_zero(self):
        result = self._run(
            "# heading\n"
            "- [x] done item\n"
            "- [ ] pending item\n"
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("TODO.md checklist format OK", result.stdout)

    def test_malformed_checklist_line_exits_nonzero(self):
        result = self._run(
            "# heading\n"
            "- [x] done item\n"
            "- [X] bad checkbox\n"
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Malformed checklist line: - [X] bad checkbox", result.stderr)


if __name__ == "__main__":
    unittest.main()
