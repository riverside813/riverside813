#*- coding: utf-8 -*-
# Coding by JH HWANG.
# version 1.0
# 1.1: 7/18: 병살타,희생타 구현
# 1.2: 7/20: logo 추가 및 공수교대 프로그램 수정, 홈팀이 이기고 있으면 9회말 안하는 기능 추가.
# 타율은 4할 정도를 기준으로 맞춤
# import time
for ii in range(0,30):
    print('')


#베이스를 표현하는 배열,[0]은 사용안함 [1]=1루, [2]=2루...
#배열의 값이 1이면 주자 있음, 0이면 주자 없음
base=[0,0,0,0]
base_prt=['','','','']
#각팀 회별 점수
a=[0,0,0,0,0,0,0,0,0,0,0]
b=[0,0,0,0,0,0,0,0,0,0,0]
#팀별 점수
score=[0,0]
#각 이닝에서 얻어지는 점수
point=0
#이닝을 나타냄
inn=1
#기본적인 타순 공격시작 순서, 1번부터 하기위해 1로 셋팅
pa_next=1
pb_next=1

pa=['','고든','이디어','맷 캠프','곤잘레스','벨트레','푸이그','시몬스','맥커친','a.j.앨리스']
pb=['','서건창','민병헌','김현수','이대호','박병호','강정호','강민호','박석민','추신수']

# 병살-희생타 순으로 맨 끝번째로 두어야함

attack={ '1':'1루타',     '2':'아웃',   '3':'2루타',    '4':'아웃',
         '5':'3루타',     '6':'삼진',   '7':'볼넷',     '8':'삼진',
         '9':'홈런',     '10':'아웃',  '11':'사구',    '12':'아웃',
        '13':'고의사구',  '14':'아웃',  '15':'1루타',   '16':'삼진',
        '17':'에러',     '18':'삼진',  '19':'1루타',   '20':'아웃',
        '21':'희생타'} #     '22':'아웃',  '23':'아웃',    '24':'아웃' }
        # '25':'아웃',     '26':'아웃',  '27':'아웃',    '28':'아웃' }

# 야수선택(19)

def print_homerun():
    print('\n')
    print('    ) ')
    print(' ( /( ')
    print(' )\())         )      (   (      ( ')
    print('((_)\   (     (      ))\  )(    ))\   ( ')
    print(' _((_)  )\    )\  " /((_)(()\  /((_)  )\ ) ')
    print('| || | ((_) _((_)) (_))   ((_)(_))(  _(_/( ')
    print('| __ |/ _ \|    \()/ -_) |  _|| || || " \)) ')
    print('|_||_|\___/|_|_|_| \___| |_|   \_,_||_||_| ')
    print('\n')
def print_win():
    print('WWWWWWWW                           WWWWWWWWIIIIIIIIIINNNNNNNN        NNNNNNNN')
    print('W::::::W                           W::::::WI::::::::IN:::::::N       N::::::N')
    print('W::::::W                           W::::::WI::::::::IN::::::::N      N::::::N')
    print('W::::::W                           W::::::WII::::::IIN:::::::::N     N::::::N')
    print(' W:::::W           WWWWW           W:::::W   I::::I  N::::::::::N    N::::::N')
    print('  W:::::W         W:::::W         W:::::W    I::::I  N:::::::::::N   N::::::N')
    print('   W:::::W       W:::::::W       W:::::W     I::::I  N:::::::N::::N  N::::::N')
    print('    W:::::W     W:::::::::W     W:::::W      I::::I  N::::::N N::::N N::::::N')
    print('     W:::::W   W:::::W:::::W   W:::::W       I::::I  N::::::N  N::::N:::::::N')
    print('      W:::::W W:::::W W:::::W W:::::W        I::::I  N::::::N   N:::::::::::N')
    print('       W:::::W:::::W   W:::::W:::::W         I::::I  N::::::N    N::::::::::N')
    print('        W:::::::::W     W:::::::::W          I::::I  N::::::N     N:::::::::N')
    print('         W:::::::W       W:::::::W         II::::::IIN::::::N      N::::::::N')
    print('          W:::::W         W:::::W          I::::::::IN::::::N       N:::::::N')
    print('           W:::W           W:::W           I::::::::IN::::::N        N::::::N')
    print('            WWW             WWW            IIIIIIIIIINNNNNNNN         NNNNNNN')
    print('\n')
    print('\n')
