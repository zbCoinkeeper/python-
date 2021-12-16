import multiprocessing
import random


def cal_distribute(q):
    min=mid1=mid2=max=0
    for i in range(2500000):
        num=random.randint(1,99)
        if num<60:
            min=min+1
        elif num<80:
            mid1=mid1+1
        elif num<90:
            mid2=mid2+1
        else:
            max=max+1
    q.put([min/2500000,mid1/2500000,mid2/2500000,max/2500000])   #返回 [1, 10] 之间的任意整数
    


if __name__ == '__main__':
    q=multiprocessing.Queue()
    p1 = multiprocessing.Process(target = cal_distribute,args=(q,))
    p2 = multiprocessing.Process(target = cal_distribute,args=(q,))
    p3 = multiprocessing.Process(target = cal_distribute,args=(q,))
    p4 = multiprocessing.Process(target = cal_distribute,args=(q,))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()

    res1=q.get()
    res2=q.get()
    res3=q.get()
    res4=q.get()
    
    allRes=[]
    for i in range(len(res1)):
        temp=(res1[i]+res2[i]+res3[i]+res4[i])/4
        allRes.append(temp)

    fo = open("./result.txt", "w")
    fo.write(f"(0,60)的分布概率是{allRes[0]}\n[60,80)的分布概率是{allRes[1]}\n[80,90)的分布概率是{allRes[2]}\n[90,100)的分布概率是{allRes[3]}\n")
    # 关闭打开的文件
    fo.close()
    print(allRes)