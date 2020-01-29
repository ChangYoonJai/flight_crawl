#-*- coding:utf-8 -*-
# import ylog as log
from selenium import webdriver
from bs4 import BeautifulSoup

# setup Driver|Chrome : 크롬드라이버를 사용하는 driver 생성
driver = webdriver.Chrome('chromedriver')
def wait(delay=1):
    driver.implicitly_wait(delay)
wait(1)
driver.get('https://www.koreanair.com/mobile/korea/ko/ibe/bookingGate.html?isDomestic=false')
wait(1)
html = driver.page_source # 페이지의 elements모두 가져오기
soup = BeautifulSoup(html, 'html.parser') # BeautifulSoup사용하기

            # <option selected="selected" value="roundtrip">
            #  왕복
            # </option>
            # <option value="oneway">
            #  편도
            # </option>
            # <option value="multimore">
            #  다구간 여정
            # </option>

tripTypeMenu = driver.find_element_by_name('tripTypeMenu') #.send_keys('multimore')
tripTypeMenu:selenium.webdriver.remote.webelemen
print(type(tripTypeMenu), tripTypeMenu)
tripTypeMenu.select('multimore')


with open('test.txt', mode='w', encoding='utf8') as fp:
    fp.write(soup.prettify())


# # Login
# driver.get('https://nid.naver.com/nidlogin.login') # 네이버 로그인 URL로 이동하기
# driver.find_element_by_name('id').send_keys('changyoonjai') # 값 입력
# driver.find_element_by_name('pw').send_keys('ynvn*4*1')
# driver.find_element_by_xpath(
#     '//*[@id="frmNIDLogin"]/fieldset/input'
# ).click() # 버튼클릭하기
# driver.get('https://order.pay.naver.com/home') # Naver 페이 들어가기
# html = driver.page_source # 페이지의 elements모두 가져오기
# soup = BeautifulSoup(html, 'html.parser') # BeautifulSoup사용하기
# notices = soup.select('div.p_inr > div.p_info > a > span')


print(input('DONE'))
