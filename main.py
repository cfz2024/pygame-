import time

import pygame
import sys

class Setting():
    def __init__(self):
        self.screen_height=600
        self.screen_width=1000
        self.bg_color=(120,200,200)
        self.clock=200
        self.people_width=20
        self.people_height=20
        self.people_color=(200,0,0)
class Body():
    def __init__(self,setting,screen):
        self.width=setting.people_width
        self.height=setting.people_height
        self.screen=screen
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.screen_rect=screen.get_rect()
        self.rect.x=self.screen_rect.centerx
        self.rect.y=self.screen_rect.centery
        self.x_init=self.rect.x
        self.y_init=self.rect.y
        self.color=setting.people_color
    def run(self,bullet0,dir,man):
        check_events(bullet0,dir,man)
        if dir[0]=='w':
            self.rect.y-=1
        if dir[0]=='s':
            self.rect.y+=1
        if dir[0]=='a':
            self.rect.x-=1
        if dir[0]=='d':
            self.rect.x+=1
        if dir[0]=='p':
            pass
    def reborn(self):
        self.rect.x=self.x_init
        self.rect.y=self.y_init
def run_bullet(self):
    if self.dir == 'a':
        self.rect.x -= 1
    elif self.dir == 'd':
        self.rect.x += 1
    elif self.dir == 's':
        self.rect.y += 1
    elif self.dir == 'w':
        self.rect.y -= 1
    #print(self.dir)
bullet_num2=0
class Bullet():
    list=[]
    i=0
    num=0
    @classmethod
    def o_bullet(cls):
        for member in cls.list:

            run_bullet(member)
            show_bullet(member)
    def __init__(self):
        self.width=5
        self.height=5
        self.color=(200,0,0)
        self.num_shoot=[0,0,0,0]
        self.rect = pygame.Rect(0, 0, self.width, self.height)
    def keep_man(self,body):
        self.body = body
        self.rect.x = float(self.body.rect.x)
        self.rect.y = float(self.body.rect.y)
    def fire(self,dir):#必须在click中调用，必须在类创建后使用，创建的类必须在主循环里更新
        self.dir = dir[0]
        #print('space')
        Bullet().list.append(self)

    def fire2(self,dir):
        self.dir=dir[0]
class Monster():
    M_list=[]
    M_survival=[1,1,1,1]
    @classmethod
    def M_show(cls):
        i=0
        broken=0
        for sur in cls.M_survival:
            if sur==1:
                cls.M_list[i].catch(people)
                cls.M_list[i].screen.blit(cls.M_list[i].image,cls.M_list[i].rect)
            else:
                broken+=1
                if broken == 4:
                    for mem in cls.M_list:
                        mem.reborn()
                '''if cls.M_list[i].rect.x>cls.M_list[i].body.rect.x:
                    cls.M_list[i].rect.x+=1
                elif cls.M_list[i].rect.x<cls.M_list[i].body.rect.x:
                    cls.M_list[i].rect.x-=1
                if cls.M_list[i].rect.y>cls.M_list[i].body.rect.y:
                    cls.M_list[i].rect.y+=1
                elif cls.M_list[i].rect.y<cls.M_list[i].body.rect.y:
                    cls.M_list[i].rect.y-=1'''
            i+=1


    def __init__(self):
        self.image=pygame.image.load("img.png").convert()
        self.x=float(0)
        self.y=float(0)
        self.sur=1
        self.english_num=0
        self.english_num_shoot_count=0
    def get_enlish_num(self,show):
        self.english_num=show.english_num
    def add_init(self,x,y,body,screen):
        self.body=body
        self.screen=screen
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.x_init=x
        self.y_init=y
        self.left_up_x=x
        self.left_up_y=y
        self.right_down_x=x+50
        self.right_down_y=y+40
        self.x=x
        self.y=y
        Monster().M_list.append(self)
    def catch(self,man):
        if self.x < man.rect.x:
            self.x += 0.09
        else:
            self.x -= 0.09
        if self.y < man.rect.y:
            self.y += 0.09
        else:
            self.y -= 0.09
        self.rect.x = self.x
        self.rect.y = self.y
        self.left_up_x=self.x
        self.left_up_y=self.y
        self.right_down_x=self.x+50
        self.right_down_y=self.y+40
    def destroy(self,bullet,chinese_num):
        if (self.left_up_x<bullet.rect.x and self.left_up_y<bullet.rect.y and self.right_down_x>bullet.rect.x
                and self.right_down_y>bullet.rect.y):  #击中
            print("击中",bullet.num_shoot[1])
            bullet.num_shoot[2] = 0
            if chinese_num==self.english_num:   #正确击中
                show_chinese.shoot=2
                self.sur=0
                bullet.num_shoot[1]+=1
                show_chinese.shoot += 1
                show_chinese.right=1
                if bullet.num_shoot[1]==1 and bullet.num_shoot[3]==0:
                    time.sleep(0.0001)
                    vocabular_refreash(chinese_num,show_chinese.right)
                    print("第一次正确击中计数")
                bullet.num_shoot[3]=0
            else:    #错误击中
                show_chinese.shoot+=1
                bullet.num_shoot[1] += 1
                show_chinese.right=0
                bullet.num_shoot[3]+=1
                #print("self.english_num_shoot_count",self.english_num_shoot_count)
                #print(self.english_num_shoot_count)
                if bullet.num_shoot[1]==1:
                    time.sleep(0.0001)
                    show_chinese.shoot = 0
                    vocabular_refreash(chinese_num,show_chinese.right)
                    print("第一次错误击中计数")
        else:
            print("没有击中,子弹序数",bullet.num_shoot[0])
            show_chinese.shoot=0

            bullet.num_shoot[2]+=1
            if bullet.num_shoot[2]>100:
                bullet.num_shoot[1] = 0
    def reborn(self):
        self.sur=1
        self.x=self.x_init
        self.y=self.y_init
        self.rect.x=self.x_init
        self.rect.y=self.y_init
