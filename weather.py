import requests
from flask import Flask, url_for
import json
import bs4

app = Flask(__name__)

@app.route("/<location>")
def get_url(location):
	url = 'https://search.naver.com/search.naver?query=날씨 ' + location
	r = requests.get(url).text
	soup = bs4.BeautifulSoup(r, 'html.parser')
	cel = soup.select('.info_temperature .todaytemp')[0].get_text()
	status = soup.select('.info_data .info_list')[0].get_text().split(',')[0]


	json_object = {
		"celsius": cel,
		"status": status
	}

	json_string = json.dumps(json_object)
	return json_string
	#return '현재 ' + location + ' 날씨는 ' + soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text + '도 입니다.'


if __name__ == "__main__":
	app.run(host="0.0.0.0", port = "1234")

