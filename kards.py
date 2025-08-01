import pyautogui, time, datetime, pygetwindow as gw, random, keyboard, sys, easyocr
from datetime import datetime

# 安装命令：
# pip install pyScreeze numpy opencv_python PyAutoGUI PyGetWindow Pillow keyboard easyocr
confirm_button_image = "confirm.png" #选派确认按钮
main_menu_button_image = "mainButton.png" #主菜单按钮
end_turn_button_image = "endTurn.png" #结束回合按钮
pass_turn_button_image = "clickedEndTurn.png"
clicked_start_game_button = "clickedstartBattle.png"
main_menu_start_button_image = "mainMenuStart.png" #主菜单开始按钮
xiuxian_image = "relax.png" #休闲模式按钮
exp_image = "exptext.png" #刷经验模组图标
continue_button_image = "continue.png"#‘继续’二字按钮
exit_button_image = "exit.png"#退出按钮
clicked_exit_button_image = "clickedExit.png"
enemy_headquarters_image = "enemy_headquarters.png"#敌方总部
bomber_image = "bomber.png"#轰炸机
fighter_image = "fighter.png"#战斗机
infantry_image = "infantry.png"#步兵
tank_image = "tank.png"#坦克
mortar_image = "mortar.png"#炮兵
guard_image = "guard.png"#守护单位
zero_tili = "zero.png"#0体力
get_gold = "gold.png"#金币
duishou_img = "duishou.png" #对手字样
reconnect_img = "reconnect.png" #重新连接
msg_img = "msg.png" #发信息图标
renji_img = "renji.png" #超时选人机操作
restart_img = "restart.png"#服务器不同步重新载入
disconnect_img = "disconnect.png" #服务器断开
start_scale125_img = "start_scale125.png" #您处于不活跃被踢125%
start_scale100_img = "start_scale100.png" #您处于不活跃被踢100%
gear_img = "gearicon.png" #右上角的齿轮图标
self_destruct_img = "selfdestruct.png" #自毁选项
close_Ad_button_image = "closeAd.png" #结算广告
daily_mission_button_image = "daily_mission.png"
frontline_images = ["frontline1.png", "frontline2.png"]
mission_failed_image = "mission_failed.png"
mission_passed_image = "mission_passed.png"

