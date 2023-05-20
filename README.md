# ToSfenpack-add  
  
## ソフトについて  
【ソフト名】　　　ToSfenpack-add  
【バージョン】　　Ver.20230520  
【著作権者】　　　末吉 竜介  
【種　別】　　　　フリーソフトウェア  
【ソースコードのライセンス】　　MIT Licence  
【連絡先】　　　　[末吉のTwitter](https://twitter.com/16shiki168)  
【配布元ページ】　https://github.com/sueyoshiryosuke/ToSfenpack-add  
【動作確認環境】　Windows11  
【同梱、使用ソフト】  
　Python　　　　　https://www.python.org/  
　やねうら王　　　https://github.com/yaneurao/YaneuraOu  
　7-Zip 　　　　　https://sevenzip.osdn.jp/  
【参考ソフト、サイト】  
　floodgate 　　　http://wdoor.c.u-tokyo.ac.jp/shogi/floodgate.html  
　ShogiGUI　　　　http://shogigui.siganus.com/  
　Electron将棋　　https://sunfish-shogi.github.io/electron-shogi/  
  
―――――――――――――――――――――――――――――――――――――  
## 著作権および免責事項  
  
　本ソフトはフリーソフトです。個人／団体／社内利用を問わず、ご自由にお使い  
下さい。  
　なお，著作権は上の【著作権者】に記載している者が保有しています。  
  
　このソフトウェアを使用したことによって生じたすべての障害・損害・不具合等に  
関しては、著作権者と著作権者の関係者および著作権者の所属するいかなる  
団体・組織とも、一切の責任を負いません。各自の責任においてご使用ください。  
  
## はじめに  
　　このソフトは、たややんさんが作成されたToSfenpackに機能を追加したものです。  
　floodgateの評価値入りのcsaファイル、  ShogiGUIで作成した評価値入りkifファイル、  
　Electron将棋のコメント入りkifファイルを、やねうら王教師局面形式（.binファイル）に  
　変換するプログラムです。  
　Windows11 を搭載したパソコンで動作します。  
  
## ファイル構成  
　0-run-CSAtoSFENPACK.bat  
　　→floodgateの評価値入りのcsaファイルを変換したいときに実行してください。  
　1-run-KIFtoSFENPACK.bat  
　　→ShogiGUIで作成した評価値入りkifファイルを変換したいときに実行してください。  
　2-run-KIFtoSFENPACK2.bat  
　　→Electron将棋のコメント入りkifファイルを変換したいときに実行してください。  
　3-make-sfen-bin.bat  
　　→やねうら王教師局面形式に変換するときに必要ですが特に実行する必要はありません。  
　README.md  
　　→この説明ファイルです。  
　ToSfenpack-Readme.txt  
　　→たややんさんが作成されたToSfenpackオリジナルのreadmeファイルです。  
　LICENSE  
　　→このソフトのライセンスの内容が書かれています。  
　csaフォルダ  
　　→floodgateの評価値入りのcsaファイルを入れる用のフォルダです。  
　kifフォルダ  
　　→ShogiGUIで作成した評価値入りkifファイルや、  
　　　Electron将棋のコメント入りkifファイルを入れる用のフォルダです。  
　　　★注意★ShogiGUIで作成したkifと、Electron将棋で作成したkifを混ぜないで  
　　　　　　　別々に処理をしてください。  
　python311フォルダ  
　　→Python3.11の実行環境です。詳細は「python311-readme.txt」に記しています。  
　YO761フォルダ  
　　→「やねうら王7.6.1」の教師局面を作成するプログラムとやねうら王7.6.1の  
　　　ソースコード、ドキュメント一式が入っています。  
　　　詳細は「YO761-readme.txt」に記しています。  
　KIFtoSFENPACK2.py  
　CSAtoSFENPACK.py  
　KIFtoSFENPACK.py  
　Board.py  
　　→それぞれ、たややんさんが作成されたToSfenpackのソースコードです。  
　　　この一式の実行環境に合わせて、ソースコードを若干変更しています。  
　　　ソースコードについての詳細は「ToSfenpack-Readme.txt」に記しています。  
　license-org.txt  
　　→ToSfenpackの各ソースコードについての扱いについて  
　　　たややんさんのコメントを記しています。  
  
## ダウンロード方法  
　[Releases](https://github.com/sueyoshiryosuke/ToSfenpack-add/releases/tag/Ver.20230516)から  
　ダウンロードできます。  
  
## インストール方法  
　「ToSfenpack-add.exe」を実行し展開しすると  
　「ToSfenpack-add」フォルダが作成されます。  
  
## アンインストール方法  
  フォルダごと削除してください。  
  
## 使用方法  
　目的に応じて「csa」や「kif」フォルダに棋譜ファイルを入れて  
　「0-run-CSAtoSFENPACK.bat」、「1-run-KIFtoSFENPACK.bat：や  
　「2-run-KIFtoSFENPACK2.bat」 を実行してください。  
　やねうら王教師局面形式の「sfenpack.bin」が作成されます。  
  
## ライセンス  
　KIFtoSFENPACK2.pyはMIT licenseです。  
　　Copyright (c) 2023 Ryosuke Sueyoshi  
　　Released under the [MIT license](https://opensource.org/licenses/mit-license.php).  
    
## 謝辞  
　　やねうらおさん、たややんさん、siganusさん、Kubo Ryosukeさん  
　将棋AIを楽しめる環境や、将棋AI開発がしやすい環境を作っていただき  
　また、その結晶を利用させていただけることに感謝、感謝、感謝です。  
　　そして、本作品によって将棋AI開発の手助けに少しでもなれば幸いです。  
  
## 更新履歴  
　Ver.20230520　　2023/05/20  
　　「宣言勝ち（入玉勝ち）」の処理を追加。  
　　除外ファイル処理の改修。  
　Ver.20230516　　2023/05/16  
　　初版公開。  
  
--以上--  
