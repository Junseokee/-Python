import myMod1

a= myMod1.mySum(32,324)
print(a)

#다른 사람들의 코드나 알고리즘을 사용 할 수 있음
#import 할 파일은 같은 경로에 있어야함

import webbrowser

webbrowser.open("http://www.naver.com")

f = open(r'd:/abc.csv')
ff = csv.reader(f) #리스트로 출력 없으면 문자형식
for line in ff:
    lineList = line.split(",")
    print(lineList[1])


    print(line[1])
f.close()

for line in f_scv:
    desc = line[1]
    print(desc)


import urllib.request #url의 html 소스코드를 가져오는 함수

import math # 자주사용되는 수학 함수들

import random #난수 생성기

#time 1970년 1월 1일 자정 이후 누적된 초를 float 단위로 반환

#date time 날짜와 관련된 함수 날짜연산에 도움됨

#os
