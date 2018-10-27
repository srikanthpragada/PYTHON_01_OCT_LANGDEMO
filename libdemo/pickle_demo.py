import pickle

nums = [10,20,30]

with open("nums.dat","wb") as f:
    pickle.dump(nums,f)

# Unpickle
f = open("nums.dat","rb")
nums = pickle.load(f)
print(nums)

