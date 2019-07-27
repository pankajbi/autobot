import argparse
from cassandra.cluster import Cluster

class UseDatabase:

    def __init__(self):
        self.cluster = Cluster()
        self.conn = self.cluster.connect()

    def __enter__(self):
        self.conn = self.cluster.connect(keyspace='vsearch_logs')
        return self.conn

    def __exit__(self, exc_type, exc_value, exc_trace):
        self.cluster.shutdown()

    def execute_query(self,query):
        self.conn.execute(query)



def delete_table(keyspace, table):

    db = UseDatabase()
    db.execute_query("USE {ks} ;".format(ks=keyspace))
    db.execute_query("DROP TABLE {tb} ;".format(tb=table))


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--ks')
    parser.add_argument('--table')
    args = parser.parse_args()

    delete_table(args.ks, args.table)

