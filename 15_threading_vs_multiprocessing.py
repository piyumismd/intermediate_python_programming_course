
# process: An instant of a programme (e.g. a Python interpreter)

# + Takes advantage of multiple CPUs and cores
# + Separate memory space -> memory is not shared between processes
# + Great for CPU bound processing
# + New process started independently of other processes
# + Processes are interruptable/killable
# + one GIL (Global Interpreter Lock) for each process -> avoid GIL limitations

# - HeavyWeight
# - Starting a process is slower than starting a thread
# - More memory
# - IPC (Inter Process Communication) is more complicated

# Threads: An entity within a process that can be scheduled (also known as " lightweight process")

# + All threads within a process share the same memory
# + Lightweight
# + Starting a thread faster than starting a process
# + Great for I/O bound (Input - Output) tasks

# - Threading is limited by GIL: only one thread at a time
# - No effect for CPU bound tasks
# - Not Interruptable/ killable
# - Careful with race conditions

