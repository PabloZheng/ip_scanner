#  ip scanner

---


- 方案一：下载advanced_port_scanner

  **指定ip范围, 端口范围，扫描当前局域网下的存在的ip地址**
  ![图片](https://user-images.githubusercontent.com/49506327/132463053-dd7aa13d-6803-4c4c-8990-108181710b2f.png)


- 方案二：paramiko精确查找
 
  **适用情形：已知账号密码，ip未知**
  1. pip install paramiko
  2. 直接运行get_ip_adress_dhu.py
  3. 替换第11行中的指定账号与密码
  4. 便可扫描当前局域网下该账号与密码的ip