#screen.blit

def check_events(bullet0,dir,man):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                dir[0]='w'
            if event.key==pygame.K_s:
                dir[0]='s'
            if event.key==pygame.K_a:
                dir[0]='a'
            if event.key==pygame.K_d:
                dir[0]='d'
            if event.key==pygame.K_ESCAPE:
                sys.exit()
            if event.key==pygame.K_SPACE:
                new_bullet=bullet0
                new_bullet.keep_man(man)
                new_bullet.fire(dir)
                #bullet0.keep_man(man)
                #bullet0.fire2(dir)
                #if bullet_num==0:
                 #   Bullet().list.append(bullet0)
                  #  bullet_num=1
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_w:
                dir[0]='p'
            if event.key==pygame.K_s:
                dir[0]='p'
            if event.key==pygame.K_a:
                dir[0]='p'
            if event.key==pygame.K_d:
                dir[0]='p'
def show_people(body):
    pygame.draw.rect(body.screen,body.color,body.rect)
def show_bullet(bullet):
    pygame.draw.rect(bullet.body.screen,bullet.color,bullet.rect)

setting = Setting()
clock=pygame.time.Clock()
game_active=True

pygame.init()

pygame.display.set_caption("English")
screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
people = Body(setting, screen)
screen.fill(setting.bg_color)
direct=['p']
bullet0=Bullet()
mon0=Monster()
mon1=Monster()
mon2=Monster()
mon3=Monster()
mon0.add_init(0,0,people,screen)
mon1.add_init(950,0,people,screen)
mon2.add_init(950,565,people,screen)
mon3.add_init(0,565,people,screen)
count=0

import  random
import file
# 加载字体
font = pygame.font.SysFont('华文宋体', 27)  # 使用默认字体，字体大小为 36

# 渲染文本
text = font.render("Hello, Pygame!", True, (255, 255, 255))  # 渲染文本，参数分别为文本内容、是否抗锯齿、颜色（RGB）

screen.fill((0, 0, 0))

class carry_chinese():
    def __init__(self):
        self.x=0
        self.y=0
        self.text=''
        self.english_num=0
        self.english_num_shoot_count=0
        self.chinese_num=0
        self.shoot=2
        self.color=(200,0,100)
        self.active_monster_kill=0
        self.active_man_kill=0
        self.grade=0
        self.total_grade=0
        self.right=0
        self.last_chinese_num=0
    def position_refreash(self,man):
        self.x=man.rect.x
        self.y=man.rect.y
    def text_refreash(self,txt):
        self.text=txt
show_chinese=carry_chinese()
show_chinese.english_num=random.randint(0,2128)
show_chinese.chinese_num=random.randint(show_chinese.english_num,show_chinese.english_num+3) #随机生成四个英语中的一个汉语
for member in range(0,2129):  #左闭右开
    show_chinese.total_grade+=int(file.words_list[member].grade)
def find_proper_grade(grade_now):
    grade_count=0
    for member in file.words_list:
        grade_now-=int(member.grade)
        grade_count += 1
        if grade_now==0 or grade_now<0:
            return grade_count

