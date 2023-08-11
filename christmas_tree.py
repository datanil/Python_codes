rows = int(input('Input the no. of rows for a christmas tree : '))

if rows < 3:
  print('Tree can not be generated')
  exit()

for i in range(rows):
  for j in range(rows-i-1):
    print(end = ' ')
  for j in range(i+1):
    print('*', end = ' ')
  print()

for trunk in range(rows-2):

      print("   | |")

