import os
import sys
import concurrent.futures

f = open(f"ip_campus.txt")

stripper = "\n"


def kill(i):
    os.system(f"./expectMock.sh {i.strip(stripper)} {command}")

def ssh_yes(i):
    os.system(f"./ssh_yes.sh {i}")


# def lms_config():
#     config = """Config {
#     editor: "code",
#     repo_path: "/root/problems",
#     navigator_url: "https://navigator.wethinkcode.co.za",
#     username: "kmasenam@student.wethinkcode.co.za",
#     review_manager_url: "https://navigator.wethinkcode.co.za",
#     keycloak_url: "https://keycloak.wethinkcode.co.za",
# }
# """

def send(i, command):
    os.system(f"./deliver_execute.sh {i.strip(stripper)} {command}")



















if "kill" in sys.argv:
    command = f"'{input()}'"
    with concurrent.futures.ThreadPoolExecutor() as exe:
        for i in f.readlines():
            exe.submit(kill,i)


if "ssh" in sys.argv:
    with concurrent.futures.ThreadPoolExecutor() as exe:
        for i in f.readlines():
            exe.submit(ssh_yes,i)

if "send" in sys.argv:
    command = f"'{input()}'"
    with concurrent.futures.ThreadPoolExecutor() as exe:
        for i in f.readlines():
            exe.submit(send,i,command)




f.close()



