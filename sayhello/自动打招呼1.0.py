import pytesseract
import pyautogui
import time
import re
def dazhaohu():
    time.sleep(10)
    left, top, width, height = pyautogui.locateOnScreen('D:/mapdesk/trainimage/dazhaohu.png')   # 寻找 点赞图片；
    center = pyautogui.center((left, top, width, height))    # 寻找 图片的中心
    pyautogui.click(center)# 点击
    time.sleep(5)
    xiayiye()
    print('打招呼成功！')
pass

def xiayiye():
    # left, top, width, height = pyautogui.locateOnScreen('D:/mapdesk/trainimage/xiayiye.png')
    # center = pyautogui.center((left, top, width, height))
    center=(1344, 449)
    pyautogui.click(center)
    time.sleep(5)
    pyautogui.moveTo(100, 100, duration=0.25)
    print('翻页成功！')
pass


def judege():
    pyautogui.screenshot('D:/mapdesk/trainimage/jietu.png', region=(1002,315,320,412))
    from PIL import Image
    pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\python\tesseract\tesseract.exe'
    image = Image.open('D:/mapdesk/trainimage/jietu.png')
    text = pytesseract.image_to_string(image,lang='chi_sim')
    mat=re.compile(r'射频工程师|射频' ,re.S)
    a=mat.findall(text)
    if a==[]:
        xiayiye()
    else:
        dazhaohu()
pass


while True:
   judege()
