import pymysql as pm
conn=pm.connect(host="Localhost",user="root",passwd="ashulucky123",database="ypl")
mycur=conn.cursor()

def add_recrd():
    team=input("enter team in which player is to be added: ")
    name=input("enter name of the player: ")
    role=input("enter role of the player: ")
    Jno=int(input("enter jesrsey no of the player: "))
    age=int(input("enter age of the palyer: "))
    matches=int(input("enter the no of matches played by the player: "))
    runs=int(input("enter no of runs: "))
    highest_score=int(input("enter the highest score: "))
    strike_rate=float(input("enter strike rate of the player: "))
    wickets=int(input("enter the no of wickets: "))
    economy=float(input("enter the economy: "))
    qry='insert into {} values("{}","{}","{}",{},{},{},{},{},{},{})'.format(team,name,role,Jno,age,matches,runs,highest_score,strike_rate,wickets,economy)
    mycur.execute(qry)
    conn.commit()


def update_player_rec():
    Team=input("Enter team of player whose details need to be changed: ")
    j=int(input("Enter jersey no. of player: "))
    Jno=int(input("Enter jersey no: "))
    Age=int(input("Enter age: "))
    Matches=int(input("Enter matches: "))
    Runs=int(input("Enter runs: "))
    HighestScore=int(input("Enter highest score: "))
    StrikeRate=float(input("Enter StrikeRate: "))
    Wickets=int(input("Enter Wickets: "))
    Economy=float(input("Enter Economy: "))
    mycur.execute("use ypl")
    qry="update {} set Jno={},Age={},Matches={},Runs={},HighestScore={},StrikeRate={},Wickets={},Economy={} where Jno={}".format(Team,Jno,Age,Matches,Runs,HighestScore,StrikeRate,Wickets,Economy,j)
    mycur.execute(qry)
    conn.commit()


def delete_rec():
    team=input("enter team of player: ")
    j=int(input("enter jersey no: "))
    qry="delete from {} where Jno={}".format(team,j)
    mycur.execute(qry)
    conn.commit()


def search_team():
    while True:
        ch=int(input("What do you want to search by? Enter: 1. By Team Name \n2. By Owner\n 3. By Home Ground\n 4.By winning year\n 5. Exit"))
        if ch==1:
            teamname=input("Enter name of team")
            qry="select * from teams where TEAM_NAME=%s"
            mycur.execute(qry,teamname)
            print(mycur.fetchall())
        elif ch==2:
            ownername=input("Enter Owner name")
            qry="select * from teams where OWNER=%s"
            mycur.execute(qry,ownername)
            print(mycur.fetchall())
        elif ch==3:
            HomeG=input("Enter Home Ground name")
            qry="select * from teams where HOME_GROUND=%s"
            mycur.execute(qry,HomeG)
            print(mycur.fetchall())
        elif ch==4:
            wyear=input("Enter winning year")
            qry="select * from teams where TROPHIES like %s "
            mycur.execute(qry,("%{}%".format(wyear)))
            print(mycur.fetchall())
        elif ch==5:
            break


def modify_pt():
    tmn=input("Enter team name whose records are to be updated")
    mtch=int(input("Enter number of matches played"))
    won=int(input("Enter number of matches won"))
    lost=int(input("Enter number of matches lsot"))
    NRR=float(input("Enter NRR"))
    pts=int(input("Enter points"))
    Lfive=input("Enter last 5 match status as W:Win, L:Loss")
    qry="update pointstable set Matches=%s,Won=%s,Lost=%s,NRR=%s,Points=%s,Last_Five=%s where Team=%s"
    val=(mtch,won,lost,NRR,pts,Lfive,tmn)
    mycur.execute(qry,val)
    conn.commit()


def update_orange_cap():
    n=input("Enter ranking of old player: ")
    Name=input("Enter name of new player: ")
    Runs=int(input("Enter runs: "))
    Team=input("Enter team of the player: ")
    qry="update orange_cap set Name=%s,Runs=%s,Team=%s where Position=%s"
    vals=(Name,Runs,Team,n)
    mycur.execute(qry,vals)
    n2=input("Enter ranking of new player: ")
    Name2=input("Enter name of old player: ")
    Runs2=int(input("Enter runs: "))
    Team2=input("Enter Team: ")
    qry2="update orange_cap set Name=%s,Runs=%s,Team=%s where Position=%s"
    vals2=(Name2,Runs2,Team2,n2)
    mycur.execute(qry2,vals2)
    conn.commit()
    
    
def update_purple_cap():
    n=input("Enter ranking of old player: ")
    Name=input("Enter name of new player: ")
    Wickets=int(input("Enter wickets: "))
    Team=input("Enter team of the player: ")
    qry="update purple_cap set Name=%s,Wickets=%s,Team=%s where Position=%s"
    vals=(Name,Wickets,Team,n)
    mycur.execute(qry,vals)
    n2=input("Enter ranking of new player: ")
    Name2=input("Enter name of old player: ")
    Wickets2=int(input("Enter Wickets: "))
    Team2=input("Enter Team: ")
    qry2="update purple_cap set Name=%s,Wickets=%s,Team=%s where Position=%s"
    vals2=(Name2,Wickets2,Team2,n2)
    mycur.execute(qry2,vals2)
    conn.commit()



while True:
    print("1.Add Player to a team \n 2.Update stats of a player \n 3.Delete Player record \n 4.Search for team(By Name, Owner, HomeGround) \n 5.Modify Points table \n 6.Update Orange cap table standings \n 7. Update purple cap standings \n 8. EXIT")
    ch=int(input("Enter Choice"))
    if ch==1:
        add_recrd()
    elif ch==2:
        update_player_rec()
    elif ch==3:
        delete_rec()
    elif ch==4:
        search_team()
    elif ch==5:
        modify_pt()
    elif ch==6:
        update_orange_cap()
    elif ch==7:
        update_purple_cap()
    elif ch==8:
        break
