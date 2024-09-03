import pdb

counter = 1

while counter <= 5:
    print(counter)
    pdb.set_trace()  # Add breakpoint
    counter += 1