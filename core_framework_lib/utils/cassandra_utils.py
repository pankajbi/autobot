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
