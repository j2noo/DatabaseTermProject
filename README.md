# DatabaseTermProject
2023-1학기 하태현교수님 데이터베이스 프로젝트 - 항공권 가격 변동 추적 프로그램✈️



<img src ="https://github.com/j2noo/DatabaseTermProject/assets/77064618/d770b83e-891e-4ee2-9b24-1369164e04b2" width = 600px >



---
경고 무시하고 푸시하다 리드미 날려먹어서 간단하게 작성합니다..ㅠㅠ

## 1. 크롤링 서버 환경 및 구축
![image](https://github.com/j2noo/DatabaseTermProject/assets/77064618/581f47ee-88b5-4e0a-9d9a-b558c91914d6)

AWS EC2에서 제공하는 프리티어 우분투 기본 사양입니다.
- 인스턴스 : t2.micro
- vCPU : 1, 메모리 : 1GiB, 네트워크 : 1Gbps, IMDSv2 : Optional
- FTP : FileZila - EC2 인스턴스 코드 배포 및 데이터 회수
- SSH Client : XShell 

## 2. 환경 세팅

### 2-1) 크롬 및 크롬드라이버 설치
```
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo apt-get update 
sudo apt-get install google-chrome-stable

sudo apt install unzip
/* 크롬 최신버전 확인하여 크롬드라이버 다운받을것*/
wget https://chromedriver.storage.googleapis.com/113.0.5672.63/chromedriver_linux64.zip
unzip chromedriver_linux64.zipls
```

### 2-2) 파이썬 설치 버전 확인 및 라이브러리 설치
```
sudo apt-get update
python3 --version /* 버전 확인! 없으면 설치하기 Python 3.10.6 */
sudo apt-get install python3-pip
pip install selenium
pip install asyncio
pip install beatifulsoup4
pip install crontab
# 필요 라이브러리 : selenium,asyncio,beautifulsoup4,crontab
```

### 2-3) 프로세스 자동화
```
crontab e
0 16 * * * /usr/bin/python3 /home/ubuntu/crawl/crawl.py
```
