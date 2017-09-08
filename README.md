### ml_hack_insta

### Installation
```
git init
git clone https://github.com/nakarin0528/ml_hack_insta.git
cd ml_hack_insta
```

### ルール
- 基本的にブランチを切って、pushしてプルリクを送り、大丈夫そうだったらmasterブランチにマージ！
1.カレントブランチをコピーしたブランチを生成して、切り替える。
```
git checkout -b [新しいブランチ名]
```

2.pushしたいとき
```
git add [変更したファイル]
git commit -m "[コメント]"
git push origin [今いるブランチ名]
```

3.サイト上でプルリクエストを送る

- できる限り新しいバージョンのmasterからブランチを切って作業しよう！
リモートのブランチの方が新しい時
```
git pull
```

- 何か問題があった時やタスクがある時はissueにあげる
