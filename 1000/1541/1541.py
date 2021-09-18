sik = input()
mode = False # -를 만났는지, 아닌지를 체크
res = 0      # 최종 결과를 저장
num = 0 

for s in range(len(sik)): # 식을 쭉 보면서 

  if  48 <= ord(sik[s]) <= 57: # 0~9라면
    num *= 10                  # 이전에 있던 num을 10 곱하고
    num += int(sik[s])         # 이번에 sik[s]를 정수로 바꿔서 1의 자리에 넣어줌

      
  elif mode == False : # sik[s]이 +나 -인데, 그전에 아직 -를 안만났으면
      res += num       # 결과에 num을 더해준다. (-를 안만났으니까 그 완성된 숫자 앞에 부호는 무조건 +)
      num = 0          # num을 0으로 
      if sik[s] == '-': # -를 만났으면 mode를 True로 
          mode = True 

  elif mode == True: # sik[s]가 +나 -인데, 그 전에 -를 만난 적이 있으면 
      res -= num     # 결과에서 num을 빼준다. (-를 만난 적 있는데, 그 후에 나오는 +이면 괄호를 쳐서 -로 바꿀 수 있음)
      num = 0        # num을 0으로

# 루프를 다 돈 후에(마지막 부호 이후로 만난 숫자들이 남아있음)
if mode == False:   # -를 만난 적이 없으면
    res += num  # 마지막 숫자들 앞의 부호는 무조건 +니까 +해줌
else:           # -를 만난 적이 있으면
    res -= num  

print(res)
