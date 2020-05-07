# REST MeCab API

## dockerコンテナのビルド方法

```
docker build -t rest_mecab_api .
```

## 起動コマンド

```
docker run -it -p 8080:80  -v /<絶対PATH>/rest_mecab_api_v2:/home rest_mecab_api
```