def print_mlb():
    print('MMMMMMMM               MMMMMMMMLLLLLLLLLLL             BBBBBBBBBBBBBBBBB')
    print('M:::::::M             M:::::::ML:::::::::L             B::::::::::::::::B')
    print('M::::::::M           M::::::::ML:::::::::L             B::::::BBBBBB:::::B')
    print('M:::::::::M         M:::::::::MLL:::::::LL             BB:::::B     B:::::B')
    print('M::::::::::M       M::::::::::M  L:::::L                 B::::B     B:::::B')
    print('M:::::::::::M     M:::::::::::M  L:::::L                 B::::B     B:::::B')
    print('M:::::::M::::M   M::::M:::::::M  L:::::L                 B::::BBBBBB:::::B')
    print('M::::::M M::::M M::::M M::::::M  L:::::L                 B:::::::::::::BB')
    print('M::::::M  M::::M::::M  M::::::M  L:::::L                 B::::BBBBBB:::::B')
    print('M::::::M   M:::::::M   M::::::M  L:::::L                 B::::B     B:::::B')
    print('M::::::M    M:::::M    M::::::M  L:::::L                 B::::B     B:::::B')
    print('M::::::M     MMMMM     M::::::M  L:::::L         LLLLLL  B::::B     B:::::B')
    print('M::::::M               M::::::MLL:::::::LLLLLLLLL:::::LBB:::::BBBBBB::::::B')
    print('M::::::M               M::::::ML::::::::::::::::::::::LB:::::::::::::::::B')
    print('M::::::M               M::::::ML::::::::::::::::::::::LB::::::::::::::::B')
    print('MMMMMMMM               MMMMMMMMLLLLLLLLLLLLLLLLLLLLLLLLBBBBBBBBBBBBBBBBB')
def print_kbo():
    print('KKKKKKKKK    KKKKKKKBBBBBBBBBBBBBBBBB        OOOOOOOOO')
    print('K:::::::K    K:::::KB::::::::::::::::B     OO:::::::::OO')
    print('K:::::::K    K:::::KB::::::BBBBBB:::::B  OO:::::::::::::OO')
    print('K:::::::K   K::::::KBB:::::B     B:::::BO:::::::OOO:::::::O')
    print('KK::::::K  K:::::KKK  B::::B     B:::::BO::::::O   O::::::O')
    print('  K:::::K K:::::K     B::::B     B:::::BO:::::O     O:::::O')
    print('  K::::::K:::::K      B::::BBBBBB:::::B O:::::O     O:::::O')
    print('  K:::::::::::K       B:::::::::::::BB  O:::::O     O:::::O')
    print('  K:::::::::::K       B::::BBBBBB:::::B O:::::O     O:::::O')
    print('  K::::::K:::::K      B::::B     B:::::BO:::::O     O:::::O')
    print('  K:::::K K:::::K     B::::B     B:::::BO:::::O     O:::::O')
    print('KK::::::K  K:::::KKK  B::::B     B:::::BO::::::O   O::::::O')
    print('K:::::::K   K::::::KBB:::::BBBBBB::::::BO:::::::OOO:::::::O')
    print('K:::::::K    K:::::KB:::::::::::::::::B  OO:::::::::::::OO')
    print('K:::::::K    K:::::KB::::::::::::::::B     OO:::::::::OO')
    print('KKKKKKKKK    KKKKKKKBBBBBBBBBBBBBBBBB        OOOOOOOOO')
