import sys

def main(argv):
   lst = []
   with open(argv[0], 'r'  ) as datFile:
      for data in datFile:
         s = ''
         val = sorted(set(data.split()), key=int)
         for i in val:
            s = s + ' ' + str(int(i) - 1) + ' ' + '1,'
         s = '{' + s[1:-1] + '}\n'
         lst.append(s)

   with open('korsarak.arff', 'w') as f:
      f.write('@relation korsarak\n')
      for i in range(41270):
         f.write('@attribute ' +str(i + 1) + ' {0,1}\n')
      f.write('@data\n')
      f.writelines(lst)

if __name__ == "__main__":
   main(sys.argv[1:])