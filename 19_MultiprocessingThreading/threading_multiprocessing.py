"""
📁 19_MultiprocessingThreading/threading_multiprocessing.py
🧠 Topic: Python Concurrency (Multithreading vs Multiprocessing)

Key Concepts Covered:
1. Multithreading (IO-bound tasks)
2. Global Interpreter Lock (GIL) and its implications
3. Multiprocessing (CPU-bound tasks - separate memory)
4. threading.Thread and multiprocessing.Process
5. Synchronization (Locks)
6. Pool and Map (Managing multiple workers)

Interview Focus:
- Why doesn't multithreading speed up a math-heavy (CPU-bound) loop? (GIL - Global Interpreter Lock)
- Difference between Thread and Process? (Shared vs Separate memory)
- When to use threading? (Waiting for internet, reading file - IO-Bound)
- When to use multiprocessing? (Massive math, image processing - CPU-Bound)
"""

import time
import threading
import multiprocessing

# 1. IO-Bound Task (Simulates waiting)
def io_task(name):
    print(f"[THREAD] Task {name} starting...")
    time.sleep(2) # simulate waiting for a response
    print(f"[THREAD] Task {name} finished!")

# 2. CPU-Bound Task (Simulates heavy calculation)
def cpu_task(n):
    print(f"[PROCESS] Heavy calculation for {n} beginning...")
    start = time.perf_counter()
    count = 0
    for i in range(10**7): # 10 million iterations
        count += i
    end = time.perf_counter()
    print(f"[PROCESS] Finished in {(end-start):.2f} seconds.")
    return count

def run_threads():
    """ Using threads for IO tasks (Concurrent - fast because of waiting). """
    print("\n--- Running Multithreading (IO-Bound) ---")
    
    start_time = time.perf_counter()
    
    # Create 2 threads
    t1 = threading.Thread(target=io_task, args=("NetworkCall_1",))
    t2 = threading.Thread(target=io_task, args=("NetworkCall_2",))
    
    # Start both
    t1.start()
    t2.start()
    
    # Wait for both to finish (join)
    t1.join()
    t2.join()
    
    end_time = time.perf_counter()
    print(f"Total time for 2 IO tasks (Threaded): {(end_time-start_time):.2f} seconds.")
    print("Optimization: If run sequentially, it would take ~4 seconds.")

def run_processes():
    """ Using separate processes for CPU tasks (Parallel - bypasses GIL). """
    print("\n--- Running Multiprocessing (CPU-Bound) ---")
    
    start_time = time.perf_counter()
    
    # Use Pool to manage multiple processes (Optimal way)
    with multiprocessing.Pool(processes=2) as pool:
        # map() distributes tasks across the pool
        results = pool.map(cpu_task, [1, 2])
        
    end_time = time.perf_counter()
    print(f"Total results: {results}")
    print(f"Total time for 2 CPU tasks (Multiprocessing): {(end_time-start_time):.2f} seconds.")

lock = threading.Lock()
shared_counter = 0

def thread_safe_task():
    """ Synchronization: Critical Section handling. """
    global shared_counter
    
    # WITHOUT lock, result could be inconsistent (Race Condition)
    for _ in range(1000):
        with lock: # ACQUIRE LOCK (Ensures only one thread enters)
            shared_counter += 1

def demonstrate_lock():
    print("\n--- Thread Safety and Synchronization (Lock) ---")
    
    t_list = []
    for _ in range(5):
        t = threading.Thread(target=thread_safe_task)
        t_list.append(t)
        t.start()
        
    for t in t_list:
        t.join()
        
    print(f"Final shared_counter (Expect 5000): {shared_counter}")

def main():
    print("🚀 Python Concurrency Practice")
    run_threads()
    # Multiprocessing must be inside if __name__ == '__main__' (Python requirement)
    run_processes()
    demonstrate_lock()

if __name__ == "__main__":
    # Always include if name == main for multiprocessing on Windows
    main()

"""
Input/Output Examples:
Output:
Total time for 2 IO tasks (Threaded): ~2.00 seconds (Concurrent)
...
Multiprocessing (CPU-Bound)
[PROCESS] Heavy calculation beginning...
...
Final shared_counter: 5000 (Consistent result via LOCK)
"""
