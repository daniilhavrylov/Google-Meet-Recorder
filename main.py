import asyncio
import os
from dotenv import load_dotenv
from playwright.async_api import Page

# from services.audio import record_to_file
from services.driver import Driver

load_dotenv()

async def connect_bot(driver):
    invite_link = os.getenv('INVITE_LINK')
    bot_name = os.getenv('BOT_NAME')
    page: Page = await driver.get_page(invite_link)
    await page.wait_for_selector("//div[contains(@class, 'qdOxv-fmcmS-yrriRe')]//input[@id='c11']")
    await page.keyboard.press('Control+d')
    await page.keyboard.press('Control+e')
    await page.fill("//div[contains(@class, 'qdOxv-fmcmS-yrriRe')]//input[@id='c11']",
                    bot_name
                    )

async def main():
    driver = Driver()
    try:
        await driver.start()
        await connect_bot(driver)

    finally:
        await driver.close()

if __name__ == '__main__':
    asyncio.run(main())
