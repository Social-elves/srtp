from django.core.management.base import BaseCommand
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from hotsearch.models import HotSearch
import time

class Command(BaseCommand):
    help = '抓取微博热搜榜并保存到数据库'

    def handle(self, *args, **kwargs):
        # 配置 Edge WebDriver 选项
        options = Options()
        options.add_argument('--headless')  # 无头模式
        options.add_argument('--disable-gpu')
        options.add_argument('window-size=1200x600')
        # 您可以根据需要添加其他选项

        # 初始化 WebDriver，并设置防自动化检测脚本
        driver = webdriver.Edge(options=options)
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => undefined
                })
            """
        })

        try:
            # 定义目标 URL
            url = 'https://s.weibo.com/top/summary'
            driver.get(url)
            time.sleep(3)  # 等待页面加载

            # 提取热搜数据
            hot_search_list = []
            rows = driver.find_elements(By.CSS_SELECTOR, 'table tbody tr')[1:]  # 跳过表头
            for row in rows:
                try:
                    # 提取热搜标题和链接
                    title = row.find_element(By.CSS_SELECTOR, '.td-02')
                    keyword = title.text.strip()
                    link_element = title.find_element(By.TAG_NAME, 'a')
                    link = link_element.get_attribute('href') if link_element else ''

                    # 检查数据库中是否已经存在该热搜
                    exists = HotSearch.objects.filter(keyword=keyword).exists()
                    if not exists:
                        # 保存到数据库
                        HotSearch.objects.create(keyword=keyword, link=link)
                        self.stdout.write(self.style.SUCCESS(f"保存成功: {keyword}"))
                    else:
                        self.stdout.write(self.style.INFO(f"已存在: {keyword}"))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"解析错误: {e}"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"发生错误: {e}"))
        finally:
            # 确保退出 WebDriver
            driver.quit()