right_times=[0]
wrong_times=[0]
def vocabular_refreash(num,y_n):
    text=''
    count=0
    if y_n==1:
        file.refreash_word_list()
        for member in file.words_list:
            if count==num:
                if int(member.grade)>1:
                    grade_now=int(member.grade)/2
                else:
                    grade_now = int(member.grade)
            else:
                grade_now=int(member.grade)
            strs = member.english + " " + member.chinese + " " +str(grade_now) + "\n"
            text += strs
            count+=1
        with open('D:\\py环境\\eyu\\english2\\record.txt', 'w', encoding='utf-8') as file1:
            file1.write(text)
            right_times[0]+=1
            #print('right',right_times[0],text)
            #time.sleep(0.0001)
            #print(content)  # 这应该输出你写入的文本
        #for member in file.words_list:
            #print(member.english,member.chinese,member.grade)
    else:
        file.refreash_word_list()
        for member in file.words_list:
            if count==num:
                if int(member.grade)>1:
                    grade_now=int(member.grade)*2 #击中错误英语，则权重乘二
                else:
                    grade_now = int(member.grade)
            else:
                grade_now = int(member.grade)
            strs = member.english + " " + member.chinese + " " + str(grade_now) + "\n"
            text += strs
            count+=1
        with open('D:\\py环境\\eyu\\english2\\record.txt', 'w', encoding='utf-8') as file1:
            file1.write(text)
            wrong_times[0]+=1
            #print('wrong',wrong_times[0],text)
while game_active:
    clock.tick(setting.clock)
    screen.fill(setting.bg_color)
    show_people(people)

    bullet0.o_bullet()

    '''Monster.destroy(mon1,Bullet().list[0])
    Monster.destroy(mon2, Bullet().list[0])
    Monster.destroy(mon3, Bullet().list[0])
    Monster.destroy(mon0, Bullet().list[0])'''

    bullet_num2=0
    for member in Bullet().list:
        bullet_num2 += 1
        member.num_shoot[0] = bullet_num2
        Monster.destroy(mon3,member,show_chinese.chinese_num)  #检测击中时中英文是否匹配,刷新sur
        Monster.destroy(mon2, member,show_chinese.chinese_num)
        Monster.destroy(mon1, member,show_chinese.chinese_num)
        Monster.destroy(mon0, member,show_chinese.chinese_num)


        #print("show_chinese.shoot",show_chinese.shoot)
        #print("monster_english_shoot_num",)
    monster_total_sur = mon3.sur and mon2.sur and mon1.sur and mon0.sur
    Monster().M_survival[3]=monster_total_sur
    Monster().M_survival[2] = monster_total_sur
    Monster().M_survival[1] = monster_total_sur
    Monster().M_survival[0] = monster_total_sur
    Monster().M_show()
    '''
    if show_chinese.shoot==1:
        print("shoot=1")
        if mon0.english_num_shoot_count!=12:
            mon0.english_num_shoot_count=10
        if mon1.english_num_shoot_count != 12:
            mon1.english_num_shoot_count = 10
        if mon2.english_num_shoot_count != 12:
            mon2.english_num_shoot_count = 10
        if mon3.english_num_shoot_count != 12:
            mon3.english_num_shoot_count = 10
        show_chinese.english_num=random.randint(0,2124)    #正确命中后重新接连生成4个英文 左闭右闭
        show_chinese.chinese_num = random.randint(show_chinese.english_num,show_chinese.english_num + 3)  # 随机生成四个英语中的一个汉语
    elif show_chinese.shoot==0:
        print("shoot=0")
        if mon0.english_num_shoot_count != -12:
            mon0.english_num_shoot_count = -10
        if mon1.english_num_shoot_count != -12:
            mon1.english_num_shoot_count = -10
        if mon2.english_num_shoot_count != -12:
            mon2.english_num_shoot_count = -10
        if mon3.english_num_shoot_count != -12:
            mon3.english_num_shoot_count = -10
        #print("run wrong shoot")
    show_chinese.shoot=2'''
    count=show_chinese.english_num
    for member in Monster().M_list:
        if (member.sur==1 and people.rect.x>member.left_up_x and people.rect.x<member.right_down_x
                and people.rect.y>member.left_up_y and people.rect.y<member.right_down_y):
            people.reborn()
        member.english_num=count

        text = font.render(file.words_list[count].english, True, (255, 255, 255))
        screen.blit(text,(member.rect.x,member.rect.y+28))
        count=count+1

    show_chinese.position_refreash(people)

    show_chinese.text_refreash(file.words_list[show_chinese.chinese_num].chinese)
    text=font.render(show_chinese.text,True,show_chinese.color)
    screen.blit(text,(show_chinese.x,show_chinese.y+15))

    pygame.display.flip()
    people.run(bullet0, direct, people)
