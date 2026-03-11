import random
import string
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# 1. Cấu hình Chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# 2. Các hàm tạo code riêng biệt để không bị lẫn
def get_25_chars():
    # Tạo kiểu: XXXXX-XXXXX-XXXXX-XXXXX-XXXXX
    chars = string.ascii_uppercase + string.digits
    parts = ["".join(random.choice(chars) for _ in range(5)) for _ in range(5)]
    return "-".join(parts)

def get_v_25_chars():
    # Tạo kiểu: V-XXXXX-XXXXX-XXXXX-XXXXX-XXXXX
    chars = string.ascii_uppercase + string.digits
    parts = ["".join(random.choice(chars) for _ in range(5)) for _ in range(5)]
    return "V-" + "-".join(parts)

def get_10_digits():
    # Tạo kiểu: 1234567890 (Chỉ số)
    return "".join(random.choice(string.digits) for _ in range(10))

# 3. Bắt đầu chạy
driver.get("https://www.minecraft.net/en-us/redeem")
print("--- HÃY ĐĂNG NHẬP RỒI QUAY LẠI ĐÂY ---")
input("Sau khi đăng nhập xong, nhấn Enter để bắt đầu...")

while True:
    try:
        # Chọn ngẫu nhiên 1 trong 3 loại code
        loai = random.randint(1, 3)
        
        if loai == 1:
            code_fake = get_25_chars()
            print(f"[CHẾ ĐỘ 1] Thử code 25 ký tự: {code_fake}")
        elif loai == 2:
            code_fake = get_v_25_chars()
            print(f"[CHẾ ĐỘ 2] Thử code V-25 ký tự: {code_fake}")
        else:
            code_fake = get_10_digits()
            print(f"[CHẾ ĐỘ 3] Thử code 10 số: {code_fake}")

        # Tìm ô nhập bằng Xpath xịn (tìm theo ID hoặc Placeholder)
        # Minecraft thường dùng ID 'redeem-code-input'
        input_field = driver.find_element(By.XPATH, "//input[contains(@id, 'code') or @type='text']")
        
        # Xóa sạch ô cũ trước khi nhập
        input_field.send_keys(Keys.CONTROL + 'a')
        input_field.send_keys(Keys.BACKSPACE)
        
        # Nhập code mới
        input_field.send_keys(code_fake)
        
        # Tìm và nhấn nút Submit (thường là nút có type='submit')
        submit_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_btn.click()
        
        # Nghỉ một lát để web load kết quả (Quan trọng: Đừng để nhanh quá sẽ bị lỗi)
        time.sleep(5) 
        
    except Exception as e:
        print(f"Lỗi: {e}. Đang thử lại sau 3 giây...")
        time.sleep(3)
