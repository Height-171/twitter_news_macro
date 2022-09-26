"""
Author : YJ Hwang
Last Modification: 2020.09.22
https://github.com/Height-171/twitter_news_macro
"""


from selenium import webdriver
import pywinmacro as pw
import pyperclip as pc
import time


class NewsBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.search_url = "https://www.google.com/search?&tbm=nws&q="
        self.news_text = ""
        self.splt =[]

    def kill(self):
        self.driver.quit()

    def refresh(self):
        pw.key_press_once("f5")

    def scrap_news(self, id, ps, keyword):
        self.driver.get(self.search_url + keyword)
        time.sleep(5)

        # 클릭할 좌표를 지정합니다.
        location = (114, 453)

        # 화면을 클릭합니다
        pw.click(location)

        # ctrl + A를 누릅니다
        pw.ctrl_a()

        # ctrl + C를 누릅니다
        pw.ctrl_c()

        # 클립보드의 내용물을 뽑아옵니다
        self.news_text = pc.paste()

        # 뉴스 텍스트를 스플릿합니다
        self.splt = self.news_text.split("\r\n\r\n")[3:-3]

        # 트위터에 접속합니다
        self.driver.get("https://twitter.com/login")
        time.sleep(5)
        # 아이디를 입력합니다
        pw.typing(id)
        # 탭 키를 칩니다
        pw.key_press_once("tab")
        # 비밀번호를 입력합니다
        pw.typing(ps)
        # 엔터키를 칩니다
        pw.key_press_once("enter")
        time.sleep(5)


        for el in self.splt:
            print(el)
            # 트위터에 글을 올립니다
            # 게시물 작성 페이지로 이동
            self.driver.get("https://twitter.com/intent/tweet")
            time.sleep(2)
            # 내용물 입력
            pw.type_in(el) #typing(영어, 숫자, 특수문자만 가능) type_in(한글의 경우)
            time.sleep(1)

            # ctrl + enter 누르기
            pw.key_on("control")
            pw.key_on("enter")
            pw.key_off("control")
            pw.key_off("enter")

            time.sleep(10)
