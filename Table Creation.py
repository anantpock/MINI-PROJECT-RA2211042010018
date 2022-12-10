import pymysql as pm
conn=pm.connect(host="Localhost",user="root",passwd="ashulucky123")
mycur=conn.cursor()

db="create database if not exists ypl"
mycur.execute(db)
conn.commit()

qr="use ypl"
mycur.execute(qr)
conn.commit()

def create_MT():
    mycur.execute("create table if not exists teams (TEAM_NAME varchar(40),\
    OWNER varchar(50), HOME_GROUND varchar(50),TROPHIES varchar(30))")
    mycur.execute("show tables")
    for x in mycur:
        print(x)
def insert_MT():
    sql='insert into teams values(%s,%s,%s,%s)'
    mi=('Mumbai Indians','Reliance Industries','Wankhede Stadium','2013, 2015, 2017, 2019, 2020')
    kkr=('Kolkata Knight Riders','Red Chillies Entertainment & Mehta Group','Eden Gardens','2012,2014')
    rcb=('Royal Challengers Bangalore','United Spirits Limited','M. Chinnaswamy Stadium','-')
    srh=('Sunrisers Hyderabad','SUN Group','Rajiv Gandhi Intl. Cricket Stadium','2016')
    dc=('Delhi Capitals','GMR Group, JSW Group','Arun Jaitley Stadium','-')
    csk=('Chennai Super Kings','The India Cements Ltd','M. A. Chidambaram Stadium',('2010, 2011, 2018'))
    mycur.execute(sql,mi)
    mycur.execute(sql,kkr)
    mycur.execute(sql,rcb)
    mycur.execute(sql,srh)
    mycur.execute(sql,dc)
    mycur.execute(sql,csk)
    conn.commit()
create_MT()
insert_MT()


def create_csk():
    mycur.execute("create table if not exists CSK (Player_Name varchar(50),\
                  Role varchar(50),\
                  Jno int(4),\
                  Age int(2),\
                  Matches int(3),\
                  Runs int(4),\
                  HighestScore int(3),\
                  StrikeRate decimal(5,2),\
                  Wickets int(3),\
                  Economy decimal(5,2))")
    mycur.execute("show tables")
def insert_csk():
    sql="insert into CSK values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    rec=[("ruturaj gaikwad","right Hand Batsman",31,24,13,400,75,124.61,None,None),
         ("faf du plesis","Right Hand Batsman",19,37,91,2622,96,131.03,None,None),
         ("moen ali","Right Hand Batsman",20,34,25,515,66,157.97,15,6.92),
         ("suresh raina","Left Hand Batsman",3,34,200,5491,100,136.89,25,7.38),
         ("ravindra jadeja","ALL ROUNDER",5,35,166,3795,100,127.77,0,7.33),
         ("ambati rayudu","right hand batsman",8,32,191,2290,62,128.07,120,7.62),
         ("MS dhoni(c)","Right Hand Batsman",7,40,211,4609,84,137,None,None),
         ("sam curran","All Rounder",58,23,30,333,55,150.67,32,8.84),
         ("Shardul Thakur","ALL ROUNDER",54,29,52,49,15,113.95,51,9.13),
         ("Deepak Chahar","ALL ROUNDER",90,29,55,78,39,139.28,53,7.67),
         ("Lungi Ngidi","Right Arm Fast",22,25,14,None,None,None,25,8.29)]
    mycur.executemany(sql,rec)
    conn.commit()
create_csk()
insert_csk() 


def create_dc():
    mycur.execute("create table if not exists DC (Player_Name varchar(50),\
                  Role varchar(50),\
                  Jno int(4),\
                  Age int(2),\
                  Matches int(3),\
                  Runs int(4),\
                  HighestScore int(3),\
                  StrikeRate decimal(5,2),\
                  Wickets int(3),\
                  Economy decimal(5,2))")
    mycur.execute("show tables")
def insert_dc():
    sql="insert into DC values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    rec=[("Rishabh pant","Left Hand Batsman",17,23,76,2292,128,149.80,None,None),
         ("Ajinkya rahane","Right Hand Batsman",4,33,48,3941,105,121.33,None,None),
         ("shikhar dhawan","Left Hand Batsman",25,35,184,5575,106,127.35,None,None),
         ("Prithvi shaw","Right Hand Batsman (c)",27,21,46,1134,99,146.13,None,None),
         ("Marcus stoinis","ALL ROUNDER",16,32,54,896,65,137.84,30,9.533),
         ("Steve smith","right hand batsman",49,32,101,2437,101,128.39,None,None),
         ("Amit Mishra","Right Arm Leg Spin",99,36,154,362,31,93.05,166,7.35),
         ("Kagiso Rabada","Fast Bowler",114,26,42,134,44,101.51,69,8.23),
         ("Ravichandran Ashwin","Right Arm Off Spin",98,35,159,419,45,111.14,139,6.90),
         ("Umesh Yadav","Right Arm Fast",19,33,121,122,24,95.31,119,8.51),
         ("Ishant Sharma","Right Arm Fast",1,33,93,55,10,90.16,73,8.09)]
    mycur.executemany(sql,rec)
    conn.commit()
