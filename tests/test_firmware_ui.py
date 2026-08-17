#!/usr/bin/env python3
"""Static firmware UI contract tests that do not require ESP-IDF."""

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class FirmwareUiTests(unittest.TestCase):
    def test_battery_footer_uses_factory_hal_at_low_frequency(self):
        app = (ROOT / "firmware/app_codex/app_codex.cpp").read_text()

        self.assertIn("kBatteryRefreshMs = 5000", app)
        self.assertIn("GetHAL().getBatteryLevel()", app)
        self.assertIn("GetHAL().isBatteryCharging(false)", app)
        self.assertIn("LV_SYMBOL_BATTERY_FULL", app)
        self.assertIn("LV_SYMBOL_BATTERY_EMPTY", app)
        self.assertIn("s_battery_icon_lbl = lv_label_create(s_root);", app)
        self.assertIn('charging ? "+" : ""', app)
        self.assertIn("level <= 15", app)
        self.assertIn("level <= 30", app)
        self.assertIn("s_battery_lbl = lv_label_create(s_root);", app)
        self.assertIn("s_battery_icon_lbl = nullptr;", app)
        self.assertIn("s_battery_lbl = nullptr;", app)
        self.assertLess(app.index("update_battery_label();"),
                        app.index("if (_key_manager)"))


if __name__ == "__main__":
    unittest.main()
