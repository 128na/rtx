# road and texture extension pack

道路と半透過の路面舗装アドオンのセット

# 導入

リリースページからダウンロードしてください。
https://github.com/128na/rtx/releases

# 開発者向け

事前にpython(3.12以上)を導入してください。
```
git clone --recursive https://github.com/128na/rtx.git

npm run setup
```

[simutrans-image-merger.exe](https://github.com/128na/simutrans-image-merger/releases/tag/latest)をダウンロードしてこのディレクトリに設置

```
npm run build
```


## info

### dat生成
jinjaテンプレート(.j2)を使用しています。

### 画像生成
テクスチャからタイル画像生成を [Road Tile Generator](https://github.com/128na/rtg)、タイル切り出しには [
simutrans-image-marger](https://github.com/128na/simutrans-image-merger) を使用しています。