#屏幕范围定义，注： 每张卡160x220 范围坐标为左上角x y 然后是宽度 高度
all_screen = (0,0,pyautogui.size()[0],pyautogui.size()[1]) #全屏幕范围
upper_half_screen = (0, 0, pyautogui.size()[0], pyautogui.size()[1]//2) #屏幕上半
upper_onethird_screen = (0, 0, pyautogui.size()[0], pyautogui.size()[1]//3) #屏幕上三分之一
lower_half_screen = (0, pyautogui.size()[1]//2, pyautogui.size()[0], pyautogui.size()[1]//2) #屏幕下半
lower_onethird_screen = (0, pyautogui.size()[1]*2//3, pyautogui.size()[0], pyautogui.size()[1]//3) #屏幕下三分之一
left_half_screen = (0, 0, pyautogui.size()[0]//2, pyautogui.size()[1]) #屏幕左半
right_half_screen = (pyautogui.size()[0]//2, 0, pyautogui.size()[0]//2, pyautogui.size()[1]) #屏幕右半
left_onethird_screen = (0, 0, pyautogui.size()[0]//3, pyautogui.size()[1]) #屏幕左三分之一
right_onethird_screen = (pyautogui.size()[0]*2//3, 0, pyautogui.size()[0]//3, pyautogui.size()[1]) #屏幕右三分之一
zero_tili_region = (0, pyautogui.size()[1]*790//1080, pyautogui.size()[0]*200//1920, (1080 - 790)) #0体力区域
pass_button_region = (pyautogui.size()[0]*1607//1920,pyautogui.size()[1]*622//1080, 270, 130) #空过按钮区域
second_row = (pyautogui.size()[0]*313//1920, pyautogui.size()[1]*643//1080, 1259 , 263) #支援战线区域
third_row = (pyautogui.size()[0]*333//1920, pyautogui.size()[1]*397//1080, 1417,261) #前线区域
enemy_guard_zone = (pyautogui.size()[0]*431//1920, pyautogui.size()[1]*129//1080, 1075, 161) #敌方支援区域状态区域
enemy_second_row = (pyautogui.size()[0]*400//1920, pyautogui.size()[1]*100//1080, 1143, 289) #地方支援区域
ocr_stamina_region = (32, 849, 53, 76) #体力数值区域

pyautogui.FAILSAFE = False
failsafe_counter = 0
ocr_stamina = 0
ocrscanner = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory

class TimestampLogger:
    def __init__(self, mode='a'):
        # 获取当前时间并格式化为字符串，作为日志文件名
        timestamp = datetime.now().strftime("%Y%m%d_%H_%M")
        self.filename = f"log_{timestamp}.txt"
        self.file = open(self.filename, mode, encoding='utf-8')
        self.stdout = sys.stdout
        sys.stdout = self

    def write(self, message):
        # 同时写入文件和控制台
        self.file.write(message)
        self.stdout.write(message)
        self.flush()

    def flush(self):
        self.file.flush()
        self.stdout.flush()

    def close(self):
        sys.stdout = self.stdout
        self.file.close()

class Box:
    def __init__(self, left, top, width, height):
        self.left = int(left)  # 确保是 int 类型
        self.top = int(top)  # 确保是 int 类型
        self.width = width
        self.height = height
    def __repr__(self):
        return f"Box(left={self.left}, top={self.top}, width={self.width}, height={self.height})"
        
def gameround_timeout_bug_reset(): #有时候20s倒计时失效，此时对局5分钟以后选择自爆
    if check_image(gear_img, 0.8, right_onethird_screen) != None :
        pyautogui.moveTo(return_img_pos, duration=random.uniform(0.6, 1.2))
        time.sleep(0.2)
        pyautogui.click(return_img_pos)
        time.sleep(0.2)
    if check_image(self_destruct_img, 0.8, right_onethird_screen) != None :
        pyautogui.moveTo(return_img_pos, duration=random.uniform(0.6, 1.2))
        time.sleep(0.2)
        pyautogui.click(return_img_pos)
        print(formatted_time + "卡死太久，自爆结束")
    return
    
def click_start_game_button():
    global game_stage
    global game_round
    global round_start_time #本手起始时间
    global logger
    global round_total_time #本局总时间
    global round_total_start_time #本局起始时间
    global failsafe_counter
    global game_window

    round_single_time = time.time() - round_start_time
    round_total_time = time.time() - round_total_start_time
    print(formatted_time+f"开始跑按钮, 点击流程:{game_stage}, 轮次:{game_round}, 本轮耗时{round_single_time:.0f}秒，全局{round_total_time:.0f}秒") #game_stage保证了进入对局的点击顺序
    
    if round_single_time > 60 * 5:   #游戏倒计时超时以后bug处理
        gameround_timeout_bug_reset()
        
    if game_stage == 0 : #查找左上角游戏图标和点击开始按钮
        if check_image(main_menu_start_button_image, 0.9, left_onethird_screen) != None or check_image(main_menu_button_image, 0.9, left_onethird_screen) != None:
            pyautogui.moveTo(pyautogui.size()[0] // 2+ random.uniform(-200, 200), pyautogui.size()[1] // 2+ random.uniform(-200, 200), duration=random.uniform(0.6, 1.2))
            pyautogui.moveTo(return_img_pos, duration=random.uniform(0.6, 1.2))
            time.sleep(0.2)
            pyautogui.click(return_img_pos)
            pyautogui.click(return_img_pos)
            time.sleep(0.2)
            failsafe_counter = 0
            if check_image(exp_image, 0.9, all_screen, True) != None:
                game_stage = 1
            print(formatted_time+"点击主屏幕开始按钮")
    if game_stage == 1 : #点击包含‘经验’二字的卡组
        failsafe_counter += 1
        if failsafe_counter >= 10:
            game_stage = 0
            return
        if check_image(exp_image, 0.9, all_screen, True) != None:
            pyautogui.moveTo(return_img_pos, duration=random.uniform(0.6, 1.2))
            pyautogui.click(return_img_pos)
            failsafe_counter = 0
            game_stage = 2
    if game_stage == 2 : #点击右侧的休闲模式，避免进入排位模式
        failsafe_counter += 1
        if failsafe_counter >= 10:
            game_stage = 0
            return
        if error_handling(xiuxian_image, "点击休闲模式", 0.8, False, right_onethird_screen):
            failsafe_counter = 0
            game_stage = 3
    if game_stage == 3 : #点击右侧开始
        failsafe_counter += 1
        if failsafe_counter >= 10:
            game_stage = 0
            return
        error_handling(clicked_start_game_button, "点击右下开始按钮", 0.8, False, right_onethird_screen)
    if check_image(renji_img, 0.7, lower_half_screen) != None :
        error_handling(renji_img, "找到超时人机选项，点击", 0.8, True, lower_half_screen)
        mouse_return_home()
    if check_image(confirm_button_image, 0.7, lower_half_screen) != None :
        error_handling(confirm_button_image, "点击了选牌以后的确认键", 0.7, True, lower_half_screen)
        mouse_return_home()
        round_total_start_time = time.time()

    error_handling(continue_button_image, "点击了继续按钮, 结束战斗（一般是输了）", 0.7, True)

    error_handling(get_gold, "找到今日金币字样，点击")

    error_handling(restart_img, "找到重新连接字样，点击")

    error_handling(disconnect_img, "找到退出(2)字样，点击")

    error_handling(close_Ad_button_image, "找到了广告，点击叉子")

    if check_image(daily_mission_button_image, 0.7, lower_half_screen) != None:
        pyautogui.moveTo((pyautogui.size()[0]*95//100, pyautogui.size()[1]*95//100), duration=random.uniform(0.6, 1.2))
        pyautogui.click((pyautogui.size()[0]*95//100, pyautogui.size()[1]*95//100))
        print(formatted_time + "触发了今日任务，点击屏幕右下角忽略")

    if check_image(reconnect_img, 0.9) != None :
        print(formatted_time+"然然触发了重新登陆，退出")
        if game_window != None: game_window.minimize()
        #logger.close()
        sys.exit(0)

def click_pass_button():
    global game_round
    global round_start_time
    
    if check_image(pass_turn_button_image, 0.8, right_onethird_screen) != None or check_image(end_turn_button_image, 0.7, right_onethird_screen) != None:
        pass_button_pos = return_img_pos
        print(formatted_time+"找到我方回合按钮，开始打牌")
        round_start_time = time.time()
        time.sleep(random.uniform(2.0, 2.5))# 等待过完讨厌的动画

        play_cards()
        send_message()

        pyautogui.moveTo(pass_button_pos[0]+ random.uniform(-100, 0), pass_button_pos[1]+ random.uniform(-100, 100), duration=random.uniform(0.6, 1.2))
        pyautogui.moveTo(pass_button_pos, duration=random.uniform(0.6, 1.6))
        pyautogui.click(pass_button_pos)
        pyautogui.click(pass_button_pos)
        game_round += 1
        mouse_return_home()
        print(formatted_time+"点击了空过按钮")

def send_message():
    global game_round
    want_to = random.randint(0, 100)
    random_msg_number = random.randint(1, 5)
    if want_to > 75 and game_round >= 1:
        if check_image(msg_img, 0.9, right_onethird_screen) != None :
            pyautogui.moveTo(return_img_pos, duration=random.uniform(0.6, 1.2))
            time.sleep(0.2)
            pyautogui.click(return_img_pos)
            #pyautogui.click(return_img_pos)
            print(formatted_time+f"开始插入聊天，聊第{random_msg_number}条天")
            if random_msg_number == 1:
                pyautogui.move(86-204, 60-360, duration=random.uniform(0.6, 1.2)) #编号2 我们决不投降 
            if random_msg_number == 2:
                pyautogui.move(45-204, 155-360, duration=random.uniform(0.6, 1.2)) #编号5 漂亮
            if random_msg_number == 3:
                pyautogui.move(61-204, 187-360, duration=random.uniform(0.6, 1.2)) #编号6 哇哈哈哈
            if random_msg_number == 4:
                pyautogui.move(49-204, 92-360, duration=random.uniform(0.6, 1.2)) #编号3 谢谢
            if random_msg_number == 5:
                pyautogui.move(92-204, 252-360, duration=random.uniform(0.6, 1.2)) #编号8 打得不错我的朋友
            pyautogui.click()
            time.sleep(0.2)
            pyautogui.click()
            time.sleep(0.2)
            mouse_return_home()

def play_cards():
    global game_round
    global enemy_headquarters_pos

    enemy_headquarters_pos = check_image(enemy_headquarters_image, 0.9, enemy_second_row)

    print(formatted_time + "轰炸机处理流程")
    try:
        posBomberBox = pyautogui.locateAllOnScreen(bomber_image, confidence=0.8, region=second_row)
        posBomberBoxFilterd = filter_boxes(posBomberBox, 10)
        for posBomber in posBomberBoxFilterd:
            enemy_fighter_pos = check_image(fighter_image, 0.8, enemy_second_row)
            guard_pos = check_image(guard_image, 0.8, enemy_second_row)
            if guard_pos != None:
                pyautogui.click(posBomber)
                pyautogui.dragTo(guard_pos, duration=random.uniform(0.7, 0.8))
                mouse_return_home()
                print(formatted_time+"指挥轰炸机攻击敌方守卫")
            elif enemy_fighter_pos != None:
                pyautogui.click(posBomber)
                pyautogui.dragTo(enemy_fighter_pos, duration=random.uniform(0.7, 0.8))
                mouse_return_home()
                print(formatted_time+"指挥轰炸机攻击敌机")
            elif enemy_headquarters_pos != None:
                pyautogui.click(posBomber)
                pyautogui.dragTo(enemy_headquarters_pos, duration=random.uniform(0.7, 0.8))
                mouse_return_home()
                print(formatted_time+"指挥轰炸机攻击总部")
            if check_abnormal(): return
    except Exception as e:
        print(formatted_time + "轰炸机处理出错 可能是没找到")

    print(formatted_time + "战斗机处理流程")
    try:
        posfighterBox = pyautogui.locateAllOnScreen(fighter_image, confidence=0.8, region=second_row)
        posfighterBoxFilterd = filter_boxes(posfighterBox, 10)
        for posfighter in posfighterBoxFilterd:
            enemy_fighter_pos = check_image(fighter_image, 0.8, enemy_second_row)
            guard_pos = check_image(guard_image, 0.84, enemy_second_row)
            if enemy_fighter_pos != None:
                pyautogui.click(posfighter)
                pyautogui.dragTo(enemy_fighter_pos, duration=random.uniform(0.7, 1.0))
                mouse_return_home()
                print(formatted_time+"指挥战斗机攻击敌机")
            elif guard_pos != None:
                pyautogui.click(posBomber)
                pyautogui.dragTo(guard_pos, duration=random.uniform(0.7, 1.0))
                mouse_return_home()
                print(formatted_time+"指挥轰炸机攻击敌方守卫")
            elif enemy_headquarters_pos != None:
                pyautogui.click(posfighter)
                pyautogui.dragTo(enemy_headquarters_pos, duration=random.uniform(0.7, 1.0))
                mouse_return_home()
                print(formatted_time+"指挥战斗机攻击总部")
            if check_abnormal(): return
    except Exception as e:
        print(formatted_time + "战斗机处理出错 可能是没找到")

    print(formatted_time+"炮炮处理")
    try:
        posMortarBox = pyautogui.locateAllOnScreen(mortar_image, confidence=0.8, region=second_row)
        posMortarBoxFilterd = filter_boxes(posMortarBox, 10)
        for posMortar in posMortarBoxFilterd:
            pyautogui.click(posMortar)
            pyautogui.dragTo(enemy_headquarters_pos, duration=random.uniform(0.7, 0.8))
            mouse_return_home()
            print(formatted_time+"指挥炮兵攻击总部")
            if check_abnormal(): return
    except Exception as e:
        print(formatted_time +"炮兵处理出错，可能是没找到")

    if True: #出牌处理
        if game_round == 0:
            play_round1()
        elif game_round <= 1:
            play_round1()
            play_round2()
        else:
            play_round2()
            play_round3()
            play_round1()
            
    #time.sleep(random.uniform(0.5, 0.9))

def play_round1(): #用于抽牌
    global enemy_headquarters_pos
    print(formatted_time +"第1轮出牌，抽最下面的牌") #阶段1，抽牌
    time.sleep(1)  # 等待过完动画
    mouse_coeff = 70
    for i in range(7):
        if check_abnormal(): return
        x = 720 + i*110
        #pyautogui.moveTo(x, y=pyautogui.size()[1] - 100, duration=random.uniform(0.2, 0.6))
        pyautogui.moveTo(x, y=pyautogui.size()[1] - mouse_coeff)
        time.sleep(0.9)  # 等待过完动画
        #------------- OCR ---------------
        ocrimage = pyautogui.screenshot('ocr.png', region=( x-470, pyautogui.size()[1] - 650  , 730, 550))
        ocrresult = ocrscanner.readtext('ocr.png', detail = 0)
        print(list(ocrresult))
        # ------------- OCR ---------------

        special_command = ['西苏精神']
        movable_unit = ['坦克', '步兵', '炮兵', '战斗机', '轰炸机', '猎兵营'] #某些介绍太长的单位也在列表里
        postive_buff = ['修复', '哈哈']
        negtive_buff = ['抑制', '伤害', '敌方']
        neutral_buff = ['指令']

        if any(key in ocrresult for key in special_command):   #特殊指令
            print(formatted_time + "特殊指令处理")
            if '西苏精神' in ocrresult: #转移伤害给敌方总部
                print(formatted_time + "西苏精神, 转移伤害给敌方总部")
                pyautogui.click(x, y=pyautogui.size()[1] - mouse_coeff)
                pyautogui.dragTo((x, pyautogui.size()[1]//2), duration=0.8)  # 按照一定的顺序把牌丢出去

        if any(key in ocrresult for key in movable_unit):   #移动兵力
            print(formatted_time + "移动兵力")
            pyautogui.click(x, y=pyautogui.size()[1] - mouse_coeff)
            pyautogui.dragTo((pyautogui.size()[0]//2, pyautogui.size()[1]*2//3), duration=0.6)

        if any(key in ocrresult for key in negtive_buff):   #把负面buff扔给敌人
            print(formatted_time + "负面buff")
            drop_card_to_anyzone()

        if any(key in ocrresult for key in postive_buff):   #正面buff扔给自己
            print(formatted_time + "正面buff")
            drop_card_to_anyzone(on_guard=False, on_region=second_row)

        if any(key in ocrresult for key in neutral_buff):   #中性buff挠头处理
            if '3张' in ocrresult:   #三选一问题,选中间
                pyautogui.click(pyautogui.size()[0]//2, y=pyautogui.size()[1]//2)
                pyautogui.click(pyautogui.size()[0]//2, y=pyautogui.size()[1]//2)
                print(formatted_time + "3张, 三选一问题,选中间")
            elif '武士之刃' in ocrresult:  # 直接消灭对方一个单位
                drop_card_to_anyzone(on_region=enemy_second_row)
                print(formatted_time + "武士之刃, 直接消灭对方一个单位")
            elif '两栖迸攻' in ocrresult:  # 直接消灭对方一个攻击小于3单位
                drop_card_to_anyzone(on_tank=False, on_guard=False, on_region=enemy_second_row)
                print(formatted_time + "两栖迸攻, 直接消灭对方一个攻击小于3单位")

        mouse_return_home()

def drop_card_to_anyzone(on_guard=True, on_infantry=True, on_tank=True, on_mortar=True, on_fighter=True, on_bomber=True, on_head = False, on_region=enemy_second_row):
    global enemy_headquarters_pos
    pyautogui.click(x, y=pyautogui.size()[1] - mouse_coeff)

    guard_pos = check_image(guard_image, 0.8, on_region)
    infantry_pos = check_image(infantry_image, 0.8, on_region)
    tank_pos = check_image(tank_image, 0.8, on_region)
    mortar_pos = check_image(mortar_image, 0.8, on_region)
    fighter_pos = check_image(fighter_image, 0.8, on_region)
    bomber_pos = check_image(bomber_image, 0.8, on_region)

    if guard_pos != None and on_guard:
        pyautogui.dragTo(guard_pos, duration=0.9)
    elif infantry_pos != None and on_infantry:
        pyautogui.dragTo(infantry_pos, duration=0.6)
    elif tank_pos != None and on_tank:
        pyautogui.dragTo(tank_pos, duration=0.6)
    elif mortar_pos != None and on_mortar:
        pyautogui.dragTo(mortar_pos, duration=0.7)
    elif fighter_pos != None and on_fighter:
        pyautogui.dragTo(fighter_pos, duration=0.8)
    elif bomber_pos != None and on_bomber:
        pyautogui.dragTo(bomber_pos, duration=0.8)
    elif enemy_headquarters_pos != None and on_head:
        pyautogui.dragTo(enemy_headquarters_pos, duration=0.9)
    return

def play_round2(): #用于移动支援线
    global game_round

    time.sleep(1)  # 等待过完动画
    print(formatted_time +"第2轮出牌，支援线前进") #阶段2，引导坦克步兵向前线前进
    try:
        posInfantryBox = pyautogui.locateAllOnScreen(infantry_image, confidence=0.9, region=second_row)
        posInfantryBoxFilterd = filter_boxes(posInfantryBox, 10)
        for posInfantry in posInfantryBoxFilterd:
            if check_abnormal():
                print(formatted_time + "阶段2a体力0或者发现异常， 退出")
                return
            pyautogui.click(posInfantry[0] + posInfantry[2]//2 + random.choice([-1, 1])*51, posInfantry[1]-50)
            pyautogui.dragTo((pyautogui.size()[0]//2 + random.choice([-1, 1])*random.uniform(54, 57), pyautogui.size()[1]//2), duration=random.uniform(0.4, 1.0))
            mouse_return_home()
            time.sleep(0.2)

    except Exception as e:
        print(formatted_time +"阶段2查找Infantry异常，可能目标已移动")

    try:
        posTankBox = pyautogui.locateAllOnScreen(tank_image, confidence=0.9, region=second_row)
        posTankBoxFilterd = filter_boxes(posTankBox, 10)
        for posTank in posTankBoxFilterd:
            if check_abnormal():
                print(formatted_time + "阶段2b体力0或者发现异常， 退出")
                return
            pyautogui.click(posTank[0] + posTank[2]//2 + random.choice([-1, 1])*51, posTank[1]-50)
            pyautogui.dragTo((pyautogui.size()[0]//2 + random.choice([-1, 1])*random.uniform(54, 57), pyautogui.size()[1]//2), duration=random.uniform(0.4, 1.0))
            mouse_return_home()
            time.sleep(0.2)

    except Exception as e:
        print(formatted_time +"阶段2查找Tank异常，可能没有目标")
        return
                
def play_round3(): #用于前线
    global game_round    
    global enemy_headquarters_pos

    time.sleep(1)  # 等待过完动画
    guard_pos = check_image(guard_image, 0.84, enemy_second_row)
    if enemy_headquarters_pos != None or guard_pos != None: #阶段3，引导坦克步兵攻击守护单位和总部
        print(formatted_time +"第3轮出牌，前线动作")
        try:
            posInfantryBox = pyautogui.locateAllOnScreen(infantry_image, confidence=0.9, region=third_row)
            posInfantryBoxFilterd = filter_boxes(posInfantryBox, 10)
            for posInfantry in posInfantryBoxFilterd:
                if check_abnormal():
                    print(formatted_time + "阶段3a体力0或者发现异常， 退出")
                    return
                pyautogui.click(posInfantry[0] + posInfantry[2]//2 + random.choice([-1, 1])*51, posInfantry[1]-50)
                if guard_pos != None:
                    pyautogui.dragTo((guard_pos[0] - 60, guard_pos[1] + 80), duration=random.uniform(0.4, 1))
                elif enemy_headquarters_pos != None:
                    pyautogui.dragTo(enemy_headquarters_pos, duration=random.uniform(0.4, 1))
                mouse_return_home()
        except Exception as e:
            print(formatted_time +"阶段3查找Infantry异常，可能目标已移动")

        try:
            posTankBox = pyautogui.locateAllOnScreen(tank_image, confidence=0.9, region=third_row)
            posTankBoxFilterd = filter_boxes(posTankBox, 10)
            for posTank in posTankBoxFilterd:
                if check_abnormal():
                    print(formatted_time + "阶段3b体力0或者发现异常，退出")
                    return
                pyautogui.click(posTank[0] + posTank[2]//2 + random.choice([-1, 1])*51, posTank[1]-50)
                if guard_pos != None:
                    pyautogui.dragTo((guard_pos[0] - 60, guard_pos[1] + 80), duration=random.uniform(0.4, 1))
                elif enemy_headquarters_pos != None:
                    pyautogui.dragTo(enemy_headquarters_pos, duration=random.uniform(0.4, 1))
                mouse_return_home()
        except Exception as e:
            print(formatted_time +"阶段3查找Tank异常，可能目标已移动")

def check_abnormal():
    global ocr_stamina
    abnormal_state = False
    if check_image(mission_failed_image, 0.8, lower_half_screen) != None: print(formatted_time +"检测到本局失败, 记录一下")
    if check_image(mission_passed_image, 0.8, lower_half_screen) != None: print(formatted_time + "检测到本局失败, 记录一下")
    if check_image(duishou_img, 0.8, pass_button_region) != None: #找到对手字样
        print(formatted_time + "异常检测程序发现 对手 字样")
        abnormal_state = True
    if check_image(continue_button_image, 0.8, lower_half_screen) != None: #找到继续字样
        print(formatted_time + "异常检测程序发现 继续 字样")
        abnormal_state = True
    if False: # -------------- OCR ----------------
        ocr_check_stamina()
        if ocr_stamina == 0:
            print(formatted_time + "OCR发现0体力")
            abnormal_state = True
    if check_image(zero_tili, 0.92, zero_tili_region, False) != None: #找到体力为0
        print(formatted_time + "异常检测程序发现 0体力")
        abnormal_state = True
    if check_image(reconnect_img, 0.9) != None :    #Check if 被别的设备踢出去了
        print(formatted_time+"然然触发了重新登陆，退出")
        if game_window != None: game_window.minimize()
        sys.exit(0)
    return abnormal_state

def reset_game_stage():
    global game_stage
    global game_round
    global round_start_time
    game_stage = 0
    game_round = 0
    round_start_time = time.time()
    round_total_start_time = time.time()

def check_image(image_name, confidence_level, detect_region=all_screen, grayscale_opt=False):  # 图像查找包装程序
    global return_img_pos
    i = 1.0
    time.sleep(0.3)
    while True:
        i = i - 0.05
        #return_img_pos = None
        try:
            return_img_pos = pyautogui.locateCenterOnScreen(image_name, confidence=i, region=detect_region, grayscale=grayscale_opt)
        except Exception as e:
            #print(formatted_time + f'没找到图片')
            return None

        if return_img_pos is not None:
            print(formatted_time + f'找到  {image_name} -> confi= {i:.2f}')
            return return_img_pos

        if i <= confidence_level:
            print(formatted_time + f'查找{image_name}尝试了所有精度，可能没找到')
            return None

def mouse_return_home():
    pyautogui.moveTo(1563 + random.uniform(-50, 50), 840 + random.uniform(-50, 50), duration=random.uniform(0.2, 0.7))  # 移动鼠标不遮挡屏幕


def filter_boxes(raw_data, threshold):
    filtered_boxes = []
    for box in raw_data:
        if all(abs(box.left - other.left) >= threshold or abs(box.top - other.top) >= threshold for other in
               filtered_boxes):
            filtered_boxes.append(box)
    return filtered_boxes

def try_restart():
    error_handling(start_scale125_img, "找到重新开始DPI 125%，点击") #启动器按钮写的太shit
    error_handling(start_scale100_img, "找到重新开始DPI 100%，点击")

def error_handling(input_img = start_scale125_img, output_string = "Error Handling", confi_level = 0.9, reset_stage = False, search_pos = all_screen):
    global return_img_pos
    if check_image(input_img, confi_level, search_pos) != None :
        #pyautogui.moveTo(pyautogui.size()[0] // 2+ random.uniform(-200, 200), pyautogui.size()[1] // 2+ random.uniform(-200, 200), duration=random.uniform(0.6, 1.2))
        pyautogui.moveTo( (return_img_pos[0] + random.uniform(-10, 10),return_img_pos[1] + random.uniform(-10, 10)), duration=random.uniform(0.6, 1.2))
        time.sleep(0.2)
        pyautogui.click(return_img_pos)
        pyautogui.click(return_img_pos)
        print(formatted_time+output_string)
        if reset_stage:
            reset_game_stage()
        return True
    else:
        return False

#-----------------------------------------------MAIN---------------------------------------------------
def main():
    global game_stage
    global game_round
    global formatted_time
    global enemy_headquarters_pos
    global round_total_start_time
    global game_window

    game_active = False
    round_total_start_time = time.time()
    reset_game_stage()
    print(" -- KARDs 1939 Better AFK, Ver 250801d by Eason -- ")
    logger = TimestampLogger("w")
    debug_testing()
    while True:
        now = datetime.now()
        formatted_time = now.strftime('%m-%d %H:%M:%S -- ')
        for i in range(14):
            time.sleep(random.uniform(0.09, 0.16))
            if keyboard.is_pressed('F9'):  # 检测是否按下退出键
                print(formatted_time + "按下了F9, 程序终止。")
                exit()
        try:
            game_window = gw.getWindowsWithTitle("kards  ")[0]
            #game_window = gw.getWindowsWithTitle("VNC")[0]
            if game_window != None:
                if game_active == False:
                    print(formatted_time+"找到游戏窗口， 切换中")
                    game_window.activate()  # 激活游戏窗口
                    game_active = True
        except Exception as e:
            game_active = False
            try_restart()
            reset_game_stage()
            print(formatted_time + "未找到游戏窗口")

        if game_active:
            click_start_game_button()
            click_pass_button()

def ocr_check_stamina(): #Check Stamina by using OCR
    global ocr_stamina
    ocrimage = pyautogui.screenshot('ocr_stamina.png', region=ocr_stamina_region)
    ocrresult = ocrscanner.readtext('ocr_stamina.png', detail=0)
    if ocrresult:
        print(formatted_time + 'OCR stamina: ' + ocrresult[0])
        ocr_stamina = ocrresult[0]
    return
#-------------------------------------------MAIN, Bro Out-----------------------------------------------

def debug_testing():
    global formatted_time
    #if True: #For debug
    if False:
        now = datetime.now()
        formatted_time = now.strftime('%m-%d %H:%M:%S -- ')

        mouse_x, mouse_y = pyautogui.position()
        x = 720
        ocrimage = pyautogui.screenshot('ocr.png', region=(x-630, pyautogui.size()[1]-100 - 892 , 390, 470))
        ocrresult = ocrscanner.readtext('ocr.png', detail = 0)
        print(list(ocrresult))

        if False:
            try:
                guard_pos = pyautogui.locateAllOnScreen(frontline_images[1], confidence=0.8, region=all_screen, grayscale=True)
                guard_pos_box = filter_boxes(guard_pos, 5)
                print(list(guard_pos_box))
            except Exception as e:
                print("Not found All")
            try:
                for images in frontline_images:
                    guard_pos = check_image(images, 0.8, all_screen)
                    print(guard_pos)
            except Exception as e:
                print("Not found 1")

# ---------------- Debug Section End --------------------
        while True: pass

if __name__ == "__main__":
    main()