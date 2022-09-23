from django.shortcuts import render
import random

def lotto(request):
  lotto_result_list = []
  today = [3, 11, 15, 29, 35, 44]
  bonus = 10

  for _ in range(5):
    lotto = random.sample(range(1, 46), 6)

    cnt = 0
    flag = False
    for num in lotto:
      if num in today:
        cnt += 1
      if num == bonus:
        flag = True

    if cnt == 6:
      lotto_result_list.append({'lotto': lotto, 'result': '1등'})
    elif cnt == 5 and flag == True:
      lotto_result_list.append({'lotto': lotto, 'result': '2등'})
    elif cnt == 5 and flag == False:
      lotto_result_list.append({'lotto': lotto, 'result': '3등'})
    elif cnt == 4:
      lotto_result_list.append({'lotto': lotto, 'result': '4등'})
    elif cnt == 3:
      lotto_result_list.append({'lotto': lotto, 'result': '5등'})
    else:
      lotto_result_list.append({'lotto': lotto, 'result': '꽝'})

  context = {
    'lotto_result_list' : lotto_result_list,
    'today': today,
    'bonus': bonus,
  }
  return render(request, 'lotto.html', context)