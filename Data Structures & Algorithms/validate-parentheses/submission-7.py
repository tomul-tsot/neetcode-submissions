class Solution:
    def isValid(self, s: str) -> bool:

        b=[]
        pairs=set()
        for char in s:
            if char=='[' or char=='(' or char=='{':
                b.append(char)
            elif (char=='}' or char==')' or char==']') and len(b)!=0:
                t=(b.pop(),char)
                pairs.add(t)
            elif (char=='}' or char==')' or char==']') and len(b)==0:
                return False
        if len(b)>0:
            return False

        if len(pairs)==1:
            if list(pairs)==[('(',')')] or list(pairs)==[('[',']')] or list(pairs)==[('{','}')]:
                return True
        elif len(pairs)==2:
            if sorted(list(pairs))==[('(',')'),('[',']')] or sorted(list(pairs))==[('(',')'),('{','}')] or sorted(list(pairs))==[('[',']'),('{','}')]:
                return True
        elif len(pairs)==3:
            if sorted(list(pairs))==[('(',')'),('[',']'),('{','}')]:
                return True
        return False