def draw_ground():
    print('')
    print('                                       (',base_prt[2],' ) ')
    print('                                        3  2 ')
    print('                                      3      2')
    print('                                    3          2')
    print('                                  3              2')
    print('                                3                  2')
    print('                              3                      2')
    print('                            3                          2')
    print('                          3                              2')
    print('                        3                                  2')
    print('                      3                                      2')
    print('                   (',base_prt[3],' )                                  (',base_prt[1],')')
    print('                      H                                      1')
    print('                        H                                  1')
    print('                          H                              1')
    print('                            H                          1')
    print('                              H                      1')
    print('                                H                  1')
    print('                                  H              1')
    print('                                    H          1')
    print('                                      H      1')
    print('                                        H  1')
    print('                                       |    |')
    print('                                       |    |')
    print('                                        \  /')
    print('                                         \/')
def draw_logo():
    print(' /$$$$$$$                                /$$                 /$$ /$$')
    print('| $$__  $$                              | $$                | $$| $$')
    print('| $$  \ $$  /$$$$$$   /$$$$$$$  /$$$$$$ | $$$$$$$   /$$$$$$ | $$| $$')
    print('| $$$$$$$  |____  $$ /$$_____/ /$$__  $$| $$__  $$ |____  $$| $$| $$')
    print('| $$__  $$  /$$$$$$$|  $$$$$$ | $$$$$$$$| $$  \ $$  /$$$$$$$| $$| $$')
    print('| $$  \ $$ /$$__  $$ \____  $$| $$_____/| $$  | $$ /$$__  $$| $$| $$')
    print('| $$$$$$$/|  $$$$$$$ /$$$$$$$/|  $$$$$$$| $$$$$$$/|  $$$$$$$| $$| $$')
    print('|_______/  \_______/|_______/  \_______/|_______/  \_______/|__/|__/')
    print('                              version1.0')
    print('                             JaeHyuk,Hwang')
    print('                         Press RETURN key to start')
    temp0=input('')

# 점수판 보여줌
def draw_score():
    print ('\n')
    a[10]=0
    b[10]=0
    # 토탈 점수 합산을 위해 a[10]에 계산하여 넣어둠
    for aa in range(1,10):
        a[10] = a[10]+a[aa]
        b[10] = b[10]+b[aa]
    print ('MLB','\t','1:',a[1],'\t','2:',a[2],'\t','3:',a[3],'\t','4:',a[4],'\t',
           '5:',a[5],'\t','6:',a[6],'\t','7:',a[7],'\t','8:',a[8],'\t','9:',a[9],'\t',
            '점수',a[10])
    print ('KBO','\t','1:',b[1],'\t','2:',b[2],'\t','3:',b[3],'\t','4:',b[4],'\t',
           '5:',b[5],'\t','6:',b[6],'\t','7:',b[7],'\t','8:',b[8],'\t','9:',b[9],'\t',
            '점수',b[10])
    print ('\n')
    return

# 랜덤 발생
def MakeRandom(x):
    from random import randint
    return str((randint(1,x)))

# 실제로 게임이 구현되는 메인Function
def playball(team,x):
    global pa_next
    global pb_next
    global point
    global inn
    global base_prt
    if x==1:
        att_menu='초'
    else:
        att_menu='말'
    print ('\n=====================',inn,'회',att_menu,' 공격이 시작됩니다.=================\n')
    count_out=0
    next_p=1
    point=0
    base=[0,0,0,0]
    base_prt=['  ','  ','  ','  ']
