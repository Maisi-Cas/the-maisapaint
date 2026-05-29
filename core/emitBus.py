class _Emit:
    def __init__(self):
        self.eventListeners = {}
        
    def conect(self, eventName, function):
        if eventName not in self.eventListeners:
            self.eventListeners[eventName] = []
            
        self.eventListeners[eventName].append(function)
        
    def emit(self,eventName, *args, **kwargs):
        if eventName in self.eventListeners:
            for function in self.eventListeners[eventName]:
                function(*args, **kwargs)
                
bus = _Emit()