import paramiko


def ssh(ip, *args):
    """
    ssh链接
    :param ip:目标设备IP
    :param args: 需要在目标设备上执行的命令
    :return: 返回命令执行结果
    """
    res = []
    res_str = []
    ssh_obj = paramiko.SSHClient()
    ssh_obj.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_obj.connect(hostname=ip, port=22, username='root', password='passok')
        for cmd in args:
            if isinstance(cmd, list):
                for cmd_tmp in cmd:
                    stdin, stdout, stderr = ssh_obj.exec_command(cmd_tmp.strip())
                    res.append(stdout.read())
            else:
                stdin, stdout, stderr = ssh_obj.exec_command(cmd)
                res.append(stdout.read())
        for res_tmp in res:
            res_str.append(res_tmp.decode().strip())
    except TimeoutError as n:
        # print("服务器无法连接，请检查！")
        print(n)
    except paramiko.ssh_exception.AuthenticationException as n:
        print(n)
    ssh_obj.close()
    return res_str