#아웃카운트가 3이 될때까지 한팀이 공격을 하도록 한다.
    while count_out < 3:
        # 만약 팀이 a이면 다음 플레이를 pa_next에서 받아온다.
        if x==1:
            next_p=pa_next
            team_name='MLB'
        # 만약 팀이 b이면 다음 플레이를 pb_next에서 받아온다.
        else:
            next_p=pb_next
            team_name='KBO'

        print(team_name,next_p,'번 타자',team[next_p],'선수 타격')

        temp=input('타격을 하려면 Return')

        # time.sleep(0.3)
        #20개의 공격중에 하나를 선택한다.
        #만약 2아웃이거나 2아웃은 아니지만 베이스가 비어있으면 병살은 안나옴
        if (count_out==2) or \
                (count_out != 2 and (base[1]==0 and base[2]==0 and base[3]==0)):
            res=MakeRandom((len(attack))-2)
        #만약 2아웃이 아니고 1,2,3중에 주자가 있으면 병살포함
        elif (count_out !=2) and (base[1]==1 or base[2]==1 or base[3]==1):
            res=MakeRandom((len(attack)-1))
        # 만약 2아웃이 아니고 주자가 3루인 경우 희생타 포함, 공격배열 맨 끝에 놓아야 함
        # len(attack)은 attack의 갯수를 포함한다. 그래서 그대로 사용하고
        # 병살만 포함하면 (len(attack))-1 빼고,
        # 병살,희생타가 포함되지 않으면 (len(attack))-2를 하면 된다.
        # 희생타는 배열의 맨 끝에, 병살은 배열의 맨끝-1에 놓으면 된다.
        elif (count_out !=2) and base[3]==1:
            res=MakeRandom((len(attack)))

        # ***(지우면 안됨) 타격결과를 보여줌 (지우면 안됨)***
        print('타격결과는 \"',attack[res],'\" 입니다.')


        if attack[res]=='아웃' or attack[res]=='삼진':
            count_out=count_out+1
        elif attack[res]=='병살':
            count_out=count_out+2
            #3루에만 주자가 있으면 3루없앰
            if base[1]==0 and base[2]==0 and base[3]==1:
                base[3]=0
            #2루에만 주자가 있으면 2루없앰
            elif base[1]==0 and base[2]==1 and base[3]==0:
                base[2]=0
            #2,3루가 있으면 1,2루를 비우고 3루자는 홈으로 들어옴
            elif base[1]==0 and base[2]==1 and base[3]==1:
                base[2]=0
                base[3]=0
                if count_out==2:
                    point=point+1
            #1루에만 주자가 있으면 1,2루 모두 비움
            elif base[1]==1 and base[2]==0 and base[3]==0:
                base[1]=0
            #1,3루에 있는 경우 1,2루 아웃되고 3루주자는 홈으로 들어옴
            elif base[1]==1 and base[2]==0 and base[3]==1:
                base[1]=0
                base[3]=0
                if count_out==2:
                    point=point+1
            #1,2루에 주자가 있으면 1,2루 아웃되고 2루주자만 3루로 진루
            elif base[1]==1 and base[2]==1 and base[3]==0:
                base[1]=0
                base[2]=0
                base[3]=1
            #만약 만루면 1,2루자 비우고 2루주자는 3루로, 3루는 홈으로
            elif base[1]==1 and base[2]==1 and base[3]==1:
                base[1]=0
                base[2]=0
                base[3]=1
                if count_out==2:
                    point=point+1
        elif attack[res]=='희생타':
            count_out=count_out+1
            point=point+1
            base[3]=0
        elif attack[res]=='1루타' or attack[res]=='에러':
            point = point + base[3]
            base[3]=base[2]
            base[2]=base[1]
            base[1]=1
        elif attack[res]=='2루타':
            point = point + base[2] + base[3]
            base[3]=base[1]
            base[2]=1
            base[1]=0
        elif attack[res]=='3루타':
            point = point + base[1] + base[2] + base[3]
            base[1]=0
            base[2]=0
            base[3]=1
        elif attack[res]=='홈런':
            print_homerun()
            point = point + base[1] + base[2] + base[3] + 1
            #모두 주자를 비운다.
            base[1]=0
            base[2]=0
            base[3]=0
        elif attack[res]=='볼넷' or attack[res]=='고의사구' or attack[res]=='사구':
            #만약 1루가 비어있는 경우는 1루만 채운다.
            if base[1]==0:
                base[1]=1
        #만약 1루에 주자가 있고, 2루가 빈경우, 2루에만 하나를 채우면 된다.
            elif base[1]==1 and base[2]==0:
                base[2]=1
        #만약 1,2루에 주자가 있고, 3루가 빈경우 3루만 채우면 된다.
            elif base[1]==1 and base[2]==1 and base[3]==0:
                base[3]=1
        #만약 1,3루에 주자가 있고, 2루가 빈경우 2루만 채우면 된다.
            elif base[1]==1 and base[2]==0 and base[3]==1:
                base[2]=1
        ##만약 1,2,3루가 다 주자가 있는 경우는 1루타와 같이 하나씩 더 이동한다.
            elif base[1]==1 and base[2]==1 and base[3]==1:
                point = point + base[3]
                base[3]=base[2]
                base[2]=base[1]
                base[1]=1

        #베이스를 검색해서 1:주자가 있으면 야구공으로 표시하도록 base_prt를 조정함

        for ii in range(1,4):
            if base[ii]==1:
                base_prt[ii]='⚾'
            else:
                base_prt[ii]='  '

        draw_ground()
        #
        # print('현재 점수는:',point,'아웃카운트는:',count_out,'\t','1루:',base_prt[1],
        #       '  2루:',base_prt[2],'  3루:',base_prt[3],'\n')
        print('현재 점수는:',point,'아웃카운트는:',count_out,'\n')
        #다음 타자를 호출하기 위해 1을 더함
        if next_p==9:
            next_p=1
        else:
            next_p=next_p+1
        # x가 1이면 선공, x가 2후면 후공, 선후공에 맞게 다음 타격순서를 기억해두고 점수도 기억해둔다.
        if x==1:
            pa_next=next_p
            a[inn]=point
        else:
            pb_next=next_p
            b[inn]=point
    #만약 X=2이면 후공이 끝난것으므로 이닝을 1을 더한다.
    if x==2:
        inn += 1
    print ('3아웃이 되어 공수를 교대합니다!!!!')



