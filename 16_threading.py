
from threading import Thread
import time


database_value = 0


def increase():
    global database_value

    local_copy = database_value

    # processing
    local_copy += 1
    time.sleep(0.1)
    database_value = local_copy


if __name__ == "__main__":
    print("start value", database_value)

    thread1 = Thread(target=increase)  # target should define a function. in this case function name is "increase"
    thread2 = Thread(target=increase)

    thread1.start()
    thread2.start()

    thread1.join()  # block the thread until all the elements in the thread are processed.
    thread2.join()

    print("end value", database_value)

    print("end main")

# when we run the above programme we can see that the end value is "0" eventhough there are
# two threads. The reason for that is our race condition runs same time. After going through
# the first thread 1 local_copy is "1" and database_copy is "1" and sleep 0.1 s.
# Then, when it goes to thread 2 database_value automatically adjust in to "0" and because of
# that local_copy is being "0".
# To overcome this error we have to lock the thread 1 after the first run.

from threading import Lock


database_value = 0


def increase(lock):
    global database_value

    lock.acquire()
    local_copy = database_value

    # processing
    local_copy += 1
    time.sleep(0.1)
    database_value = local_copy
    lock.release()


if __name__ == "__main__":

    lock = Lock()
    print("start value", database_value)

    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()  # block the thread until all the elements in the thread are processed.
    thread2.join()

    print("end value", database_value)

    print("end main")

# everytime you acquire a lock you should release it.
# we can use lock as a context manager and by one line we can perform both lock acquire and lock release.


from threading import Lock


database_value = 0


def increase(lock):
    global database_value

    with lock:
        local_copy = database_value

    # processing
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy


if __name__ == "__main__":

    lock = Lock()
    print("start value", database_value)

    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("end value", database_value)

    print("end main")

##  queues are used for thread safe and process safe data exchanges and data processing
# in multithreading or multiprocessing.
# queue is a linear data structure that follows feefo (first in first out) principle.

from queue import Queue

if __name__ == "__main__":

    q = Queue()

    q.put(1)
    q.put(2)
    q.put(3)

    # 3 2 1 --->

    first = q.get()
    print(first)

    q.task_done()  # when you are done the process
    q.join()  # this block until all the items in the queue have been gotten and processed.
# this is similar to the thread.join method it blocks main thread and wait until
# all the elements in the queue are processed.
    print("end main")


# example
from threading import current_thread


def worker(q, lock):
    while True:
        value = q.get()

        # processing...
        with lock:
            print(f"in {current_thread().name} got {value}")
        q.task_done()


if __name__ == "__main__":

    q = Queue()
    lock = Lock()

    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        thread.daemon = True  # daemon thread is a background thread. it dies when the main thread dies.
        # when main thread dies all the threads die.
        # because of this daemon thread our infinite while loop will stop at some point.
        # otherwise, we have to use conditional if statement to stop the while loop.
        thread.start()

    for i in range(1, 21):
        q.put(i)

    q.join()

    print("end main")
