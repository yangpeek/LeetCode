class LCSSolution:
    def __init__(self, inputA, inputB, layer):
        self.inputA = inputA
        self.inputB = inputB
        self.layer = layer
        print(" "*layer, "(", self.inputA, ",", self.inputB, ")")
    
    def findValue(self):
        a_l = len(self.inputA)
        b_l = len(self.inputB)
        if a_l == 0 or b_l == 0:
            return 0;
        elif self.inputA[a_l-1] == self.inputB[b_l -1]:
            return 1 + LCSSolution(self.inputA[0:a_l - 1], self.inputB[0 : b_l -1], self.layer + 1).findValue()
        else:
            return max(LCSSolution(self.inputA[0:a_l - 1], self.inputB, self.layer + 1).findValue(),
                       LCSSolution(self.inputA, self.inputB[0 : b_l - 1], self.layer + 1).findValue())
                       
if __name__ == '__main__':
    longest = LCSSolution("abcdc", "adcc", 0).findValue()
    print("res: ", longest)
