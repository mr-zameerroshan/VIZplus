import numpy as np
import scipy.stats as stats

class hyp_tst_lab:
    def __init__(self,dist):
        self.dist = dist

    def sampling(self,data,n):
           return np.random.choice(data,size=n)
        

    class t_tst:
        def __init__(self,hyp_tst_lab):
            self.h = hyp_tst_lab
            self.n = 1000            
            self.sample = self.h.sampling(self.h.dist,1000)
            self.sm = self.sample.mean()
            self.m  = np.mean(self.h.dist)
            self.sv = self.sample.var()
      
        def tnp_val(self):
            
            #analytical
            ta = (self.sm-self.m)/np.sqrt(self.sv/float(self.n))
            pa = stats.t.sf(np.abs(tt),self.n-1)*2

            #theoretical
            tt,pt = stats.ttest_1samp(self.sample,self.m)
                      
            return ta,tt,pa,pt
            

    class pt_tst:
        def __init__(self):
            pass

        def analytical(self):
                    pass
        




    class annova:
        def __init__(self):
            pass

        def analytical(self):
                    pass
        
        def theoretical():
                    pass


    class mann_whitney:
        def __init__(self):
            pass

        def analytical(self):
                    pass
        
        def theoretical():
                    pass


    class chi_sq:
        def __init__(self):
            pass

        def analytical(self):
                    pass
        
        def theoretical():
                    pass


    class ks_tst:
        def __init__(self):
            pass

        def analytical(self):
                    pass
        
        def theoretical():
                    pass

    class shapiro_wilk:
        def __init__(self):
            pass

        def analytical(self):
                    pass
        
        def theoretical():
                    pass

    class levenes_tst:
        def __init__(self):
            pass

        def analytical(self):
                    pass
        
        def theoretical():
                    pass