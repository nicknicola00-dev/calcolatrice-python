class Calcolatrice:
    
    operazioni = ('+','-','*','/')
    
    def __init__(self):
        while True:
            try:
                self._numDaSommare = int(input("Con quanti numeri operare: "))
                if self._numDaSommare >= 2:
                    break
                else: print("Almeno 2 numeri!")
            except ValueError:
                print("Devi inserire un intero!")
                
                
        while True:
            self._op=input("Che operazione fare [+ - * /]: ")
            if self._op in Calcolatrice.operazioni: break
        
        
        
    def addizione(self):
        for n in range(self._numDaSommare):
            while True:
                try:
                    num=float(input(f"{n+1}° numero: "))
                    break
                except ValueError: print("Devi inserire un numero!")
            if n==0: ris = num
            else: ris += num
        return ris
        
        
    def sottrazione(self):
        for n in range(self._numDaSommare):
            while True:
                try:
                    num=float(input(f"{n+1}° numero: "))
                    break
                except ValueError: print("Devi inserire un numero!")
            if n==0: ris = num
            else: ris -= num
        return ris
        
        
    def moltiplicazione(self):
        for n in range(self._numDaSommare):
            while True:
                try:
                    num=float(input(f"{n+1}° numero: "))
                    break
                except ValueError: print("Devi inserire un numero!")
            if n==0: ris = num
            else: ris *= num
        return ris
        
        
    def divisione(self):
        for n in range(self._numDaSommare):
            while True:
                try:
                    num=float(input(f"{n+1}° numero: "))
                    if num == 0: print("Non puoi dividere per 0!")
                    else: break
                except ValueError: print("Devi inserire un numero!")
            if n==0: ris = num
            else: ris /= num
        return ris


# MAIN
def main():
    while True:
        calc = Calcolatrice()
        if calc._op == '+': print(calc.addizione())
        elif calc._op == '-': print(calc.sottrazione())
        elif calc._op == '*': print(calc.moltiplicazione())
        elif calc._op == '/': print(calc.divisione())
        r=input("Continuare [s/n]: ").strip().lower()
        if r!='s': break

# EXECUTE
if __name__ == "__main__":
    main()