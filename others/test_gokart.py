import gokart
from luigi import IntParameter
import luigi
import pandas as pd

class SampleTask1(gokart.TaskOnKart):
    task_namespace = 'sample'
    num_param = IntParameter()
    
    def output(self):
        return self.make_target('output/sample.pkl')

    def run(self):
        df = pd.DataFrame([1]*self.num_param)
        self.dump(df)

if __name__ == '__main__':
    luigi.configuration.LuigiConfigParser.add_config_path('param.ini')
    gokart.run()
