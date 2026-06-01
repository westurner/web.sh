#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_websh
----------------------------------

Tests for `websh` module.
"""

import unittest
from unittest import mock
import runpy

from websh import websh


class TestWebsh(unittest.TestCase):
    def test_webbrowser_init(self):
        wb = websh.WebBrowser()
        self.assertIsNotNone(wb.clsmap)

        class Dummy(websh.WebBrowser):
            def setUp(self, *args, **kwargs):
                self.called = True

        d = Dummy()
        self.assertTrue(d.called)

    def test_get_browser_cls(self):
        cls = websh.WebBrowser.get_browser_cls()
        self.assertIsNotNone(cls)

    def test_open_new_tab_not_implemented(self):
        wb = websh.WebBrowser()
        with self.assertRaises(NotImplementedError):
            wb.open_new_tab("http://google.com")

    def test_x_www_browser_no_webbrowser(self):
        res = list(
            websh.WebBrowser.x_www_browser(
                ["http://google.com"], webbrowser=websh.Test_WebBrowser
            )
        )
        self.assertTrue(len(res) == 1)

    def test_x_www_browser_exception(self):
        with mock.patch.object(
            websh.Test_WebBrowser, "open_new_tab", side_effect=Exception("Test")
        ):
            with self.assertRaises(Exception):
                list(
                    websh.WebBrowser.x_www_browser(
                        ["http://google.com"], webbrowser=websh.Test_WebBrowser
                    )
                )

    def test_match_domain_suffix(self):
        self.assertTrue(websh.WebBrowser.match_domain("xyz.google.com", suffix=True))

    def test_expand_url_http_to_https(self):
        self.assertEqual(
            websh.WebBrowser.expand_url("http://google.com"), "https://google.com"
        )

    def test_expand_url_empty(self):
        self.assertEqual(websh.WebBrowser.expand_url(""), "")

    @mock.patch("subprocess.check_output")
    def test_x_www_open(self, mock_co):
        mock_co.return_value = b"ok"
        res = websh.X_www_WebBrowser.open_new_tab("google.com")
        self.assertEqual(res[1], b"ok")

    @mock.patch("subprocess.check_output")
    def test_osx_open(self, mock_co):
        mock_co.return_value = b"ok"
        websh.OSX_open_WebBrowser.BIN = "open"
        res = websh.OSX_open_WebBrowser.open_new_tab("google.com")
        self.assertEqual(res[1], b"ok")

    @mock.patch("subprocess.check_output")
    def test_win_start(self, mock_co):
        mock_co.return_value = b"ok"
        res = websh.Windows_start_WebBrowser.open_new_tab("google.com")
        self.assertEqual(res[1], b"ok")

    @mock.patch("subprocess.check_output")
    def test_py_webbrowser(self, mock_co):
        mock_co.return_value = b"ok"
        res = websh.Python_webbrowser_WebBrowser.open_new_tab("google.com")
        self.assertEqual(res[1], b"ok")

    @mock.patch("websh.websh.webbrowser", None)
    def test_py_webbrowser_no_module(self):
        with self.assertRaises(ImportError):
            websh.Python_webbrowser_WebBrowser.open_new_tab("google.com")

    @mock.patch("sys.exit")
    @mock.patch("websh.websh.WebBrowser.x_www_browser")
    def test_main(self, mock_xw, mock_exit):
        mock_xw.return_value = ["output"]
        websh.main(["google.com"])

    @mock.patch("sys.exit")
    def test_main_no_args(self, mock_exit):
        websh.main([])
        mock_exit.assert_called()

    @mock.patch("sys.exit")
    def test_main_options(self, mock_exit):
        with mock.patch("websh.websh.WebBrowser.x_www_browser") as mock_xw:
            mock_xw.return_value = []
            websh.main(["-v", "google.com"])
            websh.main(["-q", "google.com"])
            websh.main(["-b", "google.com"])
            websh.main(["-x", "google.com"])
            websh.main(["-s", "google.com"])
            websh.main(["-o", "google.com"])

            with mock.patch("unittest.main") as mock_ut:
                websh.main(["-t", "google.com"])
                mock_ut.assert_called_once()

    def test_inner_class(self):
        tb = websh.Test_WebBrowser("test_expand_url")
        tb.setUp()
        try:
            tb.test_expand_url()
            tb.test_x_www_browser()
        except Exception:
            pass

    def test_module_main(self):
        with mock.patch("sys.argv", ["websh.py", "-h"]):
            try:
                runpy.run_path(websh.__file__, run_name="__main__")
            except SystemExit:
                pass


if __name__ == "__main__":
    unittest.main()
