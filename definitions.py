#图片定义 Image Definations
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
ninegong_zone1 = (0, 0, pyautogui.size()[0]//3, pyautogui.size()[1]//3) #以下九个为屏幕九宫格
ninegong_zone2 = (pyautogui.size()[0]//3, 0, pyautogui.size()[0]//3, pyautogui.size()[1]//3)
ninegong_zone3 = (pyautogui.size()[0]*2//3, 0, pyautogui.size()[0]//3, pyautogui.size()[1]//3)
ninegong_zone4 = (0, pyautogui.size()[1]//3, pyautogui.size()[0]//3, pyautogui.size()[1]//3)
ninegong_zone5 = (pyautogui.size()[0]//3, pyautogui.size()[1]//3, pyautogui.size()[0]//3, pyautogui.size()[1]//3)
ninegong_zone6 = (pyautogui.size()[0]*2//3, pyautogui.size()[1]//3, pyautogui.size()[0]//3, pyautogui.size()[1]//3)
ninegong_zone7 = (0, pyautogui.size()[1]*2//3, pyautogui.size()[0]//3, pyautogui.size()[1]//3)
ninegong_zone8 = (pyautogui.size()[0]//3, pyautogui.size()[1]*2//3, pyautogui.size()[0]//3, pyautogui.size()[1]//3)
ninegong_zone9 = (pyautogui.size()[0]*2//3, pyautogui.size()[1]*2//3, pyautogui.size()[0]//3, pyautogui.size()[1]//3) #以上九个为屏幕九宫格
zero_tili_region = (0, pyautogui.size()[1]*790//1080, pyautogui.size()[0]*200//1920, (1080 - 790)) #0体力区域
pass_button_region = (pyautogui.size()[0]*1607//1920,pyautogui.size()[1]*622//1080, 270, 130) #空过按钮区域
second_row = (pyautogui.size()[0]*313//1920, pyautogui.size()[1]*643//1080, 1259 , 263) #支援战线区域
third_row = (pyautogui.size()[0]*333//1920, pyautogui.size()[1]*397//1080, 1417,261) #前线区域
enemy_guard_zone = (pyautogui.size()[0]*431//1920, pyautogui.size()[1]*129//1080, 1075, 161) #敌方支援区域状态区域
enemy_second_row = (pyautogui.size()[0]*400//1920, pyautogui.size()[1]*100//1080, 1143, 289) #地方支援区域
ocr_stamina_region = (32, 849, 53, 76) #体力数值区域
front_line_upper_region = (420, 370, 1000, 37) #上面前线条表达区域
front_line_lower_region = (420, 635, 1000, 37) #下面前线条表达区域


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