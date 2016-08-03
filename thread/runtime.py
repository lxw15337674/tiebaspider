# 用于查看代码运行时间
import time
import c

def main():
    for num in range(3): #代码运行次数
        c.main()


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    runtime = round((end - start), 5)  # round确定浮点数小数点后的位数
    print("代码运行%ss" % runtime)
