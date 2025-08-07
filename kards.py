import pyautogui, time, datetime, pygetwindow as gw, random, sys, easyocr, keyboard, math
from datetime import datetime
import re, cv2, numpy as np, os

pyautogui.FAILSAFE = False
# 安装命令：
# pip install pyScreeze numpy opencv_python PyAutoGUI PyGetWindow Pillow easyocr cv2 keyboard

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
chat_list = "Resource/chat_kuang.png"
training_start = "Resource/training_start.png"
card_kmark_small_tiltleft = "Resource/card_kmark_small_tiltleft.png"
card_kmark_small_middle = "Resource/card_kmark_small_middle.png"
card_kmark_small_tiltright = "Resource/card_kmark_small_tiltright.png"
frontline_downmark = "Resource/frontline_down.png"
frontline_upmark = "Resource/frontline_up.png"

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
pass_fail_region = (786, 568, 358, 223) #胜利失败判断区域

upper_row = (pyautogui.size()[0]*419//1920, pyautogui.size()[1]*135//1080, 1120, 240) #敌方支援区域
middle_row = (pyautogui.size()[0]*419//1920, pyautogui.size()[1]*401//1080, 1120, 240) #前线区域
lower_row = (pyautogui.size()[0]*419//1920, pyautogui.size()[1]*672//1080, 1120 , 240) #支援战线区域
upper_row_typeiconzone = (pyautogui.size()[0]*419//1920, pyautogui.size()[1]*303//1080, 1120, 70) #敌方支援图标区域
middle_row_typeiconzone = (pyautogui.size()[0]*419//1920, pyautogui.size()[1]*564//1080, 1120, 70) #前线图标区域
lower_row_typeiconzone = (pyautogui.size()[0]*419//1920, pyautogui.size()[1]*839//1080, 1120 , 70) #支援战线图标区域

enemy_zone = [upper_row, lower_row]
enemy_guard_zone = (pyautogui.size()[0]*431//1920, pyautogui.size()[1]*129//1080, 1075, 161) #敌方支援状态区域
enemy_hq_zone = (pyautogui.size()[0]*411//1920, pyautogui.size()[1]*254//1080, 1120, 60) #敌方总部图标区域
ocr_stamina_region = (32, 849, 53, 76) #体力数值区域
ocr_game_round_region = (80, 890, 30, 30) #左下角的指令槽区域
front_line_upper_region = (420, 370, 1000, 37) #上面前线条表达区域
front_line_lower_region = (420, 635, 1000, 37) #下面前线条表达区域
card_search_region = (pyautogui.size()[0]*10//100, pyautogui.size()[1]*30//100, pyautogui.size()[0]*80//100,\
                      pyautogui.size()[1]*70//100)#卡牌详细信息的搜索区域
springboard_region = (433, 930, 1064, 150)
#Global Veriables
ocrscanner = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
failsafe_counter = 0
ocr_stamina = 0
front_line_status = 3  #0代表未知 1代表被我占领 2代表敌方占领 3代表中立

game_stage = 0
ocr_stamina = 0
mouse_x = 0
enemy_headquarters_pos = None
current_card_cost = 1
frontline_status = ['状态未知','我方占领','敌方占领','无人占领']
kmark_location = (0,0)
ocr_gameround = 0
round_finished = False
round_single_time = 0
we_have_airforce = False
card_search_counter = 0
single_round_time_limit = 35

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



class Box:
    def __init__(self, left, top, width, height):
        self.left = int(left)  # 确保是 int 类型
        self.top = int(top)  # 确保是 int 类型
        self.width = width
        self.height = height
    def __repr__(self):
        return f"Box(left={self.left}, top={self.top}, width={self.width}, height={self.height})"



def count_unit_number(unit_image, unit_region = lower_row):
    counter = 0
    try:
        posUnitBox = pyautogui.locateAllOnScreen(unit_image, confidence=0.8, region=unit_region)
        posUnitBoxFilterd = filter_boxes(posUnitBox, 10)
        for posUnit in posUnitBoxFilterd: counter += 1
    except Exception as e:
        counter += 0
    return counter


def check_abnormal(check_orange_passbutton = True):
    global ocr_stamina
    global round_finished
    global round_single_time

    #check_frontline_status() #顺便,检查一下前线情况
    if check_mission_passfail():
        round_finished = True
        return True

    round_single_time = time.time() - round_start_time

    if round_finished and check_orange_passbutton: return True

    #if round_single_time > single_round_time_limit:
    #    print(formatted_time + "检测到本轮超时了, 直接中断")
    #    round_finished = True
    #    return True

    if check_orange_pass_button() and check_orange_passbutton:
        print(formatted_time + "找到了橙色的结束按钮")
        round_finished = True
        return True

    if check_image(duishou_img, 0.8, pass_button_region) != None: #找到对手字样
        print(formatted_time + "异常检测程序发现 [对手] 字样")
        round_finished = True
        return True
    if check_image(continue_button_image, 0.8, lower_half_screen) != None: #找到继续字样
        print(formatted_time + "异常检测程序发现 [继续] 字样")
        round_finished = True
        return True

    """
    # -------------- OCR ----------------
    if ocr_check_stamina() == 0:
        print(formatted_time + "OCR发现 [0体力]")
        return True
    #ocr_check_gameround()
    # -------------- OCR ----------------
    """
    if keyboard.is_pressed('f9'):
        print(formatted_time + "检测到F9查询按下, 程序中断退出")
        round_finished = True
        sys.exit(0)
    return False

def check_frontline_status():
    global front_line_status
    front_line_diff_threshold = 7

    mouse_return_right() #避开遮挡
    time.sleep(0.2)

    front_up = check_image(frontline_upmark, confidence_level=0.5, detect_region=front_line_lower_region, grayscale_opt=True)
    front_down = check_image(frontline_downmark, confidence_level=0.5, detect_region=front_line_lower_region,
                           grayscale_opt=True)

    front_line_status = 3
    if front_up != None and front_down == None:
        front_line_status = 1
        print(formatted_time + f"图像检测得出前线 我方占领")
    elif front_up == None and front_down != None:
        print(formatted_time + f"图像检测得出前线 敌方")
        front_line_status = 2
    else:
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
        if gray_mean_upper > gray_mean_lower and \
                abs(gray_mean_upper-gray_mean_lower) > front_line_diff_threshold:  #3代表中立 1代表被我占领 2代表敌方占领 0代表未知
            front_line_status = 1
        elif gray_mean_upper < gray_mean_lower and \
                abs(gray_mean_upper-gray_mean_lower) > front_line_diff_threshold:
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
            if image_name == enemy_headquarters_image: send_back[1] -= 30
            if image_name == guard_image:
                send_back[0] -= 60
                send_back[1] += 30
            if image_name in [infantry_image, tank_image, fighter_image, bomber_image, mortar_image]:
                #print('buchang unit')
                send_back[1] -= 70
            return_img_pos = send_back
            return send_back
        elif i <= confidence_level:
            return_img_pos = None
            #print(formatted_time + f'查找 {image_name} 尝试了所有精度')
            return None

def check_orange_pass_button():
    ocrimage = pyautogui.screenshot('OCR/ocr_orange_pass.png', region=pass_button_region)
    try:
        ratio, mask = calculate_orange_ratio('OCR/ocr_orange_pass.png')
    except Exception as e:
        pass
    #print(formatted_time + f"按钮区域橙色含量 {ratio:.1f}%")
    if ratio > 5:
        return True
    else:
        return False

def check_mission_passfail():
    if check_image(mission_failed_image, 0.7, pass_fail_region) != None:
        print(formatted_time +"检测到本局失败 等待人工处理")
        time.sleep(15)
        return True
    if check_image(mission_passed_image, 0.7, pass_fail_region) != None:
        print(formatted_time + "检测到本局胜利 等待人工处理")
        time.sleep(15)
        return True

def check_unit_type(check_region):
    if check_image(infantry_image, 0.8, detect_region=check_region): return 'infantry'
    if check_image(tank_image, 0.8, detect_region=check_region): return 'tank'
    if check_image(fighter_image, 0.8, detect_region=check_region): return 'fighter'
    if check_image(bomber_image, 0.8, detect_region=check_region): return 'bomber'
    if check_image(mortar_image, 0.8, detect_region=check_region): return 'mortar'
    return None


def calculate_orange_ratio(image_path):
    orange_ratio, orange_mask = calculate_color_ratio(image_path, np.array([16, 100, 100]), np.array([25, 255, 255]))
    #print(f'Orange: {orange_ratio:.2f}')
    return orange_ratio, orange_mask

def calculate_black_ratio(image_path):
    black_ratio, black_mask = calculate_color_ratio(image_path, np.array([0, 0, 0]), np.array([180, 255, 50]))
    #print(f'Black: {black_ratio:.2f}')
    return black_ratio, black_mask

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


def error_handling(input_img = start_scale125_img, output_string = "Error Handling", confi_level = 0.9, reset_stage = False, search_pos = all_screen):
    global return_img_pos
    if check_image(input_img, confi_level, search_pos) != None :
        #pyautogui.moveTo(pyautogui.size()[0] // 2+ random.uniform(-200, 200), pyautogui.size()[1] // 2+ random.uniform(-200, 200), duration=random.uniform(0.2, 0.5))
        pyautogui.moveTo( (return_img_pos[0] + random.uniform(-10, 10),return_img_pos[1] + random.uniform(-10, 10)), duration=random.uniform(0.2, 0.5))
        #time.sleep(0.2)
        pyautogui.click(return_img_pos)
        #pyautogui.click(return_img_pos)
        print(formatted_time+output_string)
        if reset_stage:
            reset_game_stage()
        return True
    else:
        return False


def filter_boxes(raw_data, threshold):
    filtered_boxes = []
    for box in raw_data:
        if all(abs(box.left - other.left) >= threshold or abs(box.top - other.top) >= threshold for other in
               filtered_boxes):
            filtered_boxes.append(box)
    return filtered_boxes


def find_ordered_keywords(text, kw1="", kw2="", kw3="", kw4="", kw5=""):
    keywords = [kw for kw in [kw1, kw2, kw3, kw4, kw5] if kw]
    if not keywords:
        return None
    escaped_kw = [re.escape(kw) for kw in keywords]
    pattern = r'.*?'.join(escaped_kw)
    pattern = f'.*?{pattern}.*?'
    match = re.search(pattern, text, re.DOTALL)  # re.DOTALL让.匹配包括换行符在内的所有字符
    return match.group() if match else None

def gameround_timeout_bug_reset():  # 有时候20s倒计时失效，此时单手超过4分钟以后选择自爆
    if check_image(gear_img, 0.8, ninegong_zone3) != None:
        pyautogui.moveTo(return_img_pos, duration=random.uniform(0.2, 0.5))
        time.sleep(0.2)
        pyautogui.click(return_img_pos)
        time.sleep(0.2)
        reset_game_stage()

    if check_image(self_destruct_img, 0.8, ninegong_zone3) != None:
        pyautogui.moveTo(return_img_pos, duration=random.uniform(0.2, 0.5))
        time.sleep(0.2)
        pyautogui.click(return_img_pos)
        print(formatted_time + "卡死太久，自爆结束")
        reset_game_stage()
    return

def handle_old_log(log_filename="run_log.txt"):
    """处理已存在的旧日志文件"""
    if os.path.exists(log_filename):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        old_log_filename = f"log_{timestamp}.txt"
        os.rename(log_filename, old_log_filename)


def is_target_pattern(region,  # 待检测区域 (x, y, width, height)
                      # 调整墨绿色范围（基于69,68,58，允许±10的波动）
                      dark_green_range=((40, 35, 15), (79, 78, 68)),
                      # 调整橙色范围（基于224,177,80，允许±15的波动）
                      orange_range=((200, 140, 25), (239, 192, 95)),
                      bg_threshold=0.24,  # 适当降低阈值，应对可能的边缘轻微变色
                      min_orange_pixels=20,  # 数字可能较小，减少最小像素要求
                      ):
    """
    检测指定屏幕区域是否符合：深墨绿色底色 + 橙色数字
    返回：符合条件则返回True，否则False
    """
    screenshot = pyautogui.screenshot(region=region)
    img = screenshot.convert('RGB')
    pixels = np.array(img)
    dg_low, dg_high = dark_green_range
    is_dark_green = (pixels[:, :, 0] >= dg_low[0]) & (pixels[:, :, 0] <= dg_high[0]) & (pixels[:, :, 1] >= dg_low[1]) & (pixels[:, :, 1] <= dg_high[1]) & (pixels[:, :, 2] >= dg_low[2]) & (pixels[:, :, 2] <= dg_high[2])
    dark_green_count = np.sum(is_dark_green)
    total_pixels = pixels.shape[0] * pixels.shape[1]
    dark_green_ratio = dark_green_count / total_pixels
    o_low, o_high = orange_range
    is_orange = (pixels[:, :, 0] >= o_low[0]) & (pixels[:, :, 0] <= o_high[0]) & (pixels[:, :, 1] >= o_low[1]) & (pixels[:, :, 1] <= o_high[1]) & (pixels[:, :, 2] >= o_low[2]) & (pixels[:, :, 2] <= o_high[2])  # B通道
    orange_count = np.sum(is_orange)
    return_value = (dark_green_ratio > bg_threshold) and (orange_count > min_orange_pixels)
    print(formatted_time+f"底色要{bg_threshold:.0%},实际{dark_green_ratio:.0%},橙色要{min_orange_pixels}px,实际{orange_count}px, 返回:{return_value}")
    return return_value

def mouse_return_right():
    pyautogui.click(1427 + random.uniform(-10, 10), 1000 + random.uniform(-30, 0))  # 移动鼠标不遮挡屏幕

def mouse_return_left():
    pyautogui.click(496 + random.uniform(-10, 10), 1000 + random.uniform(-30, 0))  # 移动鼠标不遮挡屏幕

def mouse_shake():
    pyautogui.mouseDown()
    pyautogui.move(10, 0)


def ocr_check_stamina(): #Check Stamina by using OCR
    global ocr_stamina
    ocrimage = pyautogui.screenshot('OCR/ocr_stamina.png', region=ocr_stamina_region)
    ocrresult = ocrscanner.readtext('OCR/ocr_stamina.png', ['ru','en'], mag_ratio=0.5, detail=0, allowlist ='0123456789')
    if ocrresult:
        #print(formatted_time + 'OCR stamina: ' + ocrresult[0])
        try:
            ocr_stamina = int(float(ocrresult[0]))
        except Exception as e:
            ocr_stamina = 0
    return ocr_stamina

def ocr_check_gameround(): #Check Stamina by using OCR
    global ocr_gameround
    ocrimage = pyautogui.screenshot('OCR/ocr_gameround.png', region=ocr_game_round_region)
    ocrresult = ocrscanner.readtext('OCR/ocr_gameround.png', ['ru','en'], mag_ratio=1.5, detail=0, allowlist ='0123456789')
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

    check_image(kmark_image, confidence_level=0.83, step_opt=0.05, failcount=6,detect_region=card_search_region)
    if return_img_pos != None:
        kmark_location = (int(return_img_pos[0]) , int(return_img_pos[1]))
        x1 = int(return_img_pos[0] - 40)
        y1 = int(return_img_pos[1] - 2)
        crop_region = (x1, y1, 31, 47)
        ocrimage = pyautogui.screenshot('OCR/ocr_cardcost.png', region=crop_region)
        try:
            ratio, mask = calculate_orange_ratio('OCR/ocr_cardcost.png')
        except Exception as e: pass
        if ratio < 10:
            print(formatted_time + f"橙色所占比例: {ratio:.1f}%, 灰色数字卡牌直接跳过")
            current_card_cost = 99  # 未找到卡消耗,给一个假的
            return current_card_cost
        else:
            print(formatted_time +f"橙色所占比例: {ratio:.1f}%, 橙色卡牌通过,继续OCR")
            ocrresult = ocrscanner.readtext('OCR/ocr_cardcost.png', ['ru', 'en'], mag_ratio=1, detail=0, allowlist='0123456789')
            if ocrresult != []:
                joined_ocrresult = ''.join(ocrresult)
                if joined_ocrresult and joined_ocrresult.strip():
                    current_card_cost = int(joined_ocrresult.strip())
                else:
                    current_card_cost = 99
                    print("警告：OCR结果为空，无法转换为整数")
                return current_card_cost
                # print('Current Card Cost Found: ' + joined_ocrresult)
            else:
                current_card_cost = 99 #未找到卡消耗,给一个假的
                return current_card_cost
    else:
        current_card_cost = 99  # 未找到卡消耗,给一个假的
        kmark_location = (0,0)
        return current_card_cost
def pixel_distance(x1, y1, x2, y2):
    """计算两个像素点(x1,y1)和(x2,y2)之间的直线距离"""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)** 2)

def reset_game_stage():
    global enter_game_seq
    global ocr_gameround
    global round_start_time
    global round_total_start_time
    global round_finished
    global round_single_time
    round_finished = False
    round_single_time = 0
    enter_game_seq = 0
    ocr_gameround = 0
    round_start_time = time.time()
    round_total_start_time = time.time()

def setup_logging(log_filename="run_log.txt"):
    handle_old_log(log_filename)
    sys.stdout = LogRedirector(log_filename)
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def send_message():
    want_to = random.randint(0, 100)
    if want_to > 80 or ocr_gameround <=1 :
        time.sleep(0.5)
        if check_image(msg_img, 0.9, right_onethird_screen) != None :
            if ocr_gameround <= 1: random_msg_number = 1
            else: random_msg_number = random.choice([3,5])
            pyautogui.moveTo(return_img_pos, duration=0.5)
            time.sleep(0.5)
            pyautogui.click(return_img_pos)
            time.sleep(0.5)
            if check_image(chat_list, 0.9, right_onethird_screen)!= None:
                pyautogui.moveTo((return_img_pos[0], return_img_pos[1]), duration=0.3)
                pyautogui.move(38, -32, duration=0.4)
                print(formatted_time+f"开始插入聊天，聊第{random_msg_number}条天") #开局只能发第一条
                pyautogui.move(0, 32 * (random_msg_number-1), duration=0.6)
                pyautogui.click()
                time.sleep(0.5)

def try_restart():
    error_handling(start_scale125_img, "找到重新开始DPI 125%，点击") #启动器按钮写的太shit
    error_handling(start_scale100_img, "找到重新开始DPI 100%，点击")


# --------------------------- Below are functions that not sorted by first alphabet (Need freqently modify)----------------

def out_of_gameround_checking_routine():
    global enter_game_seq
    global round_start_time  # 本手起始时间
    global logger
    global round_total_time  # 本局总时间
    global round_total_start_time  # 本局起始时间
    global failsafe_counter
    global game_window
    global round_single_time

    round_single_time = time.time() - round_start_time
    round_total_time = time.time() - round_total_start_time
    print(
        formatted_time + f"开始跑流程:{enter_game_seq},轮次:{ocr_gameround},本轮耗时{round_single_time:.0f}秒，本局耗时{round_total_time:.0f}秒,前线状态:" +
        frontline_status[front_line_status])  # enter_game_seq保证了进入对局的点击顺序

    if round_single_time > 60 * 3:  # 游戏倒计时超时以后bug处理
        gameround_timeout_bug_reset()


    if enter_game_seq == 0:  # 查找左上角游戏图标和点击开始按钮
        if check_image(main_menu_start_button_image, 0.9, left_onethird_screen) != None or check_image(
                main_menu_button_image, 0.9, left_onethird_screen) != None:
            #pyautogui.moveTo(pyautogui.size()[0] // 2 + random.uniform(-200, 200),
            #                 pyautogui.size()[1] // 2 + random.uniform(-200, 200), duration=0.7)
            pyautogui.moveTo(return_img_pos, duration=random.uniform(0.2, 0.5))
            time.sleep(0.2)
            pyautogui.click(return_img_pos)
            pyautogui.click(return_img_pos)
            time.sleep(0.2)
            failsafe_counter = 0
            if check_image(exp_image, 0.7, all_screen, grayscale_opt=True) != None:
                enter_game_seq = 1
            print(formatted_time + "点击主屏幕开始按钮")

    if enter_game_seq == 1:  # 点击包含‘经验’二字的卡组
        failsafe_counter += 1
        if failsafe_counter >= 5:
            enter_game_seq = 0
            return
        if check_image(exp_image, 0.7, all_screen, grayscale_opt=True) != None:
            pyautogui.moveTo(return_img_pos, duration=random.uniform(0.2, 0.5))
            pyautogui.click(return_img_pos)
            failsafe_counter = 0
            enter_game_seq = 2

    if enter_game_seq == 2:  # 点击右侧的休闲模式，避免进入排位模式
        failsafe_counter += 1
        if failsafe_counter >= 5:
            enter_game_seq = 0
            return
        if error_handling(xiuxian_image, "点击休闲模式", 0.8, False, right_onethird_screen): #进入休闲
        #if error_handling(training_start, "点击休闲模式", 0.8, False): #进去训练模式 modmod
            failsafe_counter = 0
            enter_game_seq = 3

    if enter_game_seq == 3:  # 点击右侧开始
        failsafe_counter += 1
        if failsafe_counter >= 5:
            enter_game_seq = 0
            return
        error_handling(clicked_start_game_button, "点击右下开始按钮", 0.8, False, right_onethird_screen)

    if check_image(renji_img, 0.7, lower_half_screen) != None:
        error_handling(renji_img, "找到超时人机选项，点击", 0.8, True, lower_half_screen)
        mouse_return_right()
    if check_image(confirm_button_image, 0.7, lower_half_screen) != None:
        error_handling(confirm_button_image, "点击了选牌以后的确认键", 0.7, True, lower_half_screen)
        mouse_return_right()
        round_start_time = time.time()
        round_total_start_time = time.time()
    if check_image(reconnect_img, 0.9) != None:  # Check if 被别的设备踢出去了
        print(formatted_time + "[然然]触发了重新登陆，退出")
        if game_window != None: game_window.minimize()
        sys.exit(0)

    check_mission_passfail()

    error_handling(continue_button_image, "点击了继续按钮, 结束战斗（一般是输了）", 0.7, reset_stage=True)

    error_handling(get_gold, "找到今日金币字样，点击")

    error_handling(restart_img, "找到重新连接字样，点击")

    error_handling(disconnect_img, "找到退出(2)字样，点击")

    #    error_handling(training_start, "找到教学关开始按钮，点击")

    error_handling(close_Ad_button_image, "找到了广告，点击叉子")

    error_handling(net_restart_image, confi_level=0.7, output_string="找到 网络 重启框，点击重启")

    if check_image(daily_mission_button_image, 0.7, lower_half_screen) != None:
        pyautogui.moveTo((pyautogui.size()[0] * 90 // 100, pyautogui.size()[1] * 90 // 100),
                         duration=random.uniform(0.2, 0.5))
        pyautogui.click((pyautogui.size()[0] * 90 // 100, pyautogui.size()[1] * 90 // 100))
        pyautogui.click((pyautogui.size()[0] * 90 // 100, pyautogui.size()[1] * 90 // 100))
        print(formatted_time + "跳出了今日任务，点击屏幕右下角忽略")

    if check_image(reconnect_img, 0.9) != None:
        print(formatted_time + "然然触发了游戏重新登陆，脚本退出")
        if game_window != None: game_window.minimize()
        # logger.close()
        sys.exit(0)

def begin_new_game_routine():
    global round_start_time
    global round_finished
    global round_single_time
    global card_search_counter

    if check_image(pass_turn_button_image, 0.8, right_onethird_screen) != None or check_image(end_turn_button_image, 0.7, right_onethird_screen) != None:
        pass_button_pos = return_img_pos
        print(formatted_time+"找到我方回合按钮，开始打牌")

        #reset_game_stage()
        round_start_time = time.time()
        round_finished = False
        time.sleep(3)# 等待过完讨厌的动画
        ocr_check_gameround()

        counter = 0
        card_search_counter = 0
        # 出牌处理 共运行3轮
        while round_single_time < single_round_time_limit and (not round_finished) and counter < 3:
            #print(formatted_time+f'对决时间:  {round_single_time:.0f}秒')
            play_round2()
            play_round1()
            play_round2()
            round_single_time = time.time() - round_start_time
            counter += 1

        #打完了
        #pyautogui.moveTo(pass_button_pos[0]+ random.uniform(-150, -120), pass_button_pos[1]+ random.uniform(0, 50), duration=random.uniform(0.4, 0.7))
        pyautogui.moveTo(pass_button_pos, duration=random.uniform(0.2, 0.5))
        if check_abnormal(check_orange_passbutton=False):
            mouse_return_right()
            return
        pyautogui.click(pass_button_pos)
        pyautogui.click(pass_button_pos)
        print(formatted_time+"点击了空过按钮")
#--------------- After Clicking Pass Button ----------------
        send_message()
        mouse_return_right()
        ocr_check_gameround()
        check_frontline_status()
        round_start_time = time.time()
        round_finished = False

def move_drag_to_any_target(target_type = 'ghfbmit89', target_zone='u', drag_is_True = True):
    global return_img_pos

    drag_speed_base = 1.8
    for zone_number in target_zone:
        if zone_number == 'u': on_region = upper_row
        elif zone_number == 'm': on_region = middle_row
        else: on_region = lower_row

        if zone_number == 'l':
            bak_mouse_pos = pyautogui.position()
            if pyautogui.position()[0] < pyautogui.size()[0]//2: mouse_return_left()
            else: mouse_return_right()

        for digit_char in target_type:
            match digit_char:
                case 'g':
                    if check_image(guard_image, 0.8, on_region) != None:
                        drag_speed = drag_speed_base * pixel_distance(pyautogui.position()[0], \
                                                                      pyautogui.position()[1], return_img_pos[0],
                                                                      return_img_pos[1]) / 1000
                        if zone_number == 'l': pyautogui.click(bak_mouse_pos,duration=0.5)
                        mouse_shake()
                        pyautogui.moveTo(return_img_pos, duration=drag_speed)
                        pyautogui.mouseUp()
                        return [target_type, target_zone]
                case 'h':
                    if zone_number == 'u':
                        if check_image(enemy_headquarters_image, 0.8, enemy_hq_zone) != None:
                            if zone_number == 'l': pyautogui.click(bak_mouse_pos)
                            drag_speed = drag_speed_base * pixel_distance(int(pyautogui.position()[0]),\
                                      int(pyautogui.position()[1]), int(return_img_pos[0]), int(return_img_pos[1])) / 1000
                            mouse_shake()
                            pyautogui.moveTo(return_img_pos, duration=drag_speed)
                            pyautogui.mouseUp()
                            return [target_type, target_zone]
                case 'f':
                    if check_image(fighter_image, 0.8, on_region) != None:
                        if zone_number == 'l': pyautogui.click(bak_mouse_pos)
                        drag_speed = drag_speed_base * pixel_distance(pyautogui.position()[0],\
                                  pyautogui.position()[1], return_img_pos[0], return_img_pos[1]) / 1000
                        mouse_shake()
                        pyautogui.moveTo(return_img_pos, duration=drag_speed)
                        pyautogui.mouseUp()
                        return [target_type, target_zone]
                case 'b':
                    if check_image(bomber_image, 0.8, on_region) != None:
                        if zone_number == 'l': pyautogui.click(bak_mouse_pos)
                        drag_speed = drag_speed_base * pixel_distance(pyautogui.position()[0],\
                                  pyautogui.position()[1], return_img_pos[0], return_img_pos[1]) / 1000
                        mouse_shake()
                        pyautogui.moveTo(return_img_pos, duration=drag_speed)
                        pyautogui.mouseUp()
                        return [target_type, target_zone]
                case 'm':
                    if check_image(mortar_image, 0.8, on_region) != None:
                        if zone_number == 'l': pyautogui.click(bak_mouse_pos)
                        drag_speed = drag_speed_base * pixel_distance(pyautogui.position()[0],\
                                  pyautogui.position()[1], return_img_pos[0], return_img_pos[1]) / 1000
                        mouse_shake()
                        pyautogui.moveTo(return_img_pos, duration=drag_speed)
                        pyautogui.mouseUp()
                        return [target_type, target_zone]
                case 'i':
                    if check_image(infantry_image, 0.8, on_region) != None:
                        if zone_number == 'l': pyautogui.click(bak_mouse_pos)
                        drag_speed = drag_speed_base * pixel_distance(pyautogui.position()[0],\
                                  pyautogui.position()[1], return_img_pos[0], return_img_pos[1]) / 1000
                        mouse_shake()
                        pyautogui.moveTo(return_img_pos, duration=drag_speed)
                        pyautogui.mouseUp()
                        return [target_type, target_zone]
                case 't':
                    if check_image(tank_image, 0.8, on_region) != None:
                        if zone_number == 'l': pyautogui.click(bak_mouse_pos)
                        drag_speed = drag_speed_base * pixel_distance(pyautogui.position()[0],\
                                  pyautogui.position()[1], return_img_pos[0], return_img_pos[1]) / 1000
                        mouse_shake()
                        pyautogui.moveTo(return_img_pos, duration=drag_speed)
                        pyautogui.mouseUp()
                        return [target_type, target_zone]
                case '8': # Support line units go forward
                    if zone_number == 'l': pyautogui.click(bak_mouse_pos)
                    print('.S.L.G.F.')
                    mouse_shake()
                    pyautogui.moveTo((pyautogui.size()[0] // 2 + random.choice([-1, 1]) * random.uniform(44, 50), \
                                      pyautogui.size()[1]*45//100), duration=drag_speed_base*0.7)
                    pyautogui.mouseUp()
                    return [target_type, target_zone]
                case '9': # Deal the card
                    if zone_number == 'l': pyautogui.click(bak_mouse_pos)
                    mouse_shake()
                    pyautogui.moveTo((mouse_x, pyautogui.size()[1]*65//100), duration=drag_speed_base*0.5)
                    pyautogui.mouseUp()
                    return [target_type, target_zone]
    return [target_type, target_zone]


def play_round1(): #用于抽牌
    global current_card_cost
    global mouse_x
    global card_search_counter
    mouse_yaxis_coeff = 40

    print(formatted_time +"第1轮出牌，抽最下面的牌") #阶段1，抽牌
    #time.sleep(1)  # 等待过完抽卡动画
    check_frontline_status()  # 顺便,检查一下前线情况
    match card_search_counter:
        case 0:
            card_image = card_kmark_small_middle
            card_search_counter = 1
        case 1:
            card_image = card_kmark_small_tiltright
            card_search_counter = 2
        case 2:
            card_image = card_kmark_small_tiltleft
            card_search_counter = 0
        case _:
            card_search_counter = 0
    #for i in range(7):
    posCardBoxFilterd = None
    try:
        posCardBox = pyautogui.locateAllOnScreen(card_image, confidence=0.7, region=springboard_region)
        posCardBoxFilterd = filter_boxes(posCardBox, 10)

        for card_item in posCardBoxFilterd:
            #print(card_item)
            if is_target_pattern((int(card_item[0])-18, int(card_item[1])+17,15,15), \
                              orange_range=((190, 120, 25), (239, 192, 95)), bg_threshold=0):
                if check_abnormal():
                    print(formatted_time + "第4轮出牌检查到异常, 退出")
                    return
                x = int(card_item[0])+17
                #x = 600 + i * random.randint(89, 99)
                mouse_x = x

                #pyautogui.moveTo(x, y=pyautogui.size()[1] - mouse_yaxis_coeff, duration=0.4)
                pyautogui.click(x, y=pyautogui.size()[1] - mouse_yaxis_coeff)
                time.sleep(0.2)  # 等待过完动画
                ocr_check_card_cost()
                #ocr_check_stamina()
                #if current_card_cost <= ocr_stamina:
                #if current_card_cost != 99:
                if True:
                    #print(formatted_time + f"当前手牌消耗 {current_card_cost} 小于等于体力 {ocr_stamina} ")
                    #------------- OCR ---------------
                    if kmark_location[0] != 0:
                        ocrimage = pyautogui.screenshot('OCR/ocr_card.png',
                                                        region=(kmark_location[0] - 390, kmark_location[1] - 30, 700, 500))
                    else:
                        return
                    ocrresult = ocrscanner.readtext('OCR/ocr_card.png', detail = 0)
                    joined_ocrresult = ''.join(ocrresult)
                    print(joined_ocrresult)
                    # ------------- OCR ---------------

                    # 3代表中立 1代表被我占领 2代表敌方占领 0代表未知
                    #pyautogui.moveTo(x, y=pyautogui.size()[1] - mouse_yaxis_coeff, duration=0.7)
                    #pyautogui.click(x, y=pyautogui.size()[1] - mouse_yaxis_coeff)

                    # ----------------------- 特殊单位处理开始 -----------------------
                    print(formatted_time + "特殊指令处理部分开始")
                    if '老兔子' in joined_ocrresult:
                        print(formatted_time + "老兔子专属处理")
                        if front_line_status == 1:# 3代表中立 1代表被我占领 2代表敌方占领 0代表未知
                            # 1guard 2hq 3fighter 4bomb 5motar 6infan 7tank / 1upper 2middle 3lower/ Tmove Fdrag
                            move_drag_to_any_target('it', 'm')
                        else: move_drag_to_any_target('it', 'u')
                        continue
                    if '3张' in joined_ocrresult:   #三选一问题,选中间
                        pyautogui.dragTo(x, y=pyautogui.size()[1]//3, duration=0.5)
                        time.sleep(3)
                        pyautogui.click(pyautogui.size()[0] // 2, y=pyautogui.size()[1] // 2, duration=0.5)
                        time.sleep(0.3)
                        pyautogui.click(pyautogui.size()[0] // 2, y=pyautogui.size()[1] // 2, duration=0.5)
                        print(formatted_time + "3张, 三选一问题,选中间")
                        continue

                    # ----------------------- 正则匹配处理开始 -----------------------
                    print(formatted_time + "正则表达式匹配 处理部分开始")
                    # 1guard 2hq 3fighter 4bomb 5motar 6infan 7tank / 1upper 2middle 3lower/ Tmove Fdrag
                    if find_ordered_keywords(joined_ocrresult, '指令', '最后', '击') != None: continue

                    if find_ordered_keywords(joined_ocrresult, '指令', '敌方', '单位') != None or \
                        find_ordered_keywords(joined_ocrresult, '指令', '单位', '伤害') != None or \
                            find_ordered_keywords(joined_ocrresult, '指令', '两栖进攻') != None or \
                            find_ordered_keywords(joined_ocrresult, '指令', '消灭', '敌方') != None : #Mark1
                        print(formatted_time + '正则处理: Mark1')
                        if front_line_status == 2: move_drag_to_any_target('gfbmit', 'mu') # 3代表中立 1代表被我占领 2代表敌方占领 0代表未知
                        else: move_drag_to_any_target('gfbmit', 'u')
                        continue

                    if find_ordered_keywords(joined_ocrresult, '指令', '敌方', '空军', '伤害') != None or\
                            find_ordered_keywords(joined_ocrresult, '指令', '灯火') != None: #Mark2
                        print(formatted_time + '正则处理: Mark2')
                        if front_line_status == 2:  # 3代表中立 1代表被我占领 2代表敌方占领 0代表未知
                            move_drag_to_any_target('fb', 'um')
                        else:
                            move_drag_to_any_target('fb', 'u')
                        continue
                    # 1guard 2hq 3fighter 4bomb 5motar 6infan 7tank / 1upper 2middle 3lower/ Tmove Fdrag
                    if find_ordered_keywords(joined_ocrresult, '指令', '坦克', '伤害') != None: #Mark3
                        print(formatted_time + '正则处理: Mark3')
                        if front_line_status == 2:  # 3代表中立 1代表被我占领 2代表敌方占领 0代表未知
                            move_drag_to_any_target('t', 'um')
                        else:
                            move_drag_to_any_target('t', 'u')
                        continue

                    if find_ordered_keywords(joined_ocrresult, '指令', '空军', '获得') != None: #Mark4
                        print(formatted_time + '正则处理: Mark4')
                        move_drag_to_any_target('fb', 'l')
                        continue
                    # 1guard 2hq 3fighter 4bomb 5motar 6infan 7tank / 1upper 2middle 3lower/ Tmove Fdrag
                    if find_ordered_keywords(joined_ocrresult, '指令', '敌方', '总部') != None or \
                            find_ordered_keywords(joined_ocrresult, '指令', '敌方', '总部') != None or\
                            find_ordered_keywords(joined_ocrresult, '指令', '空中', '闪击') != None: #Mark5
                        print(formatted_time + '正则处理: Mark5')
                        move_drag_to_any_target('h', 'u')
                        continue

                    if find_ordered_keywords(joined_ocrresult, '指令', '友方', '单位', '获得') != None: #Mark6
                        print(formatted_time + '正则处理: Mark6')
                        if front_line_status == 1: move_drag_to_any_target('gfbmit', 'ml')
                        else: move_drag_to_any_target('gfbmit', 'l')
                        continue
                    # 1guard 2hq 3fighter 4bomb 5motar 6infan 7tank / 1upper 2middle 3lower/ Tmove Fdrag
                    if find_ordered_keywords(joined_ocrresult, '指令', '抽', '单位') != None or \
                            find_ordered_keywords(joined_ocrresult, '指令', '所有', '敌方') != None : #Mark7
                        print(formatted_time + '正则处理: Mark7')
                        move_drag_to_any_target('9')
                        continue

                    if find_ordered_keywords(joined_ocrresult, '指令', '点槽') != None or \
                            find_ordered_keywords(joined_ocrresult, '指令', '敌方', '所有','目标','伤害') != None or \
                            find_ordered_keywords(joined_ocrresult, '指令', '扩张', '前线') != None or \
                            find_ordered_keywords(joined_ocrresult, '指令', '西苏', '精神') != None: #Mark8
                        print(formatted_time + '正则处理: Mark8')
                        move_drag_to_any_target('9')
                        continue

                    if find_ordered_keywords(joined_ocrresult, '指令', '坦克', '获得') != None: #Mark9a
                        print(formatted_time + '正则处理: Mark9a')
                        if front_line_status == 1: move_drag_to_any_target('t', 'ml') # 3代表中立 1代表被我占领 2代表敌方占领 0代表未知
                        else: move_drag_to_any_target('t', 'l')
                    if find_ordered_keywords(joined_ocrresult, '指令', '步兵', '获得') != None: #Mark9b
                        print(formatted_time + '正则处理: Mark9b')
                        if front_line_status == 1: move_drag_to_any_target('i', 'ml')
                        else: move_drag_to_any_target('i', 'l')
                        continue

                    # ----------------------- 战斗单位处理开始 -----------------------
                    movable_unit = ['坦克', '步兵', '炮兵', '战斗机', '轰炸机']  # 某些介绍太长的单位也在列表里
                    if any(word for word in movable_unit if word in joined_ocrresult):   #移动兵力
                        print(formatted_time + "移动兵力")
                        if any(word for word in ['零战', '二挺进', '第9突击队', '仙台'] if word in joined_ocrresult):
                            print(formatted_time + "需要二次拖放兵力, 专属处理")
                            # 1guard 2hq 3fighter 4bomb 5motar 6infan 7tank 9出牌 / 1upper 2middle 3lower
                            move_drag_to_any_target('9')
                            time.sleep(1)
                            if '二挺进' in joined_ocrresult:
                                print(formatted_time + "_二挺进_卡处理")
                                # 1guard 2hq 3fighter 4bomb 5motar 6infan 7tank 8rush/ 1upper 2middle 3lower/ Tmove Fdrag
                                move_drag_to_any_target('fbmi', 'um')
                                continue
                            if '仙台' in joined_ocrresult:
                                print(formatted_time + "_仙台联队_卡处理")
                                move_drag_to_any_target('gfmbti', 'um')
                                continue
                            if '第9突击队' in joined_ocrresult:
                                print(formatted_time + "_第9突击队_卡处理")
                                move_drag_to_any_target('gfmbti', 'um')
                                continue
                            move_drag_to_any_target('ghfbmit', 'um')
                            pyautogui.mouseUp()
                            pyautogui.click(clicks=2, interval=0.2)
                        else:
                            # 1guard 2hq 3fighter 4bomb 5motar 6infan 7tank 9出牌 / 1upper 2middle 3lower/ Tmove Fdrag
                            move_drag_to_any_target('9') #普通兵直接出兵
        #--------------------------- 处理完成 ---------------------------
                    print(formatted_time + "一次出牌完成")
                    mouse_return_right()
    except Exception as e:
        print(formatted_time + "出牌出错, 可能没找到卡牌")
            #mouse_return_right()
            #time.sleep(1)  # 卡牌发出, 等待过完动画
        #mouse_return_right()

def play_round2():
    global we_have_airforce
    print(formatted_time + "移动卡牌阶段开始")  # 阶段2，引导坦克步兵向前线前进
    we_have_airforce = False
    for round_stage in range(2):
        if round_stage == 0: # round_stage -> 0, playing supportline / 1, playing frontline
            print(formatted_time + "支援战线. 移动卡牌阶段")
        else:
            print(formatted_time + "前线 移动卡牌阶段")
        check_frontline_status()  # 顺便,检查一下前线情况
        # 0代表未知 1代表被我占领 2代表敌方占领 3代表中立
        if round_stage == 1 and front_line_status != 1:
            print(formatted_time + "前线不是我们的. 跳过前线 移动卡牌阶段")
            continue
        for name in ['fighter', 'bomber', 'mortar', 'infantry', 'tank']:
            dynamic_image = globals()[f"{name}_image"]
            if check_abnormal():
                print(formatted_time + "移动卡牌阶段发现异常")
                return
            try:
                if round_stage == 0: check_region = lower_row_typeiconzone
                elif round_stage == 1: check_region = middle_row_typeiconzone
                UnitBox = pyautogui.locateAllOnScreen(dynamic_image, confidence=0.8, region=check_region)
                UnitBoxFiltered = filter_boxes(UnitBox, 10)
                for posUnit in UnitBoxFiltered:
                    if is_target_pattern(region=[int(posUnit[0] - 63), int(posUnit[1] - 169), 25, 29]):
                        #print(formatted_time + "找到可移动卡牌")
                        pyautogui.click(posUnit[0] + 15, posUnit[1] - 65)
                        match name:
                            case 'fighter':
                                if round_stage == 0:
                                    we_have_airforce = True
                                    # 1guard 2hq 3fighter 4bomb 5motar 6infan 7tank 8rush/ 1upper 2middle 3lower/ Tmove Fdrag
                                    u_type, u_zone = move_drag_to_any_target('fghmti', 'u')
                                    print(formatted_time + f"指挥{name}, 攻击zone {u_zone}的type {u_type}")
                                    mouse_return_right()
                                    time.sleep(3.5)  # 过动画
                            case 'bomber':
                                if round_stage == 0:
                                    we_have_airforce = True
                                    # 1guard 2hq 3fighter 4bomb 5motar 6infan 7tank 8rush/ 1upper 2middle 3lower/ Tmove Fdrag
                                    u_type, u_zone = move_drag_to_any_target('fghbmit', 'u')
                                    print(formatted_time + f"指挥{name}, 攻击zone {u_zone}的type {u_type}")
                                    mouse_return_right()
                                    time.sleep(3.5)  # 过动画
                            case 'mortar':
                                if round_stage == 0:
                                    # 1guard 2hq 3fighter 4bomb 5motar 6infan 7tank 8rush/ 1upper 2middle 3lower/ Tmove Fdrag
                                    if we_have_airforce: u_type, u_zone = move_drag_to_any_target('fghmit', 'um')
                                    else: u_type, u_zone = move_drag_to_any_target('ghmit', 'u')
                                    print(formatted_time + f"指挥{name}, 攻击zone {u_zone}的type {u_type}")
                                    mouse_return_right()
                                    time.sleep(2)  # 过动画
                            case 'infantry' | 'tank':
                                if round_stage == 0: # operating support line (middle)
                                    # 1guard 2hq 3fighter 4bomb 5motar 6infan 7tank 8rush/ 1upper 2middle 3lower/ Tmove Fdrag
                                    u_type, u_zone = move_drag_to_any_target('gfbmit8', 'm')
                                    print(formatted_time + f"指挥{name}, 攻击zone {u_zone}的type {u_type}")
                                else: # operating front line (upper)
                                    # 1guard 2hq 3fighter 4bomb 5motar 6infan 7tank 8rush/ 1upper 2middle 3lower/ Tmove Fdrag
                                    if we_have_airforce: u_type, u_zone = move_drag_to_any_target('fghi', 'u')
                                    else: u_type, u_zone = move_drag_to_any_target('ghfi', 'u')
                                    print(formatted_time + f"指挥{name}, 攻击zone {u_zone}的type {u_type}")
                                    mouse_return_right()
                                    time.sleep(2)  # 过动画
                        print(formatted_time + f"移动卡牌阶段结束")
                    else: pass
                        #print(formatted_time + "bu可移动卡牌")
            except Exception as e:
                print(formatted_time + "移动卡牌阶段处理出错 可能是没找到")


#-----------------------------------------------MAIN---------------------------------------------------
def main():
    global enter_game_seq
    global formatted_time
    global enemy_headquarters_pos
    global round_total_start_time
    global game_window

    game_active = False
    round_total_start_time = time.time()
    reset_game_stage()
    print(" -- KARDs 1939 Better AFK, Ver 250805a by Eason -- ")
    play_ground()
    setup_logging()
    while True:
        now = datetime.now()
        formatted_time = now.strftime('%m-%d %H:%M:%S -- ')
        if keyboard.is_pressed('f9'):
            print(formatted_time + "检测到F9查询按下, 程序中断退出")
            sys.exit(0)
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
            out_of_gameround_checking_routine()
            begin_new_game_routine()
#-------------------------------------------MAIN, Bro Out-----------------------------------------------

def play_ground():
    global formatted_time
    global return_img_pos

    if False:      #For debugging
        now = datetime.now()
        formatted_time = now.strftime("DEBUG Session " + '%m-%d %H:%M:%S -- ')
# ---------------- Debug Section Start --------------------
        check_image(training_start, confidence_level=0.8)

# ---------------- Debug Section End ----------------------
        print("\nDebug Session Ends")
        while True: sys.exit(0)

if __name__ == "__main__":
    main()