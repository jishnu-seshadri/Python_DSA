# -*- coding: utf-8 -*-
"""
Created on Sun May  3 10:40:35 2020

@author: User
"""

import random

class Printer:
    def __init__(self):
        self.print_queue = []
        self.time_remaining = 0
        self.qual = 6
        self.tot_time_remaining = self.total_time()
        self.qual = self.paper_qual
         
    def new_task(self, new):
        self.print_queue.insert(0, new)
            
    def total_time(self):
        tot_pages = sum(i for i in self.print_queue)
        self.tot_time_remaining =  tot_pages * self.qual
        
    def time_stamp(self, no_pages):
        self.time_remaining = no_pages*qual
        
    def paper_qual(self):
        high_qual = 12
        low_qual = 6
        if self.tot_time_remaining > 600:
            self.qual = low_qual
        else:
            self.qual = high_qual
        self.time()
    
    def time(self):
        if self.tot_time_remaining > 0:
            self.tot_time_remaining = self.tot_time_remaining - 1
        else:
            self.print_queue = []
            
for i in range(5):
    pages = random.randrange(1, 20)
    p = Printer()
    p.new_task(pages)
    print(p.time_remaining)
            