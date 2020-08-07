try:


    file = open("info.txt", "w")

    file.close()
except Exception as e:
    print(e)
finally:
    # 파일을 닫는다
    file.close()

print("파일이 제대로 닫혔는지 확인하기")
print(file.closed)


