
## Step.0

### 0-1. dev branch の切り出し

- [方法１] サーバー側で「dev」のbranchを生成し、「dev」branchをcloneする。
    - web UI でbranchの追加
        - 左上の「main」のブランチの部分に「dev」を入力することで、branchを追加。
    - clone
        - ブランチを指定して、クローン
        ```bash
        git clone -b [branch name] [http://address]
        ```

- [方法2] ローカル側で「dev」のbranchを生成し、サーバー側に反映
    - clone
        ```bash
        git clone [http://address]
        ```

    - branchの確認
        ```bash
        git branch -a
        ```

    - branch 生成し、移動。
        - 方法１
            ```bash
            git checkout -b dev
            ```
        - 方法２
            ```bash
            git branch dev
            git checkout dev
            ```

### 0-2. commit A, B, C, D, E の実施
- commit & push
    - commit A, B, C, D, E, F
        - README.md を編集
        - コミット
            - コミット内容の確認
                - チェック
                    - コミットすべきファイルが含まれているか？
                    - 変更したファイルが意図通りか？
                ```bash
                git status
                ```
            - ファイル差分点の確認
                ```bash
                git diff
                ```
            - コミット内容にファイルを追加
                ```bash
                git add [filename] or [directory]
                ```
            - コミット
                ```bash
                git commit -m "Commit A"
                ```
        - プッシュ
            - CUIでローカルのコミットを確認
                - サーバーに反映されているコミット　　：origin/*
                - ローカルのみに反映されているコミット：それ以外
                ```bash
                git log
                ```                
            - GUIでローカルとサーバーのコミットを確認
                ```bash
                gitk
                ```
            - サーバーのorigin/devへ反映。
                - ブランチがなければ作成してくれる。
                ```bash
                git push origin dev
                ```

## Step.1　Cの状態と同じ状態のFをA,B,C,D,Eの後にコミットする。

- revert commit（元に戻す）
    - コミットIDの取得
        ```bash
        git log
        > commit 4733ac518f95b619334c266c6fec6ac575138fcc -> commit id
        ```
    - E, D の内容を戻した（変更した）状態にする。（-nのオプションでコミットはしない。）
        ```bash
        git revert -n [E の commit ID]
        git revert -n [D の commit ID]
        ```
    - 新しい状態のFとしてコミットし、サーバーへプッシュする。
        ```bash
        git add .
        git commit -m "E, D のコミットを戻した。"
        git push origin dev
        ```

- cherry-pick（過去のある状態にする。）
    - コミットIDの取得
        ```bash
        git log
        > commit 4733ac518f95b619334c266c6fec6ac575138fcc -> commit id
        ```
    - C の内容の状態にする。
        ```bash
        git cherry-pick [C の commit ID]
        ```
    - コンフリクトが発生した場合、Cの内容を採用
        ```bash
        git checkout --theirs .
        ```
    - 新しい状態のFとしてコミットし、サーバーへプッシュする。
        ```bash
        git add .
        git commit -m "[C の commit ID]の状態にした。"
        git push origin dev
        ```

- reset（過去のある状態に戻す）
    - コミットIDの取得
        ```bash
        git log
        > commit 4733ac518f95b619334c266c6fec6ac575138fcc -> commit id
        ```
    - A, B, C の状態にする。
        - "-f" のオプションで強制プッシュする必要がある。
        ```bash
        git reset --soft [Cの状態のcommit id]
        git push -f origin dev
        ```

## Step.2　python scriptにてstep1を自動化してください。

- subprocessを使って順番にコマンドを実行していく実装。

