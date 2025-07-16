import asyncio
import pygame
import time
import random
import os
import pymysql
import PIL.Image
from pygame.locals import *

def loadPng(name):
    return pygame.image.load('images/'+name+'.png')
os.environ["SDL_IME_SHOW_UI"] = "1"  # 显示输入候选框 0是False 1是True
DBHOST = 'qsq.cool'
DBPORT = '3306'
DBUSER = 'qsqiwanna'
DBPASS = 'qsqiwanna'
DBNAME = 'qsq-iwanna-rank'

RankName = []
RankDieTime = []
RankTime = []
Paiming = []
Rankt = 0

bg_color = [255, 255, 255]
RankColor = [218, 165, 32]
BLACK = (0, 0, 0)
text_color = [0, 155, 0]
BLUE = (0, 0, 128)
canvas=pygame.display.set_mode((1080, 720))

png_man=loadPng('man')
png_man_l1=loadPng('manl1')
png_man_r1=loadPng('manr1')
png_man_l2=loadPng('manl2')
png_man_r2=loadPng('manr2')
png_fire=loadPng('fire')
png_grass=loadPng('grass')
png_ground=loadPng('ground')
png_mud=loadPng('mud')
png_sky=loadPng('sky')
png_flag=loadPng('flag')
png_falsefire=loadPng('falsefire')
png_ci1=loadPng('ci1')
png_ci2=loadPng('ci2')
png_ci3=loadPng("ci3")
png_ci4=loadPng('ci4')
png_lfk=loadPng('lfk')
png_gameover=loadPng('gameover')
png_quit=loadPng('quit')
png_kokomi=loadPng('kokomi')
png_nahida=loadPng('nahida')
png_ganyu=loadPng('ganyu')
png_furina=loadPng('furina')
png_win=loadPng('win')
png_winlo=loadPng('winlo')
png_start=loadPng('start')
png_instruction=loadPng('instruction')
png_iwanna=loadPng('iwanna')
png_iwanna.set_alpha(64)
png_pause=loadPng('pause')
png_login=loadPng('login')
png_rankwin=loadPng('rank_win')
png_ranknowin=loadPng('rank_nowin')
png_rankerror=loadPng('NetConnectError')
png_button_no=loadPng('button_no')
png_button_yes=loadPng('button_yes')
png_csm=loadPng('csm')
png_csmh=loadPng('csmh')
png_pea=loadPng('pea')
png_level1=loadPng('l1')
png_level2=loadPng('l2')
png_wd0=loadPng('wd/wdss0')
png_wd1=loadPng('wd/wdss1')
png_wd2=loadPng('wd/wdss2')
png_wd3=loadPng('wd/wdss3')
png_wd4=loadPng('wd/wdss4')
png_wd5=loadPng('wd/wdss5')
png_wd6=loadPng('wd/wdss6')
png_wd7=loadPng('wd/wdss7')
png_wd8=loadPng('wd/wdss8')
png_wd9=loadPng('wd/wdss9')
png_wd10=loadPng('wd/wdss10')
png_wd11=loadPng('wd/wdss11')
png_wd12=loadPng('wd/wdss12')



dietime=0
playtime=0
readytime=0
levelonetime=0
jump = 1
vyall=-15 #-15
havepause = 0
pausetime = 0
s_1 = 0
s_2 = 0
s_3 = 0
s_4 = 0 #会触发nahida
s_5 = 0 #触发lfk标志位
s_6 = 0 #2选1成功标志位
s_7 = 0
s_8 = 0
s_9 = 0
s_10 = 0
s_11 = 0
s_12 = 0
s_13 = 0
s_14 = 0
s_15 = 0
p_0 = 0
p_1 = 0
p_1 = 0
p_2 = 0
p_3 = 0
p_4 = 0
p_5 = 0
p_6 = 0
p_7 = 0
p_8 = 0
p_9 = 0
p_10 = 0
p_11 = 0
p_12 = 0
p_13 = 0
p_14 = 0
p_15 = 0
p_16 = 0
p_17 = 0
p_18 = 0
p_19 = 0
p_20 = 0
p_21 = 0
p_22 = 0
p_23 = 0
p_24 = 0
p_25 = 0
p_26 = 0
p_27 = 0
p_28 = 0
p_29 = 0
p_30 = 0
p_31 = 0
p_32 = 0
p_33 = 0
p_34 = 0
p_35 = 0
p_36 = 0
p_37 = 0
p_38 = 0
p_39 = 0
rnd1 = 0
twd = 0 #开始吐豌豆
newpea = 0
havewin=''
haveins = 0
playshua = 0
move117118119dir = 0
text = ""
UserName = ""
playtimeL2 = 0
L2Time = pygame.time.Clock() #第二关计时器  #playtime已经弃用

async def setup():
    pygame.display.set_caption("QSQ's iwanna  v7.1")
    Icon = PIL.Image.open("images/icon.ico")
    Icon = Icon.tobytes(), Icon.size, Icon.mode
    pygame.display.set_icon(pygame.image.frombytes(*Icon))
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.init()
    canvas.fill(bg_color)
    PlayBGM()
    await asyncio.sleep(0)

async def login():
    global text,UserName,havewin
    with open("user/state.dll", "r") as rst:  # 打开文件
        havewin=rst.read()
    ok = 1
    with open("user/local.dll", "r") as rex:  # 打开文件
        userexist=rex.read()
    if userexist=='1':
        ok=0
        with open("user/UserName.dll", "r") as rnm:  # 打开文件
            username = rnm.read()
        UserName=username
    else:
        font = pygame.font.Font('fonts/font.ttf', 60)
        pos = pygame.mouse.get_pos()
        pygame.key.start_text_input()  # 打开输入模式（默认就是打开的
        # pygame.key.stop_text_input() # 关闭

        while (ok):
            pygame.key.set_text_input_rect((500, 500, 0, 0))  # 输入法框框的位置
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.constants.USEREVENT:
                    PlayBGM()
                elif event.type == KEYDOWN:
                    if event.key == K_BACKSPACE:
                        text = text[:-1]  # 如果是backspace就删除一个字
                    if event.key == K_RETURN:
                        UserName = text
                        with open("user/UserName.dll", "w") as wun:
                            wun.write(UserName)
                        with open("user/local.dll", "w") as wun:
                            wun.write('1')
                        ok = 0
                if event.type == TEXTINPUT:  # 如果是输入文字,就加入到字符串内显示
                    text += event.text

            text_image = font.render(text, True, (0, 0, 0))
            canvas.blit(png_login, (0, 0))
            canvas.blit(text_image, (350, 540))
            pygame.display.update()
            await asyncio.sleep(0)

