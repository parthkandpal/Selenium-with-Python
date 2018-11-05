'''
https://www.youtube.com/watch?v=IBC_dxr-4ps
@pytest.fixture(scope="session")
def s1():
pass
@pytest.fixture(scope="module")
def m1():
pass
@pytest.fixture
def f1(tmpdir):
pass
@pytest.fixture
def f2():
pass
def test_foo(f1, m1, f2, s1):
...

'''

from db import MyDB
import pytest
conn=None
cur=None

@pytest.fixture(scope="module")     #scpoe priority-session,module, class|function
def cur():
    print("Setting up")
    db=MyDB()
    conn=db.connect("server")
    curs=conn.cursor()
    yield curs
    print("teardown DB")            #pytest -v --capture=no
    curs.close()
    conn.close()
    print("closed DB")

# def setup_module(module):
#     global conn
#     global cur
#     db=MyDB()
#     conn = db.connect("server")
#     cur = conn.cursor()
#
# def teardown_module():
#     cur.close()
#     conn.close()


def test_johns_id(cur):
    id = cur.execute("select id from employee_db where name==John")
    assert id==123

def test_Toms_id(cur):
        id = cur.execute("select id from employee_db where name==Tom")
        assert id == 789

