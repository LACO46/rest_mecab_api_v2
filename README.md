# REST MeCab API

## dockerコンテナのビルド方法

```
docker build -t rest_mecab_api .
```

## 起動コマンド

```
docker run -it -p 8080:80  -v /<絶対PATH>/rest_mecab_api_v2:/home rest_mecab_api
```

## MeCabを利用した形態素解析

### リクエスト

```
curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"word":"<word>"}'  http://localhost:8080/v1/morphological-analysis/
```

- 形態素解析の内容を`<word>`に入力する