##############################################
# Main
##############################################

draw_logo()



print('*** MLB팀 선수를 소개합니다 ***   ')
for i in range(1,len(pa)):
    print (i,"번 타자 ", pa[i])

print('\n','*** KBO팀 선수를 소개합니다 ***','\n')
for i in range(1,len(pb)):
    print (i,"번 타자 ", pb[i])

draw_score()

#
# game=['a','b','a','b','a','b','a','b','a','b','a','b','a','b','a','b','a','b']
#
# for i in range(0,len(game)):
#     if game[i]=='a':
#         team=pa
#         x=1
#     else:
#         team=pb
#         x=2
#     playball(team,x)
#     draw_score()
# 공수 교대하는 것을 아래의 프로그램으로 바꿈
# 1회의 1를 mod하면 !=0 이므로 공격팀은 pa(초공격) 하고 x=1
# 2회의 2를 mod하면 ==0 이므로 공격팀은 pb(말공격) 하고 x=2
# 이기고 있으면 9회말 안하는 기능추가
count=1
while count <=18:
    # 만약 9회말이 되었는데 원정팀의 점수가 더 놓으면 break로 탈출.
    if count==18 and a[10]<b[10]:
        break
    if count%2==0:
        team=pb
        x=2
    else:
        team=pa
        x=1
    playball(team,x)
    draw_score()
    count += 1


print_win()

# print('****************************************')
if a[10]>b[10]:
    print_mlb()
    # print(' MLB팀이 승리하였습니다. !!')
elif a[10]<b[10]:
    print_kbo()
    # print(' KBO팀이 승리하였습니다. !!')
else:
    print(' 경기가 동점으로 끝났습니다.\n')
print('****************************************')
print(' 경기가 끝났습니다. 쓰레기는 휴지통에 버려주세요  ')
print('****************************************\n')