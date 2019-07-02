#python3

data = ''

try:
      f = open('pali.txt', 'x')
      f.close()
except FileExistsError:
      f = open('pali.txt', 'r')
      data = f.read()
      f.close()

#armazenando texto original na variavel: data_original
data_original = data

#tratando badstrings
data = data.lower()
badstrings = "'!?,.@:#$¨&*()_+=-/ " + '“"”' 
for i in range(0, len(badstrings)):
      data = data.replace(badstrings[i], " ")

acentuadasA = 'áàãâ'
acentuadasE = 'éê'
acentuadasI = 'í'
acentuadasO = 'óõô'
acentuadasU = 'ú'
for i in range(0, len(acentuadasA)):
      data = data.replace(acentuadasA[i], "a")
for i in range(0, len(acentuadasE)):
      data = data.replace(acentuadasE[i], "e")
for i in range(0, len(acentuadasI)):
      data = data.replace(acentuadasI[i], "i")
for i in range(0, len(acentuadasO)):
      data = data.replace(acentuadasO[i], "o")
for i in range(0, len(acentuadasU)):
      data = data.replace(acentuadasU[i], "u")


#Funcao que determina se é palindrome
def isPalindrome(s): 
    for i in range(0, len(s)): 
      if (s[i] != s[len(s)-i-1]): 
            return False      
    return True

#Funcao que conta cada palindrome dentro de uma string
def showAllPalindromes(s):
      for i in range(len(s)):
            x = ""
            c = 0
            for j in range(i, len(s)):
                  if (s[j] == " " and len(x)>0):
                        c += 1
                        continue
                  x += s[j]
                  if (len(x) > 1 and isPalindrome(x) == True):
                        print(i, end = ' ')
                        print(x, end = ' ')
                        print(i + len(x) + c - 1)                        
      return 1

showAllPalindromes(data)