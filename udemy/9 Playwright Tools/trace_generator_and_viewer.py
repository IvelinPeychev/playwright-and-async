import time

import pytest
from playwright.sync_api import BrowserContext, Page

DOCS_URL = 'https://playwright.dev/python/docs/intro'


@pytest.fixture(autouse=True)
def trace_test(context: BrowserContext):
    # setup
    context.tracing.start(
        name='playwright',
        screenshots=True,
        snapshots=True,
        sources=True,
    )
    yield
    context.tracing.stop(path='trace.zip')


def test_page_has_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")

    # Use Playwright's auto-wait features to wait for navigation after click
    with page.expect_navigation():
        page.get_by_role('link', name='GET STARTED').click()

    assert page.url == DOCS_URL
