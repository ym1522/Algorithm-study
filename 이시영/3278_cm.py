from sys import stdin

color=stdin.readline().split()
sum=int(color[0])*1000 + int(color[1])*1500 + int(color[2])*2000 + int(color[3])*3000 + int(color[4])*5000
print(sum)