class Person:
    def __init__(self):
        self.x=20
        self.y=700
        self.fallstate=0
        self.jumpstate=0
        self.vy=vyall
        self.gravity=1
        self.onjump=0
        self.isstand=0
        self.die=0
        self.iswin=0
        self.dietime=0
        self.dir=0
        self.printx=0
        self.nodie=0
        self.iswinLO=0
    def reset(self):
        self.x = 20
        self.y = 700
        self.fallstate = 0
        self.jumpstate = 0
        self.vy = vyall
        self.gravity = 1
        self.onjump = 0
        self.isstand = 0
        self.die = 0
        self.iswin=0
        self.dir = 0
        self.printx = 0
    def Chuansong1(self):
        self.x = 600
        self.y = 640
    def Chuansong2(self):
        self.x = 40
        self.y = 40
    def checkground(self):
        standon=0
        for fl in floors:
            if (self.x+13)>fl.getx() and self.x<(fl.getx()+20) and self.y<=fl.gety()+20 and self.y > fl.gety()-20 and self.isstand==0:
                standon=1
                self.isstand=1
                self.y=fl.gety()-19
        if standon==1:
            self.stand()
        else:
            self.fall()

    def checkbutton(self):
            for btn in buttons:
                if (self.x + 13) > btn.x and self.x < (btn.x + 20) and self.y <= btn.y + 20 and self.y > btn.y - 20 and btn.active==1:
                    btn.push()

    def checkdie(self):
        isdie=0
        if self.x<1 or self.x>1080 or self.y>720 or self.y < -200:
            isdie=1
        if ((self.x + 13 >= Ganyu.x and self.x <= Ganyu.x+115 and self.y <= Ganyu.y+60 and self.y + 20 >= Ganyu.y) and Ganyu.life ==1 and Ganyu.stop == 1) or ((self.x + 13 >= Furina.x+5 and self.x <= Furina.x+120 and self.y <= Furina.y+60 and self.y + 20 >= Furina.y) and Furina.life == 1 and Furina.stop == 1):
            isdie=1
        for fl in fires:
            if (self.x+13)>fl.getx() and self.x<(fl.getx()+20) and self.y<=fl.gety()+20 and self.y > fl.gety()-20 and self.isstand==0:
                isdie=1
        for ci in cis:
            if (self.x+13)>ci.x and self.x<(ci.x+20) and self.y<=ci.y+20 and self.y > ci.y-20 and ci.life==1:
                isdie=1
        for ps in peas:
            if (((ps.x+12)-(self.x+6))*((ps.x+12)-(self.x+6))+((ps.y+12)-(self.y+10))*((ps.y+12)-(self.y+10)))<144:
                isdie=1
        if isdie==1 and self.nodie == 0:
            self.persondie()


    def checkwin(self):
        if self.x>50 and self.x<90 and self.y>30 and self.y<70:
            self.iswin=1
        if self.x>320 and self.x<380 and self.y>340 and self.y<360:
            self.iswinLO=1
    def print(self):
        if self.isstand==0:
            self.y+=self.vy
            self.vy+=self.gravity
        if self.dir == 0:
            canvas.blit(png_man,(self.x,self.y))
        elif self.dir == 1:
            if self.printx<6:
                canvas.blit(png_man_l1, (self.x, self.y))
                self.printx += 1
            else:
                canvas.blit(png_man_l2, (self.x, self.y))
                self.printx += 1
            if self.printx > 11:
                self.printx = 0
        elif self.dir==2:
            if self.printx<6:
                canvas.blit(png_man_r1, (self.x, self.y))
                self.printx += 1
            else:
                canvas.blit(png_man_r2, (self.x, self.y))
                self.printx += 1
            if self.printx > 11:
                self.printx = 0
        person.dir = 0
    def moveL(self):
        self.x-=2
        self.dir=1
    def moveR(self):
        self.x+=2
        self.dir=2
    def persondie(self):
        self.die=1
        self.dietime+=1
        with open("user/dt.dll", "w") as wun:
            wun.write('{}'.format(self.dietime))
    def stand(self):
        self.isstand=1
        self.jumpstate=0
        self.gravity=0
        self.vy=0
    def fall(self):
        self.gravity=1
        self.isstand=0
    def jump(self):

        self.isstand=0
        if self.jumpstate==0:
            jp = pygame.mixer.Sound("./snd/jump.mp3")
            jp.set_volume(0.1)
            jp.play()
            self.gravity=1
            self.vy=vyall
            self.jumpstate+=1
        elif self.jumpstate==1:
            jp = pygame.mixer.Sound("./snd/jump.mp3")
            jp.set_volume(0.1)
            jp.play()
            self.gravity = 1
            self.vy = vyall+3
            self.jumpstate += 1
        else:
            self.gravity=1


class Floor:
    def __init__(self,x,y,type):
        self.x=x
        self.y=y
        self.type=type
    def print(self):
        if self.type==0:
            canvas.blit(png_ground,(self.x,self.y))
        elif self.type==1:
            canvas.blit(png_grass, (self.x, self.y))
        elif self.type==2:
            canvas.blit(png_sky, (self.x, self.y))
        elif self.type==3:
            canvas.blit(png_mud, (self.x, self.y))
    def getx(self):
        return self.x
    def gety(self):
        return self.y
    def moveU(self):
        self.y -= 1.5
    def moveD(self):
        self.y += 1.5
    def moveL(self):
        self.x -= 1.5
    def moveR(self):
        self.x += 1.5

class Fire:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def print(self):
        canvas.blit(png_fire,(self.x,self.y))
    def getx(self):
        return self.x
    def gety(self):
        return self.y

class Button:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.state=0
        self.active=0
        self.playover=0
    def push(self):
        if self.playover==0:
            pop = pygame.mixer.Sound("./snd/btn.mp3")
            pop.set_volume(1)
            pop.play()
            self.playover=1
        self.state=1
    def act(self):
        self.active=1
    def print(self):
        if self.active==1:
            if self.state==1:
                canvas.blit(png_button_yes,(self.x,self.y))
            else:
                canvas.blit(png_button_no, (self.x, self.y))
class Ci:
    def __init__(self,x,y,dir):
        self.x=x
        self.y=y
        self.life=0
        self.dir=dir
    def print(self):
        if self.life==1:
            if self.dir==1:
                canvas.blit(png_ci1, (self.x, self.y))
            elif self.dir==2:
                canvas.blit(png_ci2, (self.x, self.y))
            elif self.dir==3:
                canvas.blit(png_ci3, (self.x, self.y))
            elif self.dir==4:
                canvas.blit(png_ci4, (self.x, self.y))
    def moveup(self):
        if self.dir==1:
            self.y-=7
        elif self.dir==2:
            self.x+=7
        elif self.dir==3:
            self.y+=7
        elif self.dir==4:
            self.x-=7

    def cidie(self):
        self.life=0
    def active(self):
        self.life=1

class pea:
    def __init__(self,tr):
        self.x = 90
        self.y = 630
        self.tr = tr
    def move(self):
        self.x+=6
        if self.tr == 1:
            self.y = 0.00087542*self.x*self.x-0.87542*self.x+702
        elif self.tr == 2:
            self.y = 0.00199223*self.x*self.x-2.5662186*self.x+844.82258
        elif self.tr == 3:
            self.y = 0.0029449*self.x*self.x-2.9449*self.x+871.190781
    def print(self):
        canvas.blit(png_pea,(self.x,self.y))
class wdss:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.printx=0
        self.v = 0.1
        self.tr = 1
    def print(self):
        if self.printx <= 0:
            canvas.blit(png_wd0,(self.x,self.y))
            self.printx += self.v
        elif self.printx <= 1:
            canvas.blit(png_wd1,(self.x,self.y))
            self.printx += self.v
        elif self.printx <= 2:
            canvas.blit(png_wd2,(self.x,self.y))
            self.printx += self.v
        elif self.printx <= 3:
            canvas.blit(png_wd3,(self.x,self.y))
            self.printx += self.v
        elif self.printx <= 4:
            canvas.blit(png_wd4,(self.x,self.y))
            self.printx += self.v
        elif self.printx <= 5:
            canvas.blit(png_wd5,(self.x,self.y))
            self.printx += self.v
        elif self.printx <= 6:
            canvas.blit(png_wd6,(self.x,self.y))
            self.printx += self.v
        elif self.printx <= 7:
            canvas.blit(png_wd7,(self.x,self.y))
            self.printx += self.v
        elif self.printx <= 8:
            canvas.blit(png_wd8,(self.x,self.y))
            self.printx += self.v
        elif self.printx <= 9:
            canvas.blit(png_wd9,(self.x,self.y))
            self.printx += self.v
        elif self.printx <= 10:
            canvas.blit(png_wd10,(self.x,self.y))
            self.printx += self.v
        elif self.printx <= 11:
            canvas.blit(png_wd11,(self.x,self.y))
            self.printx += self.v
        elif self.printx <= 12:
            canvas.blit(png_wd12,(self.x,self.y))
            self.printx += self.v
            if self.printx>=11.8:
                self.printx = -1

