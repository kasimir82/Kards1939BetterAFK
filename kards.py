import pyautogui, time, datetime, pygetwindow as gw, random, sys, easyocr
from datetime import datetime
import cv2, numpy as np, os

pyautogui.FAILSAFE = False
# 安装命令：
# pip install pyScreeze numpy opencv_python PyAutoGUI PyGetWindow Pillow easyocr cv2

#图片定义 Image Definations
confirm_button_image = "Resource/confirm.png" #选派确认按钮
main_menu_button_image = "Resource/mainButton.png" #主菜单按钮
end_turn_button_image = "Resource/endTurn.png" #结束回合按钮
pass_turn_button_image = "Resource/clickedEndTurn.png"
clicked_start_game_button = "Resource/clickedstartBattle.png"
main_menu_start_button_image = "Resource/mainMenuStart.png" #主菜单开始按钮
xiuxian_image = "Resource/relax.png" #休闲模式按钮
exp_image = "Resource/exptext.png" #刷经验模组图标
continue_button_image = "Resource/continue.png"#‘继续’二字按钮
exit_button_image = "Resource/exit.png"#退出按钮
clicked_exit_button_image = "Resource/clickedExit.png"
enemy_headquarters_image = "Resource/enemy_headquarters.png"#敌方总部
bomber_image = "Resource/bomber.png"#轰炸机
fighter_image = "Resource/fighter.png"#战斗机
infantry_image = "Resource/infantry.png"#步兵
tank_image = "Resource/tank.png"#坦克
mortar_image = "Resource/mortar.png"#炮兵
guard_image = "Resource/guard.png"#守护单位
zero_tili = "Resource/zero.png"#0体力
get_gold = "Resource/gold.png"#金币
duishou_img = "Resource/duishou.png" #对手字样
reconnect_img = "Resource/reconnect.png" #重新连接
msg_img = "Resource/msg.png" #发信息图标
renji_img = "Resource/renji.png" #超时选人机操作
restart_img = "Resource/restart.png"#服务器不同步重新载入
disconnect_img = "Resource/disconnect.png" #服务器断开
start_scale125_img = "Resource/start_scale125.png" #您处于不活跃被踢125%
start_scale100_img = "Resource/start_scale100.png" #您处于不活跃被踢100%
gear_img = "Resource/gearicon.png" #右上角的齿轮图标
self_destruct_img = "Resource/selfdestruct.png" #自毁选项
close_Ad_button_image = "Resource/closeAd.png" #结算广告
daily_mission_button_image = "Resource/daily_mission.png" #每日任务
mission_failed_image = "Resource/mission_failed.png" #失败
mission_passed_image = "Resource/mission_passed.png" #胜利
net_restart_image = "Resource/network_restart.png" #网络重启
kmark_image = "Resource/kmark.png" #卡牌左上角K图标


