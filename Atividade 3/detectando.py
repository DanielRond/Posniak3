xi_A,yi_A,xf_A,yf_A = map(int,input().split())
xi_B,yi_B,xf_B,yf_B = map(int,input().split())
if (xi_A<=xf_B and xi_B<=xf_A) and(yi_A<=yf_B and yi_B<=yf_A):
    print("1")
else:
    print("0")