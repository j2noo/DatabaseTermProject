import tkinter as tk
from tkinter import ttk
import psycopg2


# 데이터베이스 연결
conn = psycopg2.connect(host="localhost", dbname="Flights0610", user="postgres", password="123123", port=5432)
cur = conn.cursor()

departure_li = [
    "전체",
    "ICN - 인천",
    "NRT - 나리타",
    "KIX - 간사이",
    "FUK - 후쿠오카",
    "BKK - 방콕",
    "HKG - 홍콩",
    "DAD - 다낭",
    "HAN - 하노이",
    "SGN - 싱가폴",
    "GMP - 김포",
]
arrive_li = [
    "전체",
    "ICN - 인천",
    "NRT - 나리타",
    "KIX - 간사이",
    "FUK - 후쿠오카",
    "BKK - 방콕",
    "HKG - 홍콩",
    "DAD - 다낭",
    "HAN - 하노이",
    "SGN - 싱가폴",
    "GMP - 김포",
]
nation_li = ["일본", "태국", "홍콩", "베트남", "싱가폴", "에티오피아", "중국"]
isKoreanAirline = False  # 초기값 설정
isDesc = False
global cur_menu


# 특정 노선 최저가
def button1_clicked():
    global cur_menu
    # 기존 버튼 숨기기
    button1.place_forget()
    button2.place_forget()
    button3.place_forget()
    button4.place_forget()
    title_label.pack_forget()
    title2_label.pack_forget()

    # 드롭다운과 백버튼, 조회, 체크박스 보이기
    departure_set.pack()
    arrive_set.pack()
    koreanAirlineCheckBox_set.pack()
    search_button.pack()
    treeview_set.pack()
    back_button.pack()
    cur_menu = 1


def button2_clicked():
    global cur_menu
    # 기존 버튼 숨기기
    button1.place_forget()
    button2.place_forget()
    button3.place_forget()
    button4.place_forget()
    title_label.pack_forget()
    title2_label.pack_forget()

    # 드롭다운과 백버튼 보이기
    departure_set.pack()
    arrive_set.pack()
    date_set.pack()
    airline_set.pack()
    departure_time_set.pack()
    search_button.pack()
    treeview_set.pack()
    back_button.pack()

    cur_menu = 2


# 특정 국가 최저가
def button3_clicked():
    global cur_menu
    # 기존 버튼 숨기기
    button1.place_forget()
    button2.place_forget()
    button3.place_forget()
    button4.place_forget()
    title_label.pack_forget()
    title2_label.pack_forget()

    # 드롭다운과 백버튼 보이기

    nation_set.pack()
    search_button.pack()
    treeview_set.pack()
    back_button.pack()
    cur_menu = 3


def button4_clicked():
    global cur_menu
    # 기존 버튼 숨기기
    button1.place_forget()
    button2.place_forget()
    button3.place_forget()
    button4.place_forget()
    title_label.pack_forget()
    title2_label.pack_forget()

    # 드롭다운과 백버튼 보이기
    departure_set.pack()
    arrive_set.pack()
    date_set.pack()
    airline_set.pack()
    departure_time_set.pack()
    koreanAirlineCheckBox_set.pack()
    search_button.pack()
    radio_set.pack()
    desc_checkbox.pack()
    treeview_set.pack()
    back_button.pack()

    cur_menu = 4


def show_home_screen():
    global cur_menu
    # 드롭다운 백버튼, 조회버튼 숨기기

    back_button.pack_forget()
    departure_set.pack_forget()
    arrive_set.pack_forget()
    search_button.pack_forget()
    koreanAirlineCheckBox_set.pack_forget()
    treeview_set.pack_forget()
    nation_set.pack_forget()
    radio_set.pack_forget()
    desc_checkbox.pack_forget()

    # 2
    date_set.pack_forget()
    airline_set.pack_forget()
    departure_time_set.pack_forget()

    # 홈 화면에 버튼들 다시 보이게 하기
    button1.place(x=50, y=50 + 100)
    button2.place(x=350, y=50 + 100)
    button3.place(x=650, y=50 + 100)
    button4.place(x=50, y=150 + 100)
    title_label.pack()
    title2_label.pack()
    cur_menu = 0


