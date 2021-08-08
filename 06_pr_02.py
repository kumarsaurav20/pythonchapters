# Multiplication table from 2 to 20
for i in range (2 , 21):
     with open (f"tables/Multiplication_table{i}.txt",'w')as f:
         for j in range (1,11):
            f.write(f"{i}x{j}={i*j}\n")
            if j!=10:
                 f.write('\n')
