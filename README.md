# twitter_news_macro
매크로를 활용한 트위터 뉴스 스트랩 로봇 입니다

# dependencies
> pip install selenium pyperclip pywin32

# 실행방법
> python main.py <id> <ps> <keyword>

id : 트위터 아이디

ps : 트위터 비밀번호

keyword : 구글 뉴스 검색 키워드

# 매크로 만드는 법
pw.get_mounse_position()을 통해 마우스 정보를 얻음 > location에 저장
click, ctrl+a, ctrl+c를 순서대로 진행 
text변수에 paste를 사용해 붙여넣음