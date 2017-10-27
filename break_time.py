import time
import webbrowser

loop_ctr = 0
breaks = 3

print("Work has started at "+time.ctime())
while(loop_ctr < breaks):
  time.sleep(10)
  loop_ctr = loop_ctr + 1
  print("Time for break at "+time.ctime())
  webbrowser.open("https://www.youtube.com/watch?v=s5BJXwNeKsQ")