create_dc()
insert_dc() 


def create_mi():
    mycur.execute("create table if not exists MI (Player_Name varchar(50),\
                  Role varchar(50),\
                  Jno int(4),\
                  Age int(2),\
                  Matches int(3),\
                  Runs int(4),\
                  HighestScore int(3),\
                  StrikeRate decimal(5,2),\
                  Wickets int(3),\
                  Economy decimal(5,2))")
    mycur.execute("show tables")
def insert_mi():
    sql="insert into MI values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    rec=[("Rohit Sharma","Right Hand Batsman (c)",45,34,207,5480,109,130.50,15,7.97),
         ("Quinton de Kock","Left Hand Batsman (wk)",12,28,72,2114,108,132.20,None,None),
         ("Suryakumar Yadav","Right Hand Batsman",63,30,108,2197,79,135.28,0,8.00),
         ("Ishan Kishan","Left Hand Batsman",32,23,56,1284,99,131.98,None,None),
         ("Krunal Pandya","All Rounder",36,30,78,1100,86,141.38,49,7.28),
         ("Hardik Pandya","All Rounder",33,27,87,1401,91,157.23,42,9.06),
         ("Kieron Pollard","All Rounder",55,34,171,3191,87,150.87,63,8.83),
         ("Trent Boult","Left Arm Fast",17,32,55,13,6,81.25,71,8.52),
         ("Jasprit Bumrah","Right Arm Fast",93,27,99,44,16,93.61,115,7.39),
         ("Nathan Coulter-Nile","Right Arm Fast",6,33,34,77,24,118.46,41,7.75),
         ("Rahul Chahar","Right Arm Leg Spin",28,22,38,31,10,103.33,41,7.41)]
    mycur.executemany(sql,rec)
    conn.commit()
create_mi()
insert_mi()


def create_kkr():
    mycur.execute("create table if not exists KKR (Player_Name varchar(50),\
                  Role varchar(50),\
                  Jno int(4),\
                  Age int(2),\
                  Matches int(3),\
                  Runs int(4),\
                  HighestScore int(3),\
                  StrikeRate decimal(5,2),\
                  Wickets int(3),\
                  Economy decimal(5,2))")
    mycur.execute("show tables")
def insert_kkr():
    sql="insert into KKR values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    rec=[("Nitish Rana","Left Hand Batsman",27,27,67,1638,87,133.82,7,8.27),
         ("Shubman Gill","Right Hand Batsman",77,22,48,1071,76,124.24,None,None),
         ("Rahul Tripathi","Right Hand Batsman",52,30,52,1175,93,134.90,None,None),
         ("Eoin Morgan","Left Hand Batsman (c)",16,34,73,1364,68,125.25,None,None),
         ("Sunil Narine","All Rounder",74,33,124,902,75,161.64,130,6.78),
         ("Andre Russell","All Rounder",12,33,81,1680,88,179.29,68,9.08),
         ("Dinesh Karthik","Right Hand Batsman",21,36,203,3946,97,129.88,None,None),
         ("Pat Cummins","All Rounder",30,28,37,316,66,140.44,38,8.23),
         ("Shivam Mavi","Right Arm Fast",23,22,20,28,9,77.77,16,8.55),
         ("Varun Chakravarthy","Right Arm Leg Spin",29,30,21,12,7,63.15,25,7.34),
         ("Prasidh Krishna","Right Arm Fast",43,21,31,3,2,25.00,26,9.29)]
    mycur.executemany(sql,rec)
    conn.commit()
create_kkr()
insert_kkr()  


def create_rcb():
    mycur.execute("create table if not exists rcb (Player_Name varchar(50),\
    Role varchar(50),Jno int(4), Age int(2),Matches int(3), Runs int(4), HighestScore int(3), \
    StrikeRate decimal(5,2), Wickets int(3), Economy decimal(5,2))")
    mycur.execute("show tables")
    for x in mycur:
        print(x)
