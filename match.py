import random
from operator import itemgetter

#勝敗を判定してテキストに書き込む
def player_touroku(match_result,player,player2):
    player_name = player
    player2_name = player2
    player_info = open(player_name.rstrip('\n')+'.txt', 'a')
    player2_info = open(player2_name.rstrip('\n')+'.txt', 'a')

    if match_result==1:
        player_info.write("○")
        player2_info.write("●")
    else:
        player_info.write("●")
        player2_info.write("○")


def shiaikekka(rank):

    player = []


    if rank=="a":
        player_info = open("Arank.txt","r")
        player_kazu = 10
    else:
        player_info = open("Brank.txt","r")
        player_kazu = 13

    for shiaisuu_now in range(player_kazu):
        player_name = player_info.readline()
        player.append(player_name.rstrip('\n'))
        f = open(player_name.rstrip('\n')+'.txt', 'w')
        f.close()


    for match in range(len(player)):

        new_match = False

        for i in range(len(player)):
            match_result = random.randint(0,1)

            if new_match==True:
                player_touroku(match_result,player[match],player[i])

            if match == i:
                new_match = True

def junnihantei(rank):
        player = []
        shousuu = []
        player_number = []
        if rank=="a":
            player_info = open("Arank.txt","r")
            player_kazu = 10
        else:
            player_info = open("Brank.txt","r")
            player_kazu = 13

        #勝数をカウント
        for shiaisuu_now in range(player_kazu):
            player_name = player_info.readline()
            player.append(player_name.rstrip('\n'))
            info = open(player_name.rstrip('\n')+'.txt', 'r')
            shouhai = info.readline()
            shousuu.append(shouhai.count("○"))


        player_number=zip(player,shousuu)
        list = sorted(player_number,key=itemgetter(1),reverse=True)
        player,shousuu=zip(*list)
        for kiroku in range(len(player)):
            print(shousuu[kiroku])
            print(player[kiroku])
        print("\n")
        #print(shousuu[len(shousuu)-1])
        #print(player[len(player)-1])

        rank_save = open('一時保存_'+ rank +'.txt','w')
        if rank=='a':
            rank_save_kou = open('一時保存_降a.txt','w')
        elif rank=='b':
            rank_save_shou = open('一時保存_昇b.txt','w')
            rank_save_kou = open('一時保存_降b.txt','w')

        for save in range(len(player)):
            if player[save]!=player[len(player)-1] and rank=='a':
                rank_save.write(player[save]+'\n')
            elif player[save]!=player[len(player)-1] and rank=='b' and player[save]!=player[0]:
                rank_save.write(player[save]+'\n')
            elif player[save]==player[len(player)-1]:
                rank_save_kou.write(player[len(player)-1])
            elif rank=='b':
                rank_save_shou.write(player[save])

def huriwake():
    rank_a = open("Arank.txt","w")
    rank_b = open("Brank.txt","w")
    saved_rank_a = open("一時保存_a.txt","r")
    saved_rank_b = open("一時保存_b.txt","r")
    saved_kou_a = open("一時保存_降a.txt","r")
    saved_kou_b = open("一時保存_降b.txt","r")
    saved_shou_b = open("一時保存_昇b.txt","r")
    rank_a_list = []
    rank_b_list = []

    for new_rank_a in range(9):
        rank_a_list.append(saved_rank_a.readline().rstrip('\n'))

    rank_a_list.append(saved_shou_b.read())

    for new_rank_a in range(10):
        rank_a.write(rank_a_list[new_rank_a]+'\n')
    #print(rank_a_list[0])
    #print(rank_a_list[9])


    rank_b_list.append(saved_kou_a.readline()+'\n')

    for new_rank_b in range(11):
        rank_b_list.append(saved_rank_b.readline())

    rank_b_list.append(saved_kou_b.readline())

    for new_rank_b in range(13):
        rank_b.write(rank_b_list[new_rank_b])
        #print(rank_b_list[new_rank_b])


shiaikekka("a")
shiaikekka("b")
junnihantei("a")
junnihantei("b")
huriwake()
