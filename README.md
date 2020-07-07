# REST MeCab API

## docker コンテナのビルド方法

```
docker-compose build
```

## 起動コマンド

```
docker-compose up
```

## MeCab を利用した形態素解析

### リクエスト

```
curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"word":"<word>"}'  http://localhost:8080/v1/morphological-analysis/
```

- 形態素解析したい文章を`<word>`に入力する

### 更新結果について

```
{
  "result": [
    {
      "hiragana": "すもも",
      "kana": "スモモ",
      "kanji": "李",
      "part_of_speech": {
        "one": "名詞",
        "three": "一般",
        "two": "普通名詞"
      }
    },
    ...
    {
      "hiragana": "うち",
      "kana": "ウチ",
      "kanji": "内",
      "part_of_speech": {
        "one": "名詞",
        "three": "副詞可能",
        "two": "普通名詞"
      }
    }
  ]
}

```

## MeCab で離礁する辞書の更新

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
