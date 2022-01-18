import csv
    
class Profile:

    '''Eu sei que não era necessário esse código todo, porém, você pode usar essa classe em seus códigos

    Mas se você está aqui só pelo enigma, é necessário que todos os arquivos estejam dentro da pasta enigma para 
    tudo funcionar corretamente'''


    def __init__(self, file_csv = 'file.csv', items = dict()):
        try:
            a = open(file_csv, 'r')
            a.close()
            
        except FileNotFoundError:
            a = open(file_csv, 'wt+')
            a.close()

        a = open(file_csv,'r')

        reader = csv.reader(a)
        saves = list()
    
        for line in reader: saves.append(line)

        a.close()

        self.file = file_csv
        self.items = items
        self.saves = saves[:]
   
   
    def create_profile(self, name):
        name = name.strip()

        if name == '': name = 'Profile'
        
        self.name = name
        
        return self._save_profile()


    def _save_profile(self):
        self.list = [self.name, self.items]

        a = open(self.file, 'a', newline='')

        recorder = csv.writer(a)
        recorder.writerow(self.list)

        a.close()

        self.__init__(self.file, self.items)

        return self.load_profile(-1)


    def load_profile(self, position):
        try:
            self.info = self.saves[position][:]
            self.info[1] = eval(self.info[1])
            return self.info

        except:
            print('Profile not found')
            return None


    def save_progress(self, progress, position = -1):
        self.saves[position] = progress[:]
        
        a = open(self.file, 'w', newline='')

        recorder = csv.writer(a)

        for i in self.saves: recorder.writerow(i)

        a.close()
           

    def delete_profile(self, position):
        a = open(self.file, 'w')
        recorder = csv.writer(a)

        try:
            self.saves.pop(position)
            for c, i in enumerate(self.saves): recorder.writerow(self.saves[c])  
               
        except:
            print('Profile not found')

        finally:
            a.close()
    

    def list_profiles(self):
        self.__init__(self.file, self.items)

        text = ''

        for c, i in enumerate(self.saves): text += f'{c+1} - {self.saves[c][0]}\n'

        if text == '': return None

        else: return text



a = Profile('enigma/perfis.csv')

year = int(input('Digite um número entre 0 e 2022: '))

haha = a.load_profile(year)

if haha != None:
    print(haha[0])

    for i in haha[1].keys():
       print(f'{i}: {haha[1][i]}')