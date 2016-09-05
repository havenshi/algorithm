# three classes: Printer, Task, and PrintQueue.

# 1.task: a.timestamp(time to create each task, random)
#         b.waitTime=currenttime - timestamp
# 2.queue
# 3.printer: timeRemaining(time to print each task, page/pagerate)

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):          # The tick method decrements the internal timer and sets the printer to idle if the task is completed.
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):          # The Printer class will need to track whether it has a current task. If it does, then it is busy and the amount of time needed can be computed from the number of pages in the task. 
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate # print time



import random

class Task:
    def __init__(self,time):
        self.timestamp = time  # This timestamp will represent the time that the task was created and placed in the printer queue. 
        self.pages = random.randrange(1,21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):   # The waitTime method can then be used to retrieve the amount of time spent in the queue before printing begins.
        return currenttime - self.timestamp
        



from pythonds.basic.queue import Queue

import random

def simulation(numSeconds, pagesPerMinute):

    labprinter = Printer(pagesPerMinute) # Printer(5)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds): # currentSecond in range(3600), means 1 second, 2 seconds,,,

      if newPrintTask():                 # if num=180, one task is created
         task = Task(currentSecond)      # currentSecond=1(or other random until num=180), timestamp=1
         printQueue.enqueue(task)        # add that task into queue

      if (not labprinter.busy()) and (not printQueue.isEmpty()): # if printer is not busy
        nexttask = printQueue.dequeue()                          # remove the task(nexttask) from queue, and print
        waitingtimes.append(nexttask.waitTime(currentSecond))    # waitingtimes=[nexttask.(currenttime - self.timestamp),nexttask.(currenttime - self.timestamp)nexttask.(currenttime - self.timestamp),,,]
        labprinter.startNext(nexttask)  # 1.startNext(nexttask),self.timeRemaining(unit is seconds)=randompage * pagerate

      labprinter.tick()   # 2.self.timeRemaining - 1

    averageWait=sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))

def newPrintTask():  # A boolean helper function, newPrintTask, decides whether a new printing task has been created. 
    num = random.randrange(1,181)
    if num == 180:   #  on average there will be one task every 180 seconds
        return True
    else:
        return False

for i in range(10):
    simulation(3600,5)

