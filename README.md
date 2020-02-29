# AtCoder Virtual Ranking Calculator

バーチャル参加したときの結果をもとに、実際に参加していたら何位になっていたかを調べるスクリプト

## 使い方

json_fileは https://atcoder.jp/contests/<contest>/standings/json から取ってきます（要ログイン）。
scoreと時間はバーチャル参加の順位表から取ってきます。

```
atcoder-virtual-ranking.py [-h] json_file score minutes seconds
```

### Example

```
$ python atcoder-virtual-ranking.py abc129.json 1000 35 17
765
```

## 使いみち

出場していたらどのくらいのパフォーマンスになっていたのか調べるのに便利です。
