 def mod_result(x,n,d):
        result=1
        if(x==0):
        	return 0
        while (n > 0):
            if (n % 2 == 1):
                result = (result * x) % d
            n = n >> 1
            x = (x * x) % d
        return result
        
mod_result(5,117,19)