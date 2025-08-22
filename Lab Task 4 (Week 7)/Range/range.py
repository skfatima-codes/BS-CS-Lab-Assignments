class MyRange:
    def __init__(self,start,stop=None,step=1):
        if step==0:
            raise ValueError("Step can't be zero")
        if stop is None:
            start,stop=0,start
                # Hpw many nos will be appear
        self._length=max(0,stop-start+step-1)//step
        self.start=start
        self.step=step

                # length of nos in list
    def __len__(self):
        return self._length
                        # get index of the values
    def __getitem__(self, j):
        if j < 0:
            j += len(self)  # convert negative index to positive

        if not 0 <= j < self._length:
            raise IndexError("Index out of range")

        return self.start + j * self.step                    
                        