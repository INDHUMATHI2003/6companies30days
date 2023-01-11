from collections import defaultdict
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res=[]
        temp=defaultdict(list)
        for x in transactions:
            name,time,amount,city=x.split(',')
            time=int(time)
            amount=int(amount)
            temp[name].append({'time':time,'city':city})
        for x in transactions:
            name,time,amount,city=x.split(',')
            time=int(time)
            amount=int(amount)
            if amount>1000:
                res.append(x)
            elif name in temp:
                for i in temp[name]:
                    if abs(i['time']-time)<=60 and i['city']!=city:
                        res.append(x)
                        break
                
        return res
                        