WDSS=wdss(30,640)
class move_furina:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.life = 0
        self.v = 1
        self.stop = 0
        self.play = 0
        self.wait = 0
    def print(self):
        if self.life==1:
            canvas.blit(png_furina,(self.x,self.y))
    def move(self):
        if self.life == 1:
            self.wait += 0.1
            if self.wait > 15:
                self.y -= 0.3
            if self.x <= 400:
                self.x = 380
                self.stop=1
            else:
                self.x -= self.v
                self.v += 1
        if self.x<1080:
            if self.play == 0:
                fnn = pygame.mixer.Sound("./snd/fnn.mp3")
                fnn.set_volume(1)
                fnn.play()
                self.play = 1
        if self.y<0:
            person.persondie()

    def active(self):
        self.life=1
    def die(self):
        self.life=0
class move_ganyu:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.life=0
        self.v=1
        self.stop=0
        self.play=0
        self.wait=0
    def print(self):
        if self.life == 1:
            canvas.blit(png_ganyu,(self.x,self.y))
    def die(self):
        self.life = 0
    def move(self):
        if self.life==1:
            self.wait += 0.1
            if self.wait > 32:
                self.y -= 0.5
            if self.x >= 200:
                self.x = 240
                self.stop=1
            else:
                self.x += self.v
                self.v += 1
        if self.y<0:
            person.persondie()
    def active(self):
        self.life=1
        if self.play==0:
            gy = pygame.mixer.Sound("./snd/gy.mp3")
            gy.set_volume(1)
            gy.play()
            self.play=1
Ganyu=move_ganyu(-120,340)
Furina=move_furina(2080,340)
winlo = 1

def PrintMapOnLevelOne():
    createCi(60, 420, 2)
    createCi(160, 420, 2)
    createCi(260, 420, 2)
    createCi(360, 320, 2)
    createCi(460, 220, 2)
    cis[0].active()
    cis[1].active()
    cis[2].active()
    cis[3].active()
    cis[4].active()
    createFloor(20, 700, 1)
    createFloor(40, 700, 1)
    createFloor(60, 700, 1)

    createFloor(100, 640, 1)
    createFloor(120, 640, 1)
    createFloor(160, 640, 1)
    createFloor(180, 640, 1)

    createFloor(220, 560, 1)
    createFloor(240, 560, 1)
    createFloor(260, 560, 1)
    createFloor(300, 560, 1)

    createFloor(320, 400, 1)
    createFloor(340, 400, 1)
    createFloor(360, 400, 1)
    createFloor(380, 400, 1)
async def LevelOne():
    global winlo,levelonetime

    PrintMapOnLevelOne()
    LOtime = pygame.time.Clock()
    LOtime.tick()

    while winlo:
        canvas.fill(bg_color)
        person.checkground()
        person.checkdie()
        person.checkwin()
        pygame.time.Clock().tick(60)
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.constants.USEREVENT:
            PlayBGM()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            Pause()
        if keys[pygame.K_i]:
            await Instruction()
        if keys[pygame.K_n]:
            PlayBGM()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            person.moveL()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            person.moveR()
        if keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            if jump:
                person.jump()
            jump = 0
        else:
            jump = 1
        PrintFloorOne()
        person.print()
        OnGameMapOnLevelOne()
        EndGameOnLevelOne()
        WinOnLevelOne()
        pygame.display.flip()
    levelonetime = LOtime.tick()
    PrepareForLevelTwo()

def PrepareForLevelTwo():
    floors.clear()
    cis.clear()
    person.x = 20
    person.y = 700
    person.vy = -15
def OnGameMapOnLevelOne():
    for ci in cis:
        if (ci.x > 580):
            ci.dir = 1
            ci.x = 580
        if (ci.y < 80):
            ci.dir = 4
            ci.y = 80
        if (ci.x < 40):
            ci.x = 40
            ci.dir = 3
        if (ci.y > 580):
            ci.dir = 2
            ci.y = 540

def printmap():
    global p_0
    if p_0==0:
        #testfloor



        #/testfloor


        createButton(140, 680)  # bt0
        createButton(340, 680)  # bt1
        createButton(220, 580)  # bt2
        createButton(120, 300)  # bt3
        createButton(80, 300)  # bt4
        createButton(20, 300)  # bt5
        createButton(120, 180)  # bt6
        createButton(20, 180)  # bt7




        createButton(400, 480)  # bt8
        createButton(330, 480)  # bt9
        createButton(260, 480)  # bt10
        createButton(440, 540)  # bt11  #底下一行最右边的按钮

        createButton(620, 680)  # bt12

        createButton(480, 500)  # bt13

        createButton(295, 480)  # bt14

        createButton(360, 380)  # bt15 #按下出现急停陷阱
        createButton(480, 300)  # bt16 #芙宁娜上1层
        createButton(240, 260)  # bt17 甘雨上1层
        createButton(480, 220)  # bt18 芙宁娜上2层
        createButton(240, 180)  # bt19 甘雨上2层
        createButton(480, 140)  # bt20 芙宁娜上3层
        createButton(240, 100)  # bt21 甘雨上3层
        createButton(480, 60)   # bt22 芙宁娜上4层
        createButton(580, 500)   # bt23
        createButton(740, 680)  # bt24 按钮上升
        createButton(640, 500)  #bt 25 弹跳按钮
        createButton(1040, 80) #bt26
        createButton(860, 80)  #bt27
        createButton(1060, 680) #bt28
        createButton(640, 680)  #bt29
        # test button

        #/test button

        createFloor(0, 700, 0)
        createFloor(40, 700, 0)
        createFloor(60, 700, 0)
        createFloor(80, 700, 0)
        createFloor(100, 700, 0)
        createFloor(120, 700, 0)
        createFloor(140, 700, 1)

        createFloor(340, 700, 1)
        createFloor(360, 700, 0)
        createFloor(380, 700, 0)
        createFloor(420, 700, 0)
        createFloor(440, 700, 0)
        createFloor(460, 700, 0)
        createFloor(480, 700, 1)

        createCi(100, 710, 1)
        createCi(360, 710, 1)

        createCi(-220, 420, 2)
        createCi(-200, 440, 2)
        createCi(-180, 460, 2)
        createCi(-160, 480, 2) #ci5

        createCi(160, 500, 1) #ci6


        createCi(240, -40, 3)   # ci7
        createCi(260, 220, 3)
        createCi(280, 200, 3)
        createCi(300, 180, 3)
        createCi(320, 20, 3)
        createCi(340, 0, 3)
        createCi(360, 120, 3)
        createCi(380, 100, 3)
        createCi(400, 80, 3)
        createCi(420, 60, 3)   #ci16
        createCi(240, -240, 3)   #ci17
        createCi(260, -260, 3)
        createCi(280, -280, 3)
        createCi(300, -300, 3)
        createCi(320, -320, 3)
        createCi(340, -340, 3)
        createCi(360, -360, 3)
        createCi(380, -380, 3)
        createCi(400, -400, 3)
        createCi(420, -420, 3)   #ci26

        createCi(1080, 480, 4) #ci27
        createCi(1080, 520, 4)
        createCi(1080, 560, 4)
        createCi(1080, 600, 4)
        createCi(1080, 640, 4)
        createCi(1080, 680, 4)
        createCi(1080, 720, 4)
        createCi(20, 500, 2)
        createCi(20, 540, 2)
        createCi(20, 580, 2)
        createCi(20, 620, 2)
        createCi(20, 660, 2)
        createCi(20, 700, 2) #ci39



        createCi(715, -2600, 3)  # ci40
        createCi(765, -2620, 3)
        createCi(765, -2000, 3)
        createCi(740, -2020, 3)
        createCi(715, -1500, 3)
        createCi(740, -1520, 3)
        createCi(740, -1000, 3)
        createCi(715, -700, 3)
        createCi(765, -700, 3)
        createCi(740, -380, 3)
        createCi(715, -360, 3)
        createCi(740, -50, 3)
        createCi(765, -30, 3)   # ci52

        createCi(1280, 20, 4) #ci53
        createCi(0, 20, 2)  # ci54


        createCi(380, 260, 2) #ci55
        createCi(400, 280, 2)
        createCi(380, 300, 2)
        createCi(400, 320, 2)
        createCi(380, 340, 2)
        createCi(400, 360, 2)
        createCi(380, 380, 2)
        createCi(400, 400, 2)
        createCi(380, 420, 2)
        createCi(400, 440, 2)
        createCi(380, 460, 2)
        createCi(400, 480, 2) #ci66
        p_0=1


