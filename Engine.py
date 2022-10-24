import random
name = input('''
Pick a name
''')
hp = 20
bhp = 200
dmg = 0

print('''
Something has appeared!

''')
for i in range(200):
 pc = input(f'''

 [FIGHT][ACT][ITEM][MERCY]
 {name}  {hp}/20
 ''')
 #fight
 if pc == 'fight':

  pc2 = input('''
 * Something
 
 ''')
  if pc2 == 'something':
   dmg = random.randint(10,19)
  bhp -= dmg
  print(f'''
  * {dmg} damage dealt!
  
  ''')
 #act
 elif pc == 'act':
  pc2 = input('''
 * Check
 * Talk
 ''')
  if pc2 == 'check':
   print(f'''
  * Something {random.randint(1,200)} ATK {random.randint(1,200)} DEF  
  * ? ? ?
  * ? ? ?
  ''')
  else:
   print('''
  * You tried talking to it...
  ...
  . . .
  ''')
 #item
 elif pc == 'item':
  pc2 = input('''
 * endless popato chisps
 
 ''')
 if pc2 == 'chips':
  hp += 5
  print('''
  * You ate the popato chisps
  * HP increased!
  ''')
  if hp > 20:
   hp = 20
 #mercy
 if pc == 'mercy':
  pc2 = input('''
 * Spare
 
 ''')
 if pc2 == 'spare':
  print('''
  * Its name isnt yellow!
  
  ''')

 #boss attack
 batk = random.randint(2,8)
 hp -= batk
 print(f'''
* Something attacked!
* {batk} damage dealt!
''')

 #win
if bhp < 0:
 print('''
 * YOU WON!
 * You earned 250 XP 300 G
 ''')
#loss
if hp < 0:
 print('''
 You're dead
 
 (haha)
 ''')
