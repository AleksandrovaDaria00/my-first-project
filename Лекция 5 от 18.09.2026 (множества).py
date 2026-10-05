ls = [22, 22, 22, 33, 44]
st = set(ls)
print(st)

st.add(100) # добавляем 1 объект
print(st)

st.update({2, 3}) # добавляет неск. объектов
print(st)

n = st.pop() # удаляет 1й объект в множестве
st.remove(2) # удалит, но если нет такого, ошибка
st.discard(2) # удалит, но если нет такого объекта, ошибки не будет, работу не остановит
print(st)

st1 = {3, 4, 33}
st2 = {3, 4, 44}

# res = st1.union(st2) # объединение множеств
# res = st1 | st2


res = st1.intersection(st2) # пересечение множеств
res = st1 & st2
print(res)

res = st1.difference(st2) # вычитание множеств
res = st2 - st1
print(res)

res = st1.symmetric_difference(st2)
res = st1 ^ st2
print(res)

st3 = {3, 4}
print(st3.issubset(st1))
print(st1.issuperset(st3))