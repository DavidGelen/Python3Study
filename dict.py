# -*- coding: utf-8 -*-

dd = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print('dd[\'Michael\'] = ',dd['Michael'])
print('dd[\'Michael\'] = %d' % dd['Michael'])

#如果key不存在，可以返回None，或者自己指定的value
print('Bob多大岁数呢？',dd.get('Bob'))
print('炮爷多大岁数呢？',dd.get('pao',3))

#通过in判断key是否存在 
print('\'pao\' in dd 是','pao' in dd)      

#要删除一个key，用pop(key)方法，对应的value也会从dict中删除
dd.pop('Michael')
print('dd = ',dd)