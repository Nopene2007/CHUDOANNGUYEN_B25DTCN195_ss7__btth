choice=0
raw_input = "   nGuyen vaN aN  ;  2004   "
year_now=2026
email="@company.com"
while choice !=4:
    choice=int(input('''===== HỆ THỐNG XỬ LÝ THÀNH VIÊN =====
        1. Hiển thị chuỗi dữ liệu gốc
        2. Chuẩn hóa Họ tên và tính Tuổi
        3. Tạo Mã ID và Email tự động
        4. Thoát chương trình
        =====================================
        Nhập lựa chọn của bạn (1-4): '''))
    
    match choice:
        case 1:
            print(f"chuoi du lieu hien tai:\n {raw_input}")
        case 2:
            full_name=raw_input.split(';')[0].strip().title()
            birth_year=raw_input.split(';')[1]
            birth=int(birth_year)
            print(f"Ho va ten: {full_name}")
            age= year_now- birth
            print(f"Tuoi: {age}")
        case 3:
            full_name=raw_input.split(';')[0].strip().title()
            birth_year=raw_input.split(';')[1].strip()
            sur_name=full_name.split(" ")[0]
            mid_name=full_name.split(" ")[1]
            main_name=full_name.split(" ")[2]
            emails=sur_name[0].lower()+mid_name[0].lower()+main_name[0].lower()+email
            ids=main_name.upper()+birth_year[2:]
            print(f"Ho va ten: {full_name}")
            print(f"Ma id: {ids}")
            print(f"email: {emails}")
        case 4:
            print("Thoát chương trình.")
        case _:
            print("Nhap khong hop le ")