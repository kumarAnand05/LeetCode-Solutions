import statistics
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        #To find out the point of differences in between two strings
        def differences(sample,s):
            out=0
            for n in range(8):
                if s[n]!=sample[n]:out+=1
            return out
        if end not in bank:return -1    # returning -1 as end result not in bank that means it is not a valid mutation
        elif start in bank:return differences(start,end) # if both the start and end element are in bank then the number of mutations will be equal to the number of the differences between them.
        elif differences(start,end)==1:return 1 # returning 1 as only 1 mutation is required so there is no need to look in the bank for any intermediate mutation of the start gene.
        else:
            bank.insert(0,start)    # inserting start gene in bank at index 0
            temp=[]     # to store the number of differences from the end element
            for p in range(len(bank)):  # iterating through each element of bank and storing the point of differences from end gene
                s=bank[p]
                temp.append(differences(sample=end,s=s))
            sd=[]       # to store the number of differences from start element
            for p in range(len(bank)):  # iterating through each element of bank and storing the point of differences from start gene
                s=bank[p]
                sd.append(differences(sample=start,s=s))
            final=[]       # to store the sum of the matrix of differences 
            for n in range(len(sd)):    # iterating through each element of the differences matices temp and sd
                final.append(temp[n]+sd[n])
            fp=temp[0]     # differences between start and end element 
            r=list(range(fp))       # printing the range of the natural number till the point of difference of start and end element to check for any jump in mutations in bank matrix
            if len(set(r).difference(set(temp)))!=0:return -1   # checking for any jump int the matations in bank matrix i.e checking that all intermediate mutations are in the bank matrix.
            else:return statistics.mode(final)      # returning the max occuring sum value as the differences sum will always be equal for all valid mutations.
