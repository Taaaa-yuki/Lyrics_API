# Lyrics API

<img src="https://img.shields.io/badge/Flask-v2.2.3-blue?logo=flask&logoColor=white"> <img src="https://img.shields.io/badge/Python-v3.11.3-blue?logo=python&logoColor=white"> <img src="https://img.shields.io/github/commit-activity/m/Taaaa-yuki/Lyrics_API?logo=github"> <img src="https://img.shields.io/github/repo-size/Taaaa-yuki/Lyrics_API?logo=github">

This is a Flask-based API for scraping lyrics from websites.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Taaaa-yuki/Lyrics_API
```

2. Change into the project directory:

```bash
cd Lyrics_API
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Set the FLASK_APP environment variable:

```bash
export FLASK_APP=src/app.py  
```

2. Start the server:

```bash
flask run
```

3. Get the URL of a song on uta-net.com and assign it to url:

```url
url=https://www.uta-net.com/song/335761/
```

4. Make a POST request to the /scrape endpoint with the url parameter set to the URL of the lyrics page you want to scrape:

```bash
curl -s -X POST -d "url=https://www.uta-net.com/song/335761/" http://127.0.0.1:5000/scrape | jq
```

1. The server will respond with a JSON object containing the scraped lyrics:

```json
{
    "artist": "YOASOBI",
    "body": "無敵の笑顔で荒らすメディア\n知りたいその秘密ミステリアス\n抜けてるとこさえ彼女のエリア\n完璧で嘘つきな君は\n天才的なアイドル様\n\n今日何食べた？\n好きな本は？\n遊びに行くならどこに行くの？\n何も食べてない\nそれは内緒\n何を聞かれても\nのらりくらり\n\nそう淡々と\nだけど燦々と\n見えそうで見えない秘密は蜜の味\nあれもないないない\nこれもないないない\n好きなタイプは？\n相手は？\nさあ答えて\n\n「誰かを好きになることなんて私分からなくてさ」\n嘘か本当か知り得ない\nそんな言葉にまた一人堕ちる\nまた好きにさせる\n\n誰もが目を奪われていく\n君は完璧で究極のアイドル\n金輪際現れない\n一番星の生まれ変わり\nその笑顔で愛してるで\n誰も彼も虜にしていく\nその瞳がその言葉が\n嘘でもそれは完全なアイ\n\nはいはいあの子は特別です\n我々はハナからおまけです\nお星様の引き立て役Bです\n全てがあの子のお陰なわけない\n洒落臭い\n妬み嫉妬なんてないわけがない\nこれはネタじゃない\nからこそ許せない\n完璧じゃない君じゃ許せない\n自分を許せない\n誰よりも強い君以外は認めない\n\n誰もが信じ崇めてる\nまさに最強で無敵のアイドル\n弱点なんて見当たらない\n一番星を宿している\n弱いとこなんて見せちゃダメダメ\n知りたくないとこは見せずに\n唯一無二じゃなくちゃイヤイヤ\nそれこそ本物のアイ\n\n得意の笑顔で沸かすメディア\n隠しきるこの秘密だけは\n愛してるって嘘で積むキャリア\nこれこそ私なりの愛だ\n流れる汗も綺麗なアクア\nルビーを隠したこの瞼\n歌い踊り舞う私はマリア\nそう嘘はとびきりの愛だ\n\n誰かに愛されたことも\n誰かのこと愛したこともない\nそんな私の嘘がいつか本当になること\n信じてる\n\nいつかきっと全部手に入れる\n私はそう欲張りなアイドル\n等身大でみんなのこと\nちゃんと愛したいから\n今日も嘘をつくの\nこの言葉がいつか本当になる日を願って\nそれでもまだ\n君と君にだけは言えずにいたけど\nやっと言えた\nこれは絶対嘘じゃない\n愛してる",
    "title": "アイドル"
}
```
