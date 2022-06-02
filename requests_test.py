from django import setup
import os
from bs4 import BeautifulSoup
import requests


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nurse_question.settings')
setup()
from question.models import Question


# 看護師の過去問URL
url = "https://kango.career-tasu.jp/contents/kokushi-kakomon/2018am_001-060/"

# requestsで取得
res = requests.get(url)
# HTML形式認識
soup = BeautifulSoup(res.text, "html.parser")

# 抽出、インサート処理
num = 1
for num in range(61):
    elems = soup.select("#q{0}".format(num))
    for elem in elems:
      options=elem.find_all("li")
      title=elem.find("dd", class_="mondai").text
      try:
        option1 = options[0].text
        option2 = options[1].text
        option3 = options[2].text
        option4 = options[3].text
      except:
        continue
      
      answer=elem.find("span", class_="num").text
      print(title)
      print(option1)
      print(option2)
      print(option3)
      print(option4)
      print(answer)
      q = Question(
      title=title,
      answer=answer,
      option1 = option1,
      option2 = option2,
      option3 = option3,
      option4 = option4
      )
      try:
        q.save()
      except:
        continue

print("done")