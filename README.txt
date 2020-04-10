My problem: 
I wish to be able to have two python sub-modules (testimport.a and .b) import from each other. 

I wish for this to work for two useage cases: 
- importing from a: 
    from testimports.a import a_function
- running a.py from the command line 
    python a.py 

installation: 
python setup.py develop --user
