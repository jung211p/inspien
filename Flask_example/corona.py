import requests
from flask import Flask, url_for
import json
import bs4

app = Flask(__name__)

@app.route('/')
def get_url():
	url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=코로나"
	req = requests.get(url).text
	soup = bs4.BeautifulSoup(req, 'html.parser')
	num0 = soup.select(".info_01 .info_num")[0].text
	num1 = soup.select(".info_02 .info_num")[0].text
	num2 = soup.select(".info_03 .info_num")[0].text
	num3 = soup.select(".info_04 .info_num")[0].text

	json_object = {
	"confirmed cases" : num0,
	"under inspection" : num1,
	"quarantine release" : num2,
	"death" : num3
	}
	json_string = json.dumps(json_object)
	return json_string


if __name__ == "__main__":
	app.run(host="0.0.0.0", port = "1234")
