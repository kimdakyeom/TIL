from django.shortcuts import render
import random

def lotto(request):
  all = list(range(1, 45))
  numbers1 = random.sample(all, 6)
  numbers2 = random.sample(all, 6)
  numbers3 = random.sample(all, 6)
  numbers4 = random.sample(all, 6)
  numbers5 = random.sample(all, 6)
  lotto = [3, 11, 15, 29, 35, 44]
  bonus = 10
  cnt1 = 0
  cnt2 = 0
  cnt3 = 0
  cnt4 = 0
  cnt5 = 0
  flag1 = False
  flag2 = False
  flag3 = False
  flag4 = False
  flag5 = False

  for num in numbers1:
    if num in lotto:
      cnt1 += 1
    if num == bonus:
      flag1 = True

  for num in numbers2:
    if num in lotto:
      cnt2 += 1
    if num == bonus:
      flag2 = True

  for num in numbers3:
    if num in lotto:
      cnt3 += 1
    if num == bonus:
      flag3 = True

  for num in numbers4:
    if num in lotto:
      cnt4 += 1
    if num == bonus:
      flag4 = True

  for num in numbers5:
    if num in lotto:
      cnt5 += 1
    if num == bonus:
      flag5 = True

  context = {
    'numbers1': numbers1,
    'numbers2': numbers2,
    'numbers3': numbers3,
    'numbers4': numbers4,
    'numbers5': numbers5,
    'lotto': lotto,
    'bonus': bonus,
    'cnt1': cnt1,
    'cnt2': cnt2,
    'cnt3': cnt3,
    'cnt4': cnt4,
    'cnt5': cnt5,
    'flag1': flag1,
    'flag2': flag2,
    'flag3': flag3,
    'flag4': flag4,
    'flag5': flag5,
  }
  return render(request, 'lotto.html', context)