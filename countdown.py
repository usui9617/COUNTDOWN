# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import datetime
import sys


def main():
    pygame.init()                                   # Pygameの初期化



    screen = pygame.display.set_mode((1800, 600))    # 大きさ600*500の画面を生成
    pygame.display.set_caption("count")              # タイトルバーに表示する文字

    #--------------font読み込み
    font_path = "./font/DSEG7ModernMini-Bold.ttf"
    font = pygame.font.Font(font_path, 100)               # フォントの設定(25px)
    #--------------画像読み込み
    img = pygame.image.load("./img/waku.png")
    img1 =  pygame.image.load("./img/danger.png")
    img2 = pygame.image.load("./img/tvt.png")
    img3 = pygame.image.load("./img/bar.png")
    img4 = pygame.image.load("./img/hai.png")
    img5 = pygame.image.load("./img/active.png")
    img6 = pygame.image.load("./img/racing.png")
    img7 = pygame.image.load("./img/type.png")
    img = pygame.transform.scale(img, (1750, 400))
    img3 = pygame.transform.scale(img3, (1750, 50))



    while (1):
        screen.fill((0,0,0))                                    # 画面を黒色に塗りつぶし
        x = 30
        y = 400

        #--------------残り時間表示
        dt = datetime.datetime(2021,1,24)-datetime.datetime.now()

        day = font.render(str(dt.days), True, (214,164,0))
        h = font.render(str(int(dt.seconds/3600)), True, (214,164,0))
        m = font.render(str(int(dt.seconds%3600/60)), True, (214,164,0))
        s = font.render(str(int(dt.seconds%60)), True, (214,164,0))
        ms = font.render(str(int(dt.microseconds)), True, (214,164,0))
        screen.blit(day, [x+0, y])# 残り日数の表示位置
        screen.blit(h, [x+300, y])# 残り時間の表示位置
        screen.blit(m, [x+600, y])# 残り分の表示位置
        screen.blit(s, [x+900, y])# 残り秒の表示位置
        screen.blit(ms, [x+1200, y])# 残りマイクロ秒の表示位置
        
        #--------------画像表示
        screen.blit(img1, (1310, 210))

        if int(dt.microseconds)%2 == 0: #点滅
            pygame.draw.rect(screen, (0,0,0), (1330,210,430,180))

        screen.blit(img2, (20, 10))
        screen.blit(img4, (0, 200))
        screen.blit(img3, (400, 35))
        screen.blit(img, (20, 200))
        screen.blit(img7, (30, 210))
        screen.blit(img5, (20, 100))
        screen.blit(img6, (1070, 220))
        pygame.display.update()     # 画面を更新

        #--------------イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了

                pygame.quit()       # Pygameの終了(画面閉じられる)
                sys.exit()
                
            if event.type == KEYDOWN:  # キーを押したとき
                # ESCキーならスクリプトを終了
                if event.key == K_ESCAPE: 
    
                    pygame.quit()       # Pygameの終了(画面閉じられる)
                    sys.exit()       


if __name__ == "__main__":
    main()