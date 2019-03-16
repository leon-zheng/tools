# tools

### 1. sendIP

- Replace information in these lines (35-39):

  ```python
  smtp_server = '<replace with your smtp server>'
  from_addr = '<replace with your email address>'
  username = '<replace with your username>'
  password = '<replace with your smtp authorization code>'
  to_addr = '<replace with receiver email address>'
  ```


- Run:

  ```bash
  python sendIP.py
  ```


- Example:

  ![sendIPexample](https://github.com/leon-zheng/tools/blob/master/sendIPexample.PNG)

- Tip:

  If you have a server using DHCP, you can add 'python sendIP.py' in file '/etc/rc.local'.