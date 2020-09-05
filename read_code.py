from cnocr import CnOcr

def convert(s): 
    # initialization of string to "" 
    str1 = "" 
    # using join function join the list s by  
    # separating words by str1 
    return(str1.join(s)) 

# Full Screen 2880 x 1920

imgfile = "e:\\bwin\\tmp\\code3.jpg"

ocr = CnOcr()
res = ocr.ocr(imgfile)
txt = [''.join(s) for s in res]

print("Content:\n", txt)