def insert_rcb():
    sql="insert into rcb values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    r=[("Virat Kohli","Right Hand Batsman (c)",18,32,199,6076,113,130.41,None,None),
       ("Devdutt Padikkal","Left Hand Batsman",37,21,21,68,101,131.75,None,None),
       ("Rajat Patidar","Right Hand Batsman",19,28,4,71,31,114.51,None,None),
       ("Glenn Maxwell","All-Rounder",32,32,89,1728,95,153.32,None,None),
       ("AB de Villiers","Right Hand Batsman (wk)",17,37,176,5056,133,152.38,None,None),
       ("Shahbaz Ahmed","All-rounder",21,26,7,24,14,100.00,6,6.90),
       ("Washington Sundar","All-rounder",55,21,42,217,35,111.28,27,6.93),
       ("Kyle Jamieson","Right Arm Fast",12,26,7,59,16,143.90,9,9.20),
       ("Harshal Patel","Right Arm Fast",13,30,55,163,36,139.31,63,8.80),
       ("Mohammed Siraj","Right Arm Fast",73,27,42,58,14,87.87,45,8.77),
       ("Yuzvendra Chahal","Right Arm Leg Spin",6,31,106,30,8,41.66,125,7.70)]
    mycur.executemany(sql,r)
    conn.commit()
create_rcb()
insert_rcb()


def create_srh():
    mycur.execute("create table if not exists srh (Player_Name varchar(50),\
    Role varchar(50),Jno int(4), Age int(2),Matches int(3), Runs int(4), HighestScore int(3), \
    StrikeRate decimal(5,2), Wickets int(3), Economy decimal(5,2))")
    mycur.execute("show tables")
    for x in mycur:
        print(x)
def insert_srh():
    sql="insert into srh values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    r=[("Kane Williamson","Right Hand Batsman(c)",22,31,57,1747,89,134.17,0,10.33),
       ("Wriddhiman Saha","Right Hand Batsman (wk)",6,36,126,1987,115,131.24,None,None),
       ("David Warner","Left Hand Batsman",31,34,148,5447,126,140.13,0,12.00),
       ("Abdul Samad","Right Hand Batsman ",18,37,176,147,133,152.38,None,None),
       ("Manish Pandey","Right Hand Batsman",21,31,151,3461,114,121.78,None,None),
       ("Kedar Jadhav","All-rounder",81,36,91,1181,69,124.18,None,None),
       ("Jason Holder","All-rounder",98,29,19,108,26,121.34,22,8.36),
       ("Bhuvneshwar Kumar","Right Arm Fast",15,31,126,200,24,96.15,139,7.31),
       ("Sandeep Sharma","Right Arm Fast",66,28,95,52,9,82.53,110,7.79),
       ("Rashid Khan","Right Arm Leg Spin",19,21,22,156,34,147.16,85,6.23),
       ("Mujeeb Ur Rahman","Right Arm Off Spin",88,20,19,12,10,80.00,19,8.18)]
    mycur.executemany(sql,r)
    conn.commit()
create_srh()
insert_srh()


def create_orange():
    mycur.execute("create table if not exists Orange_Cap (Position varchar(20),\
                  Name varchar(20),\
                  Runs int(4),\
                  Team varchar(4))")
    mycur.execute("show tables")
def create_purple():
    mycur.execute("create table if not exists Purple_Cap (Position varchar(5),\
                  Name varchar(20),\
                  Wickets varchar(3),\
                  Team varchar(4))")
    mycur.execute("show tables")
def insert_orange():
    sql="insert into Orange_Cap values (%s,%s,%s,%s)"
    rec=[("#1","Shikhar Dhawan",380,"DC"),
         ("#2","KL Rahul",331,"PBKS"),
         ("#3","Faf Du Plessis",320,"CSK"),
         ("#4","Prithvi Shaw",308,"DC"),
         ("#5","Rohit Sharma",283,"MI")] 
    mycur.executemany(sql,rec)
    conn.commit()
def insert_purple():
    sql="insert into Purple_Cap values (%s,%s,%s,%s)"
    rec=[("#1","Harhsal Patel",17,"RCB"),
         ("#2","Avesh Khan",14,"DC"),
         ("#3","Rahul Chahar",11,"MI"),
         ("#4","Rashid Khan",10,"SRH"),
         ("#5","Sam Curran","9","CSK")]
    mycur.executemany(sql,rec)
    conn.commit()
create_orange()
insert_orange()
create_purple()
insert_purple()


def create_sch():
    mycur.execute("create table if not exists schedule (MatchNo int(2) NOT NULL,\
    Day varchar(3) NOT NULL,Date date NOT NULL, Time TIME NOT NULL,HomeTeam varchar(5) NOT NULL, AwayTeam varchar(5) NOT NULL, Venue varchar(25) NOT NULL)")
    mycur.execute("show tables")
    for x in mycur:
        print(x)
