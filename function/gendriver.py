import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def gen_chrome_driver(headless=True, page_load_strategy='normal', download_directory=r"D:\arxiv"):
  options = Options()
  if headless:
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
  options.add_argument("--disable-dev-shm-usage")
  options.add_argument("--ignore-certificate-errors")
  options.add_argument("--allow-insecure-localhost")
  options.add_argument("--disable-gpu")
  options.add_argument("--disable-notifications")
  options.add_argument("--safebrowsing-disable-download-protection")
  options.add_argument('--allow-running-insecure-content')
  options.add_argument("--disable-notifications")
  options.page_load_strategy = page_load_strategy

  # Chrome 설정에 실험적 옵션 추가
  prefs = {
  "download.default_directory": download_directory, # 다운로드 경로 설정
  "download.prompt_for_download": False, # 다운로드 시 확인 창 띄우지 않음
  "safebrowsing.enabled": False, # 안전 브라우징 비활성화
  "download.directory_upgrade": True,
  "safebrowsing.disable_download_protection": True,
  "safebrowsing_for_trusted_sources_enabled": False, # 모든 다운로드 보호 비활성화
  "profile.default_content_setting_values.automatic_downloads": 1, # 자동 다운로드 허용
  "plugins.always_open_pdf_externally": True # PDF 자동 다운로드 허용
  }
  options.add_experimental_option("prefs", prefs)

  service = Service(r'/Users/dgsw8th58/Desktop/school/2024 머신코스 - 1/crawling/chromedriver-mac-x64/chromedriver')
  driver = webdriver.Chrome(service=service, options=options)
  return driver