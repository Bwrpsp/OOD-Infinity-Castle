class Room():
    def __init__(self,num,demon):
        self.num = num
        self.demon = demon
        
def process_room_number(method,n,m):
    if method == 1:  #add n demon
        return m + n
    elif method == 2:  #add inf demon on n busses   (n is 1 if no bus)
        return m*(n+1)
    elif method == 3: #add inf demon on inf bus
        return int(((n + m-1) * (n + m)) / 2 + m)
    else:
        return m
    
