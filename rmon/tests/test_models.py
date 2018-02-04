from rmon.models import Server

class TestServer:
    """test Server relative function"""

    def test_save(self,db):
        """test Server.save save server fuction"""

        assert Server.query.count() == 0
        server = Server(name='test',host='127.0.0.1')
        server.save()
        assert Server.query.count() == 1
        assert Server.query.first() == server

    def test_delete(self,db,server):
        """test Server.delete"""

        assert Server.query.count() == 1
        server.delete()
        assert Server.query.count() == 0
        
