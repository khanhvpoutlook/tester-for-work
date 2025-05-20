# Chương trình tính tổng các số trong danh sách
# Tác giả: [Tên của bạn]
# Ngày tạo: 20/05/2025
# Mục đích: Thực hành lập trình Python cơ bản và ghi log hoạt động

import logging

# Cấu hình logging để ghi hoạt động
logging.basicConfig(filename='dev_activity.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_sum(numbers):
    """Tính tổng của các số trong danh sách"""
    total = sum(numbers)
    logging.info(f"Tính tổng thành công: {total}")
    return total

def get_user_input():
    """Nhận danh sách số từ người dùng"""
    try:
        input_str = input("Nhập các số cách nhau bằng dấu phẩy (ví dụ: 1,2,3,4): ")
        numbers = [float(x.strip()) for x in input_str.split(',')]
        logging.info("Nhận danh sách số từ người dùng thành công")
        return numbers
    except ValueError:
        logging.error("Lỗi: Dữ liệu nhập vào không hợp lệ")
        return []

def main():
    """Hàm chính để chạy chương trình"""
    print("Chào mừng đến với chương trình tính tổng!")
    numbers = get_user_input()
    
    if numbers:
        result = calculate_sum(numbers)
        print(f"Tổng của các số là: {result}")
    else:
        print("Không thể tính tổng do dữ liệu không hợp lệ.")

if __name__ == "__main__":
    main()
