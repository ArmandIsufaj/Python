import random
import matplotlib.pyplot as plt
class Job:
    def __init__(self, arrival, service_start, duration):
        self.arrival = arrival
        self.service_start = service_start
        self.duration = duration
        self.service_end = self.service_start + self.duration
        self.wait1 = 0
        self.wait2 = 0
        self.wait3 = 0
        self.wait4 = 0
class Job1(Job):
    def __init__(self, arrival, service_start, duration):
        super().__init__(arrival, service_start, duration)
        self.wait1 = service_start - arrival
class Job2(Job):
    def __init__(self, arrival, service_start, duration):
        super().__init__(arrival, service_start, duration)
        self.wait2 = service_start - arrival
class Job3(Job):
    def __init__(self, arrival, service_start, duration):
        super().__init__(arrival, service_start, duration)
        self.wait3 = service_start - arrival
class Job4(Job):
    def __init__(self, arrival, service_start, duration):
        super().__init__(arrival, service_start, duration)
        self.wait4 = service_start - arrival
def plot(a, x, x2, finallist, qsizelist, pzlist, p5list):
    for j in range(1, 5):
        plt.subplot(1, 4, j)
        if j == 1:
            for i in range(a):
                plt.plot(x, finallist[i][::-1], label='average wait: Server' + str(i + 1))
            plt.xlabel('Simulation Time')
            plt.ylabel('Average Wait')
            plt.title('Wait Time vs Simulation Time')
            plt.legend()
        elif j == 2:
            for i in range(a):
                plt.plot(x, qsizelist[i][::-1], label='average wait: Server' + str(i + 1))
            plt.xlabel('Simulation Time')
            plt.ylabel('Average Queue Size')
            plt.title('Queue size vs Simulation Time')
            plt.legend()
        elif j == 3:
            for i in range(a):
                plt.plot(x, finallist[i][::-1], label='average wait: Server' + str(i + 1))
                plt.plot(x, qsizelist[i][::-1], label='average queue size: Server' + str(i + 1))
            plt.xlabel('Simulation Time')
            plt.ylabel('Average Wait')
            plt.title('Queue Size & Wait time vs Time  ')
            plt.legend()
        else:
            plt.plot(x2, pzlist, label='probability q size is 0 upon arrival')
            if a == 2:
                plt.plot(x2, p5list[1][::-1], label='probability q size is 5x greater than APS Non-Priority')
                plt.plot(x2, p5list[2][::-1], label='probability q size is 5x greater than APS Priority')
            else:
                plt.plot(x2, p5list[0][::-1], label='probability q size is 5x greater than APS')
            plt.xlabel('Simulation Time')
            plt.ylabel('Parameter Size')
            plt.title('Calculated parameters vs Simulation Time')
            plt.legend()
def timing(time_next_arrival, time_next_departure):
    if time_next_arrival < time_next_departure:
        return 1
    else:
        return 2
def wait_calc(x1, x2, finallist, qsizelist, pzlist, p5list, waits, queue_areas, time,zero_queue, non_zero_queue,queue_size, average_packet_size, mean_arrival,classcounter,classcounter2,zerocounter,nonzerocounter):
    for i in range(len(waits)):
        print("average wait server ", i + 1, ": ", str(sum(waits[i]) / len(waits[i])))
        print("average queue size server ", i + 1, ": ", str(queue_areas[i] / time))
        finallist[i].append(sum(waits[i]) / len(waits[i]))  # for average waits, waiting time
        qsizelist[i].append(queue_areas[i] / time)
    if len(waits)==2:
        pzlist.append(zero_queue / (zerocounter / (zerocounter + nonzerocounter)))
        p5list[1].append(classcounter[0] / (classcounter2[0] + classcounter[0] + classcounter2[1] + classcounter[1]))
        p5list[2].append(classcounter[1] / (classcounter2[0] + classcounter[0] + classcounter2[1] + classcounter[1]))
        print("probability that the queue size for Job1 is more than 5: ", classcounter[0]/(classcounter2[0]+classcounter[0]+classcounter2[1]+classcounter[1]),"probability that the queue size for Job2 is more than 5: ", classcounter[1]/(classcounter2[0]+classcounter[0]+classcounter2[1]+classcounter[1]))
        print("probability that the queue size is 0 at arrival of a new packet: ",zerocounter / (zerocounter + nonzerocounter))
    else:
        pzlist.append(zero_queue / (non_zero_queue + zero_queue))
        p5list[0].append(queue_size / (5 * average_packet_size + queue_size))
        print("probability that the queue size is 0 at arrival of a new call: ",
              zero_queue / (non_zero_queue + zero_queue))
        print("probability that the queue size is greater than 5 times the average packet size: ",
              queue_size / (5 * average_packet_size + queue_size))
    x1.append(time / mean_arrival)
    x2.append(mean_arrival)
    return x1, x2, pzlist, p5list, finallist, qsizelist