def insert_sch():
    sql="insert into schedule values(%s,%s,%s,%s,%s,%s,%s)"
    r=[("1","SAT","2021-03-23","07:30:00","CSK","MI","Chennai"),
       ("2","SUN","2021-03-24","07:30:00","KKR","CSK","Kolkata"),
       ("3","MON","2021-03-25","07:30:00","MI","RCB","Mumbai"),
       ("4","TUE","2021-03-26","07:30:00","DC","CSK","Delhi"),
       ("5","WED","2021-03-27","07:30:00","KKR","RCB","Kolkata"),
       ("6","THU","2021-03-28","07:30:00","RCB","SRH","Bangalore"),
       ("7","FRI","2021-03-29","07:30:00","SRH","KKR","Hyderabad"),
       ("8","SAT","2021-03-30","07:30:00","DC","RCB","Delhi"),
       ("9","SUN","2021-03-31","07:30:00","SRH","CSK","Hyderabad"),
       ("10","MON","2021-04-01","07:30:00","CSK","RCB","Chennai"),
       ("11","TUE","2021-04-02","07:30:00","MI","KKR","Mumbai"),
       ("12","WED","2021-04-03","07:30:00","DC","SRH","Delhi"),
       ("13","THU","2021-04-04","07:30:00","RCB","MI","Bangalore"),
       ("14","FRI","2021-04-05","07:30:00","CSK","KKR","Chennai"),
       ("15","SAT","2021-04-06","07:30:00","SRH","DC","Hyderabad"),
       ("16","SUN","2021-04-07","07:30:00","RCB","KKR","Bangalore"),
       ("17","MON","2021-04-08","07:30:00","CSK","DC","Hyderabad"),
       ("18","TUE","2021-04-09","07:30:00","MI","DC","Mumbai"),
       ("19","WED","2021-04-10","07:30:00","KKR","MI","Kolkata"),
       ("20","THU","2021-04-11","07:30:00","MI","CSK","Mumbai"),
       ("21","FRI","2021-04-12","07:30:00","KKR","SRH","Kolkata"),
       ("22","SAT","2021-04-13","07:30:00","SRH","MI","Hyderabad"),
       ("23","SUN","2021-04-14","07:30:00","MI","SRH","Mumbai"),
       ("24","MON","2021-04-15","07:30:00","SRH","RCB","Hyderabad"),
       ("25","TUE","2021-04-16","07:30:00","DC","MI","Delhi"),
       ("26","WED","2021-04-17","07:30:00","KKR","DC","Kolkata"),
       ("27","THU","2021-04-18","07:30:00","DC","KKR","Delhi"),
       ("28","FRI","2021-04-19","07:30:00","RCB","CSK","Bangalore"),
       ("29","SAT","2021-04-20","07:30:00","RCB","DC","Bangalore"),
       ("30","SUN","2021-04-21","07:30:00","CSK","SRH","Chennai"),
       ("31","MON","2021-04-22","07:30:00","TBD","TBD","Kolkata(PLAYOFF)"),
       ("32","TUE","2021-04-23","07:30:00","TBD","TBD","Delhi(PLAYOFF)"),
       ("33","WED","2021-04-24","07:30:00","TBD","TBD","Chennai(PLAYOFF)"),
       ("34","THU","2021-04-25","07:30:00","TBD","TBD","Bangalore(FINAL)")]
    mycur.executemany(sql,r)
    conn.commit()
create_sch()
insert_sch()


def create_pt():
    mycur.execute("create table if not exists PointsTable (Team varchar(35),\
                  Matches varchar(50),\
                  Won int,\
                  Lost int,\
                  NRR decimal(4,3),\
                  Points int,\
                  Last_Five varchar(5))")
    mycur.execute("show tables")
def insert_pt():
    sql="insert into PointsTable values(%s,%s,%s,%s,%s,%s,%s)"
    values=[("Mumbai Indians",10,7,3,0.421,14,"WWWLW"),
            ("Chennai Super Kings",10,7,3,0.131,14,"WLLWW"),
            ("Delhi capitals",10,7,3,0.044,14,"LWWLW"),
            ("Sunrisers Hyderbad",10,4,6,0.577,8,"WWWLL"),
            ("Kolkata Knight Riders",10,4,6,-0.449,8,"LLWLW"),
            ("Royal Challengers Banglore",10,3,7,-0.607,6,"WLLLW")]
    mycur.executemany(sql,values)
    conn.commit()
create_pt()
insert_pt()


conn.close()