def search_clicked():
    global cur_menu

    selected_departure = departure_combobox.get()[0:3]
    # departure_var.set(selected_departure)

    selected_arrive = arrive_combobox.get()[0:3]
    # arrive_var.set(selected_arrive)

    selected_nation = nation_combobox.get()
    nation_var.set(selected_nation)

    date = date_var.get()
    airline = airline_var.get()
    departure_time = departure_time_var.get()

    if date != "":
        date = ' AND ft."Departure Date" =' + "'" + date + "'"
    if airline != "":
        airline = ' AND ft."Airline" =' + "'" + airline + "'"
    if departure_time != "":
        departure_time = ' AND ft."Depature Time" =' + "'" + departure_time + "'"

    query1 = """
            SELECT *
            FROM "Flight Ticket" ft 
                JOIN "Route" r ON r."Route ID" =ft."Route ID" 
            WHERE r."Depature Airport" =%s AND r."Arrive Airport" =%s
            ORDER BY ft."Price"
            LIMIT 500
            """
    query1_1 = """
            SELECT *
            FROM "Flight Ticket" ft 
                JOIN "Route" r ON r."Route ID" =ft."Route ID" 
                JOIN "Airline" a ON a."Airline Name" =ft."Airline" 
            WHERE r."Depature Airport" =%s AND r."Arrive Airport" =%s AND a."Nation" ='한국'
            ORDER BY ft."Price"
            LIMIT 500
            """

    query2 = """
            SELECT *
                FROM "Flight Ticket" ft JOIN "Route" r ON r."Route ID" =ft."Route ID" 
            WHERE r."Depature Airport" =%s AND r."Arrive Airport" =%s AND ft."Departure Date" =%s AND ft."Airline" =%s AND ft."Depature Time" =%s
            ORDER BY ft."Searching Date"
            LIMIT 500
            """

    query2_a = f"""
            SELECT *
                FROM "Flight Ticket" ft JOIN "Route" r ON r."Route ID" =ft."Route ID" 
            WHERE r."Depature Airport" ='{selected_departure}' AND r."Arrive Airport" ='{selected_arrive}' {date} {airline} {departure_time}
            ORDER BY ft."Searching Date"
            LIMIT 500
            """

    query3 = """
            SELECT * 
            FROM "Flight Ticket" ft 
                JOIN "Route" r ON r."Route ID" =ft."Route ID" 
                JOIN "Airport" a ON r."Arrive Airport" =a."Airport Code" 
            WHERE a."Nation" =%s
            ORDER BY ft."Price" 
            LIMIT 500 -- %s
            """
    if selected_departure == "전체":
        qr4_selected_departure = ""
    else:
        qr4_selected_departure = ' AND r."Depature Airport" =' + "'" + selected_departure + "'"

    if selected_arrive == "전체":
        qr4_selected_arrive = ""
    else:
        qr4_selected_arrive = ' AND r."Arrive Airport" =' + "'" + selected_arrive + "'"

    if isKoreanAirline == True:
        qr_isKoreanAirline = ' AND a."Nation" =' + "'" + "한국" + "'"
    else:
        qr_isKoreanAirline = ""

    if isDesc == True:
        qr_isDesc = "DESC"
    else:
        qr_isDesc = ""

    selected_field = selected_value.get()
    print("selected_field : ", selected_field)
    print("isDesc :", isDesc)
    query4 = f"""
            SELECT *
            FROM "Flight Ticket" ft 
                JOIN "Route" r ON r."Route ID" =ft."Route ID" 
                JOIN "Airline" a ON a."Airline Name" =ft."Airline" 
            WHERE 1=1 {qr4_selected_departure} {qr4_selected_arrive}
                      {date} {airline} {departure_time} {qr_isKoreanAirline}
            ORDER BY {selected_field} {qr_isDesc}
            LIMIT 50000
            """

    print("curMenu : ", cur_menu)
    if cur_menu == 1:
        values = (selected_departure, selected_arrive)
        if isKoreanAirline == True:
            cur.execute(query1_1, values)
        else:
            cur.execute(query1, values)
    elif cur_menu == 2:
        values = (selected_departure, selected_arrive, date, airline, departure_time)
        # cur.execute(query2, values)
        cur.execute(query2_a)
    elif cur_menu == 3:
        values = (selected_nation, selected_nation)
        cur.execute(query3, values)
    elif cur_menu == 4:
        cur.execute(query4)

    tree.delete(*tree.get_children())  # 데이터삭제
    result = cur.fetchall()
    for idx in range(len(result)):
        insertLi = [
            result[idx][14],
            result[idx][15],
            result[idx][1],
            result[idx][2],
            result[idx][4],
            result[idx][5],
            result[idx][7],
            result[idx][8],
        ]
        # print(insertLi)  # 또는 출력을 다른 방식으로 처리
        tree.insert("", index=idx, values=insertLi)

    print("selected_departure : ", selected_departure)
    print("selected_arrive : ", selected_arrive)
    print("isKoreanAirline : ", isKoreanAirline)


