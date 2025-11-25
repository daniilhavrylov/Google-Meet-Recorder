from playwright.async_api import async_playwright, Page

class Driver:
    def __init__(self):
        self.playwright = None
        self.browser = None

    async def start(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=False)

    async def get_page(self, link) -> Page:
        if not self.browser:
            raise Exception("Browser not started. Call 'await start()' first.")
        page = await self.browser.new_page()
        await page.goto(link)
        return page

    async def close(self):
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()