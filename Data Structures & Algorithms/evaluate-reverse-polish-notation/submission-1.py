class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        if len(tokens)==1:
            return int(tokens[0])
        s=[]
        te=0
        for i in range(len(tokens)):
            if tokens[i] in "+-*/":
                te+=1
                match(tokens[i]):
                    case "+":
                        res=s.pop()+s.pop()
                        s.append(res)
                    case "-":
                        a=s.pop()
                        b=s.pop()
                        res=b-a
                        s.append(res)
                    case "*":
                        res=s.pop()*s.pop()
                        s.append(res)
                    case "/":
                        a=s.pop()
                        b=s.pop()
                        res=int(b/a)
                        s.append(res)
            else:
                s.append(int(tokens[i]))
                
        return int(res)

                
            