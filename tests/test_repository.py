"""Regression checks for shipped configuration and package consistency."""

import copy
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from scripts.validate_repository import MODES, PLUGIN, ROOT, validate_config, validate_repository


class ConfigTests(unittest.TestCase):
    def setUp(self):
        self.config = json.loads(
            (ROOT / PLUGIN / "references/default-resources.json").read_text(encoding="utf-8")
        )

    def test_supported_modes_and_disabled_access_are_valid(self):
        for mode in MODES:
            with self.subTest(mode=mode):
                config = copy.deepcopy(self.config)
                config["mode"] = mode
                config["web_search"]["enabled"] = False
                config["instance_readonly"]["enabled"] = False
                self.assertEqual(validate_config(config), [])

    def test_unknown_or_non_string_modes_are_rejected(self):
        for mode in ("automatic", None, [], {}):
            with self.subTest(mode=mode):
                self.config["mode"] = mode
                self.assertTrue(validate_config(self.config))

    def test_enable_flags_require_real_booleans(self):
        for section in ("web_search", "instance_readonly"):
            for value in ("false", 0, None):
                with self.subTest(section=section, value=value):
                    config = copy.deepcopy(self.config)
                    config[section]["enabled"] = value
                    self.assertTrue(validate_config(config))

    def test_limits_require_positive_integers(self):
        for section, field in (("web_search", "max_results_per_tier"),
                               ("instance_readonly", "max_records_per_query")):
            for value in (0, -1, True, 1.5, "100", None):
                with self.subTest(section=section, value=value):
                    config = copy.deepcopy(self.config)
                    config[section][field] = value
                    self.assertTrue(validate_config(config))

    def test_write_methods_are_rejected(self):
        for methods in (["GET", "POST"], ["PATCH"], [], "GET"):
            with self.subTest(methods=methods):
                self.config["instance_readonly"]["http_methods_allowed"] = methods
                self.assertTrue(validate_config(self.config))

    def test_malformed_shapes_are_rejected(self):
        for config in (None, [], {}, {"mode": "manual", "web_search": []}):
            with self.subTest(config=config):
                self.assertTrue(validate_config(config))


class RepositoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for directory in (".claude-plugin", "providers", "examples"):
            shutil.copytree(ROOT / directory, self.root / directory)

    def test_shipped_repository_is_valid(self):
        self.assertEqual(validate_repository(self.root), [])

    def test_version_drift_is_rejected(self):
        path = self.root / PLUGIN / ".claude-plugin/plugin.json"
        manifest = json.loads(path.read_text(encoding="utf-8"))
        manifest["version"] = "99.0.0"
        path.write_text(json.dumps(manifest), encoding="utf-8")
        self.assertIn("marketplace plugin version does not match manifest", validate_repository(self.root))

    def test_missing_policy_is_rejected(self):
        (self.root / PLUGIN / "references/configuration-policy.md").unlink()
        self.assertIn("missing plugin file: references/configuration-policy.md", validate_repository(self.root))

    def test_malformed_json_is_reported(self):
        (self.root / "examples/sn-advisor.config.example.json").write_text("{", encoding="utf-8")
        self.assertTrue(any("examples/sn-advisor.config.example.json:" in error
                            for error in validate_repository(self.root)))

    def test_json_null_config_is_rejected(self):
        (self.root / "examples/sn-advisor.config.example.json").write_text("null", encoding="utf-8")
        self.assertIn("examples/sn-advisor.config.example.json: config must be an object",
                      validate_repository(self.root))


if __name__ == "__main__":
    unittest.main()