def task1(average_arrival, average_packet_size):
    finallist = [[], [], [], []]
    qsizelist = [[], [], [], []]
    x1 = []
    x2 = []
    pzlist = []
    p5list = [[], [], []]
    for counter in range(10):
        mean_arrival = average_arrival + counter
        time = 0
        completed_jobs = 0
        end_of_simulation = 10000
        time_next_arrival = 0
        queue_size = 0
        queue_area = 0.0
        zero_queue = 0
        non_zero_queue = 0
        Jobs = []
        while (time < end_of_simulation):
            if len(Jobs) != 0:
                next_event = timing(time_next_arrival, time_next_departure)
            else:
                next_event = 1
            if next_event == 1:
                ## arrival
                duration = random.expovariate(1 / average_packet_size)
                if len(Jobs) == 0:
                    time_next_arrival = random.expovariate(1 / mean_arrival)
                    service_start = time_next_arrival
                    time_next_departure = time_next_arrival + duration
                    zero_queue += 1
                else:
                    time_next_arrival = time_next_arrival + random.expovariate(1 / mean_arrival)
                    service_start = max(time_next_arrival, Jobs[-1].service_end)
                    non_zero_queue += 1
                Jobs.append(Job1(time_next_arrival, service_start, duration))
                queue_area += (time_next_arrival - time) * queue_size
                queue_size = queue_size + 1
                time = time_next_arrival
                if queue_size == 0:
                    time_next_departure = time + duration
            else:
                # departure
                queue_area += (time_next_departure - time) * queue_size
                queue_size = queue_size - 1
                completed_jobs = completed_jobs + 1
                time = time_next_departure
                if queue_size != 0:
                    time_next_departure = Jobs[completed_jobs].service_end
        waits1 = [job.wait1 for job in Jobs]
        waits = [waits1]
        queue_areas = [queue_area, 0, 0, 0]
        wait_calc(x1, x2, finallist, qsizelist, pzlist, p5list, waits,
                  queue_areas, time, zero_queue, non_zero_queue,
                  queue_size, average_packet_size, mean_arrival,0,0,0,0)
    x = x1[::-1]
    x.sort()
    x2 = x2[::-1]
    plt.figure("Task 2.1")
    plot(1, x, x2, finallist, qsizelist, pzlist, p5list)
