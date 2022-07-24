import time

def my_timer(func):    
    def timer_wrapper(*arg):
        try:
            t1 = time.time()
            print(f"Time Started")
            func(4)
            t2 = round(time.time() - t1,2)
            print(f"Function {func.__name__} finished running in {t2} seconds.")
        except BaseException as err:
            print(f"{err}")
        return       
    return timer_wrapper

@my_timer
def tester():
    time.sleep(5)
    print('testerFunction')
    return

if __name__ == "__main__":
    tester()
