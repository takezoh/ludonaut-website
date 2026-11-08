import re
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

SITE = Path(__file__).resolve().parents[1] / "site"


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.body_text = []
        self.attrs = []
        self.tags = []

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        self.attrs.append((tag, dict(attrs)))
        if tag not in {"meta", "link", "br", "img", "hr", "input"}:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        assert self.stack and self.stack[-1] == tag, (tag, self.stack)
        self.stack.pop()

    def handle_data(self, data):
        if "body" in self.stack and data.strip():
            self.body_text.append(data.strip())


class SiteTests(unittest.TestCase):
    def setUp(self):
        self.text = (SITE / "index.html").read_text(encoding="utf-8")
        self.page = Page()
        self.page.feed(self.text)

    def test_markup_is_balanced(self):
        self.assertEqual(self.page.stack, [])
        self.assertTrue(self.text.lower().startswith("<!doctype html>"))

    def test_exact_public_copy(self):
        self.assertEqual(self.page.body_text, [
            "Ludonaut.ai", "Charting the unplayed",
            "A platform for AI that sees and plays games.",
            "Automate gameplay. Play together with AI.", "Classified.",
        ])

    def test_static_and_private_data_free(self):
        self.assertFalse(set(self.page.tags) & {"script", "iframe", "form", "input", "x-dc", "helmet"})
        self.assertNotRegex(self.text, r"(?i)(sk-[a-zA-Z0-9]{20,}|gh[pousr]_[a-zA-Z0-9]{20,}|-----BEGIN .*PRIVATE KEY|/home/|/tmp/|claude\.ai|support\.js|\{\{)")
        for _, attrs in self.page.attrs:
            self.assertFalse(any(key.lower().startswith("on") for key in attrs))

    def test_only_expected_font_dependencies(self):
        urls = [value for _, attrs in self.page.attrs for key, value in attrs.items() if key in {"src", "href"}]
        self.assertEqual(len(urls), 3)
        self.assertTrue(all(urlparse(url).scheme == "https" for url in urls))
        self.assertTrue(all(urlparse(url).hostname in {"fonts.googleapis.com", "fonts.gstatic.com"} for url in urls))

    def test_accessibility_basics(self):
        self.assertEqual(self.page.tags.count("main"), 1)
        self.assertEqual(self.page.tags.count("h1"), 1)
        self.assertIn(("html", {"lang": "en"}), self.page.attrs)
        self.assertIn("prefers-reduced-motion: reduce", self.text)
        self.assertIn('name="viewport"', self.text)

    def test_publish_directory(self):
        self.assertEqual([p.name for p in SITE.iterdir()], ["index.html"])


if __name__ == "__main__":
    unittest.main()