def task2(average_arrival, average_packet_size):
    finallist = [[], [], [], []]
    qsizelist = [[], [], [], []]
    x1 = []
    x2 = []
    pzlist = []
    p5list = [[], [], []]
    for counter in range(10):
        mean_arrival = average_arrival + counter
        time = 0
        completed_jobs = 0
        end_of_simulation = 10000
        queue_size = 0
        queue_areas = [0.0, 0.0, 0.0, 0.0]
        zero_queue = 0
        non_zero_queue = 0
        Jobs = []
        Job = [Job1, Job2, Job3, Job4]
        while (time < end_of_simulation):
            if len(Jobs) != 0:
                next_event = timing(time_next_arrival, time_next_departure)
            else:
                next_event = 1
            if next_event == 1:
                d = random.randint(0, 3)
                ## arrival
                duration = random.expovariate(1 / average_packet_size)
                if len(Jobs) == 0:
                    time_next_arrival = random.expovariate(1 / mean_arrival)
                    service_start = time_next_arrival
                    time_next_departure = time_next_arrival + duration
                    zero_queue += 1
                else:
                    time_next_arrival = time_next_arrival + random.expovariate(1 / mean_arrival)
                    service_start = max(time_next_arrival, Jobs[-1].service_end)
                    non_zero_queue += 1
                Jobs.append(Job[d](time_next_arrival, service_start, duration))
                queue_areas[d] += (time_next_arrival - time) * queue_size
                queue_size = queue_size + 1
                time = time_next_arrival
                if queue_size == 0:
                    time_next_departure = time + duration
            else:
                # departure
                queue_areas[d] += (time_next_departure - time) * queue_size
                queue_size = queue_size - 1
                completed_jobs = completed_jobs + 1
                time = time_next_departure
                if queue_size != 0:
                    time_next_departure = Jobs[completed_jobs].service_end
        waits1 = [Job1.wait1 for Job1 in Jobs]
        waits2 = [Job2.wait2 for Job2 in Jobs]
        waits3 = [Job3.wait3 for Job3 in Jobs]
        waits4 = [Job4.wait4 for Job4 in Jobs]
        waits = [waits1,waits2,waits3,waits4]
        wait_calc(x1, x2, finallist, qsizelist, pzlist, p5list, waits,
                  queue_areas, time, zero_queue, non_zero_queue,
                  queue_size, average_packet_size, mean_arrival,0,0,0,0)
    x = x1[::-1]
    x.sort()
    x2 = x2[::-1]
    finallist = finallist[::-1]
    qsizelist = qsizelist[::-1]
    pzlist = pzlist[::-1]
    plt.figure("Task 2.2")
    plot(4, x, x2, finallist, qsizelist, pzlist, p5list)
def task3A(average_arrival, average_packet_size):
    finallist = [[], []]
    qsizelist = [[], []]
    x1 = []
    x2 = []
    pzlist = []
    p5list = [[], [], []]
    for counter in range(10):
        mean_arrival = average_arrival + counter
        time = 0
        completed_jobs = 0
        end_of_simulation = 10000
        classcounter = [0, 0]
        classcounter2 = [0, 0]
        zerocounter = 0
        nonzerocounter = 0
        queue_size = 0
        queue_sizes = [0, 0]
        queue_areas = [0.0, 0.0, 0.0, 0.0]
        Jobs = []
        Job = [Job1, Job2, Job3, Job4]
        while (time < end_of_simulation):
            if len(Jobs) != 0:
                next_event = timing(time_next_arrival, time_next_departure)
            else:
                next_event = 1
            if next_event == 1:
                d = random.randint(1, 10)
                if d > 2:
                    d = 0
                else:
                    d = 1
                ## arrival
                duration = random.expovariate(1 / average_packet_size)
                if len(Jobs) == 0:
                    time_next_arrival = random.expovariate(1 / mean_arrival)
                    service_start = time_next_arrival
                    time_next_departure = time_next_arrival + duration
                    zerocounter += 1
                else:
                    time_next_arrival = time_next_arrival + random.expovariate(1 / mean_arrival)
                    service_start = max(time_next_arrival, Jobs[-1].service_end)
                    nonzerocounter += 1
                Jobs.append(Job[d](time_next_arrival, service_start, duration))
                queue_areas[d] += (time_next_arrival - time) * queue_size
                queue_size = queue_size + 1
                queue_sizes[d] += 1
                if queue_size > 5:
                    classcounter[d] += 1
                else:
                    classcounter2[d] += 1
                time = time_next_arrival
                if queue_size == 0:
                    time_next_departure = time + duration
            else:
                # departure
                queue_areas[d] += (time_next_departure - time) * queue_size
                queue_size = queue_size - 1
                queue_sizes[d] -= 1
                completed_jobs = completed_jobs + 1
                time = time_next_departure
                if queue_size != 0:
                    time_next_departure = Jobs[completed_jobs].service_end
        waits1 = [Job1.wait1 for Job1 in Jobs]
        waits2 = [Job2.wait2 for Job2 in Jobs]
        waits = [waits1,waits2]
        wait_calc(x1, x2, finallist, qsizelist, pzlist, p5list, waits,
                  queue_areas, time, 0, 0,
                  queue_size, average_packet_size, mean_arrival,classcounter,classcounter2,zerocounter,nonzerocounter)
    x = x1[::-1]
    x.sort()
    x2 = x2[::-1]
    plt.figure("Task 2.3A")
    plot(2, x, x2, finallist, qsizelist, pzlist, p5list)
