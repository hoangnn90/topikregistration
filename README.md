# topikregistration
Register topik examination automatically

## Install python 3.6 
- Download and install python-3.6.6-amd64.exe
- Link: <https://www.python.org/ftp/python/3.6.6/python-3.6.6-amd64.exe>

>Tick to 'Add Python 3.6 to PATH'

> Choose Customize installation

>Install for <b>all user</b>

>Install to <b> C:\Python36 </b> NOT C:\Program Files\Python36


## Install pip
- Link: <https://bootstrap.pypa.io/get-pip.py>
    ```cmd
    python get-pip.py
    ```

## Install selenium
- Without proxy
    ```cmd
    pip install selenium
    ```
- With proxy
    ```cmd
        set http_proxy=proxy_server:port
        set https_proxy=proxy_server:port
        easy_install pip
        pip install --proxy="proxy_server:port" selenium
    ``` 
## Download geckodriver.exe
- <https://github.com/mozilla/geckodriver/releases>
- Copy geckodriver.exe to python directory C:\Python36


## Prepare image
- Prepare image with path C:\image.jpg
