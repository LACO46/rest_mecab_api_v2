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

- 形態素解析したい文章を`<word>`に入力する

## MeCabで離礁する辞書の更新

### リクエスト

```
curl http://localhost:8080/v1/update/mecab-dict/
```

### 更新結果について

- 成功

```
{
  "message": "update mecab dict succeed"
}
```

- 失敗

```
{
  "message": "update mecab dict failed"
}
```