floors=[]
def createFloor(x,y,type):
    floors.append(Floor(x,y,type))

fires=[]
def createFire(x,y):
    fires.append(Fire(x,y))

cis=[]
def createCi(x,y,dir):
    cis.append(Ci(x,y,dir))
buttons=[]
def createButton(x,y):
    buttons.append(Button(x,y))
person=Person()


peas=[]
def createPea():
    peas.append(pea(WDSS.tr))
    pua = pygame.mixer.Sound("./snd/pua.mp3")
    pua.set_volume(1)
    pua.play()
def Pea():
    WDSS.print()
    global newpea
    newpea+=1
    if newpea%100==0 and newpea!=0:
        createPea()
    for ps in peas:
        ps.move()
        ps.print()

def cimove():
    for ci in cis:
        if ci.life==1:
            ci.moveup()
def PrintFloor():
    canvas.blit(png_flag, (60, 40))
    canvas.blit(png_iwanna,(244,200))
    for fl in floors:
        fl.print()
    for fr in fires:
        fr.print()
    cimove()

    for ci in cis:
        ci.print()
    for btn in buttons:
        btn.print()
    Ganyu.move()
    Ganyu.print()
    Furina.move()
    Furina.print()
def PrintFloorOne():
    canvas.blit(png_flag, (340, 340))
    canvas.blit(png_iwanna,(244,200))
    for fl in floors:
        fl.print()
    cimove()
    for ci in cis:
        ci.print()
