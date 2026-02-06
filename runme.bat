@echo off
echo github와 동기화... command: git pull
git pull
echo 변경된 파일 업로드... command: git add, commit, push
git add .
git commit -m "CSV update"
git push
echo 작업 종료
pause