#屏幕范围定义，注： 每张卡160x220 范围坐标为左上角x y 然后是宽度 高度
#Screen Location Definations
all_screen = (0,0,pyautogui.size()[0],pyautogui.size()[1]) #全屏幕范围
upper_half_screen = (0, 0, pyautogui.size()[0], pyautogui.size()[1]//2) #屏幕上半
upper_onethird_screen = (0, 0, pyautogui.size()[0], pyautogui.size()[1]//3) #屏幕上三分之一
lower_half_screen = (0, pyautogui.size()[1]//2, pyautogui.size()[0], pyautogui.size()[1]//2) #屏幕下半
lower_onethird_screen = (0, pyautogui.size()[1]*2//3, pyautogui.size()[0], pyautogui.size()[1]//3) #屏幕下三分之一
left_half_screen = (0, 0, pyautogui.size()[0]//2, pyautogui.size()[1]) #屏幕左半
right_half_screen = (pyautogui.size()[0]//2, 0, pyautogui.size()[0]//2, pyautogui.size()[1]) #屏幕右半
left_onethird_screen = (0, 0, pyautogui.size()[0]//3, pyautogui.size()[1]) #屏幕左三分之一
right_onethird_screen = (pyautogui.size()[0]*2//3, 0, pyautogui.size()[0]//3, pyautogui.size()[1]) #屏幕右三分之一
ninegong_zone3 = (pyautogui.size()[0]*2//3, 0, pyautogui.size()[0]//3, pyautogui.size()[1]//3)
zero_tili_region = (0, pyautogui.size()[1]*790//1080, pyautogui.size()[0]*200//1920, (1080 - 790)) #0体力区域
pass_button_region = (pyautogui.size()[0]*1607//1920,pyautogui.size()[1]*622//1080, 270, 130) #空过按钮区域
upper_row = (pyautogui.size()[0]*400//1920, pyautogui.size()[1]*234//1080, 1300, 140) #敌方支援图标区域
middle_row = (pyautogui.size()[0]*333//1920, pyautogui.size()[1]*566//1080, 1300,65) #前线图标区域
lower_row = (pyautogui.size()[0]*333//1920, pyautogui.size()[1]*830//1080, 1300 , 65) #支援战线图标区域
enemy_guard_zone = (pyautogui.size()[0]*431//1920, pyautogui.size()[1]*129//1080, 1075, 161) #敌方支援状态区域
enemy_hq_zone = (pyautogui.size()[0]*411//1920, pyautogui.size()[1]*254//1080, 1120, 60) #敌方总部图标区域
ocr_stamina_region = (32, 849, 53, 76) #体力数值区域
ocr_game_round_region = (80, 890, 30, 30) #左下角的指令槽区域
front_line_upper_region = (420, 370, 1000, 37) #上面前线条表达区域
front_line_lower_region = (420, 635, 1000, 37) #下面前线条表达区域
card_search_region = (pyautogui.size()[0]*10//100, pyautogui.size()[1]*30//100, pyautogui.size()[0]*80//100,pyautogui.size()[1]*70//100)#卡牌详细信息的搜索区域

#Global Veriables
ocrscanner = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
failsafe_counter = 0
ocr_stamina = 0
front_line_status = 3  #0代表未知 1代表被我占领 2代表敌方占领 3代表中立
front_line_diff_threshold = 9
front_line_upper_base = 0
front_line_lower_base = 0
game_stage = 0
ocr_stamina = 0
mouse_yaxis_coeff = 50
enemy_headquarters_pos = None
current_card_cost = 1
frontline_status = ['状态未知','我方占领','敌方占领','无人占领']
kmark_location = (0,0)
ocr_gameround = 0

class LogRedirector:

    def __init__(self, log_file):
        self.console = sys.stdout
        self.log_file = open(log_file, 'a', encoding='utf-8')

    def write(self, message):
        # 同时输出到控制台和日志文件
        self.console.write(message)
        self.log_file.write(message)
        self.log_file.flush()  # 确保内容立即写入文件

    def flush(self):
        self.console.flush()
        self.log_file.flush()

def handle_old_log(log_filename="run_log.txt"):
    """处理已存在的旧日志文件"""
    if os.path.exists(log_filename):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        old_log_filename = f"log_{timestamp}.txt"
        os.rename(log_filename, old_log_filename)

def setup_logging(log_filename="run_log.txt"):
    handle_old_log(log_filename)
    sys.stdout = LogRedirector(log_filename)
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class Box:
    def __init__(self, left, top, width, height):
        self.left = int(left)  # 确保是 int 类型
        self.top = int(top)  # 确保是 int 类型
        self.width = width
        self.height = height
    def __repr__(self):
        return f"Box(left={self.left}, top={self.top}, width={self.width}, height={self.height})"

def gameround_timeout_bug_reset(): #有时候20s倒计时失效，此时单手超过4分钟以后选择自爆
    if check_image(gear_img, 0.8, ninegong_zone3) != None :
        pyautogui.moveTo(return_img_pos, duration=random.uniform(0.2, 0.5))
        time.sleep(0.2)
        pyautogui.click(return_img_pos)
        time.sleep(0.2)
    if check_image(self_destruct_img, 0.8, ninegong_zone3) != None :
        pyautogui.moveTo(return_img_pos, duration=random.uniform(0.2, 0.5))
        time.sleep(0.2)
        pyautogui.click(return_img_pos)
        print(formatted_time + "卡死太久，自爆结束")
    return
    
def click_start_game_button():
    global game_stage
    global round_start_time #本手起始时间
    global logger
    global round_total_time #本局总时间
    global round_total_start_time #本局起始时间
    global failsafe_counter
    global game_window
    global front_line_upper_base
    global front_line_lower_base

    round_single_time = time.time() - round_start_time
    round_total_time = time.time() - round_total_start_time
    print(formatted_time+f"开始跑流程:{game_stage},轮次:{ocr_gameround},本轮耗时{round_single_time:.0f}秒，本局耗时{round_total_time:.0f}秒,前线状态:" + frontline_status[front_line_status]) #game_stage保证了进入对局的点击顺序
    
    if round_single_time > 60 * 3:   #游戏倒计时超时以后bug处理
        gameround_timeout_bug_reset()
        
    if game_stage == 0 : #查找左上角游戏图标和点击开始按钮
        if check_image(main_menu_start_button_image, 0.9, left_onethird_screen) != None or check_image(main_menu_button_image, 0.9, left_onethird_screen) != None:
            pyautogui.moveTo(pyautogui.size()[0] // 2+ random.uniform(-200, 200), pyautogui.size()[1] // 2+ random.uniform(-200, 200), duration=0.7)
            pyautogui.moveTo(return_img_pos, duration=random.uniform(0.2, 0.5))
            time.sleep(0.2)
            pyautogui.click(return_img_pos)
            pyautogui.click(return_img_pos)
            time.sleep(0.2)
            failsafe_counter = 0
            if check_image(exp_image, 0.7, all_screen, grayscale_opt=True) != None:
                game_stage = 1
            print(formatted_time+"点击主屏幕开始按钮")
    if game_stage == 1 : #点击包含‘经验’二字的卡组
        failsafe_counter += 1
        if failsafe_counter >= 10:
            game_stage = 0
            return
        if check_image(exp_image, 0.7, all_screen, grayscale_opt=True) != None:
            pyautogui.moveTo(return_img_pos, duration=random.uniform(0.2, 0.5))
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
        front_line_upper_base = 0
        mouse_return_home()
        round_total_start_time = time.time()

    if check_image(mission_failed_image, 0.6, all_screen) != None: print(formatted_time +"检测到本局失败, 记录一下")
    if check_image(mission_passed_image, 0.6, all_screen) != None: print(formatted_time + "本局胜利")

    error_handling(continue_button_image, "点击了继续按钮, 结束战斗（一般是输了）", 0.7, True)

    error_handling(get_gold, "找到今日金币字样，点击")

    error_handling(restart_img, "找到重新连接字样，点击")

    error_handling(disconnect_img, "找到退出(2)字样，点击")

    error_handling(close_Ad_button_image, "找到了广告，点击叉子")

    error_handling(net_restart_image, confi_level=0.7, output_string="找到 网络 重启框，点击重启")

    if check_image(daily_mission_button_image, 0.7, lower_half_screen) != None:
        pyautogui.moveTo((pyautogui.size()[0]*90//100, pyautogui.size()[1]*90//100), duration=random.uniform(0.2, 0.5))
        pyautogui.click((pyautogui.size()[0] * 90 // 100, pyautogui.size()[1] * 90 // 100))
        pyautogui.click((pyautogui.size()[0] * 90 // 100, pyautogui.size()[1] * 90 // 100))
        print(formatted_time + "跳出了今日任务，点击屏幕右下角忽略")

    if check_image(reconnect_img, 0.9) != None :
        print(formatted_time+"然然触发了游戏重新登陆，脚本退出")
        if game_window != None: game_window.minimize()
        #logger.close()
        sys.exit(0)

def click_pass_button():
    global round_start_time
    
    if check_image(pass_turn_button_image, 0.8, right_onethird_screen) != None or check_image(end_turn_button_image, 0.7, right_onethird_screen) != None:
        pass_button_pos = return_img_pos
        print(formatted_time+"找到我方回合按钮，开始打牌")
        round_start_time = time.time()
        time.sleep(random.uniform(1, 2))# 等待过完讨厌的动画
        ocr_check_gameround()

        play_cards()

        pyautogui.moveTo(pass_button_pos[0]+ random.uniform(-150, 0), pass_button_pos[1]+ random.uniform(-100, 100), duration=random.uniform(0.2, 0.5))
        pyautogui.moveTo(pass_button_pos, duration=random.uniform(0.2, 0.5))
        if check_abnormal_without_stemina():
            mouse_return_home()
            return
        pyautogui.click(pass_button_pos)
        pyautogui.click(pass_button_pos)
        print(formatted_time+"点击了空过按钮")
#--------------- After Clicking Pass Button ----------------
        send_message()

        mouse_return_home()

        ocr_check_gameround()
        check_frontline_status()
#--------------- After Clicking Pass Button ----------------

def send_message(msg_id = 0):
    message0_loc = (-159,-334)
    want_to = random.randint(0, 100)
    if want_to > 75 or ocr_gameround <=1 :
        time.sleep(0.5)
    #if True:
        if check_image(msg_img, 0.9, right_onethird_screen) != None :
            random_msg_number = random.choice([1,3,4,5,8])
            pyautogui.moveTo(return_img_pos, duration=0.5)
            time.sleep(0.5)
            pyautogui.click(return_img_pos)
            #pyautogui.click(return_img_pos)
            time.sleep(0.5)
            pyautogui.move(message0_loc, duration=0.3)
            if ocr_gameround <= 1: random_msg_number = 1
            print(formatted_time+f"开始插入聊天，聊第{random_msg_number}条天") #开局只能发第一条
            if msg_id != 0:
                pyautogui.move(0, 32 * (msg_id-1), duration=0.6)
            else:
                pyautogui.move(0, 32 * (random_msg_number-1), duration=0.6)
            pyautogui.click()
            time.sleep(0.5)

def play_cards():
    global enemy_headquarters_pos

    enemy_headquarters_pos = check_image(enemy_headquarters_image, 0.8, enemy_hq_zone)

    #print(formatted_time + "战斗机处理流程")
    try:
        posfighterBox = pyautogui.locateAllOnScreen(fighter_image, confidence=0.8, region=lower_row)
        posfighterBoxFilterd = filter_boxes(posfighterBox, 10)
        for posfighter in posfighterBoxFilterd:
            if check_abnormal(): return
            enemy_fighter_pos = check_image(fighter_image, 0.8, upper_row)
            guard_pos = check_image(guard_image, 0.8, enemy_guard_zone)
            if guard_pos != None:
                pyautogui.click(posBomber)
                pyautogui.dragTo((guard_pos[0], guard_pos[1]), duration=random.uniform(0.2, 0.5))
                mouse_return_home()
                print(formatted_time + "指挥轰炸机攻击敌方守卫")
            elif enemy_fighter_pos != None:
                pyautogui.click(posfighter)
                pyautogui.dragTo(enemy_fighter_pos, duration=random.uniform(0.2, 0.5))
                mouse_return_home()
                print(formatted_time+"指挥战斗机攻击敌机")
            elif enemy_headquarters_pos != None:
                pyautogui.click(posfighter)
                pyautogui.dragTo(enemy_headquarters_pos, duration=1)
                mouse_return_home()
                print(formatted_time+"指挥战斗机攻击总部")
    except Exception as e:
        print(formatted_time + "战斗机处理出错 可能是没找到")

    #print(formatted_time + "轰炸机处理流程")
    try:
        posBomberBox = pyautogui.locateAllOnScreen(bomber_image, confidence=0.8, region=lower_row)
        posBomberBoxFilterd = filter_boxes(posBomberBox, 10)
        for posBomber in posBomberBoxFilterd:
            if check_abnormal(): return
            enemy_fighter_pos = check_image(fighter_image, 0.8, upper_row)
            guard_pos = check_image(guard_image, 0.8, enemy_guard_zone)
            if guard_pos != None:
                pyautogui.click(posBomber)
                pyautogui.dragTo((guard_pos[0],guard_pos[1]), duration=random.uniform(0.2, 0.5))
                mouse_return_home()
                print(formatted_time+"指挥轰炸机攻击敌方守卫")
            elif enemy_headquarters_pos != None:
                pyautogui.click(posBomber)
                pyautogui.dragTo(enemy_headquarters_pos, duration=1)
                mouse_return_home()
                print(formatted_time+"指挥轰炸机攻击总部")
    except Exception as e:
        print(formatted_time + "轰炸机处理出错 可能是没找到")

    #print(formatted_time+"炮炮处理")
    try:
        posMortarBox = pyautogui.locateAllOnScreen(mortar_image, confidence=0.8, region=lower_row)
        posMortarBoxFilterd = filter_boxes(posMortarBox, 10)
        for posMortar in posMortarBoxFilterd:
            if check_abnormal(): return
            guard_pos = check_image(guard_image, 0.8, enemy_guard_zone)
            if guard_pos != None:
                pyautogui.click(posBomber)
                pyautogui.dragTo((guard_pos[0],guard_pos[1]), duration=random.uniform(0.2, 0.5))
                mouse_return_home()
                print(formatted_time+"指挥炮兵攻击敌方守卫")
            elif enemy_headquarters_pos != None:
                pyautogui.click(posBomber)
                pyautogui.dragTo(enemy_headquarters_pos, duration=1)
                mouse_return_home()
                print(formatted_time+"指挥炮兵攻击总部")
    except Exception as e:
        print(formatted_time +"炮兵处理出错，可能是没找到")

    ocr_check_gameround()
    #出牌处理
    if ocr_gameround == 0:
        play_round1()
        play_round4()
    elif ocr_gameround <= 1:
        play_round1()
        play_round2()
        play_round4()
    else:
        play_round2()
        play_round3()
        play_round1()
        play_round4()



def play_round1(): #用于抽牌
    global enemy_headquarters_pos
    global mouse_yaxis_coeff
    global current_card_cost
    print(formatted_time +"第1轮出牌，抽最下面的牌") #阶段1，抽牌
    #time.sleep(1)  # 等待过完抽卡动画
    check_frontline_status()  # 顺便,检查一下前线情况

    for i in range(7):
        if check_abnormal(): return
        x = 600 + i * random.randint(89, 99)

        pyautogui.moveTo(x, y=pyautogui.size()[1] - mouse_yaxis_coeff, duration=0.4)
        pyautogui.click()
        #time.sleep(0.9)  # 等待过完动画
        ocr_check_card_cost()
        ocr_check_stamina()
        if current_card_cost <= ocr_stamina:
            print(formatted_time + f"当前手牌消耗 {current_card_cost} 小于等于体力 {ocr_stamina} ")
            #------------- OCR ---------------
            if kmark_location[0] != 0:
                ocrimage = pyautogui.screenshot('ocr_card.png',
                                                region=(kmark_location[0] - 390, kmark_location[1] - 30, 700, 520))
            else:
                return
            ocrresult = ocrscanner.readtext('ocr_card.png', detail = 0)
            joined_ocrresult = ''.join(ocrresult)
            print(joined_ocrresult)
            # ------------- OCR ---------------
            mouse_return_home()

            movable_unit = ['坦克', '步兵', '炮兵', '战斗机', '轰炸机', '猎兵营'] #某些介绍太长的单位也在列表里
            # 3代表中立 1代表被我占领 2代表敌方占领 0代表未知
            print(formatted_time + "特殊指令处理")
            if '西苏精神' in joined_ocrresult: #转移伤害给敌方总部
                print(formatted_time + "西苏精神专属处理, 转移伤害给敌方总部")
                pyautogui.click(x, y=pyautogui.size()[1] - mouse_yaxis_coeff)
                pyautogui.dragTo((x, pyautogui.size()[1]//2), duration=0.3)  # 按照一定的顺序把牌丢出去
            if '老兔子' in joined_ocrresult: #转移伤害给敌方总部
                print(formatted_time + "老兔子专属处理")
                if front_line_status == 1: drop_card_to_anyzone(card_index = x,on_guard=False,on_infantry=True,on_tank=True,
                                                                on_head=False,on_mortar=False,on_fighter=False,on_bomber=False,
                                                                on_region=middle_row)
                else: drop_card_to_anyzone(card_index = x,on_guard=False,on_infantry=True,on_tank=True,on_head=False,
                                           on_mortar=False,on_fighter=False,on_bomber=False,on_region=lower_row)
            if '空中闪击' in joined_ocrresult:
                print(formatted_time + "空中闪击专属处理")
                drop_card_to_anyzone(card_index=x, on_guard=False, on_infantry=False, on_tank=False, on_head=True,
                                     on_mortar=False, on_fighter=False, on_bomber=False, on_region=upper_row)
            if '灯火' in joined_ocrresult:
                print(formatted_time + "灯火专属处理")
                pyautogui.click(x, y=pyautogui.size()[1] - mouse_yaxis_coeff)
                drag_to_anyzone(on_guard=False,on_infantry=False,on_tank=False,on_head=False,on_mortar=False,
                                on_region=upper_row)
            if '3张' in joined_ocrresult:   #三选一问题,选中间
                pyautogui.moveTo(x, y=pyautogui.size()[1] - mouse_yaxis_coeff, duration=0.3)
                pyautogui.click(x, y=pyautogui.size()[1] - mouse_yaxis_coeff)
                pyautogui.dragTo(x, y=pyautogui.size()[1]//3, duration=0.5)
                time.sleep(3)
                pyautogui.click(pyautogui.size()[0] // 2, y=pyautogui.size()[1] // 3, duration=0.5)
                time.sleep(0.3)
                pyautogui.click(pyautogui.size()[0] // 2, y=pyautogui.size()[1] // 3, duration=0.5)
                print(formatted_time + "3张, 三选一问题,选中间")
            if '两栖' in joined_ocrresult or '虎!' in joined_ocrresult:  # 直接消灭对方一个攻击小于3单位
                drop_card_to_anyzone(card_index = x, on_tank=False, on_guard=False, on_region=upper_row)
                print(formatted_time + "两栖迸攻, 直接消灭对方一个攻击小于3单位")

            if any(word for word in movable_unit if word in joined_ocrresult):   #移动兵力
                print(formatted_time + "移动兵力")
                if any(word for word in ['零战', '第二挺进', '第9', '仙台'] if word in joined_ocrresult):
                    print(formatted_time + "需要二次拖放兵力, 专属处理")
                    pyautogui.click(x, y=pyautogui.size()[1] - mouse_yaxis_coeff)
                    pyautogui.dragTo((x, pyautogui.size()[1]*73//100), duration=1)  # 按照一定的顺序把牌丢出去
                    time.sleep(1)
                    pyautogui.moveTo(x, y=pyautogui.size()[1] - mouse_yaxis_coeff)
                    move_to_anyzone(on_region=upper_row)
                    pyautogui.click()
                    pyautogui.click()
                else:
                    pyautogui.moveTo(x, y=pyautogui.size()[1] - mouse_yaxis_coeff, duration=0.5)
                    pyautogui.click(x, y=pyautogui.size()[1] - mouse_yaxis_coeff)
                    pyautogui.dragTo((x, pyautogui.size()[1]//2), duration=0.5)

            else:
                if front_line_status == 2: # 敌方占领前线,往前线扔
                    drop_card_to_anyzone(card_index=x, on_head=False, on_region=lower_row)
                else:
                    drop_card_to_anyzone(card_index=x, on_head=False, on_region=upper_row)

            time.sleep(2)  # 卡牌发出, 等待过完动画
        else:
            print(formatted_time + f"当前手牌消耗{current_card_cost}高于体力{ocr_stamina},中断")
        #mouse_shake()
        #time.sleep(0.7)  # 等待过完动画
    mouse_return_home()

def play_round2(): #用于移动支援线
    #time.sleep(1)  # 等待过完动画
    check_frontline_status()  # 顺便,检查一下前线情况
    print(formatted_time +"第2轮出牌，支援线前进") #阶段2，引导坦克步兵向前线前进
    try:
        posInfantryBox = pyautogui.locateAllOnScreen(infantry_image, confidence=0.9, region=lower_row)
        posInfantryBoxFilterd = filter_boxes(posInfantryBox, 10)
        for posInfantry in posInfantryBoxFilterd:
            if check_abnormal():
                print(formatted_time + "阶段2a体力0或者发现异常， 退出")
                return
            pyautogui.click(posInfantry[0] + posInfantry[2]//2 + random.choice([-1, 1])*51, posInfantry[1]-50)
            pyautogui.dragTo((pyautogui.size()[0]//2 + random.choice([-1, 1])*random.uniform(54, 57), pyautogui.size()[1]//2), duration=random.uniform(0.2, 0.5))
            mouse_return_home()
    except Exception as e:
        print(formatted_time +"阶段2查找Infantry异常，可能目标已移动")

    try:
        posTankBox = pyautogui.locateAllOnScreen(tank_image, confidence=0.9, region=lower_row)
        posTankBoxFilterd = filter_boxes(posTankBox, 10)
        for posTank in posTankBoxFilterd:
            if check_abnormal():
                print(formatted_time + "阶段2b体力0或者发现异常， 退出")
                return
            pyautogui.click(posTank[0] + posTank[2]//2 + random.choice([-1, 1])*51, posTank[1]-50)
            pyautogui.dragTo((pyautogui.size()[0]//2 + random.choice([-1, 1])*random.uniform(54, 57), pyautogui.size()[1]//2), duration=random.uniform(0.2, 0.5))
            mouse_return_home()
    except Exception as e:
        print(formatted_time +"阶段2查找Tank异常，可能没有目标")

def play_round3(): #用于前线
    global enemy_headquarters_pos
    global front_line_status

    check_frontline_status()  # 顺便,检查一下前线情况
    if front_line_status != 2:  #0代表未知 1代表被我占领 2代表敌方占领 3代表中立
        #time.sleep(1)  # 等待过完动画
        guard_pos = check_image(guard_image, 0.84, enemy_guard_zone)
        if enemy_headquarters_pos != None or guard_pos != None: #阶段3，引导坦克步兵攻击守护单位和总部
            print(formatted_time +"第3轮出牌，前线动作")
            try:
                posInfantryBox = pyautogui.locateAllOnScreen(infantry_image, confidence=0.9, region=middle_row)
                posInfantryBoxFilterd = filter_boxes(posInfantryBox, 10)
                for posInfantry in posInfantryBoxFilterd:
                    if check_abnormal():
                        print(formatted_time + "阶段3a体力0或者发现异常， 退出")
                        return
                    pyautogui.click(posInfantry[0] + posInfantry[2]//2 + random.choice([-1, 1])*51, posInfantry[1]-50)
                    if guard_pos != None:
                        pyautogui.dragTo((guard_pos[0], guard_pos[1]), duration=random.uniform(0.2, 0.5))
                    elif enemy_headquarters_pos != None:
                        pyautogui.dragTo(enemy_headquarters_pos, duration=1)
                    mouse_return_home()
            except Exception as e:
                print(formatted_time +"阶段3查找Infantry异常，可能目标已移动")

            try:
                posTankBox = pyautogui.locateAllOnScreen(tank_image, confidence=0.9, region=middle_row)
                posTankBoxFilterd = filter_boxes(posTankBox, 10)
                for posTank in posTankBoxFilterd:
                    if check_abnormal():
                        print(formatted_time + "阶段3b体力0或者发现异常，退出")
                        return
                    pyautogui.click(posTank[0] + posTank[2]//2 + random.choice([-1, 1])*51, posTank[1]-50)
                    if guard_pos != None:
                        pyautogui.dragTo((guard_pos[0], guard_pos[1]), duration=random.uniform(0.2, 0.5))
                    elif enemy_headquarters_pos != None:
                        pyautogui.dragTo(enemy_headquarters_pos, duration=1)
                    mouse_return_home()
            except Exception as e:
                print(formatted_time +"阶段3查找Tank异常，可能目标已移动")


def play_round4():
    global front_line_status
    time.sleep(1)
    location_2_odd = [(456, 686, 24, 24), (666, 686, 24, 24), (881, 686, 24, 24), (1098, 686, 24, 24), (1311, 686, 24, 24)]
    location_2_even = [(558, 686, 24, 24), (776, 686, 24, 24), (990, 686, 24, 24), (1208, 686, 24, 24)]
    location_3_odd = [(456, 417, 24, 24), (666, 417, 24, 24), (885, 417, 24, 24), (1098, 417, 24, 24), (1311, 417, 24, 24)]
    location_3_even = [(558, 417, 24, 24), (776, 417, 24, 24), (990, 417, 24, 24), (1208, 417, 24, 24)]

    unit_secondrow = 0
    unit_thirdrow = 0

    for filename in os.listdir('./OCR'):  # '.' 表示当前目录
        if filename.startswith("ocr_unit") and os.path.isfile(os.path.join('./OCR', filename)):
            file_path = os.path.join('./OCR', filename)
            os.remove(file_path)
    check_frontline_status()
    print(formatted_time + "第4轮出牌，检查遗漏")
    infantry_count = count_unit_number(infantry_image, lower_row)
    print('infantry_count', infantry_count)
    tank_count = count_unit_number(tank_image, lower_row)
    print('tank_count', tank_count)
    fighter_count = count_unit_number(fighter_image, lower_row)
    print('fighter_count', fighter_count)
    bomber_count = count_unit_number(bomber_image, lower_row)
    print('bomber_count', bomber_count)
    mortar_count = count_unit_number(mortar_image, lower_row)
    print('mortar_count', mortar_count)
    unit_secondrow = infantry_count + tank_count + fighter_count + bomber_count + mortar_count

    grey_threshold = 0
    orange_secondrow = 0;
    unit_secondrow += 1
    match unit_secondrow:
        case 1:
            pyautogui.screenshot('OCR/ocr_unit_icon.png', region=location_2_odd[2])
            ratio, mask = calculate_orange_ratio('OCR/ocr_unit_icon.png')
            orange_secondrow += ratio
        case 2:
            for i in range(1, 3):
                screenshot = pyautogui.screenshot(f'OCR/ocr_unit_icon{i:d}.png', region=location_2_even[i])
                ratio, mask = calculate_orange_ratio(f'OCR/ocr_unit_icon{i:d}.png')
                orange_secondrow += ratio
        case 3:
            for i in range(1, 4):
                screenshot = pyautogui.screenshot(f'OCR/ocr_unit_icon{i:d}.png', region=location_2_odd[i])
                ratio, mask = calculate_orange_ratio(f'OCR/ocr_unit_icon{i:d}.png')
                orange_secondrow += ratio
        case 4:
            for i in range(0, 4):
                screenshot = pyautogui.screenshot(f'OCR/ocr_unit_icon{i:d}.png', region=location_2_even[i])
                ratio, mask = calculate_orange_ratio(f'OCR/ocr_unit_icon{i:d}.png')
                orange_secondrow += ratio
        case 5:
            for i in range(0, 5):
                screenshot = pyautogui.screenshot(f'OCR/ocr_unit_icon{i:d}.png', region=location_2_odd[i])
                ratio, mask = calculate_orange_ratio(f'OCR/ocr_unit_icon{i:d}.png')
                orange_secondrow += ratio
        case _:
            orange_secondrow = 0

    print(f"Unit 2nd: {unit_secondrow}, Orange second row: {orange_secondrow}")
    if orange_secondrow > 5: play_round2()

    if front_line_status == 1:  # 0代表未知 1代表被我占领 2代表敌方占领 3代表中立
        infantry_count = count_unit_number(infantry_image, middle_row)
        print('infantry_count', infantry_count)
        tank_count = count_unit_number(tank_image, middle_row)
        print('tank_count', tank_count)
        fighter_count = count_unit_number(fighter_image, middle_row)
        print('fighter_count', fighter_count)
        bomber_count = count_unit_number(bomber_image, middle_row)
        print('bomber_count', bomber_count)
        mortar_count = count_unit_number(mortar_image, middle_row)
        print('mortar_count', mortar_count)
        unit_thirdrow = infantry_count + tank_count + fighter_count + bomber_count + mortar_count

        orange_thirdrow = 0;
        match unit_thirdrow:
            case 1:
                pyautogui.screenshot('OCR/ocr_unit_icon.png', region=location_3_odd[2])
                ratio, mask = calculate_orange_ratio('OCR/ocr_unit_icon.png')
                orange_thirdrow += ratio
            case 2:
                for i in range(1, 3):
                    screenshot = pyautogui.screenshot(f'OCR/ocr_unit_icon{i:d}.png', region=location_3_even[i])
                    ratio, mask = calculate_orange_ratio(f'OCR/ocr_unit_icon{i:d}.png')
                    orange_thirdrow += ratio
            case 3:
                for i in range(1, 4):
                    screenshot = pyautogui.screenshot(f'OCR/ocr_unit_icon{i:d}.png', region=location_3_odd[i])
                    ratio, mask = calculate_orange_ratio(f'OCR/ocr_unit_icon{i:d}.png')
                    orange_thirdrow += ratio
            case 4:
                for i in range(0, 4):
                    screenshot = pyautogui.screenshot(f'OCR/ocr_unit_icon{i:d}.png', region=location_3_even[i])
                    ratio, mask = calculate_orange_ratio(f'OCR/ocr_unit_icon{i:d}.png')
                    orange_thirdrow += ratio
            case 5:
                for i in range(0, 5):
                    screenshot = pyautogui.screenshot(f'OCR/ocr_unit_icon{i:d}.png', region=location_3_odd[i])
                    ratio, mask = calculate_orange_ratio(f'OCR/ocr_unit_icon{i:d}.png')
                    orange_thirdrow += ratio
            case _:
                orange_thirdrow = 0
        print(f"Unit 3rd: {unit_thirdrow}, Orange 3rd Row: {orange_thirdrow}")
        if orange_thirdrow > 10: play_round3()

def drag_to_anyzone(on_guard=True, on_infantry=True, on_tank=True, on_mortar=True, on_fighter=True, on_bomber=True, on_head = True, on_region=upper_row):
    if on_guard:
        guard_pos = check_image(guard_image, 0.8, on_region)
        if guard_pos != None:
            pyautogui.dragTo((guard_pos[0],guard_pos[1]), duration=0.9)
            return
    if on_head:
        enemy_headquarters_pos = check_image(enemy_headquarters_image, 0.8, enemy_hq_zone)
        if enemy_headquarters_pos != None:
            pyautogui.dragTo(enemy_headquarters_pos, duration=1)
            return
    if on_fighter:
        fighter_pos = check_image(fighter_image, 0.8, on_region)
        if fighter_pos != None:
            pyautogui.dragTo(fighter_pos, duration=0.8)
            return
    if on_bomber:
        bomber_pos = check_image(bomber_image, 0.8, on_region)
        if bomber_pos != None:
            pyautogui.dragTo(bomber_pos, duration=0.8)
            return
    if on_mortar:
        mortar_pos = check_image(mortar_image, 0.8, on_region)
        if mortar_pos != None:
            pyautogui.dragTo(mortar_pos, duration=0.7)
            return
    if on_infantry:
        infantry_pos = check_image(infantry_image, 0.6, on_region)
        if infantry_pos != None:
            pyautogui.dragTo(infantry_pos, duration=0.6)
            return
    if on_tank:
        tank_pos = check_image(tank_image, 0.8, on_region)
        if tank_pos != None:
            pyautogui.dragTo(tank_pos, duration=0.6)
            return
    enemy_headquarters_pos = check_image(enemy_headquarters_image, 0.8, enemy_hq_zone)
    if enemy_headquarters_pos != None:
        pyautogui.dragTo(enemy_headquarters_pos, duration=1)
    return

def move_to_anyzone(on_guard=True, on_infantry=True, on_tank=True, on_mortar=True, on_fighter=True, on_bomber=True, on_head = True, on_region=upper_row):
    if on_guard:
        guard_pos = check_image(guard_image, 0.8, on_region)
        if guard_pos != None:
            pyautogui.moveTo((guard_pos[0],guard_pos[1]), duration=0.9)
            return
    if on_head:
        enemy_headquarters_pos = check_image(enemy_headquarters_image, 0.8, enemy_hq_zone)
        if enemy_headquarters_pos != None:
            pyautogui.moveTo(enemy_headquarters_pos, duration=1)
            return
    if on_fighter:
        fighter_pos = check_image(fighter_image, 0.8, on_region)
        if fighter_pos != None:
            pyautogui.moveTo(fighter_pos, duration=0.8)
            return
    if on_bomber:
        bomber_pos = check_image(bomber_image, 0.8, on_region)
        if bomber_pos != None:
            pyautogui.moveTo(bomber_pos, duration=0.8)
            return
    if on_mortar:
        mortar_pos = check_image(mortar_image, 0.8, on_region)
        if mortar_pos != None:
            pyautogui.moveTo(mortar_pos, duration=0.7)
            return
    if on_infantry:
        infantry_pos = check_image(infantry_image, 0.6, on_region)
        if infantry_pos != None:
            pyautogui.moveTo(infantry_pos, duration=0.6)
            return
    if on_tank:
        tank_pos = check_image(tank_image, 0.8, on_region)
        if tank_pos != None:
            pyautogui.moveTo(tank_pos, duration=0.6)
            return
    enemy_headquarters_pos = check_image(enemy_headquarters_image, 0.8, enemy_hq_zone)
    if enemy_headquarters_pos != None:
        pyautogui.moveTo(enemy_headquarters_pos, duration=1)
    return

def drop_card_to_anyzone(card_index=0, on_guard=True, on_infantry=True, on_tank=True, on_mortar=True, on_fighter=True, on_bomber=True, on_head = True, on_region=upper_row):
    global enemy_headquarters_pos
    global mouse_yaxis_coeff

    pyautogui.moveTo(x=card_index, y=pyautogui.size()[1] - mouse_yaxis_coeff, duration=0.3)
    pyautogui.click(x=card_index, y=pyautogui.size()[1] - mouse_yaxis_coeff)

    drag_to_anyzone(on_guard, on_infantry, on_tank, on_mortar, on_fighter, on_bomber, on_head, on_region)


def count_unit_number(unit_image, unit_region = lower_row):
    counter = 0
    try:
        posUnitBox = pyautogui.locateAllOnScreen(unit_image, confidence=0.8, region=unit_region)
        posUnitBoxFilterd = filter_boxes(posUnitBox, 10)
        for posUnit in posUnitBoxFilterd: counter += 1
    except Exception as e:
        counter += 0
    return counter


def check_abnormal_without_stemina():
    global ocr_stamina
    abnormal_state = False

    if check_image(mission_failed_image, 0.6, all_screen) != None: print(formatted_time +"检测到本局失败, 记录一下")
    if check_image(mission_passed_image, 0.6, all_screen) != None: print(formatted_time + "本局胜利")
    if check_image(duishou_img, 0.8, pass_button_region) != None: #找到对手字样
        print(formatted_time + "异常检测程序发现 [对手] 字样")
        abnormal_state = True
    if check_image(continue_button_image, 0.8, lower_half_screen) != None: #找到继续字样
        print(formatted_time + "异常检测程序发现 [继续] 字样")
        abnormal_state = True

    if check_image(reconnect_img, 0.9) != None :    #Check if 被别的设备踢出去了
        print(formatted_time+"[然然]触发了重新登陆，退出")
        if game_window != None: game_window.minimize()
        sys.exit(0)
    return abnormal_state

def check_abnormal():
    global ocr_stamina
    abnormal_state = False

    #check_frontline_status() #顺便,检查一下前线情况
    #if check_image(mission_failed_image, 0.6, all_screen) != None: print(formatted_time +"检测到本局失败, 记录一下")
    #if check_image(mission_passed_image, 0.6, all_screen) != None: print(formatted_time + "本局胜利")
    if check_image(duishou_img, 0.8, pass_button_region) != None: #找到对手字样
        print(formatted_time + "异常检测程序发现 [对手] 字样")
        return True
    if check_image(continue_button_image, 0.8, lower_half_screen) != None: #找到继续字样
        print(formatted_time + "异常检测程序发现 [继续] 字样")
        return True
    if check_orange_pass_button():
        print(formatted_time + "找到了橙色的结束按钮")
        return True
    # -------------- OCR ----------------
    if ocr_check_stamina() == 0:
        print(formatted_time + "OCR发现 [0体力]")
        return True
    #ocr_check_gameround()
    # -------------- OCR ----------------
    if check_image(reconnect_img, 0.9) != None :    #Check if 被别的设备踢出去了
        print(formatted_time+"[然然]触发了重新登陆，退出")
        if game_window != None: game_window.minimize()
        sys.exit(0)
    return abnormal_state

def check_frontline_status():
    global front_line_status
    global front_line_diff_threshold
    global front_line_upper_base
    global front_line_lower_base

    mouse_return_home() #避开遮挡
    time.sleep(0.2)

    ocrimage = pyautogui.screenshot('OCR/ocr_frontline1.png', region=front_line_upper_region)
    try:
        ratio, mask = calculate_black_ratio('OCR/ocr_frontline1.png')
    except Exception as e:
        ratio = 0
    gray_mean_upper = ratio

    ocrimage = pyautogui.screenshot('OCR/ocr_frontline2.png', region=front_line_lower_region)
    try:
        ratio, mask = calculate_black_ratio('OCR/ocr_frontline2.png')
    except Exception as e:
        ratio = 0
    gray_mean_lower = ratio

    front_line_status = 0
    if gray_mean_upper > front_line_diff_threshold:  #3代表中立 1代表被我占领 2代表敌方占领 0代表未知
        front_line_status = 1
    elif gray_mean_lower > front_line_diff_threshold:
        front_line_status = 2
    else:
        front_line_status = 3
    print(formatted_time+f"上方前线黑色度: {gray_mean_upper: .2f} ,下方前线黑色度: {gray_mean_lower: .2f} ,前线状态: " + frontline_status[front_line_status])
    return




def check_image(image_name, confidence_level, detect_region=all_screen, step_opt=0.05, grayscale_opt=False, failcount = 3):  # 图像查找包装程序
    global return_img_pos
    i = 1.0
    failsafe_counter = 0
    #time.sleep(0.1)
    while True:
        i = i - step_opt
        #return_img_pos = None
        return_img_pos = None
        failsafe_counter += 1
        if failsafe_counter > failcount:
            #print(formatted_time + f'查找 {image_name} 超过次数限制')
            return None
        try:
            return_img_pos = pyautogui.locateCenterOnScreen(image_name, confidence=i, region=detect_region, grayscale=grayscale_opt)
        except Exception as e:
            #print(formatted_time + f'没找到图片, confi= {i:.2f}')
            i = i - step_opt
            return_img_pos = None
            #return None
        if return_img_pos != None:
            send_back = [0, 0]
            send_back[0] = int(return_img_pos[0])
            send_back[1] = int(return_img_pos[1])
            print(formatted_time + f'找到 {image_name} -> confi level= {i:.2f}')
            if image_name == enemy_headquarters_image: send_back[1] -= 40
            if image_name == guard_image:
                send_back[0] -= 105
                send_back[1] -= 84
            if image_name in [infantry_image, tank_image, fighter_image, bomber_image, mortar_image]:
                #print('buchang unit')
                send_back[1] -= 90
            return_img_pos = send_back
            return send_back
        elif i <= confidence_level:
            return_img_pos = None
            #print(formatted_time + f'查找 {image_name} 尝试了所有精度')
            return None

def mouse_return_home():
    pyautogui.moveTo(1511 + random.uniform(-50, 50), 1027 + random.uniform(-50, 50), duration=random.uniform(0.2, 0.5))  # 移动鼠标不遮挡屏幕

def mouse_shake():
    pyautogui.move(random.uniform(-30, 30), random.uniform(-30, 0), duration=random.uniform(0.2, 0.5))  # 移动

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
        #pyautogui.moveTo(pyautogui.size()[0] // 2+ random.uniform(-200, 200), pyautogui.size()[1] // 2+ random.uniform(-200, 200), duration=random.uniform(0.2, 0.5))
        pyautogui.moveTo( (return_img_pos[0] + random.uniform(-10, 10),return_img_pos[1] + random.uniform(-10, 10)), duration=random.uniform(0.2, 0.5))
        #time.sleep(0.2)
        pyautogui.click(return_img_pos)
        pyautogui.click(return_img_pos)
        print(formatted_time+output_string)
        if reset_stage:
            reset_game_stage()
        return True
    else:
        return False


def calculate_orange_ratio(image_path):
    orange_ratio, orange_mask = calculate_color_ratio(image_path, np.array([16, 100, 100]), np.array([25, 255, 255]))
    #print(f'Orange: {orange_ratio:.2f}')
    return orange_ratio, orange_mask

def calculate_black_ratio(image_path):
    black_ratio, black_mask = calculate_color_ratio(image_path, np.array([0, 0, 0]), np.array([180, 255, 40]))
    #print(f'Black: {black_ratio:.2f}')
    return black_ratio, black_mask

def calculate_grey_ratio(image_path):
    grey_ratio, grey_mask = calculate_color_ratio(image_path, np.array([20, 10, 30]), np.array([50, 40, 70]))
    print(f'Grey: {grey_ratio:.2f}')
    return grey_ratio, grey_mask

def calculate_color_ratio(image_path, lower_threshold, upper_threshold):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"无法读取图像: {image_path}")
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    color_mask = cv2.inRange(hsv_image, lower_threshold, upper_threshold)
    color_pixels = cv2.countNonZero(color_mask)
    total_pixels = image.shape[0] * image.shape[1]
    color_ratio = (color_pixels / total_pixels) * 100
    return color_ratio, color_mask

def ocr_check_stamina(): #Check Stamina by using OCR
    global ocr_stamina
    ocrimage = pyautogui.screenshot('ocr_stamina.png', region=ocr_stamina_region)
    ocrresult = ocrscanner.readtext('ocr_stamina.png', ['ru','en'], mag_ratio=0.5, detail=0, allowlist ='0123456789')
    if ocrresult:
        #print(formatted_time + 'OCR stamina: ' + ocrresult[0])
        try:
            ocr_stamina = int(float(ocrresult[0]))
        except Exception as e:
            ocr_stamina = 0
    return ocr_stamina

def ocr_check_gameround(): #Check Stamina by using OCR
    global ocr_gameround
    ocrimage = pyautogui.screenshot('ocr_gameround.png', region=ocr_game_round_region)
    ocrresult = ocrscanner.readtext('ocr_gameround.png', ['ru','en'], mag_ratio=1.5, detail=0, allowlist ='0123456789')
    if ocrresult:
        print(formatted_time + 'OCR Game Round: ' + ocrresult[0])
        try:
            ocr_gameround = int(float(ocrresult[0]))
        except Exception as e:
            ocr_gameround = 0
    return ocr_gameround

def ocr_check_card_cost():
    global return_img_pos
    global current_card_cost
    global kmark_location

    check_image(kmark_image, confidence_level=0.9, step_opt=0.01, failcount=20,detect_region=card_search_region)
    if return_img_pos != None:
        kmark_location = (int(return_img_pos[0]) , int(return_img_pos[1]))
        x1 = int(return_img_pos[0] - 43)
        y1 = int(return_img_pos[1] - 5)
        crop_region = (x1, y1, 33, 50)
        ocrimage = pyautogui.screenshot('ocr_cardcost.png', region=crop_region)
        try:
            ratio, mask = calculate_orange_ratio('ocr_cardcost.png')
        except Exception as e: pass
        if ratio < 10:
            print(formatted_time + f"橙色所占比例: {ratio:.1f}%, 灰色数字卡牌直接跳过")
            current_card_cost = 99  # 未找到卡消耗,给一个假的
            return current_card_cost
        else:
            print(formatted_time +f"橙色所占比例: {ratio:.1f}%, 橙色卡牌通过,继续OCR")
            ocrresult = ocrscanner.readtext('ocr_cardcost.png', ['ru', 'en'], mag_ratio=1, detail=0, allowlist='0123456789')
            if ocrresult != []:
                joined_ocrresult = ''.join(ocrresult)
                current_card_cost = int((joined_ocrresult))
                return current_card_cost
                # print('Current Card Cost Found: ' + joined_ocrresult)
            else:
                current_card_cost = 99 #未找到卡消耗,给一个假的
                return current_card_cost
    else:
        current_card_cost = 99  # 未找到卡消耗,给一个假的
        kmark_location = (0,0)
        return current_card_cost

def check_orange_pass_button():

    ocrimage = pyautogui.screenshot('OCR/ocr_orange_pass.png', region=pass_button_region)
    try:
        ratio, mask = calculate_orange_ratio('OCR/ocr_orange_pass.png')
    except Exception as e:
        pass
    print(formatted_time + f"按钮区域橙色含量 {ratio:.1f}%")
    if ratio > 5:
        return True
    else:
        return False

def reset_game_stage():
    global game_stage
    global ocr_gameround
    global round_start_time
    game_stage = 0
    ocr_gameround = 0
    round_start_time = time.time()
    round_total_start_time = time.time()


#-----------------------------------------------MAIN---------------------------------------------------
def main():
    global game_stage
    global formatted_time
    global enemy_headquarters_pos
    global round_total_start_time
    global game_window

    game_active = False
    round_total_start_time = time.time()
    reset_game_stage()
    print(" -- KARDs 1939 Better AFK, Ver 250802a by Eason -- ")
    debug_testing()
    setup_logging()
    while True:
        now = datetime.now()
        formatted_time = now.strftime('%m-%d %H:%M:%S -- ')
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



#-------------------------------------------MAIN, Bro Out-----------------------------------------------


def debug_testing():
    global formatted_time
    global return_img_pos

    if False:#For debugging
        now = datetime.now()
        formatted_time = now.strftime("DEBUG Session " + '%m-%d %H:%M:%S -- ')
# ---------------- Debug Section Start --------------------
        play_round4()
# ---------------- Debug Section End --------------------
        print("Forever Loop")
        while True: pass

if __name__ == "__main__":
    main()