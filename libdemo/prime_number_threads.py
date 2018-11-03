import threading

class PrimeThread(threading.Thread):
    def __init__(self, number,file):
        super().__init__()
        self.number = number
        self.file = file

    def run(self):
        # print("\nNo. of threading running : ", threading.active_count())
        for i in range(2, self.number // 2 + 1):
            if self.number % i == 0:
                self.file.write(f"{self.number} is not prime number!\n")
                break
        else:
            self.file.write(f"{self.number} is prime number!\n")


nums = [2113039, 1919191, 229292929291731, 37, 29329391379, 393939111,3938383812]

# open file for writing
with open("prime.txt","w") as f:
    for n in nums:
        t = PrimeThread(n,f)
        t.start()

print("Loop is done!")
# Close file after all threads are done