def OnGameMap():
    global rnd1,twd,playshua,move117118119dir
    global s_1,s_2,s_3,s_4,s_5,s_6,s_7,s_8,s_9
    global p_0, p_1, p_2, p_3, p_4, p_5, p_6, p_7, p_8, p_9, p_10, p_11, p_12, p_13, p_14, p_15, p_16, p_17, p_18 ,p_19,p_20,p_21,p_22,p_23,p_24,p_25,p_26,p_27,p_28,p_29,p_30 ,p_31,p_32,p_33,p_34,p_35,p_36,p_37,p_38,p_39
    buttons[0].act()
    if s_6==0 and person.x>90 and person.x<120:
        shua = pygame.mixer.Sound("./snd/shua.mp3")
        shua.set_volume(1)
        shua.play()
        cis[0].active()
        s_6=1
    if p_1==0 and buttons[0].state==1:
        createFloor(200, 600, 1)
        createFloor(220, 600, 1)
        buttons[1].act()
        p_1=1
    if s_7==0 and person.x>350 and person.x<380 and person.y>680:
        shua = pygame.mixer.Sound("./snd/shua.mp3")
        shua.set_volume(1)
        shua.play()
        cis[1].active()
        s_7 =1
    if p_2==0 and person.x > 350  and person.y < 660:
        createFire(400,600 )
        p_2=1
    if p_3==0 and person.x>460 :
        createFire(500, 700)
        createFire(500, 680)
        createFire(500, 660)
        createFire(500, 640)
        createFire(500, 620)
        createFire(500, 600)
        createFire(500, 580)
        createFire(500, 560)
        createFire(500, 540)
        buttons[2].act()
        s_1 = 1
        p_3 = 1
    if p_4==0 and buttons[1].state==1:
        createFloor(580, 700, 1)
        createFloor(600, 700, 0)
        createFloor(620, 700, 0)
        createFloor(640, 700, 1)
        p_4=1
    if s_1==1 and p_5==0 and buttons[2].state==1:
        createFloor(20, 500, 1)
        createFloor(40, 500, 0)
        createFloor(60, 500, 0)
        createFloor(80, 500, 0)
        createFloor(100, 500, 0)
        createFloor(120, 500, 1)
        p_5=1
    if p_6==0 and person.x>20 and person.x<140 and person.y < 500 and person.y>300 and s_1 == 1:
        shua = pygame.mixer.Sound("./snd/shua.mp3")
        shua.set_volume(1)
        shua.play()
        cis[2].active()
        cis[3].active()
        cis[4].active()
        cis[5].active()
        p_6=1
    if cis[5].x>0 and p_7==0:
        createFire(20, 460)
        createFire(20, 440)
        createFire(20, 420)
        createFire(20, 400)
        createFire(20, 380)
        createFire(20, 360)
        createFire(20, 340)
        createFloor(20, 320, 1)
        createFire(120, 460)
        createFire(120, 440)
        createFire(120, 420)
        createFire(120, 400)
        createFire(120, 380)
        createFire(120, 360)
        createFire(120, 340)
        createFloor(120, 320, 1)
        buttons[3].act()
        createFloor(140, 500, 1)
        createFloor(160, 500, 1)
        createFloor(180, 500, 1)
        s_3=1 #已经触发二层伸出的方块
        p_7=1
        s_2=1
        s_3=1
        s_4=1 #会触发nahida
    if cis[5].x>0 :   #打印假的红色方块
        canvas.blit(png_grass, (120, 480))
        canvas.blit(png_grass, (20, 480))
    if s_4 ==1 and person.y<340 and person.y > 280 and person.x>20 and person.x<120:
        pygame.mixer.music.load("./snd/nxd.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
        canvas.blit(png_nahida, (20, 280))
        pygame.display.flip()
        person.persondie()
        time.sleep(2)

    if p_8==0 and buttons[3].state==1:
        s_4=0
        buttons[4].act()
        buttons[5].act()
        rnd1= 0 #弃用随机算法 实在是太恶心了 ！！！！           random.randint(0,99999)%2 #随机算法 rnd1
        #print(rnd1)
        p_8=1
    if rnd1==0 and p_9==0: #rnd1是0的话，按下4号按钮死
        if buttons[4].state==1:
            s_5=1
            p_9=1
        if buttons[5].state==1:
            s_6=1
            p_9 = 1
    elif rnd1==1 and p_9==0:
        if buttons[4].state==1:
            s_6=1
            p_9 = 1
        if buttons[5].state==1:
            s_5=1
            p_9 = 1
    if s_3 == 1 and person.x > 160 and person.x < 180 and person.y > 480 and person.y < 500:
        cis[6].active()
    if p_10==0 and s_3 == 1 and person.x > 130 and person.x < 160 and person.y > 400 and person.y < 420:
        createFloor(140, 320, 1)
        createFloor(100, 320, 1)
        createFloor(80, 320, 1)
        createFloor(60, 320, 1)
        createFloor(40, 320, 1)
        p_10=1
    if p_10 == 0 and s_3 == 1 and person.x > 130 and person.x < 160 and person.y > 200 and person.y < 220:
        createFloor(140, 160, 1)
        s_4=0 #不会触发nahida
    if s_5==1:  #踩错了
        rndsndlfk=random.randint(0,99999)%2
        if rndsndlfk==1:
            pygame.mixer.music.load("./snd/ysjx.mp3")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.load("./snd/zrg.mp3")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
        canvas.blit(png_lfk,(20,240))
        pygame.display.flip()
        person.persondie()
        time.sleep(3)
    if s_6==1 and p_11 == 0 and buttons[4].state==1 and buttons[5].state==1:
        createFloor(100, 200, 1)
        createFloor(120, 200, 1)
        createFire(100, 220)
        createFire(120, 220)
        createFire(20, 220)
        createFire(40, 220)

        createFire(20, 120)
        createFire(40, 120)
        createFire(60, 120)
        createFire(80, 120)
        createFire(100, 120)
        createFire(120, 120)
        buttons[6].act()
        buttons[7].act()

        p_11=1
    if p_11==1: #绘制2边的其中一边假地面
        canvas.blit(png_grass, (20, 200))
        canvas.blit(png_grass, (40, 200))
    if p_12==0 and buttons[6].state==1:
        createFloor(260, 500, 1)
        createFloor(280, 500, 0)
        createFloor(300, 500, 0)
        createFloor(320, 500, 0)
        createFloor(340, 500, 0)
        createFloor(360, 500, 0)
        createFloor(380, 500, 0)
        createFloor(400, 500, 1)
        createFire(260, 520)
        createFire(280, 520)
        createFire(300, 520)
        createFire(320, 520)
        createFire(340, 520)
        createFire(360, 520)
        createFire(380, 520)
        createFire(400, 520)
        buttons[9].act() #左侧中间按1出2按钮
        p_12=1
    if p_13==0 and buttons[9].state==1:
        twd=1
        buttons[8].act()
        buttons[10].act()
        cis[8].active()
        cis[9].active()
        cis[10].active()
        cis[11].active()
        cis[12].active()
        cis[13].active()
        cis[14].active()
        cis[15].active()
        cis[16].active()
        cis[17].active()
        cis[18].active()
        cis[19].active()
        cis[20].active()
        cis[21].active()
        cis[22].active()
        cis[23].active()
        cis[24].active()
        cis[25].active()
        huala = pygame.mixer.Sound("./snd/ding.mp3")
        huala.set_volume(1)
        huala.play()
        p_13=1
    if twd==1:
        Pea()
    if p_14==0 and buttons[10].state==1:
        boom = pygame.mixer.Sound("./snd/boom.mp3")
        boom.set_volume(1)
        boom.play()
        createFloor(240, 560, 1)
        createFloor(260, 560, 1)
        createFloor(280, 560, 1)
        createFloor(300, 560, 1)
        createFloor(320, 560, 1)
        createFloor(340, 560, 1)
        createFloor(360, 560, 1)
        createFloor(380, 560, 1)
        createFloor(400, 560, 1)
        createFloor(420, 560, 1)
        createFloor(440, 560, 1)
        buttons[11].act()
        cis[16].cidie()
        cis[17].cidie()
        cis[18].cidie()
        cis[19].cidie()
        cis[20].cidie()
        cis[21].cidie()
        cis[22].cidie()
        cis[23].cidie()
        cis[24].cidie()
        cis[25].cidie()

        p_14=1

    if buttons[8].state==1:
        pygame.mixer.music.load("./snd/kokomi.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
        canvas.blit(png_kokomi, (360, 440))  #绘制kokomi
        pygame.display.flip()

        person.persondie()
        time.sleep(2)
    if p_15==0 and buttons[11].state==1:
        createFloor(480, 520, 1)
        buttons[12].act()
        p_15=1
    if p_15==1:
        canvas.blit(png_grass, (500, 520))  # 打印红色上面的假的绿色块
        canvas.blit(png_grass, (520, 520))
    if p_16==0 and buttons[12].state==1:
        shua = pygame.mixer.Sound("./snd/shua.mp3")
        shua.set_volume(1)
        shua.play()
        cis[31].active()
        cis[27].active()
        cis[28].active()
        cis[29].active()
        cis[30].active()
        cis[31].active()
        cis[32].active()
        cis[33].active()
        cis[34].active()
        cis[35].active()
        cis[36].active()
        cis[37].active()
        cis[38].active()
        cis[39].active()
        createFloor(580, 520, 1)
        buttons[13].act()
        p_16=1
    if p_16==1:
       canvas.blit(png_grass, (620, 520))
       canvas.blit(png_grass, (600, 520))
       canvas.blit(png_grass, (640, 520))
    if buttons[13].state==1:
        buttons[14].act()
    if p_17==0 and buttons[14].state==1:
        createFloor(340, 400, 1)
        createFloor(360, 400, 1)
        createFloor(380, 400, 1)
        buttons[15].act()
        p_17=1
    if p_18==0 and buttons[15].state == 1:
        createFloor(240, 400, 1)
        createFloor(260, 400, 1)
        createFloor(280, 400, 1)
        createFloor(300, 400, 1)
        createFloor(320, 400, 1)
        createFloor(340, 400, 1)
        createFloor(360, 400, 1)
        createFloor(380, 400, 1)
        createFloor(400, 400, 1)
        createFloor(420, 400, 1)
        createFloor(440, 400, 1)
        createFloor(460, 400, 1)
        createFloor(480, 400, 1)
        Furina.active()
        Ganyu.active()
        WDSS.tr = 2
        p_18=1
    if p_19==0 and Furina.wait>6:
        createFloor(380, 320, 1)
        createFloor(400, 320, 1)
        createFloor(420, 320, 1)
        createFloor(440, 320, 1)
        createFloor(460, 320, 1)
        createFloor(480, 320, 1)
        buttons[16].act()
        p_19 = 1
    if p_20 == 0 and buttons[16].state==1:  #甘雨上2层
        createFloor(240, 280, 1)
        createFloor(260, 280, 1)
        createFloor(280, 280, 1)
        createFloor(300, 280, 1)
        createFloor(320, 280, 1)
        createFloor(340, 280, 1)
        buttons[17].act()
        p_20 = 1
    if p_21 == 0 and buttons[17].state==1: #芙芙上1层
        createFloor(380, 240, 1)
        createFloor(400, 240, 1)
        createFloor(420, 240, 1)
        createFloor(440, 240, 1)
        createFloor(460, 240, 1)
        createFloor(480, 240, 1)
        buttons[18].act()
        p_21 = 1
    if p_22 == 0 and buttons[18].state==1:#甘雨上2层
        createFloor(240, 200, 1)
        createFloor(260, 200, 1)
        createFloor(280, 200, 1)
        createFloor(300, 200, 1)
        createFloor(320, 200, 1)
        createFloor(340, 200, 1)
        buttons[19].act()
        p_22 = 1
    if p_23 == 0 and buttons[19].state==1:
        createFloor(380, 160, 1)
        createFloor(400, 160, 1)
        createFloor(420, 160, 1)
        createFloor(440, 160, 1)
        createFloor(460, 160, 1)
        createFloor(480, 160, 1)
        buttons[20].act()
        p_23 = 1
    if p_24 == 0 and buttons[20].state==1: #芙宁娜上3层

        createFloor(240, 120, 1)
        createFloor(260, 120, 1)
        createFloor(280, 120, 1)
        createFloor(300, 120, 1)
        createFloor(320, 120, 1)
        createFloor(340, 120, 1)
        buttons[21].act()
        p_24 = 1
    if p_25 == 0 and buttons[21].state==1:
        Furina.die()
        createFloor(380, 80, 1)
        createFloor(400, 80, 1)
        createFloor(420, 80, 1)
        createFloor(440, 80, 1)
        createFloor(460, 80, 1)
        createFloor(480, 80, 1)
        createFire(140, 0)
        createFire(140, 20)
        createFire(140, 40)
        createFire(140, 60)
        createFire(140, 80)
        createFire(140, 100)
        createFire(140, 120)
        buttons[22].act()
        p_25 = 1
    if p_26 == 0 and buttons[22].state==1:
        Ganyu.die()
        buttons[23].act()
    if p_27 == 0 and buttons[23].state==1:
        WDSS.tr = 3
        createFloor(720 ,700, 2)  # FL118
        createFloor(740, 700, 2)  # FL119
        createFloor(760, 700, 2)  # FL120
        buttons[24].act()
        p_27=1
    if buttons[24].state==1 and floors[117].y>30:
        floors[117].moveU()
        floors[118].moveU()
        floors[119].moveU()
        cis[40].active()
        cis[41].active()
        cis[42].active()
        cis[43].active()
        cis[44].active()
        cis[45].active()
        cis[46].active()
        cis[47].active()
        cis[48].active()
        cis[49].active()
        cis[50].active()
        cis[51].active()
        cis[52].active()
        buttons[24].active=0
        playshua=1
    if playshua==1:
        shua = pygame.mixer.Sound("./snd/shua.mp3")
        shua.set_volume(1)
        shua.play()
        playshua=0
    if p_28 == 0 and buttons[24].state==1 and floors[117].y<=30:
        shua = pygame.mixer.Sound("./snd/shua.mp3")
        shua.set_volume(1)
        shua.play()
        createFire(180, 60)
        createFire(200, 60)
        createFire(220, 60)
        createFire(240, 60)
        createFire(260, 60)
        createFire(280, 60)
        createFire(300, 60)
        createFire(320, 60)
        createFire(340, 60)
        createFire(360, 60)
        createFire(380, 60)
        createFire(400, 60)
        createFire(420, 60)
        createFire(440, 60)
        createFire(460, 60)
        createFire(480, 60)
        createFire(500, 60)
        createFire(520, 60)
        createFire(540, 60)
        createFire(560, 60)
        createFire(580, 60)
        createFire(600, 60)
        createFire(620, 60)
        createFire(640, 60)
        createFire(660, 60)
        createFire(680, 60)
        createFire(700, 60)
        createFire(720, 60)
        createFire(740, 60)
        createFire(760, 60)
        createFire(780, 60)
        createFire(780, 80)
        cis[53].active()
        cis[54].active()
        p_28 = 1


    if p_28 == 1:
        canvas.blit(png_csm, (120, 0))
        canvas.blit(png_csm, (540, 600))
    if p_28 == 1 and s_8 == 0:
        floors[117].moveL()
        floors[118].moveL()
        floors[119].moveL()
    if p_28 == 1 and person.x >120 and person.x<160 and person.y<120 and person.y > 0:
        person.Chuansong1()
        buttons[25].act()

    if p_39 == 0 and p_28 == 1 and floors[117].x<=140:
        buttons[25].act()
        createFloor(600, 520, 1)
        createFloor(620, 520, 1)
        createFloor(640, 520, 1)
        p_39 = 1
        s_8 = 1
    if buttons[25].state==1:
        person.y -= 10
        person.vy=-20
        buttons[25].state = 0
        buttons[25].playover = 0
        s_9=1
    if p_29 == 0 and s_9 == 1:
        createFloor(60, 200, 2)
        createFloor(80, 200, 2)
        createFloor(100, 200, 2)
        createFloor(1020, 100, 1)
        createFloor(1040, 100, 1)
        createFloor(1060, 100, 1)
        buttons[26].act()
        p_29 = 1
    if p_29 == 1 and p_30 == 0:
        if floors[125].x > 1140:
            floors[123].x = -60
            floors[124].x = -40
            floors[125].x = -20
        else:
            floors[123].moveR()
            floors[124].moveR()
            floors[125].moveR()
    if p_30 == 0 and buttons[26].state == 1:
        createFloor(800, 100, 2)
        createFloor(820, 100, 2)
        createFloor(840, 100, 2)
        createFloor(860, 100, 2)
        createFloor(880, 100, 2)
        createFloor(900, 100, 2)
        createFloor(920, 100, 2)

        buttons[27].act()
        p_30 = 1
    if p_31 == 0 and buttons[27].state == 1:
        buttons[27].active=0
        createFire(780, 80)
        createFire(780, 100)
        createFire(780, 120)
        createFire(780, 140)
        createFire(780, 160)
        createFire(780, 180)
        createFire(780, 200)
        createFire(780, 220)
        createFire(780, 240)
        createFire(780, 260)
        createFire(780, 280)
        createFire(780, 300)
        createFire(780, 320)
        createFire(780, 340)
        createFire(780, 360)
        createFire(780, 380)
        createFire(780, 400)
        createFire(780, 420)
        createFire(780, 440)
        createFire(780, 460)
        createFire(780, 480)
        createFire(780, 500)
        createFire(780, 520)
        createFire(780, 540)
        createFire(780, 560)
        createFire(780, 580)
        createFire(780, 600)
        createFire(780, 620)
        createFire(780, 640)
        createFire(780, 660)
        createFire(780, 680)
        createFire(780, 700)
        createFire(940, 80)
        createFire(940, 100)
        createFire(940, 120)
        createFire(940, 140)
        createFire(940, 160)
        createFire(940, 180)
        createFire(940, 200)
        createFire(940, 220)
        createFire(940, 240)
        createFire(940, 260)
        createFire(940, 280)
        createFire(940, 300)
        createFire(940, 320)
        createFire(940, 340)
        createFire(940, 360)
        createFire(940, 380)
        createFire(940, 400)
        createFire(940, 420)
        createFire(940, 440)
        createFire(940, 460)
        createFire(940, 480)
        createFire(940, 500)
        createFire(940, 520)
        createFire(940, 540)
        createFire(940, 560)
        createFire(940, 580)
        createFire(940, 600)
        createFire(940, 620)
        createFire(940, 640)




        createFire(800, 140)
        createFire(820, 140)
        createFire(880, 140)



        createFire(840, 240)
        createFire(860, 240)
        createFire(880, 240)
        createFire(900, 240)

        createFire(940, 340)
        createFire(920, 340)

        createFire(840, 340)
        createFire(820, 340)

        createFire(900, 440)
        createFire(880, 440)
        createFire(820, 440)
        createFire(800, 440)
        createFire(780, 440)


        createFire(840, 540)
        createFire(860, 540)
        createFire(900, 540)
        createFire(920, 540)

        createFire(820, 640)
        createFire(840, 640)

        createFire(900, 640)
        createFire(920, 640)

        p_31 = 1
        p_32 = 1
    if p_31 == 1:
        if floors[129].y >= 700:
            floors[129].y = 700
            floors[130].y = 700
            floors[131].y = 700
            floors[132].y = 700
            floors[133].y = 700
            floors[134].y = 700
            floors[135].y = 700
        else:
            floors[129].moveD()
            floors[130].moveD()
            floors[131].moveD()
            floors[132].moveD()
            floors[133].moveD()
            floors[134].moveD()
            floors[135].moveD()
    if p_32 == 1:
        floors[123].x=1020
        floors[124].x=1040
        floors[125].x=1060
        floors[123].moveD()
        floors[124].moveD()
        floors[125].moveD()
        if floors[123].y >=700:
            createFloor(1000, 700, 1)
            createFloor(980, 700, 1)
            createFloor(960, 700, 1)
            createFloor(940, 700, 1)
            createFloor(960, 40, 1)
            createFloor(980, 60, 1)
            createFloor(1000, 80, 1)
            p_32 = 0
            buttons[28].act()
    if p_33 == 0 and buttons[28].state==1:
        createFire(1040, 260)
        createFire(1060, 340)
        createFire(1020, 340)
        createFire(1040, 440)
        createFire(1060, 460)
        createFire(1040, 560)
        createFire(1020, 580)
        createFire(1040, 640)
        createFire(1020, 660)
        p_33 = 1
        buttons[28].active = 0
    if p_33 == 1:
        floors[123].moveU()
        floors[124].moveU()
        floors[125].moveU()
        if floors[123].y < -40 and p_34 == 0:
            buttons[26].state = 0
            WDSS.tr = 2
            p_34 = 1
    if p_34 == 1 and buttons[26].state == 1:
        p_35 = 1
        buttons[29].act()
    if p_35 == 1:
        if floors[117].x > 920:
            floors[117].x = 920
            floors[118].x = 940
            floors[119].x = 960
            if move117118119dir == 0:
                move117118119dir = 1
            elif move117118119dir == 1:
                move117118119dir = 0
        elif floors[117].x < 160:
            floors[117].x = 160
            floors[118].x = 180
            floors[119].x = 200
            if move117118119dir == 0:
                move117118119dir = 1
            elif move117118119dir == 1:
                move117118119dir = 0
        if move117118119dir == 0:
            floors[117].moveR()
            floors[118].moveR()
            floors[119].moveR()
        elif move117118119dir == 1:
            floors[117].moveL()
            floors[118].moveL()
            floors[119].moveL()
    if buttons[29].state == 1:
        canvas.blit(png_csmh,(580,200))
        canvas.blit(png_csmh,(0,100))
        cis[55].active()
        cis[56].active()
        cis[57].active()
        cis[58].active()
        cis[59].active()
        cis[60].active()
        cis[61].active()
        cis[62].active()
        cis[63].active()
        cis[64].active()
        cis[65].active()
        cis[66].active()
        for i in range(55,67):
            if i == 66:
                shua = pygame.mixer.Sound("./snd/shua.mp3")
                shua.set_volume(1)
                shua.play()
            if cis[i].x>800:
                cis[i].x-=420
        WDSS.tr = 1
        p_36 = 1
    if p_36 == 1 and p_37 == 0:
        createFloor(0, 100, 1)
        createFloor(20, 100, 1)
        createFloor(40, 100, 1)
        createFloor(60, 100, 1)
        createFloor(80, 100, 1)
        createFloor(100, 100, 1)
        createFloor(120, 100, 1)
        p_37 = 1
    if p_36 == 1:
        if person.x>580 and person.x <700 and person.y<260:
            person.Chuansong2()

async def StartPage():
    global haveins
    pygame.display.set_caption("QSQ's iwanna  v7.1     用户名: " + UserName)
    press_m=0
    with open("user/dt.dll", "r") as rdt:  # 打开文件
        person.dietime = eval(rdt.read())

    while 1:
        canvas.blit(png_start, (0, 0))
        pygame.display.flip()
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.constants.USEREVENT:
            PlayBGM()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if haveins == 0:
                await Instruction()
                haveins = 1
            break
        elif keys[pygame.K_SPACE]:
            Rank()
        elif keys[pygame.K_u]:
            person.nodie=1
            pygame.display.set_caption("QSQ's iwanna  v7.1 无敌版    用户名: " + UserName)
        elif keys[pygame.K_m]:
            press_m=1
        if press_m:
            NewUser()
            await login()
            await StartPage()
            break
    await asyncio.sleep(0)

async def Instruction():
    canvas.blit(png_instruction, (0, 0))
    pygame.display.flip()
    exitIns = 1
    while exitIns:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.constants.USEREVENT:
            PlayBGM()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            exitIns = 0


def NewUser():
    with open("user/local.dll", "w") as rs:
        rs.write('')
    with open("user/UserName.dll", "w") as rs:
        rs.write('')
    with open("user/dt.dll", "w") as rs:
        rs.write('0')
    with open("user/state.dll", "w") as rst:
        rst.write('0')


def RankError():
    canvas.blit(png_rankerror,(0,0))
    pygame.display.flip()
    next=1
    while(next):
        pygame.event.poll()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            next=0


def Pause():
    exitpause = 1
    global pausetime,havepause
    ptime = pygame.time.Clock()
    ptime.tick()
    global playtime
    PrintDieTime()
    while exitpause:
        canvas.blit(png_pause, (0, 0))
        pygame.display.flip()
        pygame.time.wait(10)
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.constants.USEREVENT:
            PlayBGM()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            exitpause = 0
            havepause = 1
            pausetime += ptime.tick()


def PlayBGM():
    pygame.mixer.init()
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    rndsnd = random.randint(0, 999999999)%22
    if rndsnd == 0:
        pygame.mixer.music.load("./snd/bgm0.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
    elif rndsnd == 1:
        pygame.mixer.music.load("./snd/bgm1.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
    elif rndsnd == 2:
        pygame.mixer.music.load("./snd/bgm2.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
    elif rndsnd == 3:
        pygame.mixer.music.load("./snd/bgm3.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
    elif rndsnd == 4:
        pygame.mixer.music.load("./snd/bgm4.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
    elif rndsnd == 5:
        pygame.mixer.music.load("./snd/bgm5.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
    elif rndsnd == 6:
        pygame.mixer.music.load("./snd/bgm6.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
    elif rndsnd == 7:
        pygame.mixer.music.load("./snd/bgm7.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
    elif rndsnd == 8:
        pygame.mixer.music.load("./snd/bgm8.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
    elif rndsnd == 9:
        pygame.mixer.music.load("./snd/bgm9.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
    elif rndsnd == 10:
        pygame.mixer.music.load("./snd/bgm10.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
    elif rndsnd == 11:
        pygame.mixer.music.load("./snd/bgm11.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
    elif rndsnd == 12:
        pygame.mixer.music.load("./snd/bgm12.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
    elif rndsnd == 13:
        pygame.mixer.music.load("./snd/bgm13.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
    elif rndsnd == 14:
        pygame.mixer.music.load("./snd/bgm14.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
    elif rndsnd == 15:
        pygame.mixer.music.load("./snd/bgm15.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
    elif rndsnd == 16:
        pygame.mixer.music.load("./snd/bgm16.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
    elif rndsnd == 17:
        pygame.mixer.music.load("./snd/bgm17.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
    elif rndsnd == 18:
        pygame.mixer.music.load("./snd/bgm18.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
    elif rndsnd == 19:
        pygame.mixer.music.load("./snd/bgm19.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
    elif rndsnd == 20:
        pygame.mixer.music.load("./snd/bgm20.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
    elif rndsnd == 21:
        pygame.mixer.music.load("./snd/bgm21.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()

def ResetLO():
    person.die=0
    person.x = 20
    person.y = 700
    person.vy=-15
    levelonetime = 0
def Reset():
    floors.clear()
    fires.clear()
    cis.clear()
    buttons.clear()
    person.reset()
    peas.clear()
    PlayBGM()
    global readytime,pausetime,playtimeL2,L2Time
    global rnd1,twd,newpea,playshua,move117118119dir
    global s_1, s_2, s_3, s_4, s_5, s_6, s_7, s_8, s_9, s_10, s_11, s_12, s_13, s_14, s_15
    global p_0, p_1, p_2, p_3, p_4, p_5, p_6, p_7, p_8, p_9, p_10, p_11, p_12, p_13, p_14, p_15, p_16, p_17, p_18, p_19,p_20,p_21,p_22,p_23,p_24,p_25,p_26,p_27,p_28,p_29,p_30,p_31,p_32,p_33,p_34,p_35,p_36,p_37,p_38,p_39
    global Ganyu,Furina
    Ganyu = move_ganyu(-120, 340)
    Furina = move_furina(2080, 340)

    s_1 = 0
    s_2 = 0
    s_3 = 0
    s_4 = 0  # 会触发nahida
    s_5 = 0  # 触发lfk标志位
    s_6 = 0  # 2选1成功标志位
    s_7 = 0
    s_8 = 0
    s_9 = 0
    s_10 = 0
    s_11 = 0
    s_12 = 0
    s_13 = 0
    s_14 = 0
    s_15 = 0
    p_0 = 0
    p_1 = 0
    p_1 = 0
    p_2 = 0
    p_3 = 0
    p_4 = 0
    p_5 = 0
    p_6 = 0
    p_7 = 0
    p_8 = 0
    p_9 = 0
    p_10 = 0
    p_11 = 0
    p_12 = 0
    p_13 = 0
    p_14 = 0
    p_15 = 0
    p_16 = 0
    p_17 = 0
    p_18 = 0
    p_19 = 0
    p_20 = 0
    p_21 = 0
    p_22 = 0
    p_23 = 0
    p_24 = 0
    p_25 = 0
    p_26 = 0
    p_27 = 0
    p_28 = 0
    p_29 = 0
    p_30 = 0
    p_31 = 0
    p_32 = 0
    p_33 = 0
    p_34 = 0
    p_35 = 0
    p_36 = 0
    p_37 = 0
    p_38 = 0
    p_39 = 0
    rnd1 = 0
    twd = 0
    newpea = 0
    playshua = 0
    WDSS.tr = 1
    move117118119dir = 0
    readytime=pygame.time.get_ticks()
    playtimeL2 = 0
    pausetime = 0
    printmap()
    L2Time.tick()


def Win():
    if person.iswin==1:
        pygame.mixer.music.load("./snd/win.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
        time.sleep(2)
        canvas.blit(png_win, (0, 0))
        pygame.display.flip()
        if havewin=='0':
            UpLoadGrade()
        with open("user/state.dll", "w") as rs:
            rs.write('1')
        while 1:
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.constants.USEREVENT:
                PlayBGM()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                Rank()
                pygame.quit()
                exit()

def WinOnLevelOne():
    global winlo
    if person.iswinLO==1:
        pygame.mixer.music.load("./snd/win.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
        time.sleep(2)
        canvas.blit(png_winlo, (0, 0))
        pygame.display.flip()
        while 1:
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.constants.USEREVENT:
                PlayBGM()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                winlo=0
                break

def  EndGame():
    if person.die==1:
        PrintDieTime()
        pygame.mixer.music.load("./snd/cai.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
        canvas.blit(png_gameover, (0, 0))
        pygame.display.flip()
        time.sleep(2.5)
        while 1:
            pygame.event.poll()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                QuitGame()
            elif keys[pygame.K_r] or keys[pygame.K_SPACE]:
                Reset()
                break

def  EndGameOnLevelOne():
    if person.die==1:
        pygame.mixer.music.load("./snd/cai.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
        canvas.blit(png_gameover, (0, 0))
        pygame.display.flip()
        time.sleep(2.5)
        while 1:
            pygame.event.poll()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                QuitGame()
            elif keys[pygame.K_r] or keys[pygame.K_SPACE]:
                ResetLO()
                break

def QuitGame():
    if havewin=='0':
        canvas.blit(png_quit,(0,0))
        pygame.display.flip()
        pygame.mixer.music.load("./snd/sbq.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
        time.sleep(3)
    Rank()
    pygame.quit()
    exit()

async def ShowLevel(level):
    if level==1:
        canvas.blit(png_level1,(0,0))
        pygame.display.flip()
        time.sleep(2)
    elif level==2:
        canvas.blit(png_level2, (0, 0))
        pygame.display.flip()
        time.sleep(2)
    await asyncio.sleep(0)
def PrintDieTime():
    global pausetime,playtimeL2
    fontObj = pygame.font.Font('fonts/numfont.ttf', 24)
    textSurfaceObj = fontObj.render('Die: {}'.format(person.dietime), True, text_color, None)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (1020, 20)
    counttime_text = fontObj.render(str((playtimeL2-pausetime)/1000)+'s', True, (0, 0, 0))
    canvas.blit(counttime_text, (2, 2))
    canvas.blit(textSurfaceObj,textRectObj)
def UpLoadGrade():
    try:
        db = pymysql.connect(host=DBHOST, user=DBUSER, password=DBPASS, db=DBNAME)
        cur = db.cursor()
        sql_del = 'delete from timerank where UserName=%s'
        sql_ins = 'INSERT INTO timerank(UserName,Time,DieTime) VALUE(%s,%s,%s)'
        value = (UserName, '{}'.format((playtimeL2-pausetime)/1000), '{}'.format(person.dietime))
        cur.execute(sql_del, UserName)
        cur.execute(sql_ins, value)
        db.commit()
        db.close()
    except pymysql.Error:
        RankError()




def Rank():
    rankfont = pygame.font.Font('fonts/font.ttf', 40)
    global Rankt,havewin
    with open("user/state.dll", "r") as rst:  # 打开文件
        havewin=rst.read()
    try:
        RankName.clear()
        RankDieTime.clear()
        RankTime.clear()
        Rankt = 0
        db = pymysql.connect(host=DBHOST, user=DBUSER, password=DBPASS, db=DBNAME)
        cur = db.cursor()
        sql_find = "SELECT * FROM timerank ORDER BY dietime ASC,time ASC"
        cur.execute(sql_find)
        db.commit()
        RankResult = cur.fetchall()
        for RankData in RankResult:
            Paiming.append(rankfont.render('{}'.format(Rankt + 1), True, RankColor, None))
            RankName.append(rankfont.render(RankData[0], True, RankColor, None))
            RankDieTime.append(rankfont.render('{}'.format(RankData[2]), True, RankColor, None))
            RankTime.append(rankfont.render('{} s'.format(RankData[1]), True, RankColor, None))
            Rankt += 1
    except pymysql.Error as e:
        RankError()
    Printt=0
    if havewin=='1':
        canvas.blit(png_rankwin, (0, 0))
    else:
        canvas.blit(png_ranknowin, (0, 0))

    while(Printt<Rankt and Printt<10):
        canvas.blit(Paiming[Printt], (90, 160 + Printt * 45))
        canvas.blit(RankName[Printt],(270,160+Printt * 45))
        canvas.blit(RankDieTime[Printt], (590, 160 + Printt * 45))
        canvas.blit(RankTime[Printt], (855, 160 + Printt * 45))
        Printt +=1
        pygame.display.flip()
    pygame.display.flip()
    exitrank=1
    while(exitrank):
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.constants.USEREVENT:
            PlayBGM()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            exitrank = 0
            break



def Time():
    global playtime,pausetime,havepause
    playtime = pygame.time.get_ticks() - readytime - pausetime - levelonetime - 8 #showleveltime

async def main():
    print("async")
    await setup()
    await login()
    await StartPage()
    readytime=pygame.time.get_ticks()
    await ShowLevel(1)
    await LevelOne()
    printmap()
    await ShowLevel(2)


    L2Time.tick()
    while 1:

        event = pygame.event.poll()
        canvas.fill(bg_color)
        #playtimeL2 += L2Time.tick()
        person.checkground()
        person.checkdie()
        person.checkwin()
        person.checkbutton()
        pygame.time.Clock().tick(60)


        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.constants.USEREVENT:
            PlayBGM()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            Pause()
        if keys[pygame.K_i]:
            await Instruction()
        if keys[pygame.K_n]:
            PlayBGM()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            person.moveL()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            person.moveR()
        if keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            if jump:
                person.jump()
            jump = 0
        else:
            jump = 1
        PrintFloor()
        person.print()
        EndGame()
        PrintDieTime()
        OnGameMap()

        Win()
        pygame.display.flip()

asyncio.run(main())