# 메인 윈도우 생성
window = tk.Tk()
window.title("항공권 조회 어플리케이션")
window.geometry("1000x700+200+100")

# 배경 이미지 파일 경로
# image_path = "airplane.png"
# background_image = tk.PhotoImage(file="C:/Users/wlsdn/Desktop/jinwoo/languages/py/crawl/airplane.png")

# background_label = tk.Label(window, image=background_image)
# background_label.place(x=50, y=50)

# 제목 텍스트
title_label = tk.Label(window, text="<항공권 가격 변동 정보 조회 프로그램>", font=("Arial", 30, "bold"))

title2_label = tk.Label(window, text="crawled ver 23.06.20", font=("Arial", 10, "bold"))


# 버튼 생성
button1 = tk.Button(
    window,
    text="노선별 항공권 가격 변동 내역 조회",
    command=button1_clicked,
    overrelief="solid",
    width=28,
    height=3,
    font=("Arial", 10, "bold"),
)
button2 = tk.Button(
    window,
    text="항공권별 가격 변동 내역 조회",
    command=button2_clicked,
    overrelief="solid",
    width=28,
    height=3,
    font=("Arial", 10, "bold"),
)
button3 = tk.Button(
    window,
    text="국가별 항공권 가격 변동 내역 조회",
    command=button3_clicked,
    overrelief="solid",
    width=28,
    height=3,
    font=("Arial", 10, "bold"),
)
button4 = tk.Button(
    window,
    text="사용자 지정 항공권가격 변동 내역 조회",
    command=button4_clicked,
    bg="skyblue",
    overrelief="solid",
    width=49,
    height=2,
    font=("Arial", 20, "bold"),
)

back_button = tk.Button(window, text="Back", command=show_home_screen)
search_button = tk.Button(window, text="조회!", command=search_clicked)

# 출발지 드롭다운
departure_set = tk.Label(window)
departure_var = tk.StringVar()  # StringVar() 객체로 초기화
departure_label = tk.Label(departure_set, text="출발지", font=("Arial", 10, "bold"))
departure_combobox = ttk.Combobox(
    departure_set, textvariable=departure_var, height=len(departure_li), value=departure_li
)
departure_combobox.set("출발지를 선택하세요")

departure_label.pack(side="left")
departure_combobox.pack(side="left")


# 목적지 드롭다운
arrive_set = tk.Label(window)
arrive_var = tk.StringVar()  # StringVar() 객체로 초기화
arrive_label = tk.Label(arrive_set, text="목적지", font=("Arial", 10, "bold"))
arrive_combobox = ttk.Combobox(arrive_set, textvariable=arrive_var, height=len(arrive_li), value=arrive_li)
arrive_combobox.set("목적지를 선택하세요")

arrive_label.pack(side="left")
arrive_combobox.pack(side="left")

# 국가선택 드롭다운
nation_set = tk.Label(window)
nation_var = tk.StringVar()  # StringVar() 객체로 초기화
nation_label = tk.Label(nation_set, text="여행 국가", font=("Arial", 10, "bold"))
nation_combobox = ttk.Combobox(nation_set, textvariable=nation_var, height=len(nation_li), value=nation_li)
nation_combobox.set("여행 국가를 선택하세요")

nation_label.pack(side="left")
nation_combobox.pack(side="left")


# 국내항공사 체크박스
def update_airline():
    global isKoreanAirline
    isKoreanAirline = airline_checkbox_var.get()