def task3B(average_arrival, average_packet_size):
    finallist = [[], []]
    qsizelist = [[], []]
    x1 = []
    x2 = []
    pzlist = []
    p5list = [[], [], []]
    for counter in range(10):
        mean_arrival = average_arrival + counter
        time = 0
        completed_jobs = 0
        end_of_simulation = 10000
        classcounter = [0, 0]
        classcounter2 = [0, 0]
        zerocounter = 0
        nonzerocounter = 0
        queue_size = 0
        queue_areas = [0.0, 0.0, 0.0, 0.0]
        Jobs = []
        Job = [Job1, Job2, Job3, Job4]
        while (time < end_of_simulation):
            if len(Jobs) != 0:
                next_event = timing(time_next_arrival, time_next_departure)
            else:
                next_event = 1
            if next_event == 1:
                d = random.randint(1, 10)
                if d > 2:
                    d = 0
                else:
                    d = 1
                ## arrival
                duration = random.expovariate(1 / average_packet_size)
                if len(Jobs) == 0:
                    time_next_arrival = random.expovariate(1 / mean_arrival)
                    service_start = time_next_arrival
                    time_next_departure = time_next_arrival + duration
                    zerocounter += 1
                else:
                    time_next_arrival = time_next_arrival + random.expovariate(1 / mean_arrival)
                    service_start = max(time_next_arrival, Jobs[-1].service_end)
                    nonzerocounter += 1
                Jobs.append(Job[d](time_next_arrival, service_start, duration))
                queue_areas[d] += (time_next_arrival - time) * queue_size
                queue_size = queue_size + 1
                time = time_next_arrival
                if queue_size > 5:
                    classcounter[d] += 1
                else:
                    classcounter2[d] += 1
                if queue_size == 0:
                    time_next_departure = time + duration
            else:
                # departure
                if queue_areas[1] == 0:
                    queue_areas[1] += (time_next_departure - time) * queue_size
                else:
                    queue_areas[d] += (time_next_departure - time) * queue_size
                queue_size = queue_size - 1
                completed_jobs = completed_jobs + 1
                time = time_next_departure
                if queue_size != 0:
                    time_next_departure = Jobs[completed_jobs].service_end
        waits1 = [Job1.wait1 for Job1 in Jobs]
        waits2 = [Job2.wait2 for Job2 in Jobs]
        waits = [waits1, waits2]
        wait_calc(x1, x2, finallist, qsizelist, pzlist, p5list, waits,
                  queue_areas, time, 0, 0,
                  queue_size, average_packet_size, mean_arrival, classcounter, classcounter2, zerocounter,
                  nonzerocounter)
    x = x1[::-1]
    x.sort()
    x2 = x2[::-1]
    plt.figure("Task 2.3B")
    plot(2, x, x2, finallist, qsizelist, pzlist, p5list)
def Intro():
    intro = input("would you like to input your variables (y/n)?")
    if intro == 'y':
        average_arrival = int(input(" Your average arrival time:"))
        average_packet_size = int(input(" Your average packet size:"))
        task1(average_arrival, average_packet_size)
        task2(average_arrival, average_packet_size)
        task3A(average_arrival, average_packet_size)
        task3B(average_arrival, average_packet_size)
        plt.show()
    elif intro == 'n':
        average_arrival = 10
        average_packet_size = 10
        task1(average_arrival, average_packet_size)
        task2(average_arrival, average_packet_size)
        task3A(average_arrival, average_packet_size)
        task3B(average_arrival, average_packet_size)
        plt.show()
    else:
        print("That is not a valid input")
        Intro()
Intro()
