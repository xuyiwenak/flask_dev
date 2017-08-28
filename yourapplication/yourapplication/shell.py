#-*- coding: utf-8 -*-
#!/usr/bin/python 
import paramiko
import threading
def ssh2(ip,username,passwd,cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=5)
        for m in cmd:
            stdin, stdout, stderr = ssh.exec_command(m)
            stdin.write("Y")   #简单交互，输入 ‘Y’ 
            out = stdout.readlines()
            #屏幕输出
            for o in out:
                print o,
        print '%s\tOK\n'%(ip)
        ssh.close()
    except :
        print '%s\tError\n'%(ip)


if __name__=='__main__':
    ip = '10.10.252.54'
    cmd = ['echo abc','echo hello!']#你要执行的命令列表
    username = "root"  #用户名
    passwd = "linekong"    #密码
    threads = []   #多线程
    a=threading.Thread(target=ssh2,args=(ip,username,passwd,cmd))
    a.start() 