koreanAirlineCheckBox_set = tk.Label(window)
airline_checkbox_var = tk.BooleanVar()
airline_checkbox = tk.Checkbutton(
    koreanAirlineCheckBox_set, text="국내 항공사만 조회", variable=airline_checkbox_var, command=update_airline
)

airline_checkbox.pack()
koreanAirlineCheckBox_set.pack_forget()

# 날짜 입력 entry
date_set = tk.Label(window)
date_var = tk.StringVar()
date_label = tk.Label(date_set, text="출발 날짜", font=("Arial", 10, "bold"))
date_entry = tk.Entry(date_set, textvariable=date_var)
date_entry.insert(0, "2023-08-01")

date_label.pack(side="left")
date_entry.pack(side="left")
date_set.pack_forget()

# 항공사 입력 entry
airline_set = tk.Label(window)
airline_var = tk.StringVar()
airline_label = tk.Label(airline_set, text="항공사 이름", font=("Arial", 10, "bold"))
airline_entry = tk.Entry(airline_set, textvariable=airline_var)
airline_entry.insert(0, "진에어")

airline_label.pack(side="left")
airline_entry.pack(side="left")
airline_set.pack_forget()

# 출발 시각 입력 entry
departure_time_set = tk.Label(window)
departure_time_var = tk.StringVar()
departure_time_label = tk.Label(departure_time_set, text="출발 시각", font=("Arial", 10, "bold"))
departure_time_entry = tk.Entry(departure_time_set, textvariable=departure_time_var)
departure_time_entry.insert(0, "17:15")

departure_time_label.pack(side="left")
departure_time_entry.pack(side="left")
departure_time_set.pack_forget()

# treeview
treeview_set = tk.Label(window)
tree = ttk.Treeview(treeview_set)
tree["height"] = 20

tree["columns"] = ("출발공항", "도착공항", "조사날짜", "출발날짜", "출발시간", "도착시간", "항공사", "가격")

tree.column("#0", width=0, stretch=tk.NO)  # Hide the default first column
tree.column("출발공항", width=100)
tree.column("도착공항", width=100)
tree.column("조사날짜", width=100)
tree.column("출발날짜", width=100)
tree.column("출발시간", width=100)
tree.column("도착시간", width=100)
tree.column("항공사", width=100)
tree.column("가격", width=100)

# Create headings
tree.heading("출발공항", text="출발공항")
tree.heading("도착공항", text="도착공항")
tree.heading("조사날짜", text="조사날짜")
tree.heading("출발날짜", text="출발날짜")
tree.heading("출발시간", text="출발시간")
tree.heading("도착시간", text="도착시간")
tree.heading("항공사", text="항공사")
tree.heading("가격", text="가격")


tree.pack(side="left")

# Add a scrollbar
scrollbar = ttk.Scrollbar(treeview_set, orient="vertical", command=tree.yview)
scrollbar.pack(side="left", fill="y")
tree.configure(yscrollcommand=scrollbar.set)

treeview_set.pack_forget()

# 가로 라디오버튼
values = ["출발공항", "도착공항", "조사날짜", "출발날짜", "출발시간", "도착시간", "항공사", "가격"]
fields = [
    'r."Depature Airport"',
    'r."Arrive Airport"',
    'ft."Searching Date"',
    'ft."Departure Date"',
    'ft."Depature Time"',
    'ft."Arrive Time"',
    'ft."Airline"',
    'ft."Price"',
]
selected_value = tk.StringVar(value=fields[-1])  # 기본값으로 마지막 값을 설정

radio_set = tk.Label(window)
radio_label = tk.Label(radio_set, text="정렬 기준", font=("Arial", 10, "bold"))
radio_label.pack(side="left")

for i in range(len(values)):
    rb = tk.Radiobutton(radio_set, text=values[i], variable=selected_value, value=fields[i])
    rb.pack(side="left")


# 오름차순 체크박스
def update_desc():
    global isDesc
    isDesc = desc_checkbox_var.get()


desc_checkbox_var = tk.BooleanVar()
desc_checkbox = tk.Checkbutton(
    radio_set, text="내림차순 정렬", font=("Arial", 10, "bold"), variable=desc_checkbox_var, command=update_desc
)
desc_checkbox.pack_forget()

# 프로그램 시작
show_home_screen()


# GUI 루프 시작
window.mainloop()
