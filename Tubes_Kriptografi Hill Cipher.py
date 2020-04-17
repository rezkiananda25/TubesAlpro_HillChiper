import sympy as sm


'''
    +----------------------------------------+
	|        MUHAMMAD REZKI ANANDA           |
    +----------------------------------------+
	|        SI/43/09 (1202190044)	 	     |
    +----------------------------------------+
'''

class HillChiper():
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def getKey(self):
        k = 0
        for i in range(3):
            for j in range(3):
                keyMatrix[i][j] = ord(self.y[k]) % 65
                k += 1


    def getInversKey(self):
        self.getKey()
        convertSM = sm.Matrix(keyMatrix)
        minorCoFactorKeyMatrix = convertSM.adjugate()
        determinantKeyMatrix = convertSM.det()

        inverseKeyMatrix = (determinantKeyMatrix * minorCoFactorKeyMatrix % 26)
        inverseKeyMatrix = inverseKeyMatrix.tolist()

        return inverseKeyMatrix
        
    
    def encryptData(self, messageMatrix):
        for i in range(3):
            for j in range(1):
                cipherMatrix[i][j] = 0
                for x in range(3):
                    cipherMatrix[i][j] += (keyMatrix[i][x] * messageMatrix[x][j])
                cipherMatrix[i][j] = cipherMatrix[i][j] % 26

        return cipherMatrix


    def decryptData(self, cipherMatrix):
        inverseKeyMatrix = self.getInversKey()
        cipherMatrix = self.encryptData(messageMatrix)
        for i in range(3):
            for j in range(1):
                messageMatrix[i][j] = 0
                for x in range(3):
                    messageMatrix[i][j] += (inverseKeyMatrix[i][x] * cipherMatrix[x][j])
                messageMatrix[i][j] = messageMatrix[i][j] % 26        
        

    def processEncrypt(self):
        self.getKey()
        for i in range(3):
            messageMatrix[i][0] = ord(self.x[i]) % 65

        self.encryptData(messageMatrix)

        CipherText = []
        for i in range(3):
            CipherText.append(chr(cipherMatrix[i][0] + 65))
        print("Ciphertext: ", "".join(CipherText)) 


    def processDecrypt(self):
        self.decryptData(cipherMatrix)
        for i in range(3):
            cipherMatrix[i][0] = ord(self.x[i]) % 65

        MessageText = []
        for i in range(3):
            MessageText.append(chr(cipherMatrix[i][0] + 65))
        print("Dekripsi: ", "".join(MessageText)) 


class OutputHillChiper(HillChiper):
    def showMenu(self):
        return None

if __name__ == "__main__":

    keyMatrix = [[0] * 3 for i in range(3)] 
    messageMatrix = [[0] for i in range(3)] 
    cipherMatrix = [[0] for i in range(3)]

    print("\n********** APLIKASI ENKRIPSI HILL CIPHER **********\n")
    print("SEMUA KATA YANG DI INPUTKAN AKAN DI UPPERCASE")
    isMessage = input(">> Masukkan 3 huruf yang ingin di enkripsi \t:")
    
    if any(str.isdigit(c) for c in isMessage):
        print('''
            Input supplied should be of type 'str' 
            ''')
    else:
        while len(isMessage) != 3:
            print('''
            Error. Only 3 digit allowed
            ''')
            exit()

        msg__ = isMessage.upper()
        key__ = "GYBNQKURP"

        ftr = HillChiper(msg__, key__)
        ftr.processEncrypt()
        print()
        ftr.processDecrypt()

    


    
   

       

    

    
    


