# Git hub 정리

## Git 정의
- 분산버전관리시스템 -> 로컬에서도 버전을 기록하고 관리

## 저장소 처음 만들 때
- git init

## 버전을 기록할 때
- git add .
- git commit -m '커밋메시지'

## 상태를 확인 할 때
- git status : 1통, 2통
- git log : 커밋 확인
- git log --oneline : 커밋 메시지 조회

## 원격저장소 활용
- 원격저장소 처음 설정할 때
    - git remote add origin URL
- push / pull
    - git push origin master
    - git pull origin master
- clone
    - git clone URL
- 원격저장소 삭제
    - git remote rm <원격저장소>
- 원격저장소 정보 확인
    - git remote -v
- 버전관리 제외 파일 목록
    - .gitignore 파일 생성 후 제외 목록 추가

# 되돌리기
- add 전
    - git restore [filename]
- add 후
    - git restore --staged [filename]