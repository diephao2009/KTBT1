import tkinter as tk
from tkinter import messagebox

def tao_may_tinh():
    # Tạo cửa sổ chính
    cua_so = tk.Tk()
    cua_so.title("Máy Tính Đơn Giản")
    cua_so.geometry("400x500")
    cua_so.configure(bg='#f0f0f0')

    # Hàm kiểm tra đầu vào có phải là số tự nhiên
    def kiem_tra_so_tu_nhien(so):
        try:
            so = int(so)
            if so < 0:
                return False
            return True
        except ValueError:
            return False

    # Hàm thực hiện phép tính
    def thuc_hien_phep_tinh(phep_tinh):
        so1 = so1_nhap.get()
        so2 = so2_nhap.get()

        # Kiểm tra đầu vào
        if not so1 or not so2:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ hai số!")
            return
        if not kiem_tra_so_tu_nhien(so1) or not kiem_tra_so_tu_nhien(so2):
            messagebox.showerror("Lỗi", "Vui lòng chỉ nhập số tự nhiên!")
            return

        so1 = int(so1)
        so2 = int(so2)

        # Thực hiện phép tính tương ứng
        try:
            if phep_tinh == "+":
                ket_qua = so1 + so2
            elif phep_tinh == "-":
                ket_qua = so1 - so2
            elif phep_tinh == "×":
                ket_qua = so1 * so2
            else:  # phép chia
                if so2 == 0:
                    messagebox.showerror("Lỗi", "Không thể chia cho 0!")
                    return
                ket_qua = so1 / so2

            # Hiển thị kết quả
            ket_qua_label.config(text=f"Kết quả: {ket_qua}")

        except Exception as e:
            messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {str(e)}")

    # Tạo và định vị các thành phần giao diện
    # Nhãn tiêu đề
    tieu_de = tk.Label(cua_so, text="MÁY TÍNH ĐƠN GIẢN", font=("Arial", 16, "bold"), bg='#f0f0f0')
    tieu_de.pack(pady=20)

    # Khung chứa các ô nhập liệu
    khung_nhap = tk.Frame(cua_so, bg='#f0f0f0')
    khung_nhap.pack(pady=20)

    # Ô nhập số thứ nhất
    tk.Label(khung_nhap, text="Số thứ nhất:", bg='#f0f0f0').grid(row=0, column=0, padx=5)
    so1_nhap = tk.Entry(khung_nhap)
    so1_nhap.grid(row=0, column=1, padx=5)

    # Ô nhập số thứ hai
    tk.Label(khung_nhap, text="Số thứ hai:", bg='#f0f0f0').grid(row=1, column=0, padx=5, pady=10)
    so2_nhap = tk.Entry(khung_nhap)
    so2_nhap.grid(row=1, column=1, padx=5, pady=10)

    # Khung chứa các nút phép tính
    khung_nut = tk.Frame(cua_so, bg='#f0f0f0')
    khung_nut.pack(pady=20)

    # Tạo các nút phép tính
    phep_tinh = ["+", "-", "×", "÷"]
    for i, pt in enumerate(phep_tinh):
        nut = tk.Button(
            khung_nut,
            text=pt,
            width=5,
            height=2,
            command=lambda x=pt: thuc_hien_phep_tinh(x),
            font=("Arial", 12),
            bg='#4CAF50',
            fg='white'
        )
        nut.grid(row=0, column=i, padx=5)

    # Nhãn hiển thị kết quả
    ket_qua_label = tk.Label(
        cua_so,
        text="Kết quả: ",
        font=("Arial", 14),
        bg='#f0f0f0'
    )
    ket_qua_label.pack(pady=20)

    # Khởi chạy vòng lặp chính của ứng dụng
    cua_so.mainloop()

# Chạy chương trình
if __name__ == "__main__":
    tao_may_tinh()