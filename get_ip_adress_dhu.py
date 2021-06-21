import paramiko


def conncetion_test(hostname):
    try:
        # 创建SSH对象
        ssh = paramiko.SSHClient()
        # 允许连接不在know_hosts文件中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接服务器
        ssh.connect(hostname=hostname, port=22, username='dhu2', password='111111', timeout=0.001)
        # print(reply)https://docs.qq.com/sheet/DVGh3enVhamtZbVNP
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command('df -h')
        # 获取命令结果
        result = stdout.read()
        print('find it! the valid ip adress is:%s' % hostname)
        # 关闭连接
        ssh.close()
    except:
        pass
        # print("%s is not a valid ip adress" % hostname)
    finally:
        pass
        # print("程序继续运行")

#
for i in range(0, 255):
    hstname = '10.199.172.' + str(i)
    conncetion_test(hstname)

for i in range(0, 255):
    hstname = '10.199.173.' + str(i)
    conncetion_test(hstname)
