"""Q:7 How Do You Handle Exceptions With Try/Except/Finally In Python? Explainwith coding
    snippets.
    A:7 therer are four types of exception in exception handling:-
    try: when the code inside try block will run successfully
    except: if try block does'nt run the except block will be executed
    else: if try block will run successfully then else will be defaultly executed
    finally: this block will run in every situation(wather the condition gets
	run or not)"""
   # --> code :-
try:
    print("Value = ",u)
except Exception as e:
    print("Error:",e)
    
