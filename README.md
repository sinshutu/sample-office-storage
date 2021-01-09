# sample-office-storage

## Setup
サーバーの起動

```
$ docker-compose build --no-cache --pull
$ docker-compose up
```

動作させている環境にOffice Wordが入っているのであれば http://localhost:5000/ にアクセス、「編集」のリンクをクリックするとリポジトリ内の `tmp/sample.docx` に配置してあるファイルが開きます

動作環境とは別にwordがある、動作だけ他の人に見せたいのであれば [ngrok](https://www.npmjs.com/package/ngrok) を利用することをおすすめします
