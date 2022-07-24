# my_stopwatch
Time how long it takes for a given function to run.

1. Import the **"my_stopwatch"** module into your desired module.  
    example:     
            ```from my_stopwatch import stopwatch ```
2. Decorate the function you would like to time:
    example:  
      
     ``` 
      @stopwatch  
      def multiply_stuff_by_3(*num):  
              lc1 = [x * 3 for x in range(2,10)]  
              return lc1```
3. If you would like to verify that the stopwatch works, just import the **time** module and put your function to sleep:  
  example:  
    ```
    @stopwatch  
    def multiply_stuff_by_3(*num):
              time.sleep(2)
              lc1 = [x * 3 for x in range(2,10)]  